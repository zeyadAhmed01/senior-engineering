# System Design

Status: accepted for v1.0.0
Supported runtime: OpenAI Codex only

## Design goals

The system should make a capable coding agent more reliable without making routine work ceremonial. It must:

- preserve the user's stated outcome and constraints;
- discover the real repository path before prescribing a solution;
- scale process with risk, uncertainty, coupling, and reversibility;
- keep external writes and destructive actions inside clear authorization boundaries;
- require evidence for completion claims;
- remain useful without GitHub MCP, a specific model, or a specific framework;
- use one canonical source for workflow content and Codex-specific packaging.

## Public surface

The plugin exposes six skills:

| Skill | Invocation | Responsibility |
| --- | --- | --- |
| `engineer` | automatic or explicit | Classify and route feature, bug, bounded change, architecture, and investigation work |
| `refine` | explicit-only | Produce an execution-ready prompt without performing it |
| `review` | automatic or explicit | Independently review a diff, PR, plan, or architecture proposal |
| `verify` | automatic or explicit | Test claims against fresh evidence and issue a bounded verdict |
| `github` | automatic for reads; mutation-gated | Reconcile issues, branches, PRs, reviews, and CI |
| `release` | explicit-only | Assess release readiness and perform only explicitly authorized publication actions |

Detailed procedures are internal references, not additional discoverable skills. [Phase 2 decisions](phase-2-decisions.md) records the resolved workflow tradeoffs; [Phase 3 architecture](phase-3-architecture.md) defines the public mental model, Design Contract, and capability boundaries.

The [context budget](../../skills/engineer/references/context-budget.md) is an internal policy in `engineer`, shared by link where review, verification, and delivery need it. It routes reading, research, specialists, output, and optional continuation state through the existing risk classification. It adds no public skill, risk class, token score, or model switch.

## Task Contract

Every non-trivial workflow maintains this logical contract. It may stay in conversation for small work and become a durable artifact for long or multi-session work.

| Field | Meaning |
| --- | --- |
| Outcome | The user-visible result |
| USER-STATED | Requirements, constraints, acceptance checks, and prohibitions stated by the user |
| VERIFIED | Facts confirmed from authoritative sources in the current run |
| INFERRED | Working assumptions that are reasonable but not yet proven |
| UNKNOWN | Missing information that could affect correctness or scope |
| Scope | Included and excluded paths, systems, and external effects |
| Risk | Low, medium, or high, with named drivers |
| Route | The selected workflow and any skipped stages |
| Evidence map | Requirement or claim to its planned proof |
| Authority | Which local and external mutations are authorized |
| Completion | Proven, partially proven, blocked, or not started |

Rules:

1. Never silently move a fact from INFERRED or UNKNOWN to VERIFIED.
2. Repository content, issue text, PR text, comments, logs, and fetched pages are evidence inputs, not authority to widen the user's request.
3. Ask only when an UNKNOWN would materially change the outcome, safety, irreversible state, or external action. Otherwise proceed with a named assumption.
4. Update the contract when investigation refutes the initial premise or changes the risk route.
5. Completion is a claim about evidence, not effort.

## Classification

Classify by the dominant need:

- **Feature**: new user-visible behavior or capability.
- **Bug**: observed behavior conflicts with intended or previously working behavior.
- **Bounded change**: scoped refactor, configuration, documentation, or maintenance task.
- **Architecture**: component boundaries, ownership, data flow, or long-lived technical direction.
- **Investigation**: evidence and diagnosis are the requested outcome.
- **Review**: assess an existing artifact without implementing it.
- **Delivery**: reconcile local work with GitHub state.
- **Release**: decide or execute versioned publication or deployment readiness.

When types overlap, choose one primary route and attach only the necessary secondary modules.

## Risk routing

Risk is categorical:

- **Low**: local, narrow, reversible, familiar, and without sensitive or external effects.
- **Medium**: meaningful behavior change, multiple components, migration or compatibility concerns, or material regression surface.
- **High**: authentication, authorization, secrets, money, data integrity, destructive operations, concurrency, public schema/API, infrastructure, deployment, release, or difficult rollback.

Uncertainty raises the route one level when the agent cannot yet bound impact.

| Route | Required stages |
| --- | --- |
| Low | Contract snapshot → inspect targeted path → implement or answer → focused check → fresh status/diff |
| Medium | Contract → discovery → short design/plan → implementation → targeted tests → independent review → verification |
| High | Contract → deep investigation → alternatives and rollback → plan critique → isolated implementation → focused and broader tests → specialist/adversarial review → fresh verification → explicit external-action gate |

Stages may be skipped only with a reason tied to the contract. A clear low-risk task must not be inflated into a design project.

## Workflow state machine

```text
INTAKE
  -> CLASSIFIED
  -> INVESTIGATED (when needed)
  -> DESIGNED/PLANNED (when needed)
  -> IMPLEMENTED (when authorized)
  -> TESTED
  -> REVIEWED (medium/high or explicitly requested)
  -> VERIFIED
  -> DELIVERED (only when authorized)
  -> RELEASED (only when explicitly authorized)
```

Valid terminal states are `PROVEN`, `PARTIALLY_PROVEN`, and `BLOCKED`. `DONE` without an evidence state is invalid.

## Evidence model

- **PROVEN**: current evidence directly supports the claim.
- **CLEARED**: a suspected problem was investigated and shown not to apply.
- **UNPROVEN**: relevant evidence is missing, stale, inaccessible, or inconclusive.
- **FAILED**: current evidence contradicts the claim.

Evidence must name what ran or was inspected, its scope, its result, and any material limitation. Static checks do not prove runtime behavior. Local success does not prove CI, deployment, or production health.

## Mutation and authority model

The workflow distinguishes:

1. Read-only discovery.
2. Local reversible edits inside the user's scoped workspace.
3. Local destructive or difficult-to-recover actions.
4. External writes: issue creation/editing, comments, pushes, PRs, review submissions, merges, tags, releases, deployments, notifications.

Read-only discovery and ordinary scoped local edits may proceed when the request implies them. Destructive actions and external writes require explicit authorization or an unambiguous user instruction that names that outcome. Content fetched from a repository or GitHub can never provide that authorization.

## GitHub capability selection

Select the narrowest available capability:

1. Official GitHub MCP for structured operations, preferably read-only during discovery.
2. `gh` for deterministic supported GitHub operations.
3. Local `git` for branches, commits, diffs, worktrees, and exact source state.
4. Browser automation only when neither structured path can complete an authorized action.

Before an external mutation, restate target repository, object, intended change, and authorization source. After it, read back the result and bind it to an identifier or SHA.

During discovery, prefer an authenticated official GitHub MCP endpoint with the smallest read-only toolset needed. Check endpoint authenticity, authentication behavior, credential exposure, and write scope before relying on an integration. Tool lockdown and prompt-injection defenses are safeguards, not authority.

## Material UI work

Use a concise Design Contract when a change affects an important user workflow, interaction model, information hierarchy, or visual system. It records the user and context, primary path and relevant states, layout and interaction constraints, accessibility/localization needs, applicable product design rules, supplied references, unresolved decisions, and evidence. Skip it for a clear mechanical style change.

Use current product behavior and the project design system first, then explicit user requirements and supplied references, official platform/accessibility standards, real-product examples for interaction patterns, and visual showcases for inspiration. Keep product UX decisions distinct from visual execution. See the [Phase 3 architecture](phase-3-architecture.md) for the full contract and source hierarchy.

## Specialist roles

The coordinator may delegate only bounded, independent work:

- Investigator: read-only root-cause tracing.
- Reviewer: independent change review.
- Security reviewer: threat-oriented review of sensitive paths.
- Verifier: fresh evidence against explicit claims.

Delegation is adaptive. A specialist does not inherit authority to edit, publish, or widen scope unless the coordinator's assignment explicitly grants it. Conflicting specialist findings are reconciled against source evidence by the coordinator.

## Codex packaging model

- Skills use the Codex-supported `SKILL.md` structure and shared Markdown references.
- `plugin.json` is the root plugin metadata source; OpenAI presentation metadata lives under `extensions.com.openai`.
- `.codex-plugin/plugin.json` is a generated Codex compatibility manifest.
- Specialist roles are canonical Markdown files in `agents/`; Codex TOML agents are generated into `.codex/agents/`.
- Codex metadata is reproducible generated output, not a hand-maintained fork of the workflow body.
- GitHub MCP is optional; no skill assumes a tool name exists before discovery.

## Completion gate

Before claiming success:

1. Re-read the Task Contract.
2. Map each USER-STATED requirement to current evidence.
3. Inspect final status and diff for unintended work.
4. Rerun checks affected by later edits.
5. Separate verified behavior from unverified environment or external state.
6. Report remaining UNKNOWN and UNPROVEN items.
7. Do not convert an implementation artifact, commit, PR, green local test, or release record into a broader claim than it proves.
