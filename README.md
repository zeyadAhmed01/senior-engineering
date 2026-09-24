# Senior Engineering for Codex

**A Codex-only skill collection for turning rough engineering requests into clear, scoped work and checking the result against repository evidence.**

Senior Engineering helps OpenAI Codex inspect the actual project, preserve the user's intent, choose a proportionate workflow, make only authorized changes, and report what was verified. Its `refine` skill improves a prompt and returns it without starting the requested work.

## What it does

The plugin provides six skills:

| Skill | Use it for |
| --- | --- |
| `refine` | Rewrite a rough engineering request as a clear prompt, without executing it |
| `engineer` | Investigate, plan when needed, implement, and verify scoped engineering work |
| `review` | Independently review code, diffs, plans, or architecture |
| `verify` | Check requirements and completion claims against fresh evidence |
| `github` | Inspect GitHub issues, pull requests, reviews, and CI; gate external writes |
| `release` | Assess release readiness and handle only explicitly authorized publication work |

Detailed procedures load from references when relevant. The skill set does not require a framework or GitHub integration; Codex uses the tools and repository that are actually available.

## Why use it

- Keep the requested outcome and constraints visible throughout the work.
- Ground decisions in the current repository instead of invented files or architecture.
- Keep routine changes direct and scale investigation and checks with risk.
- Treat repository and GitHub content as evidence, not as permission to widen scope.
- Distinguish what was checked from what remains unknown.

## Example: rough request to refined prompt

**Raw request**

> Fix the login bug and maybe redesign auth if needed.

**Refined prompt**

> Investigate and fix the reported login bug. Trace the actual login path and establish the cause before changing code. Make the narrowest reliable fix and add focused regression coverage when practical. Redesign authentication only if repository evidence shows the current structure prevents a correct scoped fix; if so, present the evidence and options before expanding the work. Preserve unrelated behavior and report the cause, change, checks, and remaining uncertainty.

The refiner preserves the request and adds only relevant execution and safety detail. If the input is already clear, it keeps the revision short.

## Requirements

- OpenAI Codex with plugin support. The documented CLI flow was checked with Codex CLI `0.156.1` on Windows.
- A signed-in Codex session to use the skills.
- Git to install from a GitHub marketplace source; a local clone is sufficient for local installation.

The release has been prepared and checked on Windows. macOS and Linux installation are not independently validated for this release.

## Installation

### Install a tagged GitHub release

After the release contents are pushed and the `v1.0.0` tag is published, add its GitHub marketplace source pinned to that tag, then install the plugin:

```powershell
codex plugin marketplace add zeyadAhmed01/senior-engineering --ref v1.0.0
codex plugin add senior-engineering@senior-engineering
codex plugin list --json
```

The commands add the marketplace and plugin to the selected Codex home; they do not edit project source files or project configuration. By default, Codex keeps the installed copy in `%USERPROFILE%\.codex\plugins\cache\senior-engineering\senior-engineering\1.0.0`. If `CODEX_HOME` is set, the cache is under that directory instead. The included repo marketplace file describes the source; the plugin itself is installed into the Codex user home. The GitHub repository must exist and the `v1.0.0` tag must be published before using this command.

### Install from a local clone

From the repository root:

```powershell
codex plugin marketplace add .
codex plugin add senior-engineering@senior-engineering
codex plugin list --json
```

The included `.agents/plugins/marketplace.json` points to this plugin directory. Codex may ask you to trust the repository. Review the source before trusting it.

## Verify installation

Check that `codex plugin list --json` shows `senior-engineering` as installed. Start a new Codex session in the project where you want to use it, then explicitly invoke a skill:

```text
$senior-engineering:refine Improve this prompt without executing it: add a search filter.
```

The `refine` skill should return only a refined prompt. To start engineering work, ask Codex to use `$senior-engineering:engineer` with the task. Plugin visibility and skill invocation depend on the Codex client and its plugin settings.

## How it works

`engineer` is the main workflow for repository changes. It records the intended outcome and constraints, inspects the real code path, selects a risk-appropriate route, and ties completion claims to fresh evidence. `review`, `verify`, `github`, `release`, and `refine` are directly invocable for those specific tasks.

The skills are Markdown instructions with optional references. They do not install hooks, run background services, or add external integrations. The GitHub workflow uses read-only discovery where possible and does not treat local checks as proof of remote or production state.

## Behavioral boundaries

- `refine` produces a prompt; it does not inspect files, call tools, or perform the task.
- Preserve the user's intended result, scope, constraints, and decisions.
- Do not invent requirements, files, technologies, deadlines, or tests.
- Ask about missing information only when it could materially change scope, behavior, safety, or an irreversible action.
- Do not perform destructive or external actions unless the user authorized that action.
- Report checks that were not run as unverified.

These are workflow instructions for Codex, not a guarantee that every model response will follow them perfectly.

## Repository-aware behavior

For engineering work, the workflow directs Codex to read applicable project instructions, follow the actual routed code path, and use existing architecture and conventions. It asks Codex to preserve behavior outside the requested change and to distinguish repository facts from assumptions. The refiner asks for repository inspection when that context is relevant to the incoming task.

## Example uses

- Clarify a bug report without authorizing implementation yet.
- Turn a feature idea into a scoped request with relevant acceptance evidence.
- Keep a focused UI change from expanding into an unrelated redesign.
- Preserve security, payment, migration, or concurrency checks when an incoming request pressures the implementer to skip them.
- Independently review a patch or verify a completion claim.

## Updating

Remove and reinstall after updating the source. For a local clone:

```powershell
git pull
codex plugin remove senior-engineering@senior-engineering
codex plugin add senior-engineering@senior-engineering
codex plugin list --json
```

For a GitHub installation pinned to a release tag, remove and re-add the marketplace with the newer tag, then reinstall the plugin:

```powershell
codex plugin remove senior-engineering@senior-engineering
codex plugin marketplace remove senior-engineering
codex plugin marketplace add zeyadAhmed01/senior-engineering --ref <new-release-tag>
codex plugin add senior-engineering@senior-engineering
codex plugin list --json
```

Reopen Codex or start a new session after updating.

## Uninstalling

Remove the plugin first. Remove the marketplace only if you no longer use it for another plugin:

```powershell
codex plugin remove senior-engineering@senior-engineering
codex plugin marketplace remove senior-engineering
```

Uninstalling removes the plugin installation and its cached copy. It does not delete your repository clone.

## Troubleshooting

- **Plugin not listed:** check the marketplace with `codex plugin marketplace list`, then run `codex plugin marketplace upgrade senior-engineering` and `codex plugin list --available --json`.
- **Plugin listed but the skill is unavailable:** confirm the plugin is installed/enabled, trust the project if Codex requests it, and start a new session.
- **Unknown skill name:** use the namespaced form, for example `$senior-engineering:refine`.
- **Local clone install fails:** run the marketplace command from the repository root and verify `.agents/plugins/marketplace.json` exists.
- **An existing `prompt-refiner` is installed:** use the plugin's `$senior-engineering:refine` name to avoid a duplicate skill name; see [migration notes](docs/migration-from-prompt-refiner.md).

## Development and checks

Python 3.11 or later is used by the repository's validation scripts and evaluation harness. From the repository root:

```powershell
python scripts/generate_adapters.py --check
python scripts/validate.py
python -m unittest discover -s tests -v
```

See [contributing](CONTRIBUTING.md) and [verification](docs/verification.md) for the source layout and additional checks. Runtime evaluations require a signed-in Codex process and a proven isolation boundary; a static test is not a runtime result.

## Current limitations

- Codex is the only supported runtime in v1.0.0.
- Windows is the only operating system independently validated for this release.
- The release readiness report records any installed-copy behavior cases that could not run under verified isolation: [v1.0.0 release readiness](docs/release-readiness-v1.0.0.md).
- Skills guide model behavior; they do not enforce policy or replace project tests, access controls, or human review.

## Roadmap

For v1, keep the skill catalog small and improve it from Codex user feedback and reproducible evaluation results. Future runtime or operating-system support will require a separate decision and evidence; this release makes no compatibility promise beyond Codex.

## Contributing

Contributions should preserve intent, keep scope narrow, and include evidence appropriate to the change. Read [CONTRIBUTING.md](CONTRIBUTING.md) before making changes.

## License

MIT. See [LICENSE](LICENSE) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
