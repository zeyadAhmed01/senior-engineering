---
name: verify
description: Verify software requirements, fixes, reviews, or completion claims against fresh evidence. Use when the user asks to test, validate, prove, confirm, re-check, or determine whether work is actually complete.
license: MIT
---

# Verify

Verification is independent evidence gathering, not a restatement of implementation confidence.

## Build the claim set

Extract each requirement and claimed outcome. Label inputs USER-STATED, VERIFIED, INFERRED, or UNKNOWN. For each claim, define the smallest observation that could prove or refute it.

Use the Engineer [clarification protocol](../engineer/references/clarification.md) when a material UNKNOWN blocks a verification step; continue independent checks while waiting.

Read [verification method](references/verification-method.md) for test selection and evidence states. Read [completion audit](references/completion-audit.md) when assessing finished work or release readiness.

## Inspect current state

Use the current code, configuration, schema, diff, runtime, CI, or external object. Do not reuse stale results when the artifact changed afterward. Do not trust a worker, PR body, comment, or previous report without checking its cited evidence.

## Run proportionate checks

Start narrow, then expand only where risk or failures require it. Bind each result to an exact command, environment, commit/SHA, object identifier, or inspected source.

For noisy checks, use the Engineer [context budget](../engineer/references/context-budget.md): keep passing summaries, failed cases and relevant excerpts, then inspect focused raw output when diagnosis needs it.

## Verdict

For each claim report:

- PROVEN - directly demonstrated now;
- PARTIALLY_PROVEN - meaningful evidence passed but a required layer is unavailable;
- FAILED - current evidence contradicts it;
- BLOCKED - safe verification requires missing input, access, or external state.

Do not implement a fix during a verification-only request. Report the cause and smallest next action when evidence fails.

For completed verification reports, follow the Engineer [completion gate](../engineer/references/completion-gate.md) to recommend the best next step and provide a prompt scoped to that step.
