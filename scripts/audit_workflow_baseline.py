"""Read-only public workflow audit. Parse configuration; never run repository code."""
import base64
import concurrent.futures
import json
import os
import re
import subprocess
from pathlib import Path
from urllib.parse import quote
from ruamel.yaml import YAML


def inspect_workflow(name, document):
    problems = []
    if not isinstance(document, dict):
        return [f'{name}: workflow is not a mapping']
    if 'permissions' not in document:
        problems.append(f'{name}: explicit workflow permissions missing')
    for key, job in document.get('jobs', {}).items():
        if 'runs-on' in job and 'timeout-minutes' not in job:
            problems.append(f'{name}/{key}: runner timeout missing')
        if job.get('uses', '').startswith('tinkerologie/.github/.github/workflows/dependabot-auto-merge.yml@') and job.get('with', {}).get('native-auto-merge') is not True:
            problems.append(f'{name}/{key}: public Dependabot caller holds a polling runner')
        if job.get('uses', '').startswith('tinkerologie/.github/.github/workflows/dependabot-auto-merge.yml@'):
            policy = document.get('jobs', {}).get('dependency-policy', {})
            if policy.get('name') != 'Dependency Policy' or policy.get('needs') != 'auto-merge' or policy.get('if') != 'always()':
                problems.append(f'{name}: required dependency-policy aggregation missing')
        refs = [job['uses']] if 'uses' in job else []
        for step in job.get('steps', []):
            if 'uses' in step:
                refs.append(step['uses'])
            if step.get('uses', '').startswith('actions/upload-artifact@') and 'retention-days' not in step.get('with', {}):
                problems.append(f'{name}/{key}: artifact retention missing')
        for ref in refs:
            if not ref.startswith('./') and not re.search(r'@[0-9a-f]{40}$', ref):
                problems.append(f'{name}/{key}: unpinned action {ref}')
    if name == 'issue-labeler.yml':
        for schedule in document.get('on', {}).get('schedule', []):
            if schedule['cron'].split()[-1] == '*':
                problems.append(f'{name}: issue reconciliation runs more often than weekly')
    return problems


def inspect_coverage(expected, workflows, config):
    if 'Coverage Gate' not in expected['required_checks']:
        return []
    problems = []
    gate = workflows.get('coverage-gate.yml', {})
    job = gate.get('jobs', {}).get('coverage', {})
    if not job.get('uses', '').startswith('tinkerologie/.github/.github/workflows/coverage-gate.yml@'):
        problems.append('shared coverage gate missing')
    if job.get('with', {}).get('source-pattern') != expected['coverage_source_pattern']:
        problems.append('coverage source paths differ from manifest')
    events = gate.get('on', {})
    if not {'pull_request_target', 'status', 'workflow_run', 'workflow_dispatch'} <= set(events):
        problems.append('coverage reconciliation event missing')
    cc = config.get('codecov', {})
    patch = config.get('coverage', {}).get('status', {}).get('patch', {}).get('default', {})
    if cc.get('require_ci_to_pass') is not False or cc.get('notify', {}).get('wait_for_ci') is not False:
        problems.append('Codecov can wait on its own required gate')
    if config.get('github_checks') is not False:
        problems.append('Codecov commit-status delivery is not explicitly selected')
    if cc.get('strict_yaml_branch') != 'main':
        problems.append('Codecov thresholds are not locked to main')
    if patch.get('target') != expected['patch_target'] or str(patch.get('threshold')) not in {'0', '0%'}:
        problems.append('patch coverage threshold differs from manifest')
    if patch.get('informational') is not False or patch.get('if_not_found') != 'failure':
        problems.append('patch coverage is not enforced')
    return problems


def api(path):
    return json.loads(subprocess.check_output(['gh', 'api', path], text=True))


def inspect_repo(expected):
    name = expected['name']
    if expected['visibility'] != 'public':
        return []
    prefix = f'repos/tinkerologie/{name}/contents/'
    yaml = YAML(typ='safe')
    def read(path):
        data = api(prefix + quote(path, safe='/') + '?ref=main')
        return yaml.load(base64.b64decode(data['content']).decode())
    try:
        listing = api(prefix + '.github/workflows?ref=main')
        workflows = {item['name']: read(item['path']) for item in listing if item['type'] == 'file' and item['name'].endswith(('.yml', '.yaml'))}
        problems = [problem for file, doc in workflows.items() for problem in inspect_workflow(file, doc)]
        config = read(expected['codecov_config']) if 'Coverage Gate' in expected['required_checks'] else {}
        problems.extend(inspect_coverage(expected, workflows, config))
        return [f'{name}: {problem}' for problem in problems]
    except (subprocess.CalledProcessError, KeyError, ValueError, TypeError) as error:
        return [f'{name}: workflow inspection failed ({type(error).__name__})']


def main():
    entries = json.loads(Path('governance-manifest.json').read_text())['repositories']
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        problems = [problem for result in pool.map(inspect_repo, entries) for problem in result]
    report = '## Workflow baseline\n\n' + ('\n'.join('- ' + p for p in problems) if problems else 'All public workflows have pinned actions, explicit permissions, job timeouts and artifact retention. Coverage callers and thresholds match the manifest.')
    report += '\n\nPrivate repositories and billing settings need owner verification. No settings or repository code were executed or changed.\n'
    print(report)
    if os.environ.get('GITHUB_STEP_SUMMARY'):
        with open(os.environ['GITHUB_STEP_SUMMARY'], 'a') as output:
            output.write(report)
    return int(bool(problems))


if __name__ == '__main__':
    raise SystemExit(main())
