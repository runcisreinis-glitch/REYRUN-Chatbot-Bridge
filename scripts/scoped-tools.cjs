'use strict';
// Scoped front end for the three optional local programs. Tool arguments are data.
// Only the actions below are forwarded; neither existing tabs nor the user's desktop are attached.
const fs=require('node:fs'),path=require('node:path'),cp=require('node:child_process'),readline=require('node:readline');
const [mode,workspace,source,...args]=process.argv.slice(2);
const allowedOrigins=new Set(['https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site','https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site','https://reyrun-rekursive-deep-search.runcisreinis.chatgpt.site']);
const safeNames={playwright:['browser_navigate','browser_snapshot','browser_take_screenshot'],devtools:['navigate','screenshot'],commander:['list_directory','get_file_info','read_file']};
if(!Object.hasOwn(safeNames,mode))throw Error('Unknown profile.');
const child=cp.spawn(process.execPath,[source,...args],{cwd:workspace,stdio:['pipe','pipe','inherit'],windowsHide:true});
const listRequests=new Set(),root=fs.realpathSync(workspace);
function emit(m){process.stdout.write(JSON.stringify(m)+'\n');}
function send(m){child.stdin.write(JSON.stringify(m)+'\n');}
function scoped(name,a){
 if(!safeNames[mode].includes(name))throw Error('This tool is outside the selected profile.');
 if(mode==='commander'){
   const target=fs.realpathSync(path.resolve(root,a.path||'.')),rel=path.relative(root,target);
   if(rel==='..'||rel.startsWith('..'+path.sep)||path.isAbsolute(rel))throw Error('Choose a file in the REYRUN workspace.');
   if(name==='read_file'){
     if(!/\.(txt|md|json|log)$/i.test(target)||fs.statSync(target).size>1048576)throw Error('Choose a small text file.');
     return {path:target,offset:0,length:100};
   }
   return name==='list_directory'?{path:target,depth:1}:{path:target};
 }
 if(name==='navigate'||name==='browser_navigate'){
   const dest=new URL(a.url);
   if(!allowedOrigins.has(dest.origin)||dest.username||dest.password)throw Error('This starter opens the three REYRUN project sites.');
   return {url:dest.href};
 }
 return {}; // No arbitrary file path, page script, interaction or host file upload.
}
readline.createInterface({input:process.stdin,crlfDelay:Infinity}).on('line',line=>{
 let m;try{m=JSON.parse(line);}catch{return;}
 if(m.method==='tools/list'){listRequests.add(m.id);send(m);return;}
 if(m.method==='tools/call'){
   try{const name=m.params?.name;send({...m,params:{name,arguments:scoped(name,m.params?.arguments||{})}});}
   catch(e){emit({jsonrpc:'2.0',id:m.id,result:{isError:true,content:[{type:'text',text:e.message}]}});}
   return;
 }
 if(['initialize','notifications/initialized','ping','notifications/cancelled'].includes(m.method)){send(m);return;}
 if(m.id!==undefined)emit({jsonrpc:'2.0',id:m.id,error:{code:-32601,message:'Unknown method'}});
}).on('close',()=>{child.stdin.end();child.kill();});
readline.createInterface({input:child.stdout,crlfDelay:Infinity}).on('line',line=>{
 let m;try{m=JSON.parse(line);}catch{return;}
 if(m.method){if(m.id!==undefined)send({jsonrpc:'2.0',id:m.id,error:{code:-32601,message:'Client methods disabled'}});return;}
 if(listRequests.delete(m.id)&&m.result?.tools)m.result.tools=m.result.tools.filter(item=>safeNames[mode].includes(item.name));
 emit(m);
});
child.on('error',e=>{console.error(e.message);process.exitCode=1;});
child.on('exit',code=>process.exit(code||0));
