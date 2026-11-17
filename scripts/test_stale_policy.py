"""Check protected-state exemptions survive repository overrides and dry runs."""
from pathlib import Path
from ruamel.yaml import YAML

doc = YAML(typ="safe").load(Path('.github/workflows/stale.yml').read_text())
job = doc['jobs']['stale']
protected = set(job['env']['PROTECTED_WORKFLOW_LABELS'].split(','))
required = {'needs-triage','needs-info','ready-for-agent','ready-for-human','wontfix','triage','blocked','work-in-progress'}
assert required <= protected
with_ = job['steps'][0]['with']
for kind in ['issue','pr']:
    key = f'exempt-{kind}-labels'
    expression = "${{ format('{0},{1}', env.PROTECTED_WORKFLOW_LABELS, inputs." + key + ") }}"
    assert with_[key] == expression
    for override in ['', 'status: blocked', doc['on']['workflow_call']['inputs'][key]['default']]:
        effective = set('{0},{1}'.format(','.join(protected),override).split(','))
        assert required <= effective
        assert 'bug' not in effective and 'enhancement' not in effective
assert with_['debug-only'] == '${{ inputs.debug-only }}'
assert doc['on']['workflow_call']['inputs']['debug-only']['default'] is False
print('Stale policy: 8 protected labels survive empty/custom/default overrides for issues and PRs; dry-run is wired.')
