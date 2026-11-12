param([Parameter(Mandatory=$true)][string]$VerifiedFiles)
$ErrorActionPreference='Stop'
$real=(Resolve-Path -LiteralPath $VerifiedFiles).Path
$root=Join-Path ([IO.Path]::GetTempPath()) ('REYRUN-xml-test-'+[guid]::NewGuid().ToString('n'))
[void][IO.Directory]::CreateDirectory($root)
foreach($action in @('Install','Restore')){
    $file='REYRUN-RDR2-'+$action+'-XML.cmd'
    Copy-Item -LiteralPath (Join-Path (Join-Path $PSScriptRoot '../launchers') $file) -Destination $root
}
$base=Join-Path $root ('test-'+[guid]::NewGuid().ToString('n'))
$game=Join-Path $base 'game'
$savedProfile=$env:LOCALAPPDATA
try {
$env:LOCALAPPDATA=Join-Path $base 'profile'
[void][IO.Directory]::CreateDirectory($game)
$xml='Latvian Translation.xml';$out=Join-Path $game $xml;$data=Join-Path $root $xml
$cases=New-Object 'System.Collections.Generic.List[string]'
function Run-Case($action,$want,$name){
 $cmd=Join-Path $root ('REYRUN-RDR2-'+$action+'-XML.cmd')
 $lines=& $cmd $game 2>&1 | ForEach-Object { "$_" }
 if($LASTEXITCODE -ne $want){throw ($name+' returned '+$LASTEXITCODE+' '+($lines -join ' / '))}
 $cases.Add($name)
}
function Check($ok,$msg){if(!$ok){throw $msg}}
[IO.File]::WriteAllText((Join-Path $game 'RDR2.exe'),'folder marker in test fixture only')
Copy-Item -LiteralPath (Join-Path $real $xml) -Destination $data
$expected=(Get-FileHash -LiteralPath $data).Hash
$ErrorActionPreference='Continue'
Run-Case 'Install' 1 'missing-both'
Check (-not [IO.File]::Exists($out)) 'Unexpected XML after missing dependencies'
Copy-Item -LiteralPath (Join-Path $real 'dinput8.dll') -Destination $game
Copy-Item -LiteralPath (Join-Path $real 'UniversalRDR2StringTranslator.asi') -Destination $game
$other=Join-Path $game 'French Translation.xml'
[IO.File]::WriteAllText($other,'previous French')
Run-Case 'Install' 1 'conflicting-base';Check ([IO.File]::ReadAllText($other) -eq 'previous French') 'Conflict changed'
[IO.File]::Move($other,(Join-Path $base 'French.backup'))
Run-Case 'Install' 0 'clean-install'
Check ((Get-FileHash -LiteralPath $out).Hash -eq $expected) 'Wrong XML'
Run-Case 'Install' 0 'already-installed'
Run-Case 'Restore' 0 'restore-clean'
Check (-not [IO.File]::Exists($out)) 'Previously empty directory not restored'
Run-Case 'Restore' 0 'already-restored'
$game=Join-Path $base 'other fixture';[void][IO.Directory]::CreateDirectory($game)
$previousGame=Join-Path $base 'game'
foreach($file in @('RDR2.exe','dinput8.dll','UniversalRDR2StringTranslator.asi')){Copy-Item -LiteralPath (Join-Path $previousGame $file) -Destination $game}
$out=Join-Path $game $xml;[IO.File]::WriteAllText($out,'prior translation version')
Run-Case 'Install' 0 'replace-with-backup'
Check ((Get-FileHash -LiteralPath $out).Hash -eq $expected) 'Replacement failed'
[IO.File]::WriteAllText($out,'user edits')
Run-Case 'Restore' 1 'preserve-manual-edits';Check ([IO.File]::ReadAllText($out) -eq 'user edits') 'Manual edit lost'
[IO.File]::Copy($data,$out,$true)
Run-Case 'Restore' 0 'restore-previous-translation';Check ([IO.File]::ReadAllText($out) -eq 'prior translation version') 'Previous bytes not restored'
$plugin=Join-Path $game 'UniversalRDR2StringTranslator.asi';[IO.File]::WriteAllText($plugin,'unrecognized version')
Run-Case 'Install' 1 'reject-unknown-ASI';Check ([IO.File]::ReadAllText($out) -eq 'prior translation version') 'Unexpected change with unrecognized ASI'
[pscustomobject]@{os=[Environment]::OSVersion.VersionString;cases=$cases;count=$cases.Count;xmlSha256=$expected;fixture=$base} | ConvertTo-Json -Compress

} finally {
    $env:LOCALAPPDATA=$savedProfile
}
