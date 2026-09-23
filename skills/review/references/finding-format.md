# Finding Format

Use one compact item per independent defect:

```text
[severity] Short title — file:line or artifact section
Trigger: concrete input, state, actor, or timing
Impact: observable failure or risk
Evidence: code path, contract, test, or authoritative source
Direction: smallest reliable correction
```

Severities:

- Critical: credible security breach, irreversible data loss, or unsafe production effect.
- High: reachable correctness, money, auth, data-integrity, or release-blocking defect.
- Medium: reachable regression or broken behavior with bounded recovery.
- Low: substantive non-blocking improvement. Omit style preferences and trivia.

Verification limitations are not findings unless the missing evidence itself violates a requirement.

