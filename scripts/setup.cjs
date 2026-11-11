'use strict';
// Run locally. An existing Claude Desktop reads the scoped configuration on its next start.
const fs=require('node:fs');
const os=require('node:os');
const path=require('node:path');
const cp=require('node:child_process');
const crypto=require('node:crypto');
const root=process.env.REYRUN_WORKSPACE||path.join(os.homedir(),'REYRUN Bridge');
const app=path.join(root,'runtime');
const scope=path.join(root,'Workspace');
const out=path.join(root,'START.txt');
const site='https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site';
function writeText(file,text){fs.writeFileSync(file,text,{encoding:'utf8',mode:0o600});}
function configure(file,name,entry){
  const lock=file+'.reyrun-lock';
  const fd=fs.openSync(lock,'wx',0o600);
  const temp=file+'.'+crypto.randomUUID()+'.tmp';
  try {
    const original=fs.existsSync(file)?fs.readFileSync(file,'utf8'):null;
    const data=original?JSON.parse(original.replace(/^\uFEFF/,'')):{};
    if(!data || typeof data!=='object' || Array.isArray(data))throw Error('Unexpected client configuration.');
    const servers=data.mcpServers??{};
    if(!servers||typeof servers!=='object'||Array.isArray(servers))throw Error('Unexpected mcpServers configuration.');
    if(Object.hasOwn(servers,name)){
      if(JSON.stringify(servers[name])===JSON.stringify(entry))return 'already configured';
      throw Error('This name already belongs to another configuration. No overwrite.');
    }
    if(original!==null)fs.copyFileSync(file,file+'.reyrun-backup-'+crypto.randomUUID(),fs.constants.COPYFILE_EXCL);
    data.mcpServers={...servers,[name]:entry};
    writeText(temp,JSON.stringify(data,null,2)+'\n');
    if((fs.existsSync(file)?fs.readFileSync(file,'utf8'):null)!==original)throw Error('Client configuration changed. Close its settings window and retry.');
    fs.renameSync(temp,file);
    return 'configured';
  } finally {if(fs.existsSync(temp))fs.unlinkSync(temp);fs.closeSync(fd);fs.unlinkSync(lock);}
}
const defs={
  commander:{pkg:'@wonderwhy-er/desktop-commander@0.3.2',bin:'desktop-commander'},
  filesystem:{pkg:'@modelcontextprotocol/server-filesystem@2.3.0',bin:'mcp-server-filesystem'},
  playwright:{pkg:'@playwright/mcp@0.0.85',bin:'playwright-mcp'},
  devtools:{pkg:'chrome-devtools-mcp@1.13.0',bin:'chrome-devtools-mcp'}
};
function npmCli(){
  for(const file of [path.join(path.dirname(process.execPath),'node_modules/npm/bin/npm-cli.js'),path.join(path.dirname(process.execPath),'../lib/node_modules/npm/bin/npm-cli.js')])if(fs.existsSync(file))return file;
  throw Error('The official Node runtime must include npm.');
}
function installTool(mode,dir){
  const def=defs[mode];
  const pkg=def.pkg.slice(0,def.pkg.lastIndexOf('@')),dest=path.join(dir,'node_modules',pkg);
  if(!fs.existsSync(path.join(dest,'package.json'))){
    const res=cp.spawnSync(process.execPath,[npmCli(),'install','--prefix',dir,'--ignore-scripts','--no-fund','--no-audit','--save-exact',def.pkg],{stdio:'inherit',env:{...process.env,PATH:path.dirname(process.execPath)+path.delimiter+process.env.PATH}});
    if(res.status!==0)throw Error('Package download did not finish. Reopen the same launcher to retry.');
  }
  const manifest=JSON.parse(fs.readFileSync(path.join(dest,'package.json'),'utf8'));
  if(manifest.version!==def.pkg.slice(def.pkg.lastIndexOf('@')+1))throw Error('Unexpected package version.');
  const bin=typeof manifest.bin==='string'?manifest.bin:manifest.bin[def.bin];
  if(!bin||!fs.existsSync(path.join(dest,bin)))throw Error('Package entry file missing.');
  return path.join(dest,bin);
}
function findChrome(){
  const paths=process.platform==='win32'?['PROGRAMFILES','PROGRAMFILES(X86)','LOCALAPPDATA'].filter(k=>process.env[k]).map(k=>path.join(process.env[k],'Google/Chrome/Application/chrome.exe')):['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',path.join(os.homedir(),'Applications/Google Chrome.app/Contents/MacOS/Google Chrome'),'/usr/bin/chromium','/usr/bin/google-chrome'];
  return paths.find(p=>fs.existsSync(p));
}
function setup(mode,game){
  if(!['jobs',...Object.keys(defs),'rdr2'].includes(mode))throw Error('Unknown profile.');
  for(const d of [root,app,scope])fs.mkdirSync(d,{recursive:true,mode:0o700});
  const name='reyrun-'+mode;
  let entry;
  if(mode==='jobs')entry={command:process.execPath,args:[path.join(app,'bridge.cjs')],env:{REYRUN_WORKSPACE:root}};
  else{
    if(mode==='rdr2'&&(!game||!path.isAbsolute(game)||!fs.statSync(path.join(game,'RDR2.exe'),{throwIfNoEntry:false})?.isFile()))throw Error('Choose the game folder containing RDR2.exe; no game files were changed.');
    const type=mode==='rdr2'?'filesystem':mode;
    const chrome=['playwright','devtools'].includes(type)?findChrome():null;
    if(['playwright','devtools'].includes(type)&&!chrome)throw Error('This profile requires installed Chrome. The files and task-note profiles work without a browser.');
    const work=path.join(app,'packages',type);fs.mkdirSync(work,{recursive:true});
    const executable=installTool(type,work);
    const args=type==='commander'?[]:type==='filesystem'?['--confine-roots',scope,...(game?[fs.realpathSync(game)]:[])]:type==='playwright'?['--headless','--isolated','--executable-path',chrome]:['--headless','--isolated','--slim','--no-javascript-evaluation','--no-file-navigations','--no-usage-statistics','--no-performance-crux','--executablePath',chrome];
    entry=type==='filesystem'?{command:process.execPath,args:[executable,...args]}:{command:process.execPath,args:[path.join(app,'scoped-tools.cjs'),type,scope,executable,...args]};
  }
  const candidate=process.env.REYRUN_TEST_CLIENT|| (process.platform==='win32'&&process.env.APPDATA?path.join(process.env.APPDATA,'Claude'):process.platform==='darwin'?path.join(os.homedir(),'Library/Application Support/Claude'):null);
  const text=['REYRUN Bridge',site,'Profile: '+name,'Workspace: '+scope];
  if(candidate&&fs.existsSync(candidate)){
    const file=path.join(candidate,'claude_desktop_config.json');text.push('Claude Desktop: '+configure(file,name,entry)+'. Fully quit and reopen the app when convenient.');
  }else{
    text.push('No supported local Claude Desktop profile detected. No chat was connected.', 'Plain web chat: open '+site+'/start/ and choose one file to prepare a handoff.','A compatible local stdio client can import the adjacent MCP entry.');
  }
  writeText(path.join(app,name+'-client.json'),JSON.stringify({mcpServers:{[name]:entry}},null,2)+'\n');
  text.push('First test: '+(mode==='jobs'?'call bridge_status, save a checkpoint, then read the same job.':mode==='rdr2'?'list the allowed folders and confirm RDR2.exe is in the selected one.':mode==='commander'?'list the REYRUN Workspace and inspect a small note.':mode==='filesystem'?'list the allowed folders, create a note in Workspace and read it back.':'open a public test page in the isolated browser and read its title.'));
  writeText(out,text.join('\n')+'\n');console.log(text.join('\n'));
}
if(require.main===module){try{setup(process.argv[2]||'jobs',process.argv[3]);}catch(err){console.error(err.message);process.exitCode=1;}}
module.exports={setup,configure};
