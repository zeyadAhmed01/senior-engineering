# Authorized Publication

Proceed only with explicit action-specific authorization.

Immediately before mutation:

- resolve target repository, environment, release convention, version, and exact commit SHA;
- confirm the working tree and branch are in the required state;
- confirm required checks and approvals live;
- verify version fields and artifacts according to repository policy;
- verify credentials have least practical scope;
- establish rollback and confirm no concurrent release conflicts.

Perform one mutation at a time. After uncertain results, read state before retrying. Never force or bypass protection unless the user explicitly authorizes that exact action and the platform permits it.

Afterward, verify in order as applicable:

1. tag points to intended SHA;
2. release record references intended tag and assets;
3. registry contains the expected immutable artifact;
4. deployment references the expected artifact;
5. health and smoke checks pass in the target environment.

Stop and report at the first failed boundary. Do not describe downstream stages as complete.

