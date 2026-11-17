"""Run the actual reusable coverage script with isolated GitHub API fixtures."""
import json
import subprocess
from pathlib import Path
from ruamel.yaml import YAML

workflow = YAML(typ="safe").load(Path('.github/workflows/coverage-gate.yml').read_text())
script = workflow['jobs']['evaluate']['steps'][0]['with']['script']
harness = r'''
const assert = require('node:assert/strict');
const execute = new (Object.getPrototypeOf(async function() {}).constructor)('github','context','core', SCRIPT);
let count=0;
async function run(options={}) {
  const files=options.files || [{filename:'src/app.ts',additions:2}];
  const pr={number:7,state:options.closed?'closed':'open',changed_files:options.fileCount ?? files.length,head:{sha:'head'},base:{ref:'main',repo:{full_name:'example/project'}}};
  const status={id:2,context:'codecov/patch',state:options.state || 'success',creator:{login:'codecov[bot]',id:22429695}};
  const writes=[];let gets=0;
  const github={rest:{pulls:{list:'prs',listFiles:'files',get:async()=>{gets++;return {data:options.moved && gets>1?{...pr,head:{sha:'new'}}:pr};}},
    repos:{listCommitStatusesForRef:'statuses'},checks:{listForRef:'checks',create:async p=>writes.push(p),update:async p=>writes.push(p)}},
    paginate:async(method,p)=>{
      assert.equal(p.per_page,100);
      if(options.apiError) throw new Error('API unavailable');
      return method==='prs'?[pr]:method==='files'?files:method==='checks'?(options.checks||[]):options.statuses ?? [status];
    }};
  const context={repo:{owner:'example',repo:'project'},eventName:options.eventName || 'pull_request_target',payload:options.payload ?? {pull_request:{number:7,head:{sha:'head'}}}};
  const summary={addHeading:()=>summary,addRaw:()=>summary,write:async()=>{}};
  process.env.SOURCE_PATTERN=options.pattern || '^src/.*\\.[cm]?[jt]sx?$';
  process.env.DRY_RUN=options.dryRun?'true':'false';process.env.PR_NUMBER=String(options.pr || 0);
  await execute(github,context,{info:()=>{},summary});count++;
  return writes;
}
const file=(filename,additions=1)=>({filename,additions});
(async()=>{
 for(const path of ['README.md','docs/example.ts','package.json','package-lock.json','uv.lock','.github/workflows/ci.yml','src/example.test.ts','src/tests/helper.ts','src/types.d.ts']) {
   const writes=await run({files:[file(path)],statuses:[]});assert.equal(writes[0].conclusion,'success',path);
 }
 assert.equal((await run({files:[file('src/app.ts',0)],statuses:[]}))[0].conclusion,'success');
 assert.equal((await run({files:[file('package-lock.json'),file('src/app.ts')],statuses:[]}))[0].status,'in_progress');
 for(const state of ['failure','error']) assert.equal((await run({state}))[0].conclusion,'failure');
 assert.equal((await run({state:'success'}))[0].conclusion,'success');
 assert.equal((await run({state:'pending'}))[0].status,'in_progress');
 assert.equal((await run({statuses:[{id:99,context:'codecov/patch',state:'success',creator:{login:'codecov[bot]',id:999}}]}))[0].status,'in_progress');
 assert.equal((await run({statuses:[{id:1,context:'codecov/patch',state:'success',creator:{login:'codecov[bot]',id:22429695}},{id:2,context:'codecov/patch',state:'failure',creator:{login:'codecov[bot]',id:22429695}}]}))[0].conclusion,'failure');
 assert.equal((await run({payload:{pull_request:{number:7,head:{sha:'old'}}}})).length,0);
 assert.equal((await run({moved:true})).length,0);
 assert.equal((await run({dryRun:true,closed:true})).length,0);
 assert.equal((await run({closed:true})).length,0);
 assert.equal((await run({eventName:'status',payload:{sha:'head'}}))[0].head_sha,'head');
 assert.equal((await run({eventName:'workflow_run',payload:{workflow_run:{head_sha:'head'}}}))[0].head_sha,'head');
 assert.equal((await run({eventName:'workflow_dispatch',payload:{},pr:7}))[0].conclusion,'success');
 assert.equal((await run({eventName:'workflow_dispatch',payload:{}}))[0].conclusion,'success');
 await assert.rejects(run({fileCount:2}),/Incomplete/);
 await assert.rejects(run({files:Array.from({length:3000},()=>file('README.md'))}),/Incomplete/);
 await assert.rejects(run({apiError:true}),/API unavailable/);
 const prev={id:10,external_id:'coverage-gate:7',app:{id:15368},status:'completed',conclusion:'failure'};
 assert.equal((await run({checks:[prev]}))[0].check_run_id,10);
 assert.equal((await run({checks:[prev],statuses:[]}))[0].head_sha,'head');
 for(const [pattern,path] of [['^custom_components/.*\\.py$','custom_components/example/sensor.py'],['\\.go$','daemon/main.go'],['^web/src/.*\\.svelte$','web/src/App.svelte']]) assert.equal((await run({pattern,files:[file(path)],statuses:[]}))[0].status,'in_progress');
 console.log(`Coverage gate: ${count+3} scenarios passed, including fail-closed API and pagination cases.`);
})().catch(e=>{console.error(e);process.exit(1)});
'''
subprocess.run(['node','-e',harness.replace('SCRIPT',json.dumps(script))],check=True)
