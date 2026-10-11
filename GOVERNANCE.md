# Contribution Governance

These rules apply to every tinkerologie repository and to every contributor,
including AI coding agents (Codex, Claude Code, Copilot, and others).

## 1. Issue first, with a type label

- Open an issue from the **Bug report** or **Enhancement request** template
  before opening a pull request.
- Keep the template title prefix: `[Bug]: ...` or `[Enhancement]: ...`.
  Issues created with `gh issue create` or the API skip the template's labels,
  so automation labels them `bug` or `enhancement` from the title prefix and
  the template headings.
- CodeRabbit posts a **Coding Plan** on the issue once it is labeled. Use that
  plan when implementing.

## 2. Link the issue from the pull request

In the PR template's **Related Issues** section, use one of:

| Keyword | Effect |
| --- | --- |
| `Closes #123`, `Fixes #123`, `Resolves #123` (any tense) | Links the issue and closes it on merge |
| `Part of #123`, `Related to #123`, `Addresses #123`, `Implements #123` | Links without closing |
| `owner/repo#123` or a full issue URL | Cross-repository reference |
| `None` | Self-contained change with no issue |

## 3. One change at a time

- Contributors without write access can have at most **2 open pull requests**
  per repository (enforced by GitHub). Drafts do not count.
- Do not open several PRs that edit the same files (`CHANGELOG.md`,
  translations, `README.md`, generated bundles). Merging one makes the rest
  conflict. Finish, get merged, rebase, then start the next.
- When a PR gets the `conflicts` label, rebase on the default branch, resolve
  the conflicts, re-run the tests, and force-push before doing anything else.

## 4. Coverage

In repositories that report to Codecov, `codecov/patch` must pass: at least
**90%** of the lines you add or change must be covered by tests. Read the
Codecov PR comment and add tests for every uncovered line it lists before
requesting review. Do not lower coverage targets or add ignore rules to pass.

## 5. Stale items

Issues and pull requests with no activity for **14 days** are labeled `stale`
and closed **30 days** later if nothing changes. Any comment, push, or label
change resets the timer. `pinned`, `security`, `confirmed`, and
`work-in-progress` are exempt.

## Automation

Shared reusable workflows live in [`.github/workflows`](.github/workflows):

| Workflow | Purpose |
| --- | --- |
| `issue-labeler.yml` | Adds `bug` or `enhancement` to untyped open issues |
| `pr-conflicts.yml` | Labels and comments on PRs that conflict with the default branch |
| `stale.yml` | Marks inactive issues and PRs stale, then closes them |

Each repository calls them from small caller workflows, for example:

```yaml
jobs:
  label:
    permissions:
      issues: write
    uses: tinkerologie/.github/.github/workflows/issue-labeler.yml@v1
```

CodeRabbit organization settings live in
[`tinkerologie/coderabbit`](https://github.com/tinkerologie/coderabbit).
