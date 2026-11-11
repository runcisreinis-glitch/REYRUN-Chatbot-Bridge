'use strict';
// A local stdio MCP. The only writes are new revisions inside its own task directory.
// Each revision is immutable. Atomic hard-link creation selects a single winner on a race.
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const crypto = require('node:crypto');
const readline = require('node:readline');
const root = process.env.REYRUN_WORKSPACE || path.join(os.homedir(), 'REYRUN Bridge');
const jobs = path.join(root, 'jobs');
fs.mkdirSync(jobs, { recursive: true, mode: 0o700 });
const safeDirectory = p => fs.lstatSync(p).isDirectory() && !fs.lstatSync(p).isSymbolicLink();
if (!safeDirectory(root) || !safeDirectory(jobs)) throw Error('Use an ordinary local workspace directory.');
const idPattern = /^[a-z][a-z0-9-]{0,47}$/;
const key = {type:'string',pattern:'^[a-z][a-z0-9-]{0,47}$'};
const note = {type:'string',maxLength:24000};
function spec(name, description, properties, required = []) {
  return {name,description,inputSchema:{type:'object',properties,required,additionalProperties:false}};
}
const catalog = [
  spec('bridge_status','Identify the local device platform and workspace capabilities. No network or shell.',{}),
  spec('list_jobs','List task IDs available for handoff to another connected chat.',{}),
  spec('read_checkpoint','Read a job and its current revision. Revision zero means the job has no checkpoint.',{job:key},['job']),
  spec('save_checkpoint','Save completed work and the next step. Supply the last observed revision. An outdated revision is rejected.',{job:key,revision:{type:'integer',minimum:0},done:note,next:note},['job','revision','done','next'])
];
function directory(id) {
  if (typeof id !== 'string' || !idPattern.test(id) || /^(aux|con|prn|nul|com[1-9]|lpt[1-9])$/.test(id)) throw Error('Choose a short job name such as game-check.');
  const dir=path.join(jobs,id);
  if(fs.existsSync(dir) && !safeDirectory(dir)) throw Error('Unsupported task directory.');
  return dir;
}
function latest(dir,id) {
  if(!fs.existsSync(dir)) return {job:id,revision:0};
  const names=fs.readdirSync(dir).filter(n=>/^\d{8}\.json$/.test(n)).sort();
  if(!names.length) return {job:id,revision:0};
  const file=path.join(dir,names.at(-1));
  if(!fs.lstatSync(file).isFile()) throw Error('Unexpected checkpoint type.');
  return JSON.parse(fs.readFileSync(file,'utf8'));
}
function run(name,a={}) {
  if(name==='bridge_status') return {bridge:'REYRUN',version:'1.0.0',platform:process.platform,transport:'stdio',access:'local task notes',writes:'revision checked'};
  if(name==='list_jobs') return {jobs:fs.readdirSync(jobs,{withFileTypes:true}).filter(v=>v.isDirectory() && idPattern.test(v.name)).map(v=>v.name).sort()};
  if(!['read_checkpoint','save_checkpoint'].includes(name)) throw Error('Unknown tool.');
  const dir=directory(a.job), old=latest(dir,a.job);
  if(name==='read_checkpoint') return old;
  if(!Number.isSafeInteger(a.revision)||a.revision<0||a.revision!==old.revision) throw Error('Revision conflict. Read the current checkpoint before retrying.');
  if(a.revision>=99999999) throw Error('Start a new job ID.');
  for(const field of ['done','next']) if(typeof a[field]!=='string'||!a[field].trim()||a[field].length>24000) throw Error('Provide short done and next notes.');
  fs.mkdirSync(dir,{recursive:true,mode:0o700});
  const result={job:a.job,revision:a.revision+1,done:a.done,next:a.next,saved:new Date().toISOString()};
  const tmp=path.join(dir,'.pending-'+crypto.randomUUID()),final=path.join(dir,String(result.revision).padStart(8,'0')+'.json');
  fs.writeFileSync(tmp, JSON.stringify(result,null,2)+'\n',{flag:'wx',mode:0o600});
  try {fs.linkSync(tmp,final);}
  catch(e){if(e.code==='EEXIST')throw Error('Another chat saved first. Read the new checkpoint.');throw e;}
  finally {fs.unlinkSync(tmp);}
  return result;
}
const versions=['2025-11-25','2025-06-18','2025-03-26','2024-11-05'];
function dispatch(msg){
  if(msg.id===undefined)return;
  const base={jsonrpc:'2.0',id:msg.id};
  switch(msg.method){
    case 'initialize': return {...base,result:{protocolVersion:versions.includes(msg.params?.protocolVersion)?msg.params.protocolVersion:versions[0],capabilities:{tools:{}},serverInfo:{name:'reyrun-local-bridge',version:'1.0.0'}}};
    case 'ping':return {...base,result:{}};
    case 'tools/list':return {...base,result:{tools:catalog}};
    case 'tools/call':
      try{return {...base,result:{content:[{type:'text',text:JSON.stringify(run(msg.params?.name,msg.params?.arguments),null,2)}]}};}
      catch(err){return {...base,result:{isError:true,content:[{type:'text',text:err.message}]}};}
    default:return {...base,error:{code:-32601,message:'Method not found'}};
  }
}
if(require.main===module)readline.createInterface({input:process.stdin,crlfDelay:Infinity}).on('line',line=>{
  try{const res=dispatch(JSON.parse(line));if(res)process.stdout.write(JSON.stringify(res)+'\n');}
  catch {process.stdout.write(JSON.stringify({jsonrpc:'2.0',id:null,error:{code:-32700,message:'Invalid JSON'}})+'\n');}
});
module.exports={run,dispatch};
