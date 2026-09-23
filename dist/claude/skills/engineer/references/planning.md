# Planning and Critique

Plan when sequencing, coupling, risk, or uncertainty makes direct execution unsafe. Skip a formal plan for clear low-risk work.

## Plan content

Each step names:

- outcome and files/systems likely affected;
- invariant or requirement it satisfies;
- dependency on earlier steps;
- verification point;
- rollback or recovery for risky state.

Plans describe behavior and seams, not invented line numbers or APIs. Cite inspected code when available.

## Critique before high-risk execution

Challenge:

- premise and missing alternatives;
- hidden scope and dual implementations;
- state ownership, identity, lifetime, and concurrency;
- authorization, validation, secrets, and failure recovery;
- migration compatibility and rollback;
- whether proposed tests would actually detect the failure;
- whether the plan is larger than the requested outcome.

Revise once around material findings. Do not cycle on preferences or turn critique into design paralysis.

