# Implementation and Testing

## Implement in evidence-backed slices

For each observable behavior:

1. Demonstrate the gap or characterize current behavior.
2. Make the smallest coherent change.
3. Run the focused proof.
4. Refactor only inside scope while green.
5. Inspect the slice for unintended contracts, secrets, generated noise, and error paths.

Follow repository conventions and authoritative current documentation. Keep business logic reusable where the repository requires it; do not create layers solely to satisfy a generic pattern.

## Select tests by risk

- Pure invariant: unit or property test.
- Module collaboration: integration test.
- Public API/event: contract and consumer compatibility.
- Storage/migration: realistic persistence, restart, rollback, and partial failure.
- User workflow: runtime or end-to-end behavior.
- Timing/concurrency: deterministic coordination first, repetition/stress second.
- Security: allowed and denied paths at the trust boundary.

For bugs, prefer a focused red-to-green regression when safe and practical. Do not delete valid prior work because it was not written test-first. Do not weaken, skip, or delete a valid test merely to obtain green output.

## Verification order

Run narrow checks during implementation, then the broadest proportionate set: focused tests, affected suite, type/static analysis, lint/format, build/package validation, and runtime/security/performance checks created by the change.

Classify failures as change-caused, pre-existing, flaky, environment, or unknown with evidence. Rerun affected checks after later edits.

