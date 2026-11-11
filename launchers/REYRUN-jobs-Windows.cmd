@echo off
setlocal
set "REYRUN_START_FILE=%~f0"
powershell.exe -NoProfile -Command "$src=[IO.File]::ReadAllLines($env:REYRUN_START_FILE);$a=[array]::IndexOf($src,':BEGIN_POWERSHELL');$b=[array]::IndexOf($src,':END_POWERSHELL');if($a -lt 0 -or $b -le $a){exit 2};& ([scriptblock]::Create(($src[($a+1)..($b-1)] -join [Environment]::NewLine)))"
set "REYRUN_RESULT=%ERRORLEVEL%"
if not defined REYRUN_TEST_MODE pause
exit /b %REYRUN_RESULT%
:BEGIN_POWERSHELL
$ErrorActionPreference='Stop'
$base=if($env:REYRUN_WORKSPACE){$env:REYRUN_WORKSPACE}else{Join-Path $env:USERPROFILE 'REYRUN Bridge'}
$rt=Join-Path $base 'runtime'
[void][IO.Directory]::CreateDirectory($rt)
$tmp=Join-Path ([IO.Path]::GetTempPath()) ('reyrun-'+[guid]::NewGuid())
[void][IO.Directory]::CreateDirectory($tmp)
try {
  $zip=Join-Path $tmp 'starter.zip'
  $encoded=([IO.File]::ReadAllLines($env:REYRUN_START_FILE) | Where-Object { $_.StartsWith('::DATA:') } | ForEach-Object { $_.Substring(7) }) -join ''
  [IO.File]::WriteAllBytes($zip,[Convert]::FromBase64String($encoded))
  if((Get-FileHash -LiteralPath $zip -Algorithm SHA256).Hash -ne '20a486446b5c4d641d3772afe39bf77f6e3748325c2370f68aec233fe3a4e730'){throw 'Starter file is incomplete. Download again.'}
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
      if((Get-FileHash -LiteralPath $pkg -Algorithm SHA256).Hash -ne $sum){throw 'Official Node archive did not match its published SHA-256.'}
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
::DATA:M3wR3Isygni1ZgBrMQj0m0JHHOl3oAzpwKgi0gWnjzVDY4DVuAJ5gVZu1uFC+VNcmtmn4cvBf1BLAwQUAAAACAAAAGxdEk9P+PEF
::DATA:AAAtDQAAEAAAAHNjb3BlZC10b29scy5janO1Vm1v2zYQ/u5fwQBDJaEKnWRbN8hwiqErsA5DMiQthiENAlo62WwoUiOpOJ7k/747
::DATA:Sn6J+4Z+WIBY4vHuyLt77jlFjQPmvJW5jyaj8Zhd56aGgpXWaM9A45uxzC8A/y0AM7WXRgvFlMnxt7ZmbkXlOHtrjGLCzpsKtHf4
::DATA:BqwQXnDyeanVKvgQOVk7NgNllkEHvS+FLaCYMA0SdSyDR+m81HPmxcwxPRyP97SRYwW4e2/qYCu8F/kCCj7K0alnpZta+KeRFuJI
::DATA:mwKy0kVJWgu/OJCTCHfy+kCeL6Qq7jCmHByZWhCFkhoO1DbiKJkMJ99UKE+Xxt67WuSQOtNYfHDOMSPudjq4pNUDd0rmEJ9tjYXC
::DATA:ZEBxaeVcajfVsGTX4OObaOF97bLx2MLKNvo4Xwg/M/54ZmUxB46iXDoLUkvHaW9ee+6khyg9tLSFPTtWwj9Idy+/yRDuG+vkAxwX
::DATA:APWxA2HzxRcc3G6DcqKEC1GBm7a1EqslBrfw2U00s2aJlbzT4kHORThzI3Ja1G5h/J7Ii3u4czkCT4ed27SAB49Ic+hqz8UTldxU
::DATA:ldAFWNRRCKW7AkuXe2NXqDkHf1dKBXdSlwbXVMsgiG7Xk5Es46PL2QfU5gvhLpc63saRUomTBLsAkfvaWmPj6J2+12apqQvIBd8B
::DATA:IiBpmtcc8YBeNvWHR8j/RPClNwcISdt8WWR7APKFNHj/WtYU3/CQGvtDUoxLqQtM0W8S4ehtA+vtyRTxFcIVnN9hCaFsjJ+WjmO8
::DATA:iuB/vdJ5vD0PrUssKjUng0r6uErazZ3xKqbxHCvoIf79+vKCE13ouSxXqPY8eq8x7PXO3iFpkH1IAVlL/Q3GgX1ijRlPRdKOGFVk
::DATA:W4PQZrdc6lw1SARB7aAkbxfSMUIIwyfe22GGAn84UFhWZLb9YpF78jmdTqMtbCI6l7E+nR7LAx9njl5Q4ox6gJhymwpOsq6L0DEx
::DATA:h5oOOth3cqPUe6ODGR1NWngy51HX4TvmRljv/kIajEn4PHhwUCddF16l+2WGRzaYS1Q/iPzVwhjkcsEoOiZ1iPrq9d9X7y7YttB9
::DATA:1OFwSh6dvuuAPu6weTR+z2P/6Luq6D44oztl5sl3Y8k94ioewui6kuAhfEjJIEQi+BfOT09++PnHn1585oauQs5jHh4925WC/iz4
::DATA:xmrWUrRZ7zA1ZenAZyepAj1H8enJyTqor0c7i00wB/3+8omnAmqyX2f7UvK1Hu0nZMsrXbcRfcRa+xBBJPrQae+u/ogFb6za5vjo
::DATA:KbcTqcSkzk0QYAbDimYbHTUsa+EcVqz4BLIDQnBGYpfgGN2N5aHOiG0iL0Zk7DZp3SQVL5YF/2hRDmFv9tYThnP6wuBcnUlvhV31
::DATA:MKJEpfg7xwbKrax9isjCC/SDnOFsXhjXV5E1tTICh/F6tBmQHGkZs/WGLEpEX9xKXTc+26MWqdPcqvJXbJNV9kaXOFP8ap1wo+Mo
::DATA:zNg0DOBzzLcCz6qJt6u2mgYqqYV1ENM+ckgufL5o+3gmfUErXoFfmIIqGIbGmOCBtdvnSC4KpCsui2QyMNfkK07wu0cNAKDL9CAI
::DATA:SKnoSvg19JLTsvfXIsVXaS/P2p7YNl9J2T7d7Yy3+13XrpP1mhiS0EYRxpC0gaFbaktb51l0xk+iVBYZBYHE4xrls1a6AJswHHAi
::DATA:YgU0jt/Wr2rIIuq8KKXfDDA857C+69vtQUP8m764iagoUihsbBxC2nhZSrwMfcmNd1tFmFN6/pFKLnQOSqHCHnVv0pok7WfSLouj
::DATA:6bRBQkZMQJF8KWgIoWIlcBoef3/24uQ0HaLKtjO6Py6iIEcDvnKFdBSlcYLw2p9WdJ9k0kvupVK4IKuvoXrrAsfO/w/qpP1UlnrI
::DATA:fXuWXimJABmShF/Z0okZVYzS9eT4J61T4EzFWRS659mzivfge8lDnySbdb+cPl1ypAzMX4xEVU3PPzvhaZv3Yx7xOHyaUAHxcyek
::DATA:m1IaAotSSig1o8GJEkTxFtzJZPcFJv0rmvinkwMnuBGllJzp+b5yTKKuO6EL/AdQSwMEFAAAAAgAAABsXRqbIp1BCwAA3xsAAAkA
::DATA:AABzZXR1cC5janOlWW1T20gS/p5fMfnCWIUkE1K3t2XKSzgCe7lLAgWkdrdYHyVLY1tY1uhmRoDL9n+/p2ckSzKQ3burSgU009PT
::DATA:r093D7zUgmmj0tjwozf9Prsqc5bJOMqyZchOciaeUm3SfMpOs6hMBPso9NzIgikRJZqZGU7HshAJi2U+Saelikwqc4Z/qdEsF08G
::DATA:7CNlwjcg0IZN9FCJf5epEj2ey0QMJpp7R9Wm3N2Urc0iMrOdbVpqCOJiZzuepVlyVygZC91iFKtlYeQurV1siJSUZlgdDUX+EF6d
::DATA:/Xb17evdLxdX/7y+PDk9W6/p9vBepnlP6nAmFyJJVc/zuaNkf1NpMhUNx6gohs0R4u9zVeYmXbSIrDGfkf0i1VwXUdwilKV5RnZ9
::DATA:c3J1E5on0+KXGjHkM2MKPej3lVjixiCeRWYsTTC2EoZYilOtRJqnOqS9aWFCOoiImGDPOvRRYeEG7uxN0kz4Br95q4kO7fo5lq6X
::DATA:edzs+SuRxzJB4Ax4aSY/cn9BVj6QPxwcbLyjTcO4jhvhDufRQvgiN2rprd4w5rRAQM6HtL3Pw0oHWoJ8NcUkGUIY2C63ctCuzx+f
::DATA:uG9v9BpCIxZFzYrvO6+HKsoTufj27dPHnod1sygsawjBSIj6rFTpNM2jjK6yeaG3SnvHWKOc6JrC6e4N8jLLjlqckshEw5rd8T+u
::DATA:L76GRaS06NVr4FVkcHiv/6/fy/Oz8/O+z7nnDVYbxyad9N4SE7ZeM7MshJxYnm+HQy7H9wLZTDsnSkXLMNX2Z48IPM/MlHxkZ0pJ
::DATA:1ePfkKAFqCl/sxRm76ZxyL221FqoB6H0kBiFi7i4dt/Hx22pKqL1uhKr+m5Jtl535aooXhetueoV8XDvheUdziJ98ZjXLG00eZ7z
::DATA:oSWzpia8y6fpZHv1LdGNvOFwuLPvAtFTwpQqZzzKyMXLJmYTflTx7sh+M0uBfeDJ6hNjkcl8CsCULMolYFPtqMK+SiYhi82nrWKb
::DATA:Wr06LmBGiiUP0QakWHajrZsh4yiel0XwYpD79jx8GuVGh6cXl7+df/p8dnf26+nn6uYdHw9XYRjWVnXmGljjVJ5v4IESzN8xIzHz
::DATA:SW7/EPn1e97yW+9/yiUPdqhN0g2b0xfCmAHU8qlIQhQxiXpHlUkLQ2VNs8cUZnmEVxLUNCi0tb0VgjS1Ili1rHRutw6JnVDYsAnJ
::DATA:lAE4oFxXN2LhkefKPEvzebN2RN4gyZyyiV1oERGaEWZuKlBPBKqoQ8fFAoILNVgVcyDth0dJX4+zZSBUP3GlOthSfTgI34eH3B+n
::DATA:+YA/2+UbHyxJRb3UkKvmScCd4WKCdRREI2OZ9V0oBA31h0PwPqh4I26CZxSOP1BtiWCZzkzNv1np4xxkPAh//EvFqNkLsOc4JOLB
::DATA:SJnp6nwM7y9EUK8S3Yd34btGmBcIOGzZqm15sUDY9CxOTBBEVUmB5AwAdtuUWfsbqjxFRW/bHDyJ+BIbqPzUSdzBXiV07oNrHwLQ
::DATA:zwDgGt6jBfH/PK8w7GfpuP+HLEfes0CzYVqDFn3YYtYFKFJtksZplAF50NdVnQhblFA9zeOMmj3cY9OhVa5TAo0su4EpexQZPlRo
::DATA:VWqE5pDC85b2Rk3ZhatoPcTPUGcpCtuBX39nkTafEIFPF5Me/4Aqhx3d7m5wRde23Mc5m4hUcbrKt46Bi8/RNs0jdDn3WgJ36mJQ
::DATA:NXlCD+MiRGv16PqGXT8A6qrY8HmlOfd5EBRKTFJ0F1ayIEinuVQi0LFKC6MtRS4D2Cypf0fvnBr7oaMHEYinCIWwtsDIX2mTpHKA
::DATA:O1AZiBAd54Agt9WB+pcnN38ffD9s9t22yNIF8FjttxtYOr7ZNMgL5QHRkSmpNh90UfTSGY0BGfNMRglL0oShbhG6pXoWsitBvZbr
::DATA:/6nOYTjIY6pqKHBtGN1sIwAgk07Ir61uZxfnv++7ugLUjq85hlSUEJtQoxtirwXY/rvXe43qSlbxrNRwKiD1hlVXs72b1tDauFrH
::DATA:j9vrg/bHLQmDn6M6avH7ev392AWJ573sGFt7HUQtUq1xdyVplfUvcOqkMfyYnFpg7LWyl07p7dQD8DWAwwXphyr5/pAf3/LLq4uf
::DATA:r06+ULtwjXhuf/Z+/fEHD2ufL05PPp9cXn48uTnhoxBCIhR78+FPrWi8nY+8cBEVdrnBxA6Bz3+WcpqJvhO0f1IUcKut6H0H6hT4
::DATA:1BXf8vam7rtzzJ0LMXj1T6l+odfpf4nii+suAfdfm+T+H6Y43i+1snhtpU3LBW+tTS114BThox3f6ZA81CuGP+1EiNf1I9qYsnBA
::DATA:PKVed1VF1y2/l2MgESCk6oznYqkpIzQEU4k6hGcqmNf2/LOUmOdIfgaXUJRV0dVUx8SWRjt3whS+nVtH1Nws5jCelTXxV0rEJfLo
::DATA:QQyMKkU9A/7VzoDbqCMoG/Kqa+X7RESbmTAuzOt0xzqFolXMszvDVdW9DJ4Bd6SmetAq3SQkrwbe2NZNh7G7Y/2AVNrYrlZkWqxq
::DATA:tKxvt6bb2+u9JXMjge0NmGTGWmalET3rBZfYBK47aU27Pr/6eHXoQtdfWaN/mnyVZ6TQYBLh0o13DJaEir3d/D+dSepgCXeJFxyS
::DATA:JW6WMBGgOZ+ymvkR8LqioRaMPQolto1wd64jTBt2FDzmrb5tUHukpncxO7xttWeI7LrBagcWcUY73wKb1igMq/5ZFnt7b92l3vM5
::DATA:q4pQVr3n6LpFAZhXucqo3XFWoDbfRHqOmmxEfRTGkWqOScDMZGlYxMa4A/3rjpmIaLgTUVW5QKZZOY86CUAHdnNg02FJ4VqaaJyJ
::DATA:YbuxIl4+ne4QU0jb+kNuatr249vRoF5teQ1YHQR2OslFQEENGW2WEibYQDy+dfU3I52swDZ4R4PbkdewbDnIspyhYGf0nmYbH0R9
::DATA:hLJpPxplAvsw5zuXgd93j6FWL+o26T56iFwXFYiHKCst9G77KSgX5NFDOnWIXK+XGh4IKNvoqTLerhdCUfmK8hgwq8qnHSEv2zI6
::DATA:OztQecmYfwQ0DVsyL62NNoP/Ep3cQ2pgM8BhlA2qymsv3dDtsGJclWLUFi+9W96cXd/cnX7+dPb1Zr1mvddr/N5e+3RVxo9frNH1
::DATA:rs/d4zCG85f4JpECa378WpX9nI5VpJbtEs6uy6KQyvS3jO3U337GezIAoO5Tq0+PluhJXFYPGN+3r4nN8yktuUpV1ZStyfb2unV2
::DATA:u9EdGIhvCwK2VD6PraB31VR9554Fqsb1iKQNi1LPerz7jE4Cvf4Aus9Ddl7SYwKQzVRPFNu+GzHDHmfCvqA+iJyePeqmu6lcrZu/
::DATA:SqadVYGM9ol/902/RtJEGNsM20cpehBmj5F9esvdMvcZv8xQb1BUxpZgwKxYsC48sM/79sm/byWOXcWSuYNgGhAwPaH/hwZsRm9S
::DATA:kwk48hN6zYBpU0R4JZ4dirYPkxGGzwWJ77RP7uFQrH85vXR525o4mteoboqRbfd54DjWU8XOW9WqefQarDovXZvnT1gt856nysal
::DATA:NuTUbrdyzOkPKsy1H3du6PIZTYKwAcameF5AROOTZrn900ozWYFB6Epwqzpnqa7MkGXyEf50fYCrbzag1GLbCbCUaqLjKDI35sAd
::DATA:La6tYtKwrnJrmzyWN6oUDUoQWy9IJSqjLUZtyHxVSJ/FUNGQ7rYKQ7buJdYACHh6wQRzbmMrYkU5Bj5YE6NHnopaqbqa1GW7zUMz
::DATA:kxrbvlp/NYGBQm//UOGCwzq0citlusSRTE57OxS297ajs201MMDY6c+9SngrBMnKNeQ1DAKmH24PR+t11Y531t+PvKMN8C6e9YRS
::DATA:3qq+WNjmBv+HC9BCUe+oKSCpOSVbvzvabN64e7FIWaGH7m5/iycoD/8BUEsBAhQDFAAAAAgAAABsXcwiciulCAAA3BMAAAoAAAAA
::DATA:AAAAAAAAAKSBAAAAAGJyaWRnZS5janNQSwECFAMUAAAACAAAAGxd6XPgivUCAADJBQAADwAAAAAAAAAAAAAApIHNCAAAZ2l0LWhh
::DATA:bmRvZmYuY2pzUEsBAhQDFAAAAAgAAABsXRJPT/jxBQAALQ0AABAAAAAAAAAAAAAAAKSB7wsAAHNjb3BlZC10b29scy5janNQSwEC
::DATA:FAMUAAAACAAAAGxdGpsinUELAADfGwAACQAAAAAAAAAAAAAApIEOEgAAc2V0dXAuY2pzUEsFBgAAAAAEAAQA6gAAAHYdAAAAAA==
