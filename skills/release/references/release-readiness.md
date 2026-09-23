# Release Readiness

Inspect repository-specific evidence:

1. Scope: intended commits/diff, target branch, version or release identifier.
2. Policy: protected branch rules, approvals, required checks, signing, merge queue, ownership.
3. Quality: focused and broader tests, static analysis, build/package validation, behavioral verification.
4. Security: secret scan, dependency/advisory state, auth/security review where relevant.
5. Data: migrations, compatibility windows, backups, forward/backward behavior, rollback.
6. Artifacts: reproducible build, provenance/signing/checksums when required, registry destination.
7. Operations: configuration, feature flags, observability, capacity, runbook, support ownership.
8. Rollback: trigger, mechanism, data consequences, and rehearsal/evidence.
9. Documentation: user-facing changes, upgrade/migration notes, known limitations.
10. External state: current CI, prior releases/tags, environment health, and unresolved incidents.

Classify each requirement as PROVEN, PARTIALLY_PROVEN, FAILED, or BLOCKED. Do not average a failed safety requirement into an overall pass.

