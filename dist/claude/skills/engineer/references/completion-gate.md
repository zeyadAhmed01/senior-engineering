# Completion Gate

Run this gate immediately before the final claim.

1. Re-read the Task Contract and current user request.
2. Map each USER-STATED requirement to the changed seam and fresh evidence.
3. Inspect current status and the complete relevant diff.
4. Confirm later edits did not invalidate earlier checks; rerun affected checks.
5. Distinguish code/artifact readiness, local runtime behavior, CI, deployment, and production state.
6. Check authorization before any remaining external mutation.
7. Record material UNKNOWN and UNPROVEN items.

Use these outcomes:

- **PROVEN**: current evidence directly demonstrates the claim.
- **PARTIALLY_PROVEN**: important evidence passed but a relevant layer/environment remains unavailable.
- **FAILED**: evidence contradicts a requirement.
- **BLOCKED**: required evidence or safe progress depends on missing access, input, or external state.

Never claim success from reasoning alone, a stale run, a worker summary, a passing command that missed the changed behavior, a commit, a PR, or a release record.

Final reports lead with the outcome, then changed behavior, exact verification, and material limitations. Keep them concise without concealing failures, security implications, migration steps, or unresolved risk.
