'use strict';

const assert = require('node:assert/strict');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const readline = require('node:readline');
const {spawn} = require('node:child_process');
const {once} = require('node:events');

const directory = fs.mkdtempSync(path.join(os.tmpdir(),'reyrun-checkpoint-race-'));
const server = path.resolve(__dirname,'../scripts/bridge.cjs');
const clients = [];
function startClient() {
  const child = spawn(process.execPath,[server],{
    stdio:['pipe','pipe','inherit'], windowsHide:true,
    env:{...process.env,REYRUN_WORKSPACE:directory}
  });
  const closed = once(child,'close');
  const pending = new Map();
  let serial = 0;
  const lines = readline.createInterface({input:child.stdout,crlfDelay:Infinity});
  lines.on('line',line=>{
    const msg=JSON.parse(line);
    const request=pending.get(msg.id);
    assert.ok(request,'unexpected MCP response id');
    pending.delete(msg.id);request.resolve(msg);
  });
  child.once('exit',()=>{
    for(const {reject} of pending.values()) reject(Error('MCP server closed before responding'));
    pending.clear();
  });
  function rpc(method,params) {
    const id=++serial;
    return new Promise((resolve,reject)=>{
      pending.set(id,{resolve,reject});
      child.stdin.write(JSON.stringify({jsonrpc:'2.0',id,method,params})+'\n');
    });
  }
  async function call(name,args={}) {
    const message=await rpc('tools/call',{name,arguments:args});
    assert.ok(!message.error,JSON.stringify(message.error));
    if(message.result.isError) return {error:message.result.content[0].text};
    return JSON.parse(message.result.content[0].text);
  }
  const client={child,rpc,call,closed};
  clients.push(client);
  return client;
}
async function main() {
  const group=Array.from({length:4},startClient);
  const handshakes=await Promise.all(group.map(c=>c.rpc('initialize',{
    protocolVersion:'2025-11-25',capabilities:{},clientInfo:{name:'concurrency-fixture',version:'1'}
  })));
  assert.ok(handshakes.every(h=>h.result.serverInfo.name==='reyrun-local-bridge'));
  assert.equal(new Set(group.map(c=>c.child.pid)).size,4);
  assert.ok(group.every(c=>c.child.exitCode===null));
  const notes=await Promise.all(group.map((c,i)=>c.call('save_checkpoint',{
    job:'job-'+i,revision:0,done:'stage '+i,next:'inspect'
  })));
  assert.deepEqual(notes.map(v=>v.revision),[1,1,1,1]);
  const observed=await Promise.all(group.map(c=>c.call('read_checkpoint',{job:'shared-job'})));
  assert.deepEqual(observed.map(r=>r.revision),[0,0,0,0]);
  const results=await Promise.all(group.map((c,i)=>c.call('save_checkpoint',{
    job:'shared-job',revision:0,done:'writer '+i,next:'continue'
  })));
  const winners=results.filter(r=>r.revision===1);
  const rejected=results.filter(r=>/Revision conflict|Another chat saved first/.test(r.error||''));
  assert.equal(winners.length,1);assert.equal(rejected.length,3);
  assert.ok(group.every(c=>c.child.exitCode===null));
  group.forEach(c=>c.child.stdin.end());
  await Promise.all(group.map(c=>c.closed));
  const resumed=startClient();
  await resumed.rpc('initialize',{protocolVersion:'2025-11-25',capabilities:{},clientInfo:{name:'restarter',version:'1'}});
  const found=await resumed.call('list_jobs');
  assert.equal(found.jobs.length,5);
  const previous=await resumed.call('read_checkpoint',{job:'shared-job'});
  assert.equal(previous.done,winners[0].done);
  for(let i=0;i<group.length;i++) assert.equal((await resumed.call('read_checkpoint',{job:'job-'+i})).done,'stage '+i);
  assert.equal((await resumed.call('save_checkpoint',{job:'shared-job',revision:1,done:'resumed',next:'verify'})).revision,2);
  resumed.child.stdin.end();await resumed.closed;
  console.log(JSON.stringify({observedUtc:new Date().toISOString(),platform:process.platform,node:process.version,
    independentConcurrentStdioProcesses:4,independentJobsSaved:4,sharedRevisionWinners:1,
    competingWritesRejected:3,jobsRecoveredAfterRestart:5,resumedRevision:2,
    scope:'Four local standard-I/O MCP clients. Live chatbot front ends and GUI control were outside this test.'},null,2));
}
const timeout=setTimeout(()=>{console.error('MCP concurrency test timed out');for(const c of clients)c.child.kill();},15000);
main().catch(e=>{console.error(e);process.exitCode=1;}).finally(async()=>{
  clearTimeout(timeout);
  for(const c of clients) if(c.child.exitCode===null && !c.child.stdin.destroyed)c.child.stdin.end();
  await Promise.allSettled(clients.map(c=>c.closed));
  fs.rmSync(directory,{recursive:true,force:true});
});
