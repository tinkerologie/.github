"""Exercise the real reporting script against a fake GitHub API; never post comments."""
import json
import subprocess
from pathlib import Path
from ruamel.yaml import YAML

workflow = YAML(typ="safe").load(Path(".github/workflows/governance-report.yml").read_text())
step = workflow["jobs"]["report"]["steps"][-1]
assert "inputs.use-github-token" in step["with"]["github-token"]
assert "'github-actions'" in step["env"]["BOT_LOGIN"]
script = step["with"]["script"]
harness = r'''
const assert = require('node:assert/strict');
const report = new (Object.getPrototypeOf(async function() {}).constructor)('github','context','core', SCRIPT);
let comments = [], writes = [], head = 'head1';
const github = {
  rest: {
    issues: {listComments: 'comments',
      createComment: async (p) => { writes.push(p); comments.push({id:1,user:{login:'github-actions[bot]'},body:p.body}); return {data:{id:1}}; },
      updateComment: async (p) => { writes.push(p); comments[0].body=p.body; }
    },
    checks: {listForRef:'checks'},
    pulls: {get:async () => ({data:{head:{sha:head}}})}
  },
  paginate:async (method) => method==='comments' ? comments : []
};
const context={repo:{owner:'example',repo:'private'},payload:{pull_request:{head:{sha:'head1'}}}};
const core={info:()=>{}};
Object.assign(process.env,{PR_NUMBER:'1',RESULT:'failure',ERRORS:JSON.stringify(['Problem from @someone <script>']),RUN_ID:'100',CHECK_NAME:'PR Governance',RUN_URL:'https://github.com/example/private/actions/runs/100',BOT_LOGIN:'github-actions[bot]'});
(async () => {
  await report(github,context,core);
  assert.equal(writes.length,1);
  assert(!writes[0].body.includes('@someone'));
  assert(!writes[0].body.includes('<script>'));
  await report(github,context,core);
  assert.equal(writes.length,1,'unchanged report must not create noise');
  process.env.RESULT='success'; process.env.RUN_ID='101';
  await report(github,context,core);
  assert.equal(writes.length,2); assert.equal(writes[1].comment_id,1);
  assert(writes[1].body.includes('checklist complete'));
  process.env.RESULT='failure'; process.env.RUN_ID='99';
  await report(github,context,core);
  assert.equal(writes.length,2,'old run must not overwrite newer success');
  comments=[]; head='new-head'; process.env.RUN_ID='102';
  await report(github,context,core);
  assert.equal(writes.length,2,'outdated PR head must not post');
  console.log('Repository-token reporting: create, sanitize, deduplicate, recover and stale-run guards passed.');
})().catch(error=>{console.error(error);process.exitCode=1;});
'''
subprocess.run(["node", "-e", harness.replace("SCRIPT", json.dumps(script))], check=True)
