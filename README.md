# Tinkerologie shared GitHub configuration

This public `.github` repository holds the organisation profile, default community
files and reusable GitHub Actions workflows for Tinkerologie projects.

Looking for an integration, plugin or library? Start with the
[organisation profile](https://github.com/tinkerologie), maintained in
[profile/README.md](profile/README.md).

## What lives here

| File or directory | Purpose |
| --- | --- |
| [profile/README.md](profile/README.md) | Public organisation overview and project directory |
| [GOVERNANCE.md](GOVERNANCE.md) | Contribution and pull request requirements |
| [STANDARDS.md](STANDARDS.md) | Repository settings, automation and free-tier operating policy |
| [SECURITY.md](SECURITY.md) | How to report vulnerabilities privately |
| [SUPPORT.md](SUPPORT.md) | Where to get help |
| [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) | Community expectations |
| [.github/workflows](.github/workflows) | Shared label, stale-item, dependency, governance and coverage automation |
| [governance-manifest.json](governance-manifest.json) | Expected repository profiles and required checks |
| [scripts](scripts) | Configuration validation, automation tests and drift detection |

## How inheritance works

GitHub can use supported community health files from this repository when a project
does not provide its own. A project's own files take precedence. `GOVERNANCE.md` and
`STANDARDS.md` are organisation conventions, not automatically enforced GitHub settings.

Workflows are **not inherited automatically**. Each project explicitly calls a shared
workflow, pinned to a full commit SHA. Publishing a change here does not update existing
callers; update their pins after testing. The manifest and weekly Governance Drift check
help detect missing required checks and repository-setting drift.

## Maintaining the automation

Use standard GitHub-hosted runners and free service features. Keep paid usage blocked;
do not add trials, paid review requirements or larger runners. Coverage gating is
metadata-only and event-driven; docs and dependency-only changes do not wait for Codecov.
See [STANDARDS.md](STANDARDS.md) for thresholds, exceptions and recovery instructions.

Before changing shared workflows, run the checks used by
[CI](.github/workflows/ci.yml), validate workflow syntax with `actionlint`, and verify a
caller on GitHub. Never execute pull request code in privileged metadata workflows.

For project bugs and feature requests, use that project's issue tracker. For shared
configuration changes, open an issue in this repository. Read the governance and security
policies before contributing or reporting a vulnerability.
