"""Test real eligibility shell and native auto-merge revocation wiring."""
import os
import subprocess
import tempfile
from pathlib import Path
from ruamel.yaml import YAML

workflow = YAML(typ="safe").load(Path('.github/workflows/dependabot-auto-merge.yml').read_text())
steps = workflow['jobs']['merge']['steps']
decide = next(step for step in steps if step.get('id') == 'decide')
revoke = next(step for step in steps if step.get('name') == 'Revoke stale auto-merge eligibility')
enable = next(step for step in steps if step.get('name') == 'Enable native auto-merge after required checks')
assert "always()" in revoke['if'] and "eligible != 'true'" in revoke['if']
assert steps.index(revoke) < steps.index(enable)
cases = [('version-update:semver-patch','package','npm','1.0.1',True),
         ('version-update:semver-minor','package','npm','1.1.0',True),
         ('version-update:semver-major','package','npm','2.0.0',False),
         ('','unknown/action','github_actions','a'*40,False),
         ('','hacs/action','github_actions','a'*40,True),
         ('','hacs/action, unknown/action','github_actions','a'*40,False)]
with tempfile.TemporaryDirectory() as directory:
    root = Path(directory)
    for kind, dep, eco, version, wanted in cases:
        output = root/'output'
        output.write_text('')
        env = dict(os.environ, UPDATE_TYPE=kind, DEPENDENCIES=dep, ECOSYSTEM=eco, NEW_VERSION=version, GITHUB_OUTPUT=str(output))
        subprocess.run(['bash','-c',decide['run']],env=env,check=True,capture_output=True)
        assert output.read_text().strip() == 'eligible=' + str(wanted).lower()
    fake = root/'gh'
    fake.write_text('#!/bin/sh\nif [ "$2" = view ]; then echo "$AUTO_ENABLED"; else echo "$*" >> "$GH_CALLS"; fi\n')
    fake.chmod(0o755)
    calls = root/'calls'
    for enabled in ['false','true']:
        calls.write_text('')
        env = dict(os.environ, PATH=str(root)+os.pathsep+os.environ['PATH'], AUTO_ENABLED=enabled, GH_CALLS=str(calls), PR_NUMBER='7', GITHUB_REPOSITORY='example/repo')
        subprocess.run(['bash','-c',revoke['run']],env=env,check=True)
        assert ('--disable-auto' in calls.read_text()) == (enabled == 'true')
print('Dependabot policy: 8 eligibility and revocation scenarios passed.')
