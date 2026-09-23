# Completion Audit

1. Reconstruct the Task Contract from the current request and any authoritative artifacts.
2. Inspect final status and complete relevant diff.
3. List each acceptance criterion and its evidence.
4. Check unauthorized scope, hidden generated changes, stale docs, migrations, and dependency effects.
5. Confirm test edits retain intended protection.
6. Check the highest-risk failure and rollback path.
7. Verify CI, PR, release, deployment, or production state live when those claims are made.
8. Classify every claim; do not average failures into an overall pass.

An overall `PROVEN` verdict requires every material USER-STATED criterion to be PROVEN and no relevant FAILED item. `PARTIALLY_PROVEN` is appropriate when the artifact is ready but external or environment-specific evidence is unavailable.

