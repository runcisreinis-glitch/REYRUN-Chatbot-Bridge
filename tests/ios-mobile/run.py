"""Run the checked-in mobile starter in a fresh Apple iOS Simulator WKWebView."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import hashlib
import json
import platform
import plistlib
import shutil
import subprocess
import sys
import tempfile
import threading
import time
import uuid
from urllib.request import urlopen

HERE = Path(__file__).resolve().parent
WEB = HERE.parents[1] / "web"
STARTER = WEB / "start/index.html"
BUNDLE = "org.reyrun.MobileSmoke"


def run(*args):
    return subprocess.check_output(args, text=True, timeout=240).strip()


def launch_and_read(device, output, temp):
    # simctl can keep a pipe open after handing off to the app. The atomic
    # receipt from WKWebView is the completion signal, independent of simctl.
    for attempt in range(1, 3):
        log = temp / f"launch-{attempt}.log"
        args = ["xcrun", "simctl", "launch"]
        if attempt == 2:
            args.append("--terminate-running-process")
        print(f"Launching the simulator app (attempt {attempt})", flush=True)
        with log.open("wb") as log_file:
            process = subprocess.Popen([*args, device, BUNDLE], stdin=subprocess.DEVNULL,
                                       stdout=log_file, stderr=subprocess.STDOUT)
            try:
                deadline = time.monotonic() + 120
                while time.monotonic() < deadline:
                    if output.is_file():
                        return json.loads(output.read_bytes())
                    if process.poll() not in (None, 0):
                        break
                    time.sleep(0.5)
            finally:
                if process.poll() is None:
                    process.terminate()
                    try:
                        process.wait(timeout=5)
                    except subprocess.TimeoutExpired:
                        process.kill()
                        process.wait(timeout=5)
        if output.is_file():
            return json.loads(output.read_bytes())
        print(f"No WKWebView receipt; simctl status {process.returncode}. "
              + log.read_text(errors="replace")[-2400:], flush=True)
    raise RuntimeError("No result from the installed WKWebView app after two bounded launches")


def public_pages_from_mac():
    # Hosting reachability is informational and is independent of the local receipt.
    pages = {}
    for site in ("reyrun-rekursive-deep-search", "reyrun-rdr2-latviski", "reyrun-chatbot-bridge"):
        url = f"https://{site}.runcisreinis.chatgpt.site/"
        try:
            with urlopen(url, timeout=5) as response:
                pages[url] = {"status": response.status, "containsBrand": b"REYRUN" in response.read(262144).upper()}
        except OSError as exc:
            pages[url] = {"error": str(exc)}
    print("Public page observations from macOS:", json.dumps(pages), flush=True)
    return pages


def choose_iphone():
    devices = json.loads(run("xcrun", "simctl", "list", "devices", "available", "--json"))["devices"]
    sdk = tuple(map(int, run("xcrun", "--sdk", "iphonesimulator", "--show-sdk-version").split(".")))
    options = []
    for runtime, entries in devices.items():
        if ".iOS-" not in runtime:
            continue
        version = tuple(map(int, runtime.split(".iOS-")[1].split("-")))
        for device in entries:
            if version <= sdk and device["name"].startswith("iPhone") and device.get("deviceTypeIdentifier"):
                options.append((version, device["name"], runtime, device["deviceTypeIdentifier"]))
    if not options:
        raise RuntimeError("No supported iOS runtime and iPhone device type found in this Xcode installation")
    return max(options)


def exercise(temp, http_port):
    version, name, runtime, device_type = choose_iphone()
    print(f"Testing {name} on iOS Simulator runtime {version}", flush=True)
    app = temp / "Smoke.app"
    app.mkdir()
    plist = {
        "CFBundleName": "Smoke", "CFBundleDisplayName": "REYRUN Smoke", "CFBundleIdentifier": BUNDLE,
        "CFBundleExecutable": "Smoke", "CFBundleVersion": "1", "CFBundleShortVersionString": "1.0",
        "CFBundlePackageType": "APPL", "CFBundleInfoDictionaryVersion": "6.0", "LSRequiresIPhoneOS": True,
        "CFBundleSupportedPlatforms": ["iPhoneSimulator"], "MinimumOSVersion": "16.0", "UIDeviceFamily": [1],
        "NSAppTransportSecurity": {"NSAllowsLocalNetworking": True}, "UILaunchScreen": {},
        "UIApplicationSceneManifest": {"UIApplicationSupportsMultipleScenes": False, "UISceneConfigurations": {
            "UIWindowSceneSessionRoleApplication": [{"UISceneConfigurationName": "Smoke", "UISceneDelegateClassName": "Scene"}]}},
        "REYRUNTestURL": f"http://localhost:{http_port}/start/",
    }
    (app / "Info.plist").write_bytes(plistlib.dumps(plist))
    shutil.copyfile(HERE / "scenario.js", app / "scenario.js")
    run("xcrun", "--sdk", "iphonesimulator", "clang", "-fobjc-arc", "-target",
        platform.machine() + "-apple-ios16.0-simulator", "-isysroot", run("xcrun", "--sdk", "iphonesimulator", "--show-sdk-path"),
        "-framework", "UIKit", "-framework", "WebKit", "-framework", "Foundation", "-framework", "CoreGraphics",
        str(HERE / "Smoke.m"), "-o", str(app / "Smoke"))
    run("codesign", "--force", "--sign", "-", str(app))
    sim = partial(run, "xcrun", "simctl")
    device = sim("create", "REYRUN smoke " + uuid.uuid4().hex[:8], device_type, runtime)
    try:
        sim("bootstatus", device, "-b")
        sim("install", device, str(app))
        data = Path(sim("get_app_container", device, BUNDLE, "data"))
        output = data / "Documents" / "smoke-result.json"
        result = launch_and_read(device, output, temp)
        expected = {"schema": "reyrun.mobile.receipt/1", "id": "phone-test-01", "action": "inspect-text",
                    "bytes": 13, "lines": 2, "sha256": hashlib.sha256("REYRUN\nRīga\n".encode()).hexdigest()}
        if result.get("receipt") != expected or result.get("rejected") is not True:
            raise RuntimeError(json.dumps(result, ensure_ascii=False))
        print("PASS actual iOS Simulator WKWebView:", json.dumps(result, ensure_ascii=False))
        if len(sys.argv) == 2:
            report = {"simulator": name, "runtime": runtime, "pageSha256": hashlib.sha256(STARTER.read_bytes()).hexdigest(), **result}
            report["publicPagesFromMac"] = public_pages_from_mac()
            Path(sys.argv[1]).write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    finally:
        try:
            subprocess.run(["xcrun", "simctl", "delete", device], timeout=30, check=True)
        except (subprocess.SubprocessError, OSError) as exc:
            print(f"Could not remove temporary simulator {device}: {exc}", file=sys.stderr)


if __name__ == "__main__":
    handler = partial(SimpleHTTPRequestHandler, directory=str(WEB))
    with ThreadingHTTPServer(("127.0.0.1", 0), handler) as server, tempfile.TemporaryDirectory() as scratch:
        threading.Thread(target=server.serve_forever, daemon=True).start()
        exercise(Path(scratch), server.server_port)
