import json
from pathlib import Path
import re
import runpy
import subprocess
import time
check=runpy.run_path('tests/public-sites/check.py')['check']
end=time.monotonic()+290
while time.monotonic()<end:
    log=subprocess.check_output(['adb','logcat','-d','-v','raw','-s','ReyrunMobile:I','*:S'],text=True)
    if error:=re.search(r'^ERROR (.+)$',log,re.M):
        raise RuntimeError(error.group(1))
    if done:=re.search(r'^DONE (.+)$',log,re.M):
        rows=[json.loads(s) for s in re.findall(r'^ROW (.+)$',log,re.M)]
        data={'pages':rows,'webview':done.group(1)}
        check(data)
        Path('android-mobile-result.json').write_text(json.dumps(data))
        print('PASS Android System WebView',done.group(1))
        break
    time.sleep(1)
else: raise TimeoutError('Android tests timed out')
