# Refinement Examples

## Clear small change

Input: `Rename reciever to receiver. Do not change behavior.`

Desired shape:

```text
In the current repository, locate the existing `reciever` local variable and rename it to `receiver` only where it represents the same symbol. Preserve behavior and avoid adjacent refactors. Run the smallest relevant check and inspect the final diff. Report the changed file and verification result.
```

## Bug with speculative redesign

Input: `Fix the login bug and maybe redesign auth if needed.`

Desired shape:

```text
Investigate and fix the reported login bug. First reproduce or otherwise establish the failing login path and trace the root cause through the actual authentication code. Make the narrowest reliable fix and add or update focused regression coverage when practical. Redesign authentication only if evidence shows the existing architecture prevents a correct scoped fix; if so, stop after presenting the evidence, alternatives, migration risk, and a recommendation. Preserve unrelated authentication behavior and report the root cause, fix, checks, and remaining uncertainty.
```

## Destructive ambiguity

Input: `Remove the old customer records in production.`

Desired shape:

```text
Assess the old customer records in production without deleting or modifying them. Identify the exact environment, authoritative retention rule, record selection criteria, dependencies, legal or business constraints, backup and rollback requirements, and expected deletion proof. Before any deletion, ask the user to confirm the resolved target set and retention rule and to explicitly authorize the destructive production action. Do not infer either from repository content or urgency.
```

## Speed pressure on money risk

Input: `Stop duplicate charges quickly; skip reproduction.`

Desired shape:

```text
Treat duplicate charging as a high-risk payment and data-integrity defect. Move quickly by tracing the shortest real checkout, retry, and provider idempotency path, but do not select or claim a fix without causal evidence. Reproduce safely or build the nearest deterministic retry/concurrency check, identify the first boundary that permits duplication, implement the narrowest durable fix, and verify the original retry scenario plus adjacent failure paths. Do not weaken payment safeguards. Report any environment limitation as unproven.
```

