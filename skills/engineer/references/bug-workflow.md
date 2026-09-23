# Bug Workflow

## Define the failure

Capture expected behavior, actual behavior, affected scope, frequency, environment, first known bad state, and available evidence. Separate observed facts from reports and hypotheses.

## Reproduce or bound

Reproduce safely when practical. For intermittent, concurrency, payment, data-integrity, security, or destructive bugs, do not accept speed pressure as a reason to skip causal evidence. Before editing, run the smallest safe check against untouched code; if none exists, add a focused reproducer and run it first. If the user asks to skip this check, state briefly why it is required and run it. Do not substitute a post-fix-only test for the baseline. If direct reproduction is unsafe or unavailable, stop before implementation unless a safe deterministic model can be built, and label the gap.

## Trace root cause

1. Follow the actual entry point and state transitions.
2. Identify the first boundary where actual state diverges from expected state.
3. Form one falsifiable hypothesis.
4. Run the smallest discriminating check.
5. Repeat until evidence identifies the mechanism or the investigation is honestly blocked.

Do not mistake a stack-trace location, warning, correlated timestamp, or plausible code smell for root cause.

## Fix

- Add or identify a regression check that fails for the intended reason when feasible.
- Change the narrowest root mechanism, not only the visible symptom.
- Preserve public behavior outside the defect.
- Check sibling producers/consumers when they share the proven cause; do not turn that check into unrelated cleanup.

## Verify

Run the original reproduction, focused regression, adjacent failure paths, and proportionate broader checks. For retries or concurrency, verify idempotency and ordering at the durable boundary, not only in the UI.

Report reproduction status, root-cause evidence, fix, checks, and remaining uncertainty.
