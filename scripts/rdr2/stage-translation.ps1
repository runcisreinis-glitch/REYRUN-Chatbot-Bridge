    if($LASTEXITCODE -ne 0){exit $LASTEXITCODE}
    $releaseUrl='https://raw.githubusercontent.com/runcisreinis-glitch/REYRUN-RDR2-Latvian/3de3d4df5b4cbf415bc1f0e56cec3adfea8d4258/REYRUN-RDR2-LV.zip'
    $zipHash='11d7ee80bac9ac820a2c20e87f2f7fc736e3fab5ceb6e9cf7842543f9f3237da'
    $xmlHash='c72337da664b3999ca4fc2de2600c1e79c551b29fa1e69d79d1330485aef5045'
    $scope=Join-Path $base 'Workspace'
    $xml=Join-Path $scope 'Latvian Translation.xml'
    $zipCache=Join-Path $scope 'REYRUN-RDR2-LV.zip'
    $pendingXml=$null
    try {
      # Resolve actual directories as well as junctions before staging any translation.
      $outsideGame=& $n -e "const f=require('node:fs'),p=require('node:path');const d=p.relative(f.realpathSync.native(process.argv[1]),f.realpathSync.native(process.argv[2]));if(d==='..'||d.startsWith('..'+p.sep)||p.isAbsolute(d))console.log('outside');" $game $scope
      if($LASTEXITCODE -ne 0 -or $outsideGame -ne 'outside'){throw 'Choose a REYRUN workspace outside the game folder.'}
      if([IO.File]::Exists($xml)){
        if((Get-StarterDigest $xml) -ne $xmlHash){throw 'A different Latvian Translation.xml already exists in the workspace. It was left untouched.'}
        $stageInfo='Already staged and verified: '+$xml
      } else {
        $sourceZip=Join-Path $tmp 'REYRUN-RDR2-LV.zip'
        if([IO.File]::Exists($zipCache) -and (Get-StarterDigest $zipCache) -eq $zipHash){
          $sourceZip=$zipCache
        } else {
          Invoke-WebRequest -UseBasicParsing -TimeoutSec 35 -Uri $releaseUrl -OutFile $sourceZip
        }
        if((Get-StarterDigest $sourceZip) -ne $zipHash){throw 'The downloaded release ZIP failed its SHA-256 check.'}
        Add-Type -AssemblyName System.IO.Compression.FileSystem
        $archive=[IO.Compression.ZipFile]::OpenRead($sourceZip)
        try {
          $members=@($archive.Entries | Where-Object {$_.FullName -ceq 'Latvian Translation.xml'})
          if($members.Count -ne 1 -or $members[0].Length -ne 20782582){throw 'Unexpected XML entry in the release ZIP.'}
          $pendingXml=Join-Path $scope ('.reyrun-'+[guid]::NewGuid().ToString('n')+'.tmp')
          $outFile=[IO.File]::Open($pendingXml,[IO.FileMode]::CreateNew,[IO.FileAccess]::Write,[IO.FileShare]::None)
          try {$inFile=$members[0].Open();try {$inFile.CopyTo($outFile)}finally{$inFile.Dispose()}}finally{$outFile.Dispose()}
        } finally {$archive.Dispose()}
        if((Get-StarterDigest $pendingXml) -ne $xmlHash){throw 'The extracted translation XML failed its SHA-256 check.'}
        try {[IO.File]::Move($pendingXml,$xml)} catch {
          if(![IO.File]::Exists($xml) -or (Get-StarterDigest $xml) -ne $xmlHash){throw}
        }
        $stageInfo='Staged and verified: '+$xml
      }
      $stageInfo+=[Environment]::NewLine+'This is a workspace copy. Follow the installation guide for the ASI plug-in, loader, backup and game-folder copy.'
    } catch {
      $stageInfo='Translation XML is not ready. '+$_.Exception.Message+' For an offline retry, put the official REYRUN-RDR2-LV.zip in the allowed Workspace folder and run this launcher again. Release: '+$releaseUrl
    } finally {
      if($pendingXml -and [IO.File]::Exists($pendingXml)){[IO.File]::Delete($pendingXml)}
    }
    [IO.File]::AppendAllText((Join-Path $base 'START.txt'),$stageInfo+[Environment]::NewLine)
    Write-Output $stageInfo
