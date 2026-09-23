# Classification and Risk

## Primary task types

- Feature: new externally meaningful behavior.
- Bug: actual behavior conflicts with intended behavior.
- Bounded change: maintenance, configuration, docs, refactor, or narrow compatibility work.
- Architecture: ownership, component, data-flow, or long-lived design decision.
- Investigation: diagnosis or evidence is the deliverable.
- Review: assess an artifact without modifying it.
- Delivery: reconcile implemented work with GitHub.
- Release: assess or execute versioned publication/deployment readiness.

Choose one primary type. Attach secondary modules only when they change the required evidence.

## Risk

### Low

Narrow, local, reversible, familiar, and without sensitive data or external effects.

Route: contract snapshot, targeted inspection, edit or answer, focused check, final status/diff.

### Medium

Meaningful behavior change, several files or components, migration/compatibility concerns, or material regression surface.

Route: contract, discovery, short design/plan, implementation, targeted tests, independent review, verification.

### High

Any material authentication/authorization, secrets, money, data integrity, destructive state change, concurrency, public schema/API, infrastructure, deployment, release, or difficult rollback.

Route: contract, deep investigation, alternatives/rollback, plan critique, isolated implementation, focused and broader tests, specialist/adversarial review, fresh verification, explicit external-action gate.

## Modifiers

- Raise one level when uncertainty prevents bounding impact.
- Dirty shared workspaces, stale branches, missing tests, unavailable environments, and unclear ownership increase operational risk.
- A request for speed changes sequencing, not the evidence needed for a safety claim.
- Do not lower high risk because a path seems unlikely. Establish reachability and consequence.
- Do not inflate a clear low-risk task into architecture work.

