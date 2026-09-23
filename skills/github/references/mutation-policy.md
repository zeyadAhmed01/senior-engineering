# GitHub Mutation Policy

## Read-only by default

Inspection includes reading issues/comments, PR metadata/diffs/reviews, checks/logs, branches, releases, and security findings. It does not include comments, labels, assignments, edits, pushes, reviews, merges, tags, releases, or reruns that consume or alter remote state.

## Authorization

External mutation is authorized only when the user explicitly requests that outcome or the active request unambiguously includes it, such as “open a PR” or “comment this finding.” “Review,” “investigate,” “check,” and “tell me” are read-only.

When a verb such as “ship” could mean push, open a PR, merge, tag, release, or deploy, finish the read-only readiness check and ask which action the user intends before any external mutation. A missing remote or deployment target is a separate blocker; it does not resolve the ambiguity.

Before mutation confirm:

- target host and repository;
- object and current state;
- exact intended change;
- user authorization source;
- credentials/capability have least practical scope;
- local/remote SHA or concurrency precondition where relevant.

High-impact actions—merge, tag, release, deployment, branch deletion, force-push, security-advisory publication—require explicit action-specific authorization.

## Write and verify

Use an idempotent or uniquely identifiable operation where possible. After uncertain failure, read current state before retrying. Read back the result and bind it to URL/number/SHA. Never expose credentials in commands, comments, logs, or reports.
