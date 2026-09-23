# Context efficiency baseline — 2026-09-23

This records the source state before changing workflow behavior. Counts are UTF-8 file bytes, not model tokens. The repository currently has no tracked files, so there is no Git commit baseline; this report identifies the inspected canonical files.

## Skill graph and activation

Six public skills are declared: `engineer`, `refine`, `review`, `verify`, `github`, and `release`. Their `SKILL.md` files total 11,360 bytes. All canonical skill Markdown under `skills/` totals 41,948 bytes. Metadata is visible at discovery; skill bodies load when selected; references are linked for conditional loading. `refine` and `release` are explicit-only. Generated Codex agent files are outputs, not separate policy sources.

`engineer` is the main router. It always directs the reader to classification and risk (1,978 bytes) and completion gate (1,190 bytes), then to a task-specific workflow and conditional planning/testing references. Its own body is 2,795 bytes. `review`, `verify`, `github`, and `release` select small references by operation. No reference is automatically loaded by the file layout itself.

## Other persistent context

Repository `AGENTS.md` is 2,160 bytes and principally covers authority, canonical structure, and required checks. User-global instructions were excluded because they belong to a separate application workspace. `docs/research/phase-1-reconnaissance.md` is 17,338 bytes and `docs/design/system-design.md` is 8,969 bytes. Repository instructions require them for provenance and public-boundary changes, respectively, but routine engineering tasks should not load them.

The pre-existing `%USERPROFILE%\.codex\skills\prompt-refiner` is explicit-only and remains separate. This plugin's `refine` preserves the non-execution contract; `docs/migration-from-prompt-refiner.md` documents coexistence.

## Hot spots and safeguards

- Risk routing already distinguishes low, medium, and high, but has no explicit context/read budget. A low-risk task could still trigger broad instruction or repository reads.
- `AGENTS.md`, `engineer`, risk, discovery, and completion references repeat general authority, scope, and verification advice. Most repetition is brief, so consolidation should target only wording that causes extra reads or behavior.
- Orchestration permits adaptive specialists, but does not require a unique question, minimum inputs, or explicit non-overlap for each assignment.
- The Task Contract is durable only when useful, but lacks a concise continuation-state shape. A long session can re-read prior detail.
- GitHub guidance correctly insists on fresh direct Git/GitHub evidence; compact summaries must not weaken that gate.
- `evals/cases.json` has 19 behavioral cases, including low-risk edits, production bugs, payment retries, GitHub boundaries, and verification pressure. The latest recorded Codex evaluation is a qualitative 19-case grouped smoke plus two seeded fixtures, not a new independent before/after run.
- RTK is not on the current PowerShell `PATH`; no `RTK.md` or Codex `hooks.json` was found in the inspected user and project locations.

## Measurement baseline

The current workflow does not record per-task files read, repeated reads, reference activation, subagent count, or command-output size. Therefore no numeric claim about actual saved model context or ChatGPT Plus allowance can be made from the existing logs. The optimization evaluation must distinguish static instruction size, observed command bytes, and behavioral quality.
