@echo off
setlocal
set "REYRUN_START_FILE=%~f0"
powershell.exe -NoProfile -Command "$src=[IO.File]::ReadAllLines($env:REYRUN_START_FILE);$a=[array]::IndexOf($src,':BEGIN_POWERSHELL');$b=[array]::IndexOf($src,':END_POWERSHELL');if($a -lt 0 -or $b -le $a){exit 2};& ([scriptblock]::Create(($src[($a+1)..($b-1)] -join [Environment]::NewLine)))"
set "REYRUN_RESULT=%ERRORLEVEL%"
if not defined REYRUN_TEST_MODE pause
exit /b %REYRUN_RESULT%
:BEGIN_POWERSHELL
$ErrorActionPreference='Stop'
# Windows PowerShell may inherit PowerShell 7's module path when launched from a terminal or CI.
$stockModules=[IO.Path]::Combine($PSHOME,'Modules')
$env:PSModulePath=$stockModules+[IO.Path]::PathSeparator+$env:PSModulePath
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
  if((Get-StarterDigest $zip) -ne '69e66b04240b10aba5229ccd7680490ab45ed53d5d861383e47ad8434e5cf966'){throw 'Starter file is incomplete. Download again.'}
  Expand-Archive -LiteralPath $zip -DestinationPath $rt -Force
  $n=(Get-Command node.exe -ErrorAction SilentlyContinue | Select-Object -First 1).Source
  if(!$n -or ((& $n --version) -notmatch '^v(2[4-9]|[3-9][0-9])\.')){
    $arch=if($env:PROCESSOR_ARCHITECTURE -eq 'ARM64'){'arm64'}else{'x64'}
    $tag='node-v24.22.3-win-'+$arch
    $cached=Join-Path (Join-Path $rt $tag) 'node.exe'
    if(!(Test-Path -LiteralPath $cached)){
      $pkg=Join-Path $tmp 'node.zip'
      Invoke-WebRequest -UseBasicParsing -Uri ('https://nodejs.org/dist/v24.22.3/'+$tag+'.zip') -OutFile $pkg
      $sum=if($arch -eq 'arm64'){'b3cc74a295b39d4f273271e96f58c06dd2b35757ca12abec64c7d0598b434f14'}else{'e612af99f626ab415ea225af6bce5c971feb448cb5cae250bb1c3fa50c5f7d9f'}
      if((Get-StarterDigest $pkg) -ne $sum){throw 'Official Node archive did not match its published SHA-256.'}
      Expand-Archive -LiteralPath $pkg -DestinationPath $rt -Force
    }
    $n=$cached
  }
  $mode='jobs'
  if($mode -eq 'git-handoff'){& $n (Join-Path $rt 'git-handoff.cjs')}
  elseif($mode -eq 'rdr2'){
    $game=$env:REYRUN_GAME_ROOT
    if(!$game){Add-Type -AssemblyName System.Windows.Forms;$pick=New-Object System.Windows.Forms.FolderBrowserDialog;$pick.Description='Select the folder containing RDR2.exe';if($pick.ShowDialog() -ne 'OK'){throw 'No game folder selected.'};$game=$pick.SelectedPath}
    & $n (Join-Path $rt 'setup.cjs') $mode $game
  } else {& $n (Join-Path $rt 'setup.cjs') $mode}
  if($LASTEXITCODE -ne 0){exit $LASTEXITCODE}
} finally {if(Test-Path -LiteralPath $tmp){Remove-Item -LiteralPath $tmp -Recurse -Force}}
:END_POWERSHELL
::DATA:UEsDBBQAAAAIAAAAbF3MInIrpQgAANwTAAAKAAAAYnJpZGdlLmNqc41Ya3PTSBb9zq/oVE2NpEJWnAwwoKyZYkm2KrsMUAT2USFD
::DATA:daS2LSJ1a7tbToLj/77ndutlG7aGD7Hd6vs+99wrgsYIZqwuMhucPDo8ZK9YqTJe4iwvFPv99fuEfVwKpmR5z251YYVhXAsmxS3T
::DATA:YlWYQknDCmmKXLDCGqZuJbPc3LC80CKzSt8npPaMZ8tegBUQqarG8utSJOyVVVWRsSXX+aQs5A3LtOCW7hlRQgcsMlPIRSnYbSGl
::DATA:0PAGR5pnInmUwb5lc8NmUP/fBkbDQKpcpHMTRCftY7X/WI0e19wu9y7Q4XAl0/e1VXuX/PFwDY7nCEHsXewejK4qZXGt1ioTxiRC
::DATA:rpIPZ//58Ontl3+9+/CPi/evXp+xhwfnW/JVFTJUJlmqSiCvYRSzwF9mf9VFvhip/aquKdhBjOzgOp3TrblJqhvouLiXWUiHMVvD
::DATA:16zRpliJlFndiJhV5DObql+nU7bpdRs+F6ddWckIm71E6pPSWG6dwjpKCtNfCSP288/sYP/GxX11rcoie4Nqh1BfzFl4sKXduR1R
::DATA:AnbOyeUoYnap1S0701rpMPgEDHPJlM4LyeGZR/Ct0jemBkhGUBzyVOTvubVCS8Rx+Mcln3y7oj/TyYvJ1XoaP/l189Nhd/dGULRr
::DATA:e1+LNKBmkYsgrr14GnxfONh00lJZsS9e8bs3Qi7sMj1+Mp1OcXveyMyjvhZZKHmFOuTCZLqo6TgmqNRC20KgZi26cii+vIrY+hHD
::DATA:kW0QztpJjgULWTf2IluKiqetF+r6KzKCIAaVncaY53lBcrx83z9N57w0YgMvN11DcMtLtSD7sO1cDq4dFr9QrRsTxMF5LqQt5veo
::DATA:lmiLkoMCUJG65HaudIWy5aNCZbzm10VZkMmEvVWgGUtPUVpmlqIskyBeb6K4t1gWxn5x0I6DN/juqef8FJSx4kVJ/MJgB9wiczWf
::DATA:M7QwRz2W4BCEIZEDpDBbcrurmPr1C1KW3dRoImQq+IATsA6MOaeJ69A0GhH2vJawDx3DfRNasUpwkCMFT1JLboAFNiglm3iQAl6b
::DATA:+JI6NLgauWD4Smy7cIET+F3VpSC/XWbIF7IgxR0a1Io6YRdNXZdt0jmx37URegWBwc9X6JbG5tyOTomVtfjqcjJyLe6ed9iBL2Ih
::DATA:NCBcyKJqqnS6iXMlRUpAj8kP960LKQ46BfhK9/BBlxDro6sR6vsmDYvcA5pYgUyqObqVHcxmrOsexwt9BycYStZJ4fjwj5A3dw+o
::DATA:7kOt5YNsSnyvLo8mL64eytq6L9FPh73MDpW8XipFbAK4Ke3YlFE/MdNgfqGAC/yYuKI4LmHMdwOcnw2U62gVuk9cECH4T9wBnMYR
::DATA:IK56WtzmNTrepTVpUEm4gSLtjFRvu+14HFNf9plEb1FwOI6HVIYH+25EPWdQrYt8KDXxURcbxW9mkKae6CYHiSfzokT+Qzl7efjH
::DATA:53z9fPM5+WqU7LIroygxcD/sEnHgVCWl470/ZxwmxCizFJNXwm04OYp6zVszhoRozPwNn+F+VsVd3TV+11yMcLad1b9fvHub1Fwb
::DATA:Ebaxk7pefxw0dv48IA9GqdeN9MzNZ6CTLvV0MpvNdvhxSIA/T9uRHsQroV0igqNkmkzB0i1bpt2y0B3EVoNhCCI0WLCwBTHP6EYa
::DATA:eLp1sKFuBEH67S3t29GHL/Jgc7Lt5kCqWzXCENjGgIP5+rawS8rMR2TQpLQ+bHpkrGYvV/sLwU7jrhIyDKxUvPYS7ncLnc65g8vv
::DATA:cPIuRV4lhczKBsMv9Dp3S38j3X6qVLnXvgP/cGDtGiuWKvPZqJf88U6udn3qMwbhzvO3TXUtNK096Phzz54w0tUhengYfvxlOv4F
::DATA:zoOe4eZ2OP2wQRBzbFOW5g/346AbTSOIXwtARpB/+h4k2iYADg72Xs5etP92TF1YDjbkbu0nTjw/bcWhMuw6VZQ5A1df7rA8mWhp
::DATA:nF+6W1eIq6Pyh4eD7jTBSRVSOroDzxQv3Ya04xF2kxW9c3ieJotuFLox6ADfOTjed6mM62HZdbuuW3XdprsZIUIL05R25rjJFX6g
::DATA:pyFdj4/84OMJffjRxxP6iAmZeUrpOgWCwiix6vzi3YWLuQW1N2SreoffgqQWEpvsYhI89u8Xiab1pfr06fwUdBbPseWWO0KtZu/2
::DATA:ABgQWO5qFz6Pg2kQPQ4cQ/epcZzQ8xp8iT3v+eJgdWs1xpijZXwM+c8Y4+t5yRdpcHsXdNl71mUP2GJrImNs9r1O53B0sqGguc2W
::DATA:oYjWAIVIMkhTF52d/fv84mMQbVX4VbeoYT1jLp/AmDZjlFN+x/tUdOI1CGfLmS29P40ce+R9aTvVRzhsti37mtllcDw9fjo5Opoc
::DATA:PwWc3Y/ps8nR8/7HL5PjZ/7HE7o2fRpsbzTYaincyiyidhTga1LkiLmRuYCDIo+8GwMirrkRAB7KpOssDY5pAhR56iUdcgw416tN
::DATA:KmGXKnfaKblYXbCfYX/mZfFNBGnP30mSkN7YB5uuMUmsylT5z3bUdEEPBEraMf54ZX5Ldm5Hvw0Pkx9pupxexeN9HusjaBcfm03s
::DATA:9lF9Lucqda8rNJTuMTsnbmpN/Dzcm4ObjYu+i7Mm+kh/FOD2XWf6kAbbjyW8e+17zffE4VoZpO7YAX39I02oowX5ppftxmyJCGP6
::DATA:m+52F/aFcaLd7jA+4HrRVNBloq4FN1fwbdN60baT1tEPnSmM6ydPdv/HMygBmozhCzEyAZByUrOrXTida2rgdPLL8bPpUdwKp8Hv
::DATA:DpPEwhgPwHngk7lBh6ED2vdMTPtCog9AIA22te7/RxL3fz9uSuo5XgnDtXt77Tcf2nJknOlyfipKfp8CQ4T3e+wcStL7IE0e+jt7
::DATA:ufZ0tO4JfdY35Gi3o7tY4pxjJhqZwfuRp8dwnxE9D44Yja3/jOR+U7ua7uQSk2jI5blcoZVzx8rI42CY6NbnDls9bYBmtgaa4i5G
::DATA:pPx/UEsDBBQAAAAIAAAAbF3pc+CK9QIAAMkFAAAPAAAAZ2l0LWhhbmRvZmYuY2pzdVTLbtswELznKwj0QAmRifYWyFDRPNymaJEG
::DATA:eaAt4iCgyZXERCJdkrZsOPn3LiX5ESO5yMiQ3JmdnSydOSDOWyU8HR4Io50nYppZ+DdTFiKqjYRUlKqSD1NrBDhH4yR3exfygJp9
::DATA:1AR0yn25hwcIT4RdTr3Zp2pBGq+1TLiDrGdmoOfsavT36vbi4fevqx/Xl8eno+fnUI49GqUj41hpapDKRnFCu5vkxCpZQKiYz7Tw
::DATA:ymhSc7wcrw5Ix5Fn2xKBL6El19Lk2FVCH81kQA87WcwGvL69/X4WxcxVSkD0MTmK42HuWP2EvNdLLaI8WVkQM+vUHFJvZ/CC5D1X
::DATA:oXwWMca4LVycfRZTBgsQX1UF7VOK5zS5owOB1DgayzSvIetaQWiLAzZRZZURvPoCC15PK2BKz3ml5PqeMHWtPCumhVOFznJeOdie
::DATA:WUCzzJO7DAOih1sLcmTQyCEH7TlOqtd7n6xEI9M8AS2MVLpI6cznRzRpFNrSuHMld/rFTiKqdOiHDv6FzwQ/wXr8cWZmRTsUgtY1
::DATA:VnnYePBKSX8xoRejPzeslqiGfiDn3XzGeqzPjIaUYEIeQWB0LXAPko31BSx8SiQ4YdUEiC+BaISI5+6JKE2WWJiYRpPG2CdvAfAN
::DATA:3egenNIdbi7lroLhG1c6r9tWa/xee2494aSdD+nj1LVrbNRFwZoKiMnJHfUoDB9ZmCto6H38Rv21yo2ajaWhTLLrWQDibeImMy0r
::DATA:yF652gti3dnbHfVn2FrrKU06AEkHvKres2rzag5W5cv1q60cpXOT0Z+7vqynlhJ6mB/Ssb5pzGYsLiXBnoR07jBy0hZMyesexnrE
::DATA:RUlEyT3B7Dr03sGUW6y7nTC5MCTHmDnSgMW1BxpnpJdNiX8x2ktE91hliigIbf+x30tntyqub46vbpjHAcZJeBL0B3NeDrxdrrpN
::DATA:M3wR3Isygni1ZgBrMQj0m0JHHOl3oAzpwKgi0gWnjzVDY4DVuAJ5gVZu1uFC+VNcmtmn4cvBf1BLAwQUAAAACAAAAGxdt9Ga25cJ
::DATA:AABzFgAAEAAAAHNjb3BlZC10b29scy5janO1WGlz2zgS/e5fAVdNhWSGomTHySTUKq4ZJ7Pjrc1RTlJTux6vCyYhCTEJcAFItiLp
::DATA:v+9r8NARZ44P60okEkej0f36dbeCmRXMOiMzFwwP+n32IdOVyNnYaOWYUHjShrmpwH8jBNOVk1rxghU6w2dl9MTw0ibso9YF42Yy
::DATA:K4VyFk+C5dzxhGS+U8XCy+AZ7bbsRhT6zq+B9DtucpEPmRISawwT99I6qSbM8RvLVHM89DSBZbmwt05Xfi93jmdTkScHGYQ6NrYj
::DATA:I/47k0aEgdK5SMc2iOKKu+neOA1hJqv2xrOpLPJr3CkTlrYawfNCKrG3rB0OomFzst4/WdvN5GWJkfhOm1tb8UzEVs8MvpIkgbns
::DATA:1ag5j97miS1kJsLjbjMvYCmRvzNyIpUdKXHHPggXXgZT5yqb9vtGLMxM9bIpdzfa9W6MzCciwVAmrRFSSZvQ3KRyiZVOBPH+TpOb
::DATA:417B3VzaW/mXNorbmbFyLnq5EFXPCm6y6e8IuOouZflYvOWlsKNlVfDFHS43dellcGP0Hdx8rfhcTrg/sx2yild2qt3WkOO34tpm
::DATA:QKXyM1dxLuYOMLQQtSViZ0mmy5KrXBisKYCz6xxOy5w2C6ycCHc9loW4lmqs8U6O9gPB1Xp4IMfh4bubz1idTLl9d6fC7h4xuTiK
::DATA:ECKA9WtjtAmDT+pW6TtFIUIikg0gNgpdaO3YiNFuNhqNWNDeIDhg7BSATqBCQXD9sFBZiPfyNneirPwrjSeftVShtokrK1wljGIW
::DATA:NP5pZfWCKIogL2VqVhStEo0VX6s5FNjVyJ+9BD5bZAo1j9nHN+9fnV+ke2v9+AODr78eXXsdtmS2qviwG2VVgviAVbsV9yJ7jyvG
::DATA:l3sREy+zuzzdBBREpZvrxNblUsO9lazI/c2XVOAWSRC4kyrH4l8k4tSZmVh3jiFAXCCOhXWbUAMNQPnRvi+64x9yayMDlu2kEH5Y
::DATA:uGuRiC1hk/a+WoUBuA8QZ2HERi/9JGPOLNjSQ6H0B++begn81nGYMrpOTJyadS8lv78Q4HdhU/YkZgbPi1cCUZeyo8EAd2drf0zG
::DATA:XTbFQf3H7NfaQNi6QGqQRcGmusgZbzGDtaBdRqhm+cwQVdvpzGGPStjjvhdIRl0fEPmfIShKAeoGtZXszdl7hnh3wjIJA71/+3cm
::DATA:FUSPjbBTVgnTy3jlZmB3O7vpYpMhZKF6pY2r93no76QWsKMDWSJ1eThBRwURVeWnpWVzXsxEws4KifzU8zMSi0kQkoyY41rwL0zg
::DATA:cx3iJjkYg8ooX0E20f0rMackZ89qBUNoPCsaH9YIqDWE1BGrJxNk1llGq/Mz5FOcfJqALiyfCHZ62i7K2qkxDB9m5PoscYuq4QQn
::DATA:7l0QnSb0PcRZhCOa1ePNgYe0kNK4mgRstWKH3kDS/nhjdTFzpGy9MorYDku9kdZ6B3aoqm1LbNVea+OGUT2JAQXa2wht1dqZ7bZF
::DATA:Xr091iMl+//JPDg2VFVmVe+S97782Pv3oPfiavls/V0fF7euFn3DrdiTHXn0MpK3u6RTrjFOd3xSNUbaD+ndHZu3Jg53yV3cV9AA
::DATA:pt+yHNVEBJjGeuvOgoAm8TwOLOhx97TWeIc0BZ/9jLgCAUBBP2DlF8H+xk6e7o68ZE+O2WPE8PFJ8xX9GRVp745zYYxaM0p2dPTD
::DATA:ymFZgojkxvBFOIifR4nTHzzewmAq7oPGys9fPB2ciJMfBvmAH/EBD7a8AwmbPdxmUgbx0XF89KzZe/7Lq4sGvFhK6nw6V+7J8U+v
::DATA:Q1rz4MTxINo9odOxd3T8DR0Hzd/Ji5On0PWEi5PjZ4Pnx8GeAc8VOENuW68xHIw1I0a4/dpUnqYBTj+zASlNgXlnRrFlE+0pu1xS
::DATA:FKcskCX4AKxfylJ83BrqE1BjX0ane+YjlD87CaI1FSbrDVOJUrqwjJZtTkEu1DOXeMYN//Hh3dukJgk5XmDZ98FvClfa2o/YyWm/
::DATA:51DaLdVf2Oxbh5CiL+YRooYqpq5G8mXwVSJVVsxQxftleyXTRyJqIgKGb+htkaI9H1tR1EjeLqZIPMkESQZdWRdEPlprbDuUC+Lr
::DATA:1O15AtyrizlogpIoT2hstQogmMr+YtSsQV0s20W1NO9LOppW4eQkCVYrPMM2HNnpV/QwIQ1+7yVYUUWr1ddkXOzd/GyqNRoxXidV
::DATA:ZES69cXrf118esu6SqOBHx1OxqPTNxVqfW8/edj/LQndvVuV+eqz1WpV6En0XV/WRNpcY7UaEzwaMmoGPbW8PBqcPH/6w7NvaGhL
::DATA:pFlGyYhtXEF/LcDptmktMNbjsRUuHcSFUBMMU8nhl/uio9nRXmavHj/dkZSLivav0+1RkrU+2DZIV/evVu3QV13FNkSAROdLvU8X
::DATA:/wx5MjNFZ+PD3d6Liv6QlifaD8CC/o0aUzqqea24tfBY/gCyPUJQZyBK0ANveurGz8A2NReMmiXbmrU1KhRLvXzsGDfXbufWQ4ZK
::DATA:6K1GU3wjneFI1B5GZKgYnyg2wGGyQrEowT2m7sIZGuuptrUX2awqNEcnvT5ou9sEtAdrndOOMdAXLqWqZi7dohap4swU47qcPFco
::DATA:X6RbrCNfyfoGOfbd80vYuxCOlUPUnsty5Kmk4saKkObBIb74XNb3GdYOLVEouanOyYO+NugTPOC77SI94TnoKpEg34a5hn8gJINT
::DATA:GwCQMjVyayh4vJSkGC/taeJpbPOLxs/aUPU32ia5zeJu2Wq1XLcBscVPXV/HHj3q8L7VmEYPdA9bl6vl+StSX1bG9bnpsuba9vB0
::DATA:X9t1o4uPNm/kUERLnySWxAymytLgOBkEscxTOiquS9J0Ka1Hrm+Q4jZlNRmrrkhj+kxFW88iE60pG3SY7ULzMiBcSOTSL9SIKe3k
::DATA:WNaFku1vpnLfq1HG21uCSj4TVNkHW9mj9WwULb/heZkj28+QEwBLZOffu7TwV0VmRkfYe4Ji4ChubpV2bXx9XOAt2kA8K8CIQRxG
::DATA:QPh2wiR9omE9cov2CS+0648CqxOBzPf/j6to+ZCVaoj9dSvVbVVjJIuOwfIb8hiZa+f4nejNkdaRDj3GHz0qkxp86HQoVKL2vX4d
::DATA:7b6iVypgvxBcWY5efrPIoOmkrjTqguGBMNvWgsKzPYieD7tTm4BouoG6KW8nRw83iO1022O3LXa37U9HGfKH6LrvHDUpIqSlf87q
::DATA:MpVa6TG6qbo/NnIOjIEy0N5RQ0KFImmBf02NSDAeHtSg8z89kCZBTLAiPtRI7X4o7EI8Gm5+mpHujKjtaLgnxP9+QRAZvdxeHNLQ
::DATA:ajUgN/wPUEsDBBQAAAAIAAAAbF0amyKdQQsAAN8bAAAJAAAAc2V0dXAuY2pzpVltU9tIEv6eXzH5wliFJBNSt7dlyks4Anu5SwIF
::DATA:pHa3WB8lS2NbWNboZkaAy/Z/v6dnJEsykN27q0oFNNPT069Pdw+81IJpo9LY8KM3/T67KnOWyTjKsmXITnImnlJt0nzKTrOoTAT7
::DATA:KPTcyIIpESWamRlOx7IQCYtlPkmnpYpMKnOGf6nRLBdPBuwjZcI3INCGTfRQiX+XqRI9nstEDCaae0fVptzdlK3NIjKznW1aagji
::DATA:Ymc7nqVZclcoGQvdYhSrZWHkLq1dbIiUlGZYHQ1F/hBenf129e3r3S8XV/+8vjw5PVuv6fbwXqZ5T+pwJhciSVXP87mjZH9TaTIV
::DATA:DceoKIbNEeLvc1XmJl20iKwxn5H9ItVcF1HcIpSleUZ2fXNydROaJ9Pilxox5DNjCj3o95VY4sYgnkVmLE0wthKGWIpTrUSapzqk
::DATA:vWlhQjqIiJhgzzr0UWHhBu7sTdJM+Aa/eauJDu36OZaul3nc7PkrkccyQeAMeGkmP3J/QVY+kD8cHGy8o03DuI4b4Q7n0UL4Ijdq
::DATA:6a3eMOa0QEDOh7S9z8NKB1qCfDXFJBlCGNgut3LQrs8fn7hvb/QaQiMWRc2K7zuvhyrKE7n49u3Tx56HdbMoLGsIwUiI+qxU6TTN
::DATA:o4yusnmht0p7x1ijnOiawunuDfIyy45anJLIRMOa3fE/ri++hkWktOjVa+BVZHB4r/+v38vzs/Pzvs+55w1WG8cmnfTeEhO2XjOz
::DATA:LIScWJ5vh0Mux/cC2Uw7J0pFyzDV9mePCDzPzJR8ZGdKSdXj35CgBagpf7MUZu+mcci9ttRaqAeh9JAYhYu4uHbfx8dtqSqi9boS
::DATA:q/puSbZed+WqKF4XrbnqFfFw74XlHc4iffGY1yxtNHme86Els6YmvMun6WR79S3RjbzhcLiz7wLRU8KUKmc8ysjFyyZmE35U8e7I
::DATA:fjNLgX3gyeoTY5HJfArAlCzKJWBT7ajCvkomIYvNp61im1q9Oi5gRoolD9EGpFh2o62bIeMonpdF8GKQ+/Y8fBrlRoenF5e/nX/6
::DATA:fHZ39uvp5+rmHR8PV2EY1lZ15hpY41Seb+CBEszfMSMx80lu/xD59Xve8lvvf8olD3aoTdINm9MXwpgB1PKpSEIUMYl6R5VJC0Nl
::DATA:TbPHFGZ5hFcS1DQotLW9FYI0tSJYtax0brcOiZ1Q2LAJyZQBOKBcVzdi4ZHnyjxL83mzdkTeIMmcsoldaBERmhFmbipQTwSqqEPH
::DATA:xQKCCzVYFXMg7YdHSV+Ps2UgVD9xpTrYUn04CN+Hh9wfp/mAP9vlGx8sSUW91JCr5knAneFignUURCNjmfVdKAQN9YdD8D6oeCNu
::DATA:gmcUjj9QbYlgmc5Mzb9Z6eMcZDwIf/xLxajZC7DnOCTiwUiZ6ep8DO8vRFCvEt2Hd+G7RpgXCDhs2aptebFA2PQsTkwQRFVJgeQM
::DATA:AHbblFn7G6o8RUVv2xw8ifgSG6j81EncwV4ldO6Dax8C0M8A4BreowXx/zyvMOxn6bj/hyxH3rNAs2FagxZ92GLWBShSbZLGaZQB
::DATA:edDXVZ0IW5RQPc3jjJo93GPToVWuUwKNLLuBKXsUGT5UaFVqhOaQwvOW9kZN2YWraD3Ez1BnKQrbgV9/Z5E2nxCBTxeTHv+AKocd
::DATA:3e5ucEXXttzHOZuIVHG6yreOgYvP0TbNI3Q591oCd+piUDV5Qg/jIkRr9ej6hl0/AOqq2PB5pTn3eRAUSkxSdBdWsiBIp7lUItCx
::DATA:SgujLUUuA9gsqX9H75wa+6GjBxGIpwiFsLbAyF9pk6RygDtQGYgQHeeAILfVgfqXJzd/H3w/bPbdtsjSBfBY7bcbWDq+2TTIC+UB
::DATA:0ZEpqTYfdFH00hmNARnzTEYJS9KEoW4RuqV6FrIrQb2W6/+pzmE4yGOqaihwbRjdbCMAIJNOyK+tbmcX57/vu7oC1I6vOYZUlBCb
::DATA:UKMbYq8F2P6713uN6kpW8azUcCog9YZVV7O9m9bQ2rhax4/b64P2xy0Jg5+jOmrx+3r9/dgFiee97Bhbex1ELVKtcXclaZX1L3Dq
::DATA:pDH8mJxaYOy1spdO6e3UA/A1gMMF6Ycq+f6QH9/yy6uLn69OvlC7cI14bn/2fv3xBw9rny9OTz6fXF5+PLk54aMQQiIUe/PhT61o
::DATA:vJ2PvHARFXa5wcQOgc9/lnKaib4TtH9SFHCrreh9B+oU+NQV3/L2pu67c8ydCzF49U+pfqHX6X+J4ovrLgH3X5vk/h+mON4vtbJ4
::DATA:baVNywVvrU0tdeAU4aMd3+mQPNQrhj/tRIjX9SPamLJwQDylXndVRdctv5djIBEgpOqM52KpKSM0BFOJOoRnKpjX9vyzlJjnSH4G
::DATA:l1CUVdHVVMfElkY7d8IUvp1bR9TcLOYwnpU18VdKxCXy6EEMjCpFPQP+1c6A26gjKBvyqmvl+0REm5kwLszrdMc6haJVzLM7w1XV
::DATA:vQyeAXekpnrQKt0kJK8G3tjWTYexu2P9gFTa2K5WZFqsarSsb7em29vrvSVzI4HtDZhkxlpmpRE96wWX2ASuO2lNuz6/+nh16ELX
::DATA:X1mjf5p8lWek0GAS4dKNdwyWhIq93fw/nUnqYAl3iRcckiVuljARoDmfspr5EfC6oqEWjD0KJbaNcHeuI0wbdhQ85q2+bVB7pKZ3
::DATA:MTu8bbVniOy6wWoHFnFGO98Cm9YoDKv+WRZ7e2/dpd7zOauKUFa95+i6RQGYV7nKqN1xVqA230R6jppsRH0UxpFqjknAzGRpWMTG
::DATA:uAP9646ZiGi4E1FVuUCmWTmPOglAB3ZzYNNhSeFammiciWG7sSJePp3uEFNI2/pDbmra9uPb0aBebXkNWB0EdjrJRUBBDRltlhIm
::DATA:2EA8vnX1NyOdrMA2eEeD25HXsGw5yLKcoWBn9J5mGx9EfYSyaT8aZQL7MOc7l4Hfd4+hVi/qNuk+eohcFxWIhygrLfRu+ykoF+TR
::DATA:Qzp1iFyvlxoeCCjb6Kky3q4XQlH5ivIYMKvKpx0hL9syOjs7UHnJmH8ENA1bMi+tjTaD/xKd3ENqYDPAYZQNqsprL93Q7bBiXJVi
::DATA:1BYvvVvenF3f3J1+/nT29Wa9Zr3Xa/zeXvt0VcaPX6zR9a7P3eMwhvOX+CaRAmt+/FqV/ZyOVaSW7RLOrsuikMr0t4zt1N9+xnsy
::DATA:AKDuU6tPj5boSVxWDxjft6+JzfMpLblKVdWUrcn29rp1drvRHRiIbwsCtlQ+j62gd9VUfeeeBarG9YikDYtSz3q8+4xOAr3+ALrP
::DATA:Q3Ze0mMCkM1UTxTbvhsxwx5nwr6gPoicnj3qprupXK2bv0qmnVWBjPaJf/dNv0bSRBjbDNtHKXoQZo+RfXrL3TL3Gb/MUG9QVMaW
::DATA:YMCsWLAuPLDP+/bJv28ljl3FkrmDYBoQMD2h/4cGbEZvUpMJOPITes2AaVNEeCWeHYq2D5MRhs8Fie+0T+7hUKx/Ob10eduaOJrX
::DATA:qG6KkW33eeA41lPFzlvVqnn0Gqw6L12b509YLfOep8rGpTbk1G63cszpDyrMtR93bujyGU2CsAHGpnheQETjk2a5/dNKM1mBQehK
::DATA:cKs6Z6muzJBl8hH+dH2Aq282oNRi2wmwlGqi4ygyN+bAHS2urWLSsK5ya5s8ljeqFA1KEFsvSCUqoy1Gbch8VUifxVDRkO62CkO2
::DATA:7iXWAAh4esEEc25jK2JFOQY+WBOjR56KWqm6mtRlu81DM5Ma275afzWBgUJv/1DhgsM6tHIrZbrEkUxOezsUtve2o7NtNTDA2OnP
::DATA:vUp4KwTJyjXkNQwCph9uD0frddWOd9bfj7yjDfAunvWEUt6qvljY5gb/hwvQQlHvqCkgqTklW7872mzeuHuxSFmhh+5uf4snKA//
::DATA:AVBLAQIUAxQAAAAIAAAAbF3MInIrpQgAANwTAAAKAAAAAAAAAAAAAACkgQAAAABicmlkZ2UuY2pzUEsBAhQDFAAAAAgAAABsXelz
::DATA:4Ir1AgAAyQUAAA8AAAAAAAAAAAAAAKSBzQgAAGdpdC1oYW5kb2ZmLmNqc1BLAQIUAxQAAAAIAAAAbF230ZrblwkAAHMWAAAQAAAA
::DATA:AAAAAAAAAACkge8LAABzY29wZWQtdG9vbHMuY2pzUEsBAhQDFAAAAAgAAABsXRqbIp1BCwAA3xsAAAkAAAAAAAAAAAAAAKSBtBUA
::DATA:AHNldHVwLmNqc1BLBQYAAAAABAAEAOoAAAAcIQAAAAA=
