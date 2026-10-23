# Repository Standards

Every tinkerologie repository follows this layout and these conventions, so
all projects look the same and contributors (human or AI agent) always know
where things are. [GOVERNANCE.md](GOVERNANCE.md) covers how to contribute;
this file covers how repositories are set up.

## 1. Repository settings

| Setting | Value |
| --- | --- |
| Default branch | `main` |
| Merge methods | **Squash only**, commit title = PR title, message = PR description |
| Delete branch after merge | On |
| Auto-merge | Allowed |
| Wiki, Projects | Off |
| Private vulnerability reporting | On |
| Secret scanning and push protection | On |
| Dependabot alerts and security updates | On |
| Open pull request limit (users without write access) | 2, drafts excluded |
| Description and topics | Required (topics drive the org README) |

## 2. Default branch ruleset

One ruleset per repository, named **Default branch protection**:

- Block deletion and force pushes of `main`.
- Changes through pull requests only; squash merge only.
- All review conversations must be resolved before merging (CodeRabbit included).
- Required status check: **PR Governance**.
- No Copilot code review: CodeRabbit is the only review bot.
- Repository admins may bypass.

## 3. Files every repository has

| Path | Purpose |
| --- | --- |
| `README.md` | What it is, install, usage |
| `CHANGELOG.md` | [Keep a Changelog](https://keepachangelog.com/) with an `[Unreleased]` section |
| `CONTRIBUTING.md` | Contribution steps, ending with the shared *Issue and Pull Request Governance* section |
| `AGENTS.md` | Instructions for AI coding agents (single source of truth) |
| `CLAUDE.md` | Points Claude Code at `AGENTS.md` |
| `LICENSE` | Project licence |
| `.editorconfig`, `.gitattributes` | Shared whitespace and line-ending rules |
| `.github/CODEOWNERS` | Review ownership |
| `.github/dependabot.yml` | Dependency updates (section 6) |
| `.github/PULL_REQUEST_TEMPLATE.md` | PR template checked by PR Governance |
| `.github/ISSUE_TEMPLATE/01-bug-report.yml`, `02-enhancement-request.yml`, `config.yml` | Issue forms |

Code of Conduct, Security policy, Support and Funding come from this
organization repository and apply to every project automatically. A
repository only adds its own copy when it needs project-specific content.

## 4. Workflows

### Naming

- File names are kebab-case and end in `.yml` (never `.yaml`).
- The `name:` of a workflow and of every job is Title Case and describes the
  purpose, for example `CI` and `Test`.
- Matrix jobs append the variable: `Test (Python 3.13)`, `Test (Node 22)`.

### Standard set

| File | Workflow name | Jobs | Repositories |
| --- | --- | --- | --- |
| `ci.yml` | CI | Lint, Test, Build (as applicable) | All |
| `validate.yml` | Validate | HACS, Hassfest | Home Assistant integrations |
| `release.yml` | Release | (project specific) | All that publish releases |
| `pr-governance.yml` | PR Governance | PR Governance, Governance Report | All |
| `pr-conflicts.yml` | PR Conflicts | Conflicts | All |
| `issue-labeler.yml` | Issue Labeler | Label | All |
| `stale.yml` | Stale | Stale | All |
| `labeler.yml` | PR Labeler | Label | All (path rules in `.github/labeler.yml`) |
| `dependabot-auto-merge.yml` | Dependabot Auto-merge | Merge when CI passes | All |

Project-specific extras keep a descriptive kebab-case name, for example
`codeql.yml`, `docker.yml`, `docs.yml`, `playwright.yml`,
`check-api-boundary.yml`. `copilot-setup-steps.yml` keeps the name GitHub requires.

### Conventions

- Third-party actions are pinned to a full commit SHA with the version as a
  comment: `uses: actions/checkout@<sha> # v7.0.1`. Dependabot keeps them current.
- Workflows declare `permissions` explicitly and request the minimum.
- CI runs on `push` to `main`, `pull_request` (opened, synchronize, reopened,
  ready_for_review), and `workflow_dispatch`, with a concurrency group that
  cancels superseded pull request runs.
- Every `schedule` entry sets `timezone: Australia/Brisbane` (no daylight
  saving, so runs never shift).
- Checkouts use `persist-credentials: false`. A step that must push passes the
  token explicitly to that one `git push`.
- Release workflows: workflow-level `permissions: contents: read`; each job
  requests only what it uses, with a comment saying why (`contents: write` to
  publish the release, `id-token: write` for trusted publishing); no `${{ }}`
  expressions inside `run:` scripts (pass them through `env:`); no dependency
  caches. `zizmor` reports no errors or warnings.
- Shared governance workflows are called from
  [`tinkerologie/.github`](.github/workflows) pinned by SHA.
- `labeler.yml` calls the shared `pr-labeler.yml`: path labels from the repository's
  `.github/labeler.yml`, then at most one type label, `enhancement` or `bug`. The title's Conventional Commit type decides (`feat` → `enhancement`, `fix`
  → `bug`, any other type → neither), then the branch prefix, then a single ticked Type
  of Change box, then the linked issues. A contradicting type label is removed only if
  automation added it. `documentation` never comes from CHANGELOG.md alone, because every
  pull request updates it.

## 5. Labels

The organization label set below is synced to every repository by the
`Label Sync` workflow in this repository. Repositories may add their own
`area: <name>` labels; those are never deleted by the sync.

| Group | Labels |
| --- | --- |
| Type | `bug`, `enhancement`, `documentation`, `question`, `dependencies`, `security` |
| Status | `triage`, `confirmed`, `blocked`, `work-in-progress`, `stale`, `conflicts` |
| Priority | `priority: critical`, `priority: high`, `priority: medium`, `priority: low` |
| Resolution | `duplicate`, `invalid`, `wontfix` |
| Community | `good first issue`, `help wanted` |
| Automation | `pinned`, `no-type`, `no-plan` |

## 6. Dependabot

- One update block per ecosystem in use, plus `github-actions`.
- Weekly schedule (Monday), grouped minor and patch updates. Exception: Home Assistant
  integrations check their Python ecosystem daily so new Home Assistant releases are
  picked up quickly.
- Labels: `dependencies`. Commit messages use the `chore(deps)` prefix.
- Python projects with a `uv.lock` use the `uv` ecosystem (not `pip`), so version and
  security updates reach the lock file that security alerts are raised from.
- Hold back majors that cannot pass CI on their own, with the reason in a comment:
  `typescript` where typescript-eslint is used (it supports TypeScript below 6.1),
  `homebridge` (v2 is the supported runtime), and `@types/node`, which tracks the oldest
  Node version in `engines`.
- Home Assistant integrations ignore every package that `pytest-homeassistant-custom-component`
  pins exactly (`pytest`, `pytest-asyncio`, `pytest-cov`, `syrupy`, `freezegun`, `respx`,
  `pydantic` and the rest of its `==` pins) when the project lists it directly. Bumping one on
  its own makes the lock unsatisfiable and fails the whole update run; they move when
  `pytest-homeassistant-custom-component` does. `homeassistant` itself is grouped with
  `pytest-homeassistant-custom-component` for the same reason.
- `dependabot-auto-merge.yml` merges a Dependabot pull request whose largest update is a
  patch or minor version, or that moves an action from `home-assistant/actions` or
  `hacs/action` from one commit to another (those have no releases, so Dependabot cannot
  classify the bump), once the other checks and commit statuses on its head commit have
  finished without a failure (skipped and neutral results are fine). A Codecov check that is still pending is not waited for (patch coverage never
  reports on lock-file-only changes); a Codecov failure blocks the merge. GitHub's
  built-in auto-merge would not wait: it waits only for required checks, and PR
  Governance is skipped for Dependabot. Majors and grouped pull requests containing a
  major are left for a person, and open review threads still block the merge. A merge that
  races another push to the default branch is retried. After
  re-running a failed check, re-run the Auto-merge job too (or comment
  `@dependabot rebase`); nothing restarts it automatically.

## 7. Issues and pull requests

Issue forms and the PR template share one structure across all repositories;
only the project-specific fields differ (versions, affected areas, standards
checklists). See [GOVERNANCE.md](GOVERNANCE.md) for the contribution rules
they enforce.
