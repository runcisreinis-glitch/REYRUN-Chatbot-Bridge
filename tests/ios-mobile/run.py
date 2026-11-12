"""Check public REYRUN pages in the iOS Simulator and macOS system WebKit."""
from functools import partial
from pathlib import Path
import json
import platform
import plistlib
import shutil
import subprocess
import sys
import tempfile
import time
import uuid
import runpy

PUBLIC = Path("tests/public-sites").resolve()
check = runpy.run_path(str(PUBLIC / "check.py"))["check"]

HERE = Path(__file__).resolve().parent
STARTER = HERE.parents[1] / "web/start/index.html"
BUNDLE = "org.reyrun.MobileSmoke"


def run(*args):
    return subprocess.check_output(args, text=True, timeout=240).strip()


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


def exercise(temp):
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
    }
    (app / "Info.plist").write_bytes(plistlib.dumps(plist))
    for file in ("geometry.js", "pages.json"):
        shutil.copyfile(PUBLIC / file, app / file)
    run("xcrun", "--sdk", "iphonesimulator", "clang", "-fobjc-arc", "-target",
        platform.machine() + "-apple-ios16.0-simulator", "-isysroot", run("xcrun", "--sdk", "iphonesimulator", "--show-sdk-path"),
        "-framework", "UIKit", "-framework", "WebKit", "-framework", "Foundation", "-framework", "CoreGraphics",
        str(PUBLIC / "AppleViews.m"), "-o", str(app / "Smoke"))
    run("codesign", "--force", "--sign", "-", str(app))
    sim = partial(run, "xcrun", "simctl")
    device = sim("create", "REYRUN smoke " + uuid.uuid4().hex[:8], device_type, runtime)
    try:
        sim("bootstatus", device, "-b")
        sim("install", device, str(app))
        sim("launch", device, BUNDLE)
        data = Path(sim("get_app_container", device, BUNDLE, "data"))
        output = data / "Documents" / "smoke-result.json"
        for _ in range(300):
            if output.is_file():
                break
            time.sleep(1)
        else:
            raise RuntimeError("The WKWebView app did not write a result within 300 seconds")
        result = json.loads(output.read_bytes())
        check(result)
        print("PASS iOS Simulator", name, runtime)
        mac=temp / "desktop"
        run("xcrun","clang","-fobjc-arc","-framework","AppKit","-framework","WebKit",str(PUBLIC/"AppleViews.m"),"-o",str(mac))
        mac_result=temp / "desktop.json"
        run(str(mac),str(PUBLIC),str(mac_result))
        desktop=json.loads(mac_result.read_text())
        check(desktop)
        print("PASS macOS WKWebView", platform.mac_ver()[0])
        if len(sys.argv)==2:
            Path(sys.argv[1]).write_text(json.dumps({"ios":result,"simulator":name,"runtime":runtime,"macOS":desktop}))
    finally:
        sim("delete", device)


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as scratch:
        exercise(Path(scratch))
