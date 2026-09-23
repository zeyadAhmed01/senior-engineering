# Context efficiency

The internal [context budget](../skills/engineer/references/context-budget.md) applies the existing low/medium/high risk route to repository reads, research, tool output, optional specialists, and long-task state. It does not cap investigation or replace direct source evidence. `review`, `verify`, and `github` link to the same policy without copying it. `refine` and `release` retain their distinct invocation and authority rules.

## Use and measurement

Start with the actual entry point, trace its path, and expand as evidence requires. Search for the relevant section before reading a large file. Keep successful command summaries; for failures inspect failed cases and excerpts, then focused raw output or a full rerun when the compact output does not expose the cause. For GitHub delivery, inspect the current diff, CI, reviews, and merge state directly. Keep optional task state only for long or resumable work; its schema is in the context-budget reference.

Run `python scripts/context_audit.py --global-agents "$env:USERPROFILE\.codex\AGENTS.md"` to list instruction bytes and exact repeated paragraphs. These are file sizes, not consumed tokens. Track files/ranges read, duplicate reads, references loaded, tool calls, specialists, command-output bytes, check results, and final-report length for representative tasks. Record actual model tokens only when the runtime exposes trustworthy usage. Do not infer ChatGPT Plus allowance savings from RTK's command statistics.

## RTK on this Windows host

The official [Windows installation guide](https://github.com/rtk-ai/rtk/blob/develop/docs/guide/getting-started/installation.md) offers `winget install rtk-ai.rtk`, Cargo with the explicit `rtk-ai/rtk` Git URL, and release ZIPs. `cargo install rtk` risks installing the unrelated Rust Type Kit. On 2026-09-23, winget installed RTK 0.48.0 with a verified package hash. The official [0.49.0 release](https://github.com/rtk-ai/rtk/releases/tag/v0.49.0) was also tested from a temporary Windows ZIP verified against the release API's SHA-256 digest `cb971046598f0e8bd51f6c27780fcdd2c39a4c459a811bd95b0d77ba8c0d7c9f`.

**V1 integration is native Windows, a released RTK binary, and selective explicit invocation.** RTK is optional: use it for commands whose noisy output it materially reduces, and use raw commands when reduction is negligible or detail is needed. No Codex hook is required for v1 readiness. We did not run `rtk init -g --codex` or add global RTK instructions. The local packaged-plugin evaluation did register a temporary Codex marketplace and install `senior-engineering@se-context-v1-eval` in Codex config; it did not add an RTK hook.

The current [development documentation](https://github.com/rtk-ai/rtk/blob/develop/hooks/codex/README.md) describes a native Codex `PreToolUse` hook. The released 0.48.0 and 0.49.0 Windows binaries tested here differ: `rtk init --codex --dry-run` says Codex has no command hook and would only write `RTK.md` plus an `@RTK.md` line in `AGENTS.md`. Transparent rewriting is a possible future enhancement, not a v1 condition. When a stable release claims native-Windows Codex support, verify its release documentation, test it in isolation against selective use, check Codex approval and sandbox behavior, and confirm failing-command diagnostics before adoption. Do not use RTK development or prerelease builds for this gate.

The current release offers `rtk test`, `rtk git`, `rtk rg`, `rtk gain --project --format json`, and `rtk discover --project <path> --format json`. `discover` inspects Claude Code history, so zero Codex sessions is expected. `rtk gain` estimates savings in filtered command output; it is not account-level usage. The local `rtk telemetry status` reported consent never asked and telemetry disabled. Upstream [telemetry documentation](https://github.com/rtk-ai/rtk/blob/develop/docs/TELEMETRY.md) says external telemetry requires opt-in; no credentials or repository contents were sent by this integration.

### Diagnostic fallback

For a failure, inspect compact output first. If failed case names, stack traces, warnings, security output, or Git details are absent, obtain them through `rtk recall <hash>` or a focused raw command **before diagnosis**. `rtk proxy <command>` runs raw while tracking usage. Re-run directly if recall is unavailable or the wrapper changes behavior. Preserve exit code separately. Never filter interactive or destructive operations merely to save output.

### Rollback

No RTK hook or `AGENTS.md` reference was installed. To stop using RTK, use raw commands. To remove the temporary evaluation plugin and marketplace from Codex, use the current supported commands `codex plugin remove senior-engineering@se-context-v1-eval` and then `codex plugin marketplace remove se-context-v1-eval`; this does not delete the source repository. The pre-install Codex config was backed up under `%TEMP%\se-context-v1-20260923-1\config-before.toml`. To remove the winget RTK package, run `winget uninstall --id rtk-ai.rtk --exact` after confirming removal is intended. The verified 0.49.0 trial ZIP and extracted binary are under `%TEMP%\rtk-v0.49.0-codex`; they are independent of Codex configuration. If a future transparent integration is installed, first back up `%USERPROFILE%\.codex\AGENTS.md`, `RTK.md`, and `hooks.json` (or their project equivalents), preview `rtk init -g --codex --uninstall --dry-run`, run the matching uninstall command, then compare the restored instruction and hook files with the backups. Do not overwrite unrelated user content.

## External options

| Tool | Problem | Overlap / potential benefit | Risk | Reconsider when |
| --- | --- | --- | --- | --- |
| Spec Kit | Structured specs and plans | Duplicates this plugin's Task Contract and planning | More artifacts and context | A separate product specification method is needed for reasons beyond token use |
| Caveman | Terse answers | Concise reporting is already in the policy | Always-loaded instructions for a small output benefit | Measured response verbosity remains material |
| Headroom | Compresses repeated inputs/tool payloads via proxy | Could help very large MCP/JSON contexts | Model request and OAuth compatibility, quality, privacy | Substantial remaining input overhead is measured and current subscription compatibility is verified; test isolated, reversible A/B first |
| token-router | Local processing of huge files/logs | Could avoid loading irrelevant ranges | Extra model/Ollama dependency and fidelity risk | Huge traces or generated files are frequent despite scoped reads |

No external compression system in this table was installed. Model/reasoning selection remains a runtime or user control; this plugin only gives a risk-based recommendation when useful. It does not silently switch models, use a proxy, or promise allowance savings.

## Manual Plus usage observation

For comparable tasks, record the starting and ending Codex usage window in the app, the exact task and model settings, outcome quality, elapsed time, and RTK command measurements. Repeat a few similar low, medium, and high-risk tasks with and without selective RTK use. Compare useful completed work and correctness first; the subscription window is shared and affected by other activity, so treat the comparison as observational rather than a controlled token-meter result. Do not share account credentials.
