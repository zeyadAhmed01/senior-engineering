# Verification

## Deterministic repository checks

Run from the repository root with Python 3.11 or later:

```powershell
python scripts/generate_adapters.py --check
python scripts/validate.py
python -B -m unittest discover -s tests -v
```

`generate_adapters.py --check` confirms that the Codex manifests and agent files match their canonical sources and fails on stale files in managed output directories. `validate.py` checks required files, skill metadata, local Markdown links, evaluation contracts, retired compatibility paths, and generated-file freshness. Unit tests also seed unexpected generated files to verify orphan detection.

If Codex's bundled plugin and skill validators are available, run them against the repository root and each directory under `skills/`. They provide additional static package checks; they do not test model behavior.

## Installed-copy behavior evaluations

`evals/cases.json` contains 43 behavior contracts. The original 19 cases from the initial Codex evaluation set remain present, ten additional cases extend those workflows, and fourteen explicit prompt-refinement cases cover vague and detailed requests, bug reports, refactoring, UI, performance, authentication/security, failing tests, Laravel/backend, frontend, payments, destructive migrations, concurrency, and already-good prompts. `evals/context-efficiency/run_contract_suite.py` runs one contract per fresh `codex exec` process against a disposable fixture and an installed plugin. `run_isolated.py` provides 11 additional context-efficiency scenarios.

The runners require a dedicated `CODEX_HOME` under `%LOCALAPPDATA%\CodexEval`, separate from both the user's normal `%USERPROFILE%\.codex` and the temporary fixture tree. They strip inherited credential variables and disable app integrations and remote plugins so cases exercise the installed local plugin without account-provisioned tools. The Windows permission profile must allow the installed skill package to be read, deny the user's normal `.codex` directory and the isolated home's `auth.json`, limit writes to the active fixture, and disable command networking. Configuration inspection alone does not prove a sandbox is enforced. Verify that the skill file is readable, both credential locations are denied, and command networking is blocked with a harmless canary before running model evaluations. Refinement cases receive only the user request so fixture safety text cannot become accidental prompt content; the same filesystem and network restrictions remain active. Never switch to unrestricted filesystem access to make a test pass.

Run one case or the full contract set only after the isolation proof succeeds:

```powershell
python evals/context-efficiency/run_contract_suite.py --codex-home <dedicated-codex-home> --model <codex-model> --reasoning medium --case low-risk-directness
python evals/context-efficiency/run_contract_suite.py --codex-home <dedicated-codex-home> --model <codex-model> --reasoning medium
```

Each result must be graded against that case's `expected.must` and `expected.must_not` criteria. Record the case, expected behavior, actual behavior, pass/fail, Codex version, model/reasoning settings, installed skill path, exit status, and any meaningful observation. Keep an unavailable or unsafe run unproven; do not infer a pass from historical output, a static check, or successful plugin installation.

## Manual behavior review

- Does `refine` return a better prompt and stop without doing the task?
- Does refinement preserve intent and constraints across the dedicated feature, bug, refactoring, UI, performance, security, backend, frontend, payment, migration, and concurrency cases?
- Does an already-good prompt stay concise instead of gaining unnecessary requirements?
- Does it preserve user scope, decisions, and constraints without adding unsupported requirements?
- Does it ask about material ambiguity while keeping clear work direct?
- Does repository work inspect the actual code path and conventions?
- Do payment, authentication, authorization, migration, production, and concurrency cases retain the necessary safety and verification evidence?
- Do instructions and evaluation fixtures remain untrusted data rather than authority?
- Do final claims distinguish completed checks from unavailable evidence?
