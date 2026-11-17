"""Read public repository settings and compare them with the approved manifest."""
import json
import os
import subprocess
import sys
from pathlib import Path


def api(path):
    return json.loads(subprocess.check_output(["gh", "api", path], text=True))


UNAVAILABLE = []

def inspect(expected):
    name = expected["name"]
    if expected["visibility"] == "private":
        return []  # No privileged credentials or private metadata needed by this job.
    root = "repos/tinkerologie/" + name
    repo = api(root)
    problems = []
    wanted = {"visibility": "public", "default_branch": "main", "allow_squash_merge": True,
              "allow_merge_commit": False, "allow_rebase_merge": False,
              "delete_branch_on_merge": True, "allow_auto_merge": True}
    hidden = [key for key in wanted if key not in repo]
    if hidden:
        UNAVAILABLE.append(f"{name}: " + ", ".join(hidden))
    for key, value in wanted.items():
        if key in repo and repo[key] != value:
            problems.append(f"{name}: {key} is {repo.get(key)!r}; expected {value!r}")
    rules = []
    for summary in api(root + "/rulesets?per_page=100"):
        if summary["name"] == "Default branch protection" and summary["enforcement"] == "active":
            detail = api(root + "/rulesets/" + str(summary["id"]))
            refs = detail.get("conditions", {}).get("ref_name", {})
            if not refs.get("exclude") and any(ref in refs.get("include", []) for ref in ["~DEFAULT_BRANCH", "refs/heads/main", "~ALL"]):
                rules.extend(detail["rules"])
    types = {r["type"] for r in rules}
    for kind in ["pull_request", "deletion", "non_fast_forward", "required_status_checks"]:
        if kind not in types:
            problems.append(f"{name}: missing active {kind} protection")
    for rule in rules:
        if rule["type"] == "pull_request":
            params = rule["parameters"]
            if params.get("required_approving_review_count") != 0 or not params.get("required_review_thread_resolution") or params.get("allowed_merge_methods") != ["squash"]:
                problems.append(f"{name}: solo-maintainer PR policy changed")
    checks = {c["context"] for r in rules if r["type"] == "required_status_checks"
              for c in r["parameters"]["required_status_checks"] if c.get("integration_id") == 15368}
    for check in expected["required_checks"]:
        if check not in checks:
            problems.append(f"{name}: missing required {check}")
    return problems


def main():
    manifest = json.loads(Path("governance-manifest.json").read_text())
    problems = []
    actual = api("orgs/tinkerologie/repos?per_page=100&type=public")
    known = {r["name"] for r in manifest["repositories"]}
    problems.extend(f"{r['name']}: new public repository needs a governance profile" for r in actual if r["name"] not in known)
    for expected in manifest["repositories"]:
        try:
            problems.extend(inspect(expected))
        except (subprocess.CalledProcessError, KeyError, ValueError) as error:
            problems.append(f"{expected['name']}: inspection failed ({type(error).__name__})")
    report = "## Governance drift\n\n" + ("\n".join("- " + p for p in problems) if problems else "All public repository settings and required CI checks match the manifest.")
    if UNAVAILABLE:
        report += "\n\nMerge settings hidden from this read-only token (owner verification required):\n" + "\n".join("- " + item for item in UNAVAILABLE)
    report += "\n\nPrivate Free-plan exceptions and third-party billing require owner review. No settings were changed.\n"
    print(report)
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a") as output:
            output.write(report)
    return int(bool(problems))


if __name__ == "__main__":
    sys.exit(main())
