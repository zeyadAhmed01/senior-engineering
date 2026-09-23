# Adversarial Review

Use for high-risk changes and workflow pressure tests.

Challenge the strongest assumptions:

- What user input, timing, state, or actor makes this fail?
- Which retry, duplicate, reorder, cancellation, partial failure, or stale identity violates the invariant?
- Which trust boundary accepts attacker-controlled data?
- Which local success is being mistaken for CI, deployment, or production proof?
- Which external mutation could occur without explicit authority?
- Which rollback depends on data or infrastructure that will not exist?
- Which requirement has no evidence path?
- Which extra abstraction survives only because the plan assumes future needs?

Pressure does not justify a fictional blocker. Retain only challenges with a plausible trigger or a safety-sensitive uncertainty.

