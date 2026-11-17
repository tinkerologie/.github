"""Check that baseline regressions are reported without making network requests."""
import copy
import unittest
from audit_workflow_baseline import inspect_workflow, inspect_coverage


class BaselineTests(unittest.TestCase):
    def test_runner_bounds_and_pins(self):
        valid = {'permissions': {}, 'jobs': {'test': {'runs-on': 'ubuntu-latest', 'timeout-minutes': 10, 'steps': [{'uses': 'actions/upload-artifact@' + 'a' * 40, 'with': {'retention-days': 7}}]}}}
        self.assertEqual(inspect_workflow('ci', valid), [])
        broken = copy.deepcopy(valid)
        del broken['permissions']
        del broken['jobs']['test']['timeout-minutes']
        broken['jobs']['test']['steps'][0] = {'uses': 'actions/upload-artifact@main'}
        self.assertEqual(len(inspect_workflow('ci', broken)), 4)
        self.assertEqual(len(inspect_workflow('issue-labeler.yml', {'permissions': {}, 'on': {'schedule': [{'cron': '17 3 * * *'}]}})), 1)
        self.assertEqual(len(inspect_workflow('caller', {'permissions': {}, 'jobs': {'merge': {'uses': 'tinkerologie/.github/.github/workflows/dependabot-auto-merge.yml@' + 'a' * 40}}})), 2)
        self.assertEqual(inspect_workflow('caller', {'permissions': {}, 'jobs': {'call': {'uses': 'org/repo/.github/workflows/ci.yml@' + 'a' * 40}}}), [])

    def test_coverage_fail_open_and_deadlock(self):
        expected = {'required_checks': ['Coverage Gate'], 'coverage_source_pattern': '^src/', 'patch_target': '90%'}
        gate = {'on': {event: {} for event in ['pull_request_target', 'status', 'workflow_run', 'workflow_dispatch']}, 'jobs': {'coverage': {'uses': 'tinkerologie/.github/.github/workflows/coverage-gate.yml@' + 'a' * 40, 'with': {'source-pattern': '^src/'}}}}
        config = {'github_checks': False, 'codecov': {'require_ci_to_pass': False, 'strict_yaml_branch': 'main', 'notify': {'wait_for_ci': False}}, 'coverage': {'status': {'patch': {'default': {'target': '90%', 'threshold': '0%', 'informational': False, 'if_not_found': 'failure'}}}}}
        self.assertEqual(inspect_coverage(expected, {'coverage-gate.yml': gate}, config), [])
        config['codecov']['notify']['wait_for_ci'] = True
        config['coverage']['status']['patch']['default']['informational'] = True
        gate['jobs']['coverage']['with']['source-pattern'] = '^never/'
        problems = inspect_coverage(expected, {'coverage-gate.yml': gate}, config)
        self.assertEqual(len(problems), 3)
        self.assertEqual(inspect_coverage({'required_checks': ['CI Gate']}, {}, {}), [])


if __name__ == '__main__':
    unittest.main()
