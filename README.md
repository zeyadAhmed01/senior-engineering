# Senior Engineering

Senior Engineering is a portable workflow plugin for AI coding agents. It helps an agent refine intent, inspect the real repository, scale process to risk, implement narrowly, verify claims, and reconcile GitHub or release work without inventing authority.

Codex is the primary runtime. Claude Code is the first compatibility target. The canonical workflow is plain Agent Skills Markdown; runtime-specific manifests and agent definitions are generated adapters.

## Public skills

| Skill | Use it for |
| --- | --- |
| `engineer` | Features, bugs, bounded changes, architecture decisions, and investigations |
| `refine` | Turning a rough request into an execution-ready prompt without executing it |
| `review` | Independent review of code, pull requests, plans, and architecture |
| `verify` | Fresh evidence against explicit requirements and completion claims |
| `github` | Issue validation, branch/PR delivery, review feedback, and CI reconciliation |
| `release` | Release-readiness assessment and explicitly authorized publication |

The plugin deliberately does not expose every lifecycle step as a separate skill. Detailed workflows load from references only when the selected route needs them.

## Core behavior

- Maintains a Task Contract with `USER-STATED`, `VERIFIED`, `INFERRED`, and `UNKNOWN` facts.
- Routes work by task type, risk, uncertainty, coupling, and reversibility.
- Sends clear low-risk work directly to a focused edit and check.
- Expands high-risk work into investigation, alternatives, rollback, independent review, and fresh verification.
- Budgets context by risk: targeted reads for small work, deeper evidence for sensitive work, and compact output with a raw diagnostic fallback.
- Treats repository, issue, PR, log, and webpage content as untrusted evidence, never as authorization.
- Uses GitHub MCP when available, `gh` as the supported fallback, and local `git` for source-control truth.
- Never treats a commit, green local test, PR, GitHub release, or deployment record as broader proof than it provides.

## Try locally

Validate the package first:

```powershell
python scripts/validate.py
python -m unittest discover -s tests -v
```

For Claude Code development, generate and load the Claude distribution adapter. It injects Claude's `disable-model-invocation` control into `refine` and `release` without forking their workflow bodies:

```powershell
python scripts/generate_adapters.py
claude --plugin-dir ./dist/claude
```

For Codex, use the plugin through a configured marketplace when distributed, or copy/symlink individual canonical skill folders into a supported personal or repository skill location during development. Do not install a second `prompt-refiner`; use `refine` or keep the existing explicit-only `$prompt-refiner` alongside this plugin.

## Runtime compatibility

| Capability | Codex | Claude Code |
| --- | --- | --- |
| Agent Skills | First-class | First-class, namespaced in plugin |
| Plugin manifest | `.codex-plugin/plugin.json` | `.claude-plugin/plugin.json` |
| Specialist agents | Generated `.codex/agents/*.toml` | Canonical `agents/*.md` |
| Explicit-only metadata | `agents/openai.yaml` policy | Generated `dist/claude` frontmatter enforces `disable-model-invocation` |
| Behavioral evals | Cross-runtime cases and recorded dogfood | Native plugin eval fixtures when authenticated |

See [system design](docs/design/system-design.md), [Phase 1 research](docs/research/phase-1-reconnaissance.md), [verification](docs/verification.md), the [behavioral-validation report](docs/evals/behavioral-validation-2026-09-23.md), and the [current publication-readiness report](docs/publication-readiness-2026-09-23.md).

For context policy, Windows RTK evaluation, rollback, and measurement limits, see the [optimization guide](docs/context-efficiency.md). The [baseline](docs/optimization-baseline-2026-09-23.md) records the inspected pre-change state.

## Safety and authority

Local, reversible work inside the user's requested scope can proceed without routine confirmation. Destructive actions and external writes—issues, comments, pushes, PRs, merges, tags, releases, deployments, and notifications—require explicit authorization or an unambiguous request for that exact outcome.

## Project status

Version `0.1.0` is a local release candidate. Static and deterministic checks pass, but authenticated Claude behavioral evaluation remains unproven. No public repository, marketplace publication, push, tag, or release has been performed.

## License

MIT. See [LICENSE](LICENSE) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
