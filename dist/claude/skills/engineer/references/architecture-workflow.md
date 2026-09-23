# Architecture Workflow

Architecture work is a decision, not a diagram-first exercise.

## Map current reality

Trace current components, ownership, data and control flow, persistence, trust boundaries, operational dependencies, failure modes, and measured or observed pain. Separate current architecture from proposed architecture.

## Define the decision

State the outcome, constraints, quality attributes, non-goals, migration tolerance, and decision horizon. Identify what evidence would justify change and what would justify staying put.

## Compare alternatives

Include the smallest viable option and the status quo. Compare coupling, failure isolation, consistency, latency, operational burden, team ownership, migration/rollback, security, and cost. Do not assume distributed systems or new abstractions are inherently superior.

## Recommend

Give one recommendation, evidence, tradeoffs, preconditions, migration stages, rollback, and decision triggers. Mark unverified assumptions. Stop without implementation when the user requested advice only.

