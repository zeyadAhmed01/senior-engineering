---
name: refine
description: Explicit-only prompt refinement. Use only when the user directly invokes or asks for the refiner to turn a rough request into an execution-ready prompt without executing the task.
license: MIT
---

# Refine

Return an execution-ready prompt and do not execute it.

## Preserve intent

Keep the user's outcome, scope, constraints, tone, and desired deliverable. Do not add features, tools, technologies, deadlines, files, tests, or external actions that the user did not request unless they are necessary safety or verification boundaries.

## Resolve ambiguity proportionately

- If the prompt is already clear, tighten it without expanding it.
- Do not turn common product conventions into requirements. Do not guess fields, matching rules, UI states, data scope, architecture, or acceptance criteria that the user did not specify.
- If one missing decision would materially change behavior, data, safety, scope, or irreversible/external action, make the refined prompt instruct the executing agent to ask one concise question before acting. If work can proceed without deciding it, leave the choice open instead of adding a speculative assumption.
- Do not turn optional detail into mandatory ceremony.
- For HIGH-risk work involving money, authorization, data integrity, concurrency, or destructive production changes, do not preserve a request to skip necessary causal or safety evidence. Keep the requested outcome, but have the executor explain the smallest required baseline or regression check and perform it before making or claiming the change. Do not inflate this into unrelated test suites.
- For payment idempotency or concurrency, explicitly retain focused retry/concurrent-delivery verification even when the input asks to skip it; never say the checks were skipped “as requested.”
- For concurrency requests, treat a suggested mechanism such as a lock as a hypothesis. Ask the executor to inspect competing writes and database invariants before choosing a correction; do not prescribe a lock, schema change, or other mechanism without repository evidence.
- For destructive production requests, preserve the production cleanup outcome while requiring read-only discovery of the data model, retention policy, and exact target criteria; require the user to define missing criteria and explicitly authorize deletion after a rollback and verification plan is ready.
- For access-control changes, require inspection of authorization and tenant boundaries, surface material access and audit decisions before implementation, and preserve authentication and lifecycle safeguards.

## Add execution quality

When relevant, make the prompt tell the executing agent to:

- inspect the actual repository path and applicable instructions;
- distinguish USER-STATED, VERIFIED, INFERRED, and UNKNOWN information;
- choose proportional depth based on risk;
- preserve existing behavior outside scope;
- verify the outcome with fresh evidence;
- report limitations honestly;
- avoid destructive or external actions not explicitly authorized.

## Output

Output only the refined prompt. Do not preface it, explain the rewrite, inspect files, call tools, or begin the task.

Read [examples](references/examples.md) when the input mixes objectives, includes vague expansion such as "redesign if needed," or pressures the executor to skip safety evidence.
