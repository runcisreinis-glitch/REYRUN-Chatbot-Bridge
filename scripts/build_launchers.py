"""Build deterministic single-file, user-invoked launchers without an administrator or network listener."""
from pathlib import Path
import base64, hashlib, io, json, zipfile, textwrap, runpy

root=Path(__file__).resolve().parents[1]
target=root/'launchers';target.mkdir(exist_ok=True)
site='https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site'
hashes={'win-x64':'e612af99f626ab415ea225af6bce5c971feb448cb5cae250bb1c3fa50c5f7d9f','win-arm64':'b3cc74a295b39d4f273271e96f58c06dd2b35757ca12abec64c7d0598b434f14','darwin-arm64':'ff6e17d4874b76d272212b908cc020d6e815fba5a6c7eaaa06add725840307fd','darwin-x64':'977614af0504c81045e7fd85596dbca0e5f951b96681516dadafedcca8c447f7'}
def archive(files):
 out=io.BytesIO()
 with zipfile.ZipFile(out,'w') as z:
  for name,data,mode in files:
   i=zipfile.ZipInfo(name,(2026,11,12,0,0,0));i.create_system=3;i.external_attr=mode<<16
   z.writestr(i,data,compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)
 return out.getvalue()
files=[(p.name,p.read_bytes(),0o100644) for p in sorted((root/'scripts').glob('*.cjs'))]
payload=archive(files);encoded=base64.b64encode(payload).decode();digest=hashlib.sha256(payload).hexdigest()
ps=r"""$ErrorActionPreference='Stop'
function Get-StarterDigest([string]$path){
  $hash=[Security.Cryptography.SHA256]::Create()
  try {
    $stream=[IO.File]::OpenRead($path)
    try {return [BitConverter]::ToString($hash.ComputeHash($stream)).Replace('-','').ToLowerInvariant()}
    finally {$stream.Dispose()}
  } finally {$hash.Dispose()}
}
$base=if($env:REYRUN_WORKSPACE){$env:REYRUN_WORKSPACE}else{Join-Path $env:USERPROFILE 'REYRUN Bridge'}
$rt=Join-Path $base 'runtime'
[void][IO.Directory]::CreateDirectory($rt)
$tmp=Join-Path ([IO.Path]::GetTempPath()) ('reyrun-'+[guid]::NewGuid())
[void][IO.Directory]::CreateDirectory($tmp)
try {
  $zip=Join-Path $tmp 'starter.zip'
  $encoded=([IO.File]::ReadAllLines($env:REYRUN_START_FILE) | Where-Object { $_.StartsWith('::DATA:') } | ForEach-Object { $_.Substring(7) }) -join ''
  [IO.File]::WriteAllBytes($zip,[Convert]::FromBase64String($encoded))
  if((Get-StarterDigest $zip) -ne 'DIGEST'){throw 'Starter file is incomplete. Download again.'}
  Expand-Archive -LiteralPath $zip -DestinationPath $rt -Force
  $n=(Get-Command node.exe -ErrorAction SilentlyContinue | Select-Object -First 1).Source
  if(!$n -or ((& $n --version) -notmatch '^v(2[4-9]|[3-9][0-9])\.')){
    $arch=if($env:PROCESSOR_ARCHITECTURE -eq 'ARM64'){'arm64'}else{'x64'}
    $tag='node-v24.22.3-win-'+$arch
    $cached=Join-Path (Join-Path $rt $tag) 'node.exe'
    if(!(Test-Path -LiteralPath $cached)){
      $pkg=Join-Path $tmp 'node.zip'
      Invoke-WebRequest -UseBasicParsing -Uri ('https://nodejs.org/dist/v24.22.3/'+$tag+'.zip') -OutFile $pkg
      $sum=if($arch -eq 'arm64'){'WINARM'}else{'WINX64'}
      if((Get-StarterDigest $pkg) -ne $sum){throw 'Official Node archive did not match its published SHA-256.'}
      Expand-Archive -LiteralPath $pkg -DestinationPath $rt -Force
    }
    $n=$cached
  }
  $mode='MODE'
  if($mode -eq 'git-handoff'){& $n (Join-Path $rt 'git-handoff.cjs')}
  elseif($mode -eq 'rdr2'){
    $game=$env:REYRUN_GAME_ROOT
    if(!$game){Add-Type -AssemblyName System.Windows.Forms;$pick=New-Object System.Windows.Forms.FolderBrowserDialog;$pick.Description='Select the folder containing RDR2.exe';if($pick.ShowDialog() -ne 'OK'){throw 'No game folder selected.'};$game=$pick.SelectedPath}
    & $n (Join-Path $rt 'setup.cjs') $mode $game
  } else {& $n (Join-Path $rt 'setup.cjs') $mode}
  if($LASTEXITCODE -ne 0){exit $LASTEXITCODE}
} finally {if(Test-Path -LiteralPath $tmp){Remove-Item -LiteralPath $tmp -Recurse -Force}}
"""
# PowerShell reads the plain-text commands above. No downloaded script is evaluated.
def win(mode):
 windows_payload, windows_digest, body = encoded, digest, ps
 if mode == 'rdr2':
  helper = root / 'scripts' / 'rdr2'
  rdr2_payload = archive(files + [('rdr2-detect.cjs', (helper / 'detect.cjs').read_bytes(), 0o100644)])
  windows_payload = base64.b64encode(rdr2_payload).decode()
  windows_digest = hashlib.sha256(rdr2_payload).hexdigest()
  selection = '$game=$env:REYRUN_GAME_ROOT'
  body = body.replace(selection, selection + '\n' + (helper / 'launcher-detection.ps1').read_text().rstrip())
  setup_game = "& $n (Join-Path $rt 'setup.cjs') $mode $game"
  body = body.replace(setup_game, setup_game + '\n' + (helper / 'stage-translation.ps1').read_text().rstrip())
 cmdline=body.replace('DIGEST',windows_digest).replace('WINARM',hashes['win-arm64']).replace('WINX64',hashes['win-x64']).replace('MODE',mode)
 # Wrapping the audited body as one encoded UTF-16 command can exceed cmd's length limit.
 # Keep the commands in a local marker block within this same file, readable in any text editor.
 head="""@echo off
setlocal
rem Let Windows PowerShell discover its own built-in modules when started from PowerShell 7.
set "PSModulePath="
set "REYRUN_START_FILE=%~f0"
powershell.exe -NoProfile -Command "$src=[IO.File]::ReadAllLines($env:REYRUN_START_FILE);$a=[array]::IndexOf($src,':BEGIN_POWERSHELL');$b=[array]::IndexOf($src,':END_POWERSHELL');if($a -lt 0 -or $b -le $a){exit 2};& ([scriptblock]::Create(($src[($a+1)..($b-1)] -join [Environment]::NewLine)))"
set "REYRUN_RESULT=%ERRORLEVEL%"
if not defined REYRUN_TEST_MODE pause
exit /b %REYRUN_RESULT%
:BEGIN_POWERSHELL
"""
 return (head+cmdline+':END_POWERSHELL\n'+'\n'.join('::DATA:'+x for x in textwrap.wrap(windows_payload,100))+'\n').replace('\n','\r\n').encode('ascii')
mac=r'''#!/bin/bash
set -euo pipefail
umask 077
base="${REYRUN_WORKSPACE:-$HOME/REYRUN Bridge}"
rt="$base/runtime"
mkdir -p "$rt"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
base64 --decode > "$tmp/starter.zip" <<'BRIDGE_DATA'
DATA
BRIDGE_DATA
printf '%s  %s\n' 'DIGEST' "$tmp/starter.zip" | shasum -a 256 -c -
unzip -oq "$tmp/starter.zip" -d "$rt"
nodebin="$(command -v node || true)"
if [[ -z "$nodebin" ]] || ! "$nodebin" -e 'process.exit(Number(process.versions.node.split(".")[0])>=24?0:1)'; then
  case "$(uname -m)" in arm64) arch=arm64; sum=MACARM ;; x86_64) arch=x64; sum=MACX64 ;; *) echo 'Unsupported CPU'; exit 1 ;; esac
  tag="node-v24.22.3-darwin-$arch"
  nodebin="$rt/$tag/bin/node"
  if [[ ! -x "$nodebin" ]]; then
    curl --fail --show-error --location "https://nodejs.org/dist/v24.22.3/$tag.tar.gz" -o "$tmp/node.tgz"
    printf '%s  %s\n' "$sum" "$tmp/node.tgz" | shasum -a 256 -c -
    tar -xzf "$tmp/node.tgz" -C "$rt"
  fi
fi
if [[ "MODE" = "git-handoff" ]]; then "$nodebin" "$rt/git-handoff.cjs"; else "$nodebin" "$rt/setup.cjs" "MODE"; fi
'''
mac=mac.replace("base64 --decode",'''if [[ "$(uname -s)" = Darwin ]]; then decode=(-D); else decode=(--decode); fi
base64 "${decode[@]}"''')
# Only replace the placeholder line, not the here-document delimiter.
mac=mac.replace('\nDATA\n','\n'+'\n'.join(textwrap.wrap(encoded,100))+'\n').replace('DIGEST',digest).replace('MACARM',hashes['darwin-arm64']).replace('MACX64',hashes['darwin-x64'])
for mode in ['jobs','filesystem','playwright','devtools','commander','git-handoff','rdr2']:
 (target/f'REYRUN-{mode}-Windows.cmd').write_bytes(win(mode))
 if mode!='rdr2':
  name=f'REYRUN-{mode}-macOS.command';data=mac.replace('MODE',mode).encode()
  (target/name).write_bytes(data);(target/name).chmod(0o755);(target/(name+'.zip')).write_bytes(archive([(name,data,0o100755)]))
manifest={'manifest_version':'0.3','name':'reyrun-task-bridge','version':'1.0.0','display_name':'REYRUN Task Bridge','description':'Local, revision-checked job notes. Resume a task in a second compatible chat.','author':{'name':'REYRUN'},'homepage':site,'server':{'type':'node','entry_point':'server/bridge.cjs','mcp_config':{'command':'node','args':['${__dirname}/server/bridge.cjs']}}}
(target/'REYRUN-Task-Bridge.mcpb').write_bytes(archive([('manifest.json',json.dumps(manifest,indent=2).encode(),0o100644),('server/bridge.cjs',(root/'scripts/bridge.cjs').read_bytes(),0o100644)]))
runpy.run_path(str(root/'scripts/rdr2/build-xml-launchers.py'))
checks=''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.name+'\n' for p in sorted(target.iterdir()) if p.is_file() and p.name!='SHA256SUMS.txt')
(target/'SHA256SUMS.txt').write_text(checks)
