@echo off
setlocal
set "REYRUN_XML_ACTION=install"
set "REYRUN_XML_LAUNCHER=%~f0"
set "REYRUN_XML_GAME=%~1"
powershell.exe -NoLogo -NoProfile -STA -Command "$s=[IO.File]::ReadAllText($env:REYRUN_XML_LAUNCHER,[Text.Encoding]::UTF8); $start=$s.IndexOf([char]10+'#REYRUN_XML_BODY'); if($start -lt 0){exit 1}; & ([ScriptBlock]::Create($s.Substring($start+1)))"
set "result=%errorlevel%"
if not defined REYRUN_XML_GAME (
    if "%result%"=="0" (timeout /t 8 >nul) else (pause)
)
exit /b %result%
#REYRUN_XML_BODY
# The Windows launcher runs this local, bundled script. Only translation data is downloaded.
$ErrorActionPreference = 'Stop'
$xmlName = 'Latvian Translation.xml'
$expected = 'c72337da664b3999ca4fc2de2600c1e79c551b29fa1e69d79d1330485aef5045'
$release = 'https://raw.githubusercontent.com/runcisreinis-glitch/REYRUN-RDR2-Latvian/3de3d4df5b4cbf415bc1f0e56cec3adfea8d4258/Latvian%20Translation.xml'
$language = (Get-UICulture).TwoLetterISOLanguageName
$locale = if($language -eq 'lv'){'lv'}elseif($language -eq 'ru'){'ru'}else{'en'}
function Message([string]$lv,[string]$en,[string]$ru) {
    if($locale -eq 'lv'){return $lv}; if($locale -eq 'ru'){return $ru}; return $en
}
$guide = 'https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site' + @{en='/en/install/';ru='/ru/install/';lv='/uzstadisana/'}[$locale]
function FileHash([string]$file) { (Get-FileHash -LiteralPath $file -Algorithm SHA256).Hash.ToLowerInvariant() }
function AssertLocal([string]$path) {
    if($path -notmatch '^[A-Za-z]:\\'){throw 'Select a local Windows drive.'}
    for($p=$path;$p;$p=[IO.Path]::GetDirectoryName($p)){
        if(Test-Path -LiteralPath $p){
            $item=Get-Item -LiteralPath $p -Force
            if(($item.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0){throw ('Linked path: '+$p)}
        }
    }
}
function CheckGameClosed {
    if(Get-Process -Name RDR2 -ErrorAction SilentlyContinue){
        throw (Message 'Aizver Red Dead Redemption 2 un palaid failu vēlreiz.' 'Close Red Dead Redemption 2 and open this file again.' 'Закройте Red Dead Redemption 2 и запустите этот файл ещё раз.')
    }
}
function Get-EpicGameFolders([string]$programDataRoot) {
    if (!$programDataRoot) { return }
    $directory = Join-Path $programDataRoot 'Epic\EpicGamesLauncher\Data\Manifests'
    $manifests = Get-ChildItem -LiteralPath $directory -File -Filter '*.item' -ErrorAction SilentlyContinue
    foreach ($manifest in $manifests) {
        if ($manifest.Length -gt 2MB) { continue }
        try {
            $entry = [IO.File]::ReadAllText($manifest.FullName) | ConvertFrom-Json
            if ($entry.DisplayName -isnot [string] -or $entry.DisplayName.Trim() -ine 'Red Dead Redemption 2') { continue }
            if ($entry.InstallLocation -isnot [string] -or $entry.InstallLocation -notmatch '^[A-Za-z]:[\\/]') { continue }
            $folder = [IO.Path]::GetFullPath($entry.InstallLocation)
            if ([IO.File]::Exists([IO.Path]::Combine($folder, 'RDR2.exe'))) { $folder }
        } catch {
            # Ignore incomplete or stale Epic records and keep looking.
        }
    }
}
function ChooseGame {
    if($env:REYRUN_XML_GAME){return [IO.Path]::GetFullPath($env:REYRUN_XML_GAME)}
    $candidates = @(Get-EpicGameFolders $env:ProgramData)
    if(${env:ProgramFiles(x86)}){$candidates+=Join-Path ${env:ProgramFiles(x86)} 'Steam\steamapps\common\Red Dead Redemption 2'}
    $steam=(Get-ItemProperty -LiteralPath 'HKCU:\Software\Valve\Steam' -ErrorAction SilentlyContinue).SteamPath
    if($steam){
        $candidates+=Join-Path $steam 'steamapps\common\Red Dead Redemption 2'
        $libraries=Join-Path $steam 'steamapps\libraryfolders.vdf'
        if([IO.File]::Exists($libraries)){
            foreach($match in [regex]::Matches([IO.File]::ReadAllText($libraries),'"path"\s+"([^"]+)"')){
                $lib=$match.Groups[1].Value.Replace('\\','\')
                if($lib -match '^[A-Za-z]:[\\/]'){$candidates+=Join-Path $lib 'steamapps\common\Red Dead Redemption 2'}
            }
        }
    }
    foreach($hive in @('HKLM:\SOFTWARE','HKLM:\SOFTWARE\WOW6432Node','HKCU:\Software')){
        $r=Get-ItemProperty -LiteralPath ($hive+'\Rockstar Games\Red Dead Redemption 2') -ErrorAction SilentlyContinue
        foreach($key in @('InstallFolder','InstallFolderEpic','InstallFolderSteam','InstallLocation')){if($r.$key){$candidates+=$r.$key}}
    }
    $matches=@($candidates|Where-Object {$_ -and [IO.File]::Exists((Join-Path $_ 'RDR2.exe'))}|ForEach-Object {[IO.Path]::GetFullPath($_).TrimEnd('\')}|Sort-Object -Unique)
    if($matches.Count -eq 1){return $matches[0]}
    Add-Type -AssemblyName System.Windows.Forms
    $pick=New-Object System.Windows.Forms.FolderBrowserDialog
    $pick.Description=Message 'Izvēlies mapi ar RDR2.exe.' 'Select the folder that contains RDR2.exe.' 'Выберите папку с RDR2.exe.'
    try {if($pick.ShowDialog() -ne 'OK'){throw (Message 'Atcelts.' 'Cancelled.' 'Отменено.')}; return $pick.SelectedPath}
    finally {$pick.Dispose()}
}
function ValidatePrerequisites {
    $checks=@(
        @('UniversalRDR2StringTranslator.asi','e88ec57c9e6ef03f42ab0218a0fb98fd065927ff9859ed49e5f1ef601c6871f6','https://www.nexusmods.com/reddeadredemption2/mods/10214'),
        @('dinput8.dll','031a3e5576d91dce1e438d36b9a3d462c7334ab4791990a8ff1e3ddc0e132daf','https://github.com/ThirteenAG/Ultimate-ASI-Loader')
    )
    $issues=@()
    foreach($row in $checks){
        $file=Join-Path $game $row[0];AssertLocal $file
        if(![IO.File]::Exists($file)){
            $issues+=(Message 'Trūkst faila' 'Missing file' 'Отсутствует файл')+' '+$row[0]+'  '+$row[2]
        } elseif((FileHash $file) -ne $row[1]){
            $issues+=(Message 'Cita faila versija' 'Unrecognized file version' 'Другая версия файла')+' '+$row[0]+'  '+$row[2]
        }
    }
    if($issues.Count){throw ($issues -join [Environment]::NewLine)}
}
function VerifyBaseFiles {
    $conflicts=@(Get-ChildItem -LiteralPath $game -Force | Where-Object {($_.Name -like '*Translation.xml' -and $_.Name -ine $xmlName) -or $_.Name -ieq 'rdr2-translator.asi'})
    if($conflicts){throw ((Message 'Mapē ir cits pamata tulkojums vai vecais spraudnis. Skat. rezerves kopijas norādes.' 'Another base translation or the old plug-in is present. See the backup instructions.' 'В папке есть другой основной перевод или старый плагин. См. инструкцию по резервной копии.')+' '+(($conflicts|ForEach-Object {$_.Name}) -join ', '))}
}
function ReadState {
    if(![IO.File]::Exists($journal)){return $null}
    $r=Get-Content -LiteralPath $journal -Encoding UTF8 -Raw|ConvertFrom-Json
    if($r.schema -ne 1 -or $r.folder -ine $game -or $r.release -ne $expected -or ($r.original -ne '' -and $r.original -notmatch '^[a-f0-9]{64}$')){throw 'Unrecognized installation record.'}
    if($r.original -and (![IO.File]::Exists($backup) -or (FileHash $backup) -ne $r.original)){throw 'Backup checksum mismatch.'}
    return $r
}
function SaveState([string]$hash) {
    if($hash){
        if([IO.File]::Exists($backup)){if((FileHash $backup) -ne $hash){throw 'A different backup already exists.'}}
        else {
            $tmp=Join-Path $store ('backup-'+[guid]::NewGuid().ToString('n')+'.tmp')
            try{[IO.File]::Copy($destination,$tmp);if((FileHash $tmp) -ne $hash){throw 'Backup checksum mismatch.'};[IO.File]::Move($tmp,$backup)}
            finally{if([IO.File]::Exists($tmp)){[IO.File]::Delete($tmp)}}
        }
    }
    $tmp=Join-Path $store ('record-'+[guid]::NewGuid().ToString('n')+'.tmp')
    try{
        $r=@{schema=1;folder=$game;original=$hash;release=$expected} | ConvertTo-Json -Compress
        [IO.File]::WriteAllText($tmp,$r);[IO.File]::Move($tmp,$journal)
    }finally{if([IO.File]::Exists($tmp)){[IO.File]::Delete($tmp)}}
}
function CurrentHash { if([IO.File]::Exists($destination)){return (FileHash $destination)};return '' }
function ApplyXml {
    CheckGameClosed
    $restore=$env:REYRUN_XML_ACTION -eq 'restore'
    if(!$restore){ValidatePrerequisites}
    VerifyBaseFiles
    $r=ReadState
    $old=CurrentHash
    if($restore){
        if(!$r){throw (Message 'Šai mapei nav REYRUN uzstādīšanas ieraksta.' 'No REYRUN install record for this folder.' 'Для этой папки нет записи об установке REYRUN.')}
        if($old -eq $r.original){return (Message 'Iepriekšējais stāvoklis jau ir atjaunots.' 'The previous state is already restored.' 'Прежнее состояние уже восстановлено.')}
        if($old -ne $expected){throw 'The installed XML has changed. Keep the edited file and inspect the backup.'}
    } else {
        if($old -eq $expected){return (Message 'Latviešu XML jau ir uzstādīts. Kontrolsumma sakrīt.' 'The Latvian XML is already installed. Its checksum matches.' 'Латышский XML уже установлен. Контрольная сумма совпадает.')}
        if($r -and $r.original -ne $old){throw 'The current XML differs from the installation record.'}
    }
    $pending=Join-Path $game ('.reyrun-'+[guid]::NewGuid().ToString('n')+'.tmp')
    try{
        if(!$restore){
            $offline=Join-Path ([IO.Path]::GetDirectoryName($env:REYRUN_XML_LAUNCHER)) $xmlName
            if([IO.File]::Exists($offline)){[IO.File]::Copy($offline,$pending)}
            else{[Net.ServicePointManager]::SecurityProtocol=[Net.SecurityProtocolType]::Tls12
                Invoke-WebRequest -UseBasicParsing -Uri $release -OutFile $pending -TimeoutSec 120}
            if((FileHash $pending) -ne $expected){throw 'Translation SHA-256 mismatch.'}
            if(!$r){SaveState $old}
        }elseif($r.original){[IO.File]::Copy($backup,$pending);if((FileHash $pending) -ne $r.original){throw 'Backup checksum mismatch.'}}
        CheckGameClosed
        VerifyBaseFiles
        if((CurrentHash) -ne $old){throw 'The XML changed during installation. Try again.'}
        if($restore -and !$r.original){[IO.File]::Delete($destination)}
        elseif($old){[IO.File]::Replace($pending,$destination,[NullString]::Value)}
        else{[IO.File]::Move($pending,$destination)}
        $wanted=if($restore){$r.original}else{$expected}
        if((CurrentHash) -ne $wanted){throw 'Final file verification failed.'}
    }finally{if([IO.File]::Exists($pending)){[IO.File]::Delete($pending)}}
    if($restore){return (Message 'Iepriekšējais stāvoklis ir atjaunots.' 'Previous state restored.' 'Прежнее состояние восстановлено.')}
    return (Message 'Latviešu XML ir uzstādīts un pārbaudīts. Sāc stāsta režīmu.' 'Latvian XML installed and verified. Start Story Mode.' 'Латышский XML установлен и проверен. Запустите сюжетный режим.')
}
try{
    $game=[IO.Path]::GetFullPath((ChooseGame)).TrimEnd('\')
    $exe=Join-Path $game 'RDR2.exe';AssertLocal $exe
    if(![IO.File]::Exists($exe)){throw 'RDR2.exe not found.'}
    $destination=Join-Path $game $xmlName;AssertLocal $destination
    if([IO.Directory]::Exists($destination)){throw 'A directory occupies the XML filename.'}
    $key=[Security.Cryptography.SHA256]::Create()
    try{$identity=[BitConverter]::ToString($key.ComputeHash([Text.Encoding]::UTF8.GetBytes($game.ToUpperInvariant()))).Replace('-','').ToLowerInvariant()}finally{$key.Dispose()}
    $store=Join-Path $env:LOCALAPPDATA ('REYRUN\RDR2-XML\'+$identity)
    if(($store+'\').StartsWith($game+'\',[StringComparison]::OrdinalIgnoreCase)){throw 'Backup must be outside the game folder.'}
    $backup=Join-Path $store 'previous.xml';$journal=Join-Path $store 'installation.json'
    AssertLocal $journal; AssertLocal $backup
    [void][IO.Directory]::CreateDirectory($store)
    $lockPath=Join-Path $store 'install.lock';AssertLocal $lockPath
    $lock=[IO.File]::Open($lockPath,[IO.FileMode]::OpenOrCreate,[IO.FileAccess]::ReadWrite,[IO.FileShare]::None)
    try{Write-Output (ApplyXml);Write-Output $game;Write-Output $store}finally{$lock.Dispose()}
    exit 0
}catch{[Console]::Error.WriteLine($_.Exception.Message);[Console]::Error.WriteLine($guide);exit 1}
