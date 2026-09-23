# Context Budget

Spend context, reasoning, tool output, and specialist effort where they improve the next engineering decision. Use the existing low/medium/high risk classification; this is a routing policy, not a second risk score or fixed token quota. Correctness, causal diagnosis, safety, and verification override compactness.

| Risk | Initial investigation | Research and review | Output and state |
| --- | --- | --- | --- |
| Low | Target entry point, nearby convention, affected check | One focused path; no delegation unless the runtime permits it and a distinct need is established | Concise command result and final report; working contract usually stays in context |
| Medium | Execution path, direct dependencies, relevant tests and docs | Expand to consumers and failure paths; plan and independent review where required by the route | Summarize successful checks; retain failure excerpts and optional continuation state |
| High | Trust/data boundaries, architecture, failure and rollback paths, relevant history and tests | Deep or parallel research when justified; specialist/adversarial review and stronger verification | Preserve diagnostic evidence; use durable state when the work spans phases or sessions |

## Read deliberately

Start at the entry point, follow the actual execution path, then direct dependencies, relevant tests, and authoritative documentation. Expand when the evidence points outward. Before a large read, identify the decision it informs, search for the relevant section, prefer a bounded range, and check whether verified facts are already in the contract. Reopen the source when the decision needs exact current detail; a summary never supersedes source truth.

Keep tool output as small as the next decision permits. On native Windows, a released RTK binary may be invoked selectively for noisy commands when it materially reduces output; it is optional and needs no transparent hook. Skip it where measured benefit is negligible. For successful tests/builds, a compact summary with command, scope, exit status, and counts is usually enough. On failures, inspect the compact result first; if failed names, warnings, stack frames, or causal diagnostics are missing, obtain `rtk recall` output or focused raw output before diagnosing or claiming verification. Raw commands remain authoritative when needed. Use deterministic scripts for mechanical audits instead of loading raw listings into model context.

## Research and delegation

Low risk normally needs one focused investigation; medium risk needs execution-path evidence and affected tests; high risk may need architecture, security, or domain research. These are starting depths, not caps. Follow [orchestration](orchestration.md) before delegation. Assign each specialist one independent question, minimum sufficient inputs, explicit authority, evidence requirements, and a short output. Avoid duplicate broad searches. The coordinator verifies conclusions against current source.

## Continuation state

Create a compact task-state artifact only when long work, multiple phases, several specialists, growing context, or likely resumption makes it useful. Use the repository's existing task/planning location, or a temporary `.task-state.md` only when no convention exists and the artifact will be managed deliberately. Do not create it for small work.

```text
Objective / current phase:
Verified facts (with source pointers):
Relevant files:
Decisions and constraints:
Checks run (result and environment):
Failures / unknowns:
Remaining work / next action:
```

Keep the Task Contract as the authority for intent and acceptance; state records execution continuity. Link rather than copy code, plans, logs, or conversation history. Remove or archive temporary state according to repository convention when it no longer serves the task; never delete a user-owned file without authorization.

## Reasoning and communication

Use deeper reasoning when root cause, architecture, security, money, concurrency, migrations, or destructive effects require it. A skill cannot change the current model or reasoning effort. Suggest a higher or lower execution profile only when the runtime exposes a safe user-controlled choice and the recommendation materially helps; do not silently override the user's selection or hard-code model names.

Share progress when a discovery, decision, risk, or blocker matters, not for each routine tool call. Final reports state outcome, changes, evidence, and material limitations once. Before compacting any content, ask: did this retain the evidence required for the next decision?
