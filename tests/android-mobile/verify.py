"""Tap the sample once using Android's input service, then verify the returned public receipt."""
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import time

payload = "REYRUN\nRīga\n".encode("utf-8")
expected = dict(schema="reyrun.mobile.receipt/1", id="phone-test-01", action="inspect-text",
                bytes=len(payload), lines=2, sha256=hashlib.sha256(payload).hexdigest())
page = Path(sys.argv[1])
deadline = time.monotonic() + 75
tapped = False
while time.monotonic() < deadline:
    logs = subprocess.check_output(["adb", "logcat", "-d", "-v", "raw", "-s", "ReyrunMobile:I", "*:S"], text=True)
    if error := re.search(r"^ERROR (.+)$", logs, re.M):
        sys.exit(error.group(1))
    if not tapped and (button := re.search(r"^BUTTON (\d+) (\d+)$", logs, re.M)):
        subprocess.run(["adb", "shell", "input", "tap", *button.groups()], check=True)
        tapped = True
    if result := re.search(r"^RESULT (.+)$", logs, re.M):
        evidence = json.loads(result.group(1))
        if not tapped or evidence["receipt"] != expected:
            sys.exit("Unexpected Android receipt or tap count: " + str(evidence))
        evidence.update(environment="Android emulator", physicalPhone=False, filePickerTested=False,
                        nativeInputTaps=1, starterSHA256=hashlib.sha256(page.read_bytes()).hexdigest())
        output = json.dumps(evidence, indent=2, ensure_ascii=False)
        Path("android-mobile-result.json").write_text(output + "\n", encoding="utf-8")
        print(output)
        break
    time.sleep(0.5)
else:
    sys.exit(f"Android System WebView did not produce a receipt within 75 seconds. Native tap sent: {tapped}")
