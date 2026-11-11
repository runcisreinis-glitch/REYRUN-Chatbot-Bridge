    if(!$game){
      $records=@{steam=@();rockstar=@();epicManifests=@()}
      foreach($key in @('HKCU:\Software\Valve\Steam','HKLM:\SOFTWARE\Valve\Steam','HKLM:\SOFTWARE\WOW6432Node\Valve\Steam')){
        $record=Get-ItemProperty -LiteralPath $key -ErrorAction SilentlyContinue
        foreach($field in @('SteamPath','InstallPath')){if($record.$field){$records.steam+=@([string]$record.$field)}}
      }
      if(${env:ProgramFiles(x86)}){$records.steam+=@(Join-Path ${env:ProgramFiles(x86)} 'Steam')}
      foreach($root in @('HKLM:\SOFTWARE','HKLM:\SOFTWARE\WOW6432Node','HKCU:\Software')){
        $record=Get-ItemProperty -LiteralPath ($root+'\Rockstar Games\Red Dead Redemption 2') -ErrorAction SilentlyContinue
        foreach($field in @('InstallFolder','InstallFolderEpic','InstallFolderSteam','InstallLocation')){if($record.$field){$records.rockstar+=@([string]$record.$field)}}
      }
      if($env:ProgramData){$records.epicManifests+=@(Join-Path $env:ProgramData 'Epic\EpicGamesLauncher\Data\Manifests')}
      $index=Join-Path $tmp 'game-locations.json'
      [IO.File]::WriteAllText($index,($records|ConvertTo-Json -Compress))
      $guess=& $n (Join-Path $rt 'rdr2-detect.cjs') $index
      if($LASTEXITCODE -eq 0 -and $guess){$game=[Text.Encoding]::UTF8.GetString([Convert]::FromBase64String([string]$guess))}
    }
