---
name: refine
description: Explicit-only prompt refinement. Use only when the user directly invokes or asks for the refiner to turn a rough request into an execution-ready prompt without executing the task.
license: MIT
disable-model-invocation: true
---

# Refine

Return an execution-ready prompt and do not execute it.

## Preserve intent

Keep the user's outcome, scope, constraints, tone, and desired deliverable. Do not add features, tools, technologies, deadlines, files, tests, or external actions that the user did not request unless they are necessary safety or verification boundaries.

## Resolve ambiguity proportionately

- If the prompt is already clear, tighten it without expanding it.
- If a safe narrow assumption preserves intent, state it inside the refined prompt.
- If one missing decision would materially change behavior, data, safety, scope, or irreversible/external action, make the refined prompt instruct the executing agent to ask that question before acting.
- Do not turn optional detail into mandatory ceremony.

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
