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

## Recommend the next step

Every final response that reports a workflow outcome—complete, partial, failed, or blocked—ends with one evidence-based next step. Name why it is the best next action from the current state, then include a copy/paste-ready prompt the user can send to Codex to do that step.

- Choose from the actual outcome, risk, user's goal, and remaining evidence. Recommend an independent, read-only review before commit when it would materially improve confidence, especially for medium/high-risk changes or meaningful unresolved correctness or regression concerns. For a narrow, low-risk change whose focused check and diff establish the request, do not manufacture a review or commit step; say no further Codex step is recommended if none is warranted. If checks are missing or failing, recommend completing or fixing verification first. After a review finds issues, recommend addressing those findings rather than repeating the review.
- Keep the prompt bounded to that one next step. Carry forward the user's requirements, relevant files or current diff, known verification, and constraints. Use the relevant `senior-engineering` skill when applicable.
- Do not invent acceptance criteria, repeat work already completed, imply an unperformed check passed, or grant authority for edits, destructive actions, or external writes that the user has not authorized.
- If no meaningful follow-up is warranted, say that no further Codex step is recommended instead of manufacturing work. A prompt is needed only when there is an actionable recommendation. Do not add this section to progress updates or a response that is still waiting for a clarification answer.
- For `refine`, the refined prompt itself is the recommended next step and ready-to-send prompt. Preserve its output-only contract; do not append a second recommendation.

Example when independent review is the best next step after a feature implementation and passing focused checks:

**Recommended next step:** Get an independent review of the feature for regressions before extending it.

**Prompt for Codex:**

```text
Use $senior-engineering:review to review the feature I just implemented. Compare the current diff with the original requirements, inspect relevant code and tests, and report actionable bugs, regressions, security concerns, and verification gaps with file and line locations. Do not modify files; stop after the review.
```
