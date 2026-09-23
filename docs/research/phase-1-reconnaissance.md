# Phase 1 Reconnaissance

Status: historical research retained for v1.0.0 provenance
Date: 2026-09-22
Scope: research and architecture evidence only; no workflow implementation files were created in this phase. This record is not a runtime support promise.

## Mission boundary

Build an open-source senior engineering workflow for OpenAI Codex. The system must cover intent refinement, task classification, investigation, design, planning, implementation, testing, review, adversarial verification, GitHub delivery, and release without turning every task into the same heavyweight process.

The source system lives in a dedicated repository outside the unrelated, modified host checkout. No public repository, push, merge, tag, or release is authorized by this work.

## Evidence policy

- Official runtime and platform documentation outranks third-party repositories.
- Repository source at the pinned commit outranks its README or marketing copy.
- Existing local behavior is preserved unless the new design has a demonstrated reason to change it.
- Upstream material is synthesized by concept. Text or code is not copied unless its license permits reuse and attribution is recorded.
- Unlicensed material is concept-only.

## Existing local prompt refiner

Inspected source: the installed user-level `%USERPROFILE%\.codex\skills\prompt-refiner`.

Confirmed behavior:

- It is already runtime-neutral at the skill layer: `SKILL.md`, `agents/openai.yaml`, and a reference example set.
- Invocation is intentionally explicit-only.
- It preserves user intent, does not execute the refined prompt, and resists prompt inflation.
- It uses quick, standard, and deep modes and distinguishes blocking ambiguity from useful assumptions.
- Its examples are calibrated across coding and non-coding requests.

Migration decision:

- Do not overwrite or silently change the installed `$prompt-refiner`.
- Preserve it as an existing Codex intake tool.
- Build a canonical internal Task Refiner that carries forward its intent-preservation, ambiguity, scope, and non-execution rules.
- Publish a first-class `refine` skill in the new plugin and document the explicit migration path. Avoid a second installed `prompt-refiner` name that could shadow the existing skill.

## Official runtime constraints

### Codex

Official sources establish these boundaries:

- Plugins are the distribution unit; a plugin can package skills and optional integrations.
- Skills use progressive disclosure: catalog metadata first, `SKILL.md` only when selected, and references or scripts only when needed.
- Repository skills live in `.agents/skills`; durable repository instructions belong in a concise `AGENTS.md`.
- Custom agents are appropriate for narrow, isolated, or noisy work, not as a replacement for the main workflow.
- MCP is the external capability layer. Tool allowlists and approval modes can narrow access.

Design consequence: keep the discoverable skill catalog small, put detailed lifecycle modules in references, keep `AGENTS.md` thin, and make GitHub integration optional rather than a hard dependency.

### GitHub

Official documentation confirms:

- Protected branches can require reviews, status checks, resolved conversations, signed commits, merge queues, and other repository-specific gates.
- A skipped or neutral required check can count as successful; pending and failing states require explicit interpretation.
- `gh pr checks` can filter required checks and returns a distinct pending exit status.
- GitHub releases are tag-based release records, not proof of deployment.
- The official GitHub MCP server supports focused toolsets and a read-only mode. Its prompt-injection lockdown is defense in depth, not an authorization boundary.
- Current `gh issue create` supports issue types and relationship flags, so older third-party limitations must not be copied into the workflow.

Design consequence: use GitHub MCP for structured reads and writes when available, `gh` as the deterministic fallback, and local `git` for source-control truth. External writes remain explicit user-authorized actions.

## Product UX and visual-design research

Product UX references and visual-design inspiration answer different questions. Inspect the product's real workflow, user, states, permissions, and existing design system before borrowing a visual treatment. Prefer real product interfaces such as Mobbin examples for interaction patterns; use visual showcases such as Dribbble only for visual inspiration, with Pinterest as a fallback. User-supplied references and project design rules take precedence over external examples.

The Taste skill v2 at `Leonxlnx/taste-skill@c184364c58658b2f131b4ae8bd3d206cabb3deee` is MIT-licensed at that revision. Its visual-quality guidance is useful selectively, but it explicitly excludes dashboard, table, and multi-step product-flow use. Do not adopt it as a universal product-UI workflow.

UI/UX Pro Max at `nextlevelbuilder/ui-ux-pro-max-skill@dcc40ff5133ef78276117db0cc34e7b83cc8aeba` has a repository MIT license. That does not establish the license or provenance of every indexed recommendation, image, or data record. Inspect the exact file and revision before adapting any such material. This project does not vendor its corpora; use independently implemented general ideas only when an exact source cannot be cleared.

Resolution: keep product-flow and visual-design guidance as conditional internal modules under `engineer`. Use project and user-provided evidence first; use real product examples for interaction and showcase sites for visual direction only. Exact file/revision licensing governs any reuse; when uncertain, do not copy.

## Upstream repository pins and licensing

| Source | Branch | Commit | License at pin | Strongest contribution |
| --- | --- | --- | --- | --- |
| `owainlewis/blueprint` | `main` | `54c952bad7dea5d40fa7951b4bd831008b567a6b` | MIT | Small lifecycle skeleton, outcome/constraints/proof, independent review |
| `obra/superpowers` | `main` | `5bf4e78011075bcfc0dc295f0724994cd123ee71` | MIT | Root-cause debugging, fresh verification, behavioral pressure testing |
| `affaan-m/ECC` | `main` | `bf70150eb2df8070024e5bdf08e4aa08959e2735` | MIT | Context budgeting, iterative retrieval, security review, specialist boundaries |
| `kevinlin/skills` | `main` | `951dbf8f4a8ffd58036d75d47e47ca12b691c7c3` | MIT | Research-plan-implement loop and intentional compaction |
| `msitarzewski/agency-agents` | `main` | `053ddbbf392a1688fc7043d81529f47ef2cf86c8` | MIT | Explicit role contracts and minimal-change posture |
| `github/awesome-copilot` | `main` | `db8d563aefebf9dd569bc72596c4ebd817847534` | MIT | GitHub issue, PR, checks, release, and secret-screening workflows |
| `github/github-mcp-server` | `main` | `85598ba6e1256f7ebf4867b95d63b833c4549264` | MIT | Official structured GitHub capability and read-only mode |
| `richkuo/rk-skills` | `main` | `369cab825d81416a5a51fbdf3d774ed2fa02d23b` | MIT | Claim-level issue validation, review reconciliation, delivery gates |
| `thatjuan/agent-skills` | `main` | `1a22763c98f0a37cd7dda121d48a0f5451771a28` | No root license found | Small issue capture, batch orchestration, secret-aware commit concepts only |

The final `THIRD_PARTY_NOTICES.md` must record every studied source, pin, license finding, and whether material was adapted or only influenced the design.

## Source-by-source synthesis

### Blueprint

Keep:

- A compact phase model based on outcome, constraints, and proof.
- Direct execution for small clear changes.
- Current architecture separated from proposed design.
- Independent read-only review and acceptance-criterion-to-evidence mapping.

Reject or narrow:

- Treating writing, debugging, and test strategy as assumed primitives when the target workflow must make them explicit.
- A phase-per-public-skill catalog that expands discovery cost.

### Superpowers

Keep:

- Root cause before fixes.
- One hypothesis and one discriminating check at a time during debugging.
- Regression proof for defects when feasible.
- Fresh evidence immediately before completion claims.
- RED/GREEN/REFACTOR pressure testing for workflow instructions.
- Worktree isolation when the active checkout is unsafe.

Reject or narrow:

- Universal, rigid TDD and deletion of code written before a test.
- Mandatory brainstorming for all work.
- Mandatory invocation based on tiny relevance probabilities.
- Fixed agent fan-out or a mandatory full suite for every change.

### Kevin Lin skills

Keep:

- Research, plan, implement as a useful deep-work sequence.
- Durable concise artifacts for long investigations.
- Intentional compaction at stable boundaries.
- Adaptive depth and repository-code-first investigation.

Reject or narrow:

- Fixed minimum agent counts.
- Requiring persistent documents and user stops for routine small work.
- Tool-specific task-tracker conventions.

### Agency Agents

Keep:

- Role definitions with purpose, responsibility, workflow, deliverable, and success conditions.
- The minimal-change principle.

Reject or narrow:

- Persona theater, arbitrary productivity metrics, and default-negative scoring.
- Hundreds of roles and framework-specific defaults.

### Awesome Copilot

Keep:

- MCP-first structured GitHub operations with `gh` fallback.
- Intentional staging, secret checks, and review/CI reconciliation.
- Verification that external actions actually landed.

Reject or narrow:

- Assuming Conventional Commits or semantic versioning when the repository says otherwise.
- Automatic release or merge actions.

### GitHub MCP server

Keep:

- Read-only discovery by default.
- Toolset selection to reduce context and authority.
- Structured issue, PR, Actions, security, and release operations.

Important limit:

- Lockdown and push protection reduce risk but do not replace user authorization, least-privilege credentials, or independent validation of untrusted content.

### RK Skills

Keep:

- Claim-by-claim issue validation against the target branch.
- A review finding is a hypothesis until traced to current code.
- Prior review dispositions must be reconciled, not ignored.
- Safety carve-outs for money, data integrity, authentication, and security.
- Worktree isolation and branch/head verification.

Reject or narrow:

- Model-specific complexity routing tables.
- Fixed scoring formulas presented as universal truth.
- Automatic pushes, issue writes, review comments, and releases without an authorization gate.
- Mandatory semantic tags and generated release notes when the repository has different conventions.

### Agent Skills collection

Keep as concepts only because no license was found:

- Fewer, coherent issues rather than issue fragmentation.
- Explicit staging and secret-aware delivery.
- Dependency-aware batch ordering.

Reject or narrow:

- Writing issues directly without confirming external mutation authority.
- One fresh subagent per issue as a fixed rule.
- Automatic rebase recovery after a rejected push.

## Duplication and conflict map

| Repeated concern | Upstreams | Resolution |
| --- | --- | --- |
| Research before implementation | Blueprint, Superpowers, Kevin Lin, RK | One investigation module with depth selected by risk and uncertainty |
| Planning | Blueprint, Kevin Lin, RK | Plan only when uncertainty, coupling, or rollback cost warrants it |
| Testing | Blueprint, Superpowers, ECC | Risk-appropriate test strategy; regression-first for defects and safety-sensitive behavior |
| Independent review | Blueprint, ECC, Agency Agents, RK | One fresh-context review gate with optional specialist lanes |
| GitHub delivery | Awesome Copilot, GitHub MCP, RK, Agent Skills | One GitHub skill with MCP/CLI/local adapters and explicit mutation gates |
| Agent orchestration | ECC, Kevin Lin, Agency Agents, Agent Skills | Adaptive delegation only for independent, bounded work; never a fixed fan-out |
| Release | Awesome Copilot, RK | Inspect repository release convention first; require explicit release authorization |
| Documentation | RK, Blueprint | Update only documentation made stale by the change; avoid mandatory documentation churn |

## Resolved contradictions

1. **Rigid lifecycle versus proportional process**
   Resolution: classify task type, risk, ambiguity, coupling, reversibility, and external effects. Low-risk clear work may go directly to implementation and focused verification. High-risk work expands into investigation, design, plan critique, adversarial review, and rollback checks.

2. **Autonomy versus external mutations**
   Resolution: local reversible work can proceed autonomously within user scope. Issue creation, comments, pushes, PR creation, merges, tags, releases, deployments, and destructive operations require explicit or clearly inherited authorization.

3. **TDD as discipline versus TDD as dogma**
   Resolution: require observable acceptance evidence. Prefer red-to-green regression tests for bugs and safety-sensitive changes when feasible. Do not force artificial tests for prose, configuration, or untestable external behavior.

4. **Many specialist skills versus small discovery surface**
   Resolution: six public skills backed by internal reference modules and four narrow reviewer roles.

5. **Codex packaging versus portable skill structure**
   Resolution: keep Codex-supported Agent Skills as the source format and generate only the Codex package metadata needed by this project.

6. **MCP-first versus tool independence**
   Resolution: GitHub MCP is preferred for structured operations when available; `gh` and local `git` provide the fallback. Capabilities are detected, never assumed.

7. **Fresh-context independence versus excessive agents**
   Resolution: fresh-context review is required only where its independence materially improves confidence. Parallel agents are used only for separable questions and within the host's concurrency budget.

## Proposed final architecture

### Public skills

1. `engineer` — classify and route feature, bug, change, architecture, and investigation work.
2. `refine` — explicit-only intent refinement without execution.
3. `review` — independent diff, PR, plan, or architecture review.
4. `verify` — fresh evidence and claim verification.
5. `github` — issue, branch, PR, review, CI, and delivery reconciliation.
6. `release` — explicit-only release readiness and authorized publication.

### Internal modules

- Task Contract and evidence labels.
- Task classification and risk routing.
- Repository discovery and instruction precedence.
- Bug investigation.
- Feature discovery and acceptance criteria.
- Architecture analysis and design.
- Plan creation and critique.
- Scoped implementation.
- Test strategy.
- Review and adversarial challenge.
- Verification and completion claims.
- GitHub capability selection and mutation gates.
- Release readiness, rollback, and publication.

### Specialist roles

- `investigator` — read-only root-cause and code-path tracing.
- `reviewer` — independent correctness, regression, and maintainability review.
- `security-reviewer` — threat-oriented review of sensitive changes.
- `verifier` — fresh evidence against the Task Contract.

The main agent remains coordinator and owner of the Task Contract. Specialists return evidence and do not independently widen scope or mutate external systems.

## Preliminary risk model

Risk is categorical rather than a false-precision score.

- **Low**: narrow, reversible, local, well-understood, no sensitive data or external effects.
- **Medium**: multiple files or components, meaningful behavior change, migration or compatibility concern, non-trivial regression surface.
- **High**: security/auth, money, data integrity, destructive state change, concurrency, public API/schema, infrastructure, deployment/release, or hard-to-reverse external effects.

Uncertainty can raise the route even when apparent impact is small. Explicit user constraints can narrow scope but cannot waive evidence needed for a safety claim.

## Phase 2 decisions to formalize

- Exact Task Contract schema and update rules.
- Evidence status vocabulary and completion gate.
- Which public skills may be model-invoked versus explicit-only per runtime adapter.
- Capability-detection order for GitHub MCP, `gh`, and local `git`.
- Canonical specialist-role format and deterministic adapter generation.
- Eval cases that expose rationalization, overengineering, skipped verification, unsafe GitHub writes, and premature completion.

## Phase 1 exit criteria

- Existing refiner inspected and migration direction recorded: met.
- Ten upstream repositories inspected at pinned commits: met.
- Official Codex and GitHub conventions checked: met.
- Licensing and provenance constraints recorded: met.
- Duplicates, contradictions, strongest concepts, and rejected patterns documented: met.
- Recommended architecture proposed without creating implementation files: met.
