# Review and CI Reconciliation

## Gather current state

Fetch formal reviews, inline threads, issue comments, required and optional checks, mergeability, base/head SHA, and prior disposition comments. Bind the snapshot to the current head.

## Validate findings

Treat each review finding and CI explanation as a hypothesis. Trace it to current code. Classify confirmed, partial, refuted, judgment, or unverified. Reconcile duplicates and prior dispositions by claim.

Fix only when the user requested fixes or the active delivery task authorizes them. A review-only request stops at findings.

## CI

Distinguish required, optional, pending, skipped/neutral, cancelled, and failed checks according to current repository rules. Inspect logs for the first relevant failure and determine whether the change caused it. Local success is not CI success.

## Converge

After authorized fixes, rerun affected local checks, inspect the diff, push with authorization, and confirm remote head. Post dispositions or request rereview only when authorized. Do not merge merely because findings are cleared; merge is a separate high-impact action.

