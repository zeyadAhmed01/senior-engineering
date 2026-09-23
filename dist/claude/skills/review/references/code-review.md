# Code Review

## Completeness passes

Sweep the change separately for:

1. correctness and boundary behavior;
2. error paths and recovery;
3. state, identity, lifetime, concurrency, and ordering;
4. authorization, validation, secrets, and untrusted input;
5. persistence, migrations, and compatibility;
6. performance and resource cost where material;
7. tests, observability, operations, and rollback;
8. scope drift and unintended generated or dependency changes.

For stateful or asynchronous work, map states, transitions, owners, stale identities/generations, repetition, cancellation, replacement, reset, and re-entry.

## Findings

Report a defect only when a realistic trigger and meaningful consequence are supported by code evidence. Expand a confirmed bug through sibling producers/consumers and inverse transitions enough to bound the class, without inventing unrelated scope.

Security, authentication, money, data integrity, and auto-protective mechanisms are always surfaced. If evidence cannot resolve a plausible safety issue, mark it for human review rather than silently dropping it.

Review test edits skeptically. A deleted, skipped, loosened, or narrowed test needs a checkable reason tied to intended behavior, not merely a green suite.

## Counterfactual closure

After drafting findings, assume each suggested fix is applied. Re-read the relevant change and add any defect that would survive. Stop when a full pass adds nothing material.

