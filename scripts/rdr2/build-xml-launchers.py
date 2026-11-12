"""Wrap the inspectable local PowerShell source for a normal Windows double-click."""
from pathlib import Path
HERE=Path(__file__).resolve().parent
body=(HERE/'install-xml.ps1').read_text(encoding='utf-8')
for action in ('Install','Restore'):
    prefix = f'''@echo off
setlocal
set "REYRUN_XML_ACTION={action.lower()}"
set "REYRUN_XML_LAUNCHER=%~f0"
set "REYRUN_XML_GAME=%~1"
powershell.exe -NoLogo -NoProfile -STA -Command "$s=[IO.File]::ReadAllText($env:REYRUN_XML_LAUNCHER,[Text.Encoding]::UTF8); $start=$s.IndexOf([char]10+'#REYRUN_XML_BODY'); if($start -lt 0){{exit 1}}; & ([ScriptBlock]::Create($s.Substring($start+1)))"
set "result=%errorlevel%"
if not defined REYRUN_XML_GAME (
    if "%result%"=="0" (timeout /t 8 >nul) else (pause)
)
exit /b %result%
#REYRUN_XML_BODY
'''
    (HERE.parents[1]/'launchers'/f'REYRUN-RDR2-{action}-XML.cmd').write_bytes((prefix+body).replace('\n','\r\n').encode('utf-8'))
