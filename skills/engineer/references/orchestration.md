# Adaptive Orchestration

Delegation is an optimization, not a requirement or additional authority. Follow the active runtime's delegation rules; a skill cannot enable agents where the runtime forbids them.

## Delegate when

- questions are independent and can run concurrently;
- a noisy investigation benefits from an isolated context;
- a fresh reviewer should not inherit implementation reasoning;
- a narrow security or verification specialty materially changes confidence.

## Keep local when

- the task is small;
- hypotheses depend on one another;
- agents would edit the same files, schema, lockfile, shared interface, database, or environment;
- coordination cost exceeds expected benefit.

## Assignment contract

Before assigning work, identify the independent question, why delegation improves quality or time, and the minimum context needed. Give each specialist a bounded question, named files/seams when known, read/write authority, expected evidence, concise output, and stop conditions. Partition questions so specialists do not repeat the same broad route/model/test/document scan unless independent overlap is intentional for review. Specialists do not inherit conversation history, user authority, or permission for external actions unless explicitly included.

Use one coordinator to reconcile findings, resolve overlap, inspect integrated state, and run fresh verification. Never call work complete by collecting worker assertions.
