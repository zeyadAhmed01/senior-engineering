# Issue to Pull Request

## Validate the issue

Read the title, full body, comments, links, target branch, and overlapping PRs. Extract each current-behavior claim and acceptance criterion. Trace them against current target-branch code; mark verified, refuted, conditional, or unverified.

An issue may be already fixed, based on a false premise, too ambiguous, or too broad. Report that before implementation. Do not edit the issue unless authorized.

## Prepare delivery

When implementation and delivery are authorized:

1. Resolve and fetch the exact base.
2. Inspect existing local/remote issue branches and PRs before creating another.
3. Use an isolated worktree when the current checkout is dirty or branch isolation materially reduces risk.
4. Implement under the Engineer workflow and verify locally.
5. Screen the staged scope and diff for unrelated work and secrets.
6. Commit and push only when authorized; follow repository conventions rather than forcing a commit standard.
7. Recheck the base, overlapping PRs, and remote head before creating or updating a PR.
8. Include requirement mapping, verification, limitations, issue linkage, and plan deviations in the PR body.
9. Read back the PR and confirm base/head SHA.

Never create an empty PR for already-satisfied work. Never force-push to repair an unexplained remote mismatch.

