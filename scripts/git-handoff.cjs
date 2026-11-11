'use strict';
const cp=require('node:child_process'),fs=require('node:fs'),os=require('node:os'),path=require('node:path'),crypto=require('node:crypto');
const base=process.env.REYRUN_WORKSPACE||path.join(os.homedir(),'REYRUN Bridge');
function main(){
 const f=path.join(base,'handoffs','job-'+crypto.randomUUID().slice(0,8));fs.mkdirSync(f,{recursive:true});
 const git=(...args)=>cp.execFileSync('git',['-c','user.name=REYRUN','-c','user.email=local@example.invalid','-c','commit.gpgsign=false','-c','core.hooksPath='+path.join(f,'unused-hooks'),...args],{cwd:f,encoding:'utf8',windowsHide:true});
 git('init','-q','-b','main','source');
 fs.writeFileSync(path.join(f,'source','NEXT.md'),'# Handoff\n\nDone: project created.\nNext: describe the next task in your own worktree.\n');
 git('-C','source','add','NEXT.md');git('-C','source','commit','-qm','Start a local handoff');
 for(const role of ['text','review'])git('-C','source','worktree','add','-q','-b',role,path.join(f,role));
 const bundle=path.join(f,'handoff.bundle');git('-C','source','bundle','create',bundle,'--all');
 git('-C','source','bundle','verify',bundle);
 const info='Local handoff created: '+f+'\nTwo worktrees: text, review. Bundle: handoff.bundle\nEach chat uses a separate worktree. No files were sent anywhere.';
 console.log(info);fs.writeFileSync(path.join(base,'START.txt'),info+'\n');
}
try{main();}catch(e){console.error('Git is required for this local project. '+e.message);process.exitCode=1;}
