# Context efficiency evaluation — 2026-09-23

This compares the pre-change source recorded in [the baseline](../optimization-baseline-2026-09-23.md) with the current canonical policy. It includes a static contract comparison, the earlier grouped routing run, local command measurements, and eleven later independent installed-plugin Codex evaluations.

| Scenario | Before | After contract | Quality guard |
| --- | --- | --- | --- |
| A: button padding | Existing low-risk route called for targeted inspection and focused check, but gave no explicit read/output budget | Read target style source and affected check; concise report; no default specialist | Existing `small-ui-padding` eval still forbids adjacent redesign |
| B: filtered CRUD field | Existing feature workflow traced user seam and acceptance, with no large-read gate | Trace entry point, direct dependencies, tests, and relevant docs; expand to consumers only when evidence requires | Medium route still requires targeted tests, independent review, and verification |
| C: substring/prefix ordering bug | Existing bug route required reproduction and first divergent boundary | Search actual ordering path and discriminating checks before broader research | Root-cause and regression requirements unchanged |
| D: production-only failure | Existing production 2FA eval requires environment comparison | Start at failing route and relevant environment differences, then deepen when evidence points outward | High-risk auth checks and production-equivalent limitation remain |
| E: duplicate payment webhook | Existing high-risk route requires durable idempotency and adversarial review | Deep payment/data path, specialist review when permitted and useful, full diagnostics | No context cap on money, concurrency, or data integrity |
| F: noisy test output | No shared failure-output rule | Passing summary; on failure collect failed cases and excerpts, then raw or recall | Actual RTK failure test showed the first compact result omitted failed names, so raw/recall is mandatory |
| G: long workflow | Task Contract could persist, but no compact continuation shape | Optional state records facts, files, decisions, checks, failures, and next action | Contract remains intent authority; source remains implementation truth |

## Measured command output

Measured on this Windows host with the verified RTK 0.49.0 release binary. Byte counts are captured stdout/stderr files, not model token counts. All comparisons ran the same command in the same repository state and compared exit codes.

| Command/case | Raw bytes | RTK bytes | Exit codes | Observation |
| --- | ---: | ---: | --- | --- |
| `python -m unittest discover -s tests -v` while generated adapters were stale | 3,836 | 189 | 1 / 1 | Compact output retained failure count but hid failed test names; `rtk recall 8c1bfa9aaddc` returned the full diagnostics |
| `rg -n -i 'verified\|evidence' skills` | 16,650 | 16,650 | 0 / 0 | No benefit; use bounded search/range instead |
| `git status --short` | 287 | 286 | 0 / 0 | Negligible benefit |
| `python -m unittest discover -s tests -v` after regeneration | 1,797 | 133 | 0 / 0 | Compact output retained `Ran 13 tests` and `OK` |

After those commands, `rtk gain --project --format json` reported 4 tracked commands, input estimate 5,625, output estimate 4,313, and saved estimate 1,312, all in RTK's own token estimator. `rtk discover --project 'D:\Herd\senior-engineering' --format json` found zero Claude Code sessions and no supported or unsupported missed commands. Neither metric represents ChatGPT Plus usage.

## Scope and decision

The current documentation and `rtk init --codex --dry-run` in released Windows binaries disagree about automatic Codex hooks. The released binary's observed behavior governs this host. Automatic RTK routing was therefore not enabled. No Spec Kit, Caveman, Headroom, or token-router component was installed. The existing 19-case qualitative routing smoke remains the pre-change agent behavior baseline; it has no comparable per-case token telemetry.

## Grouped Codex behavior check

One read-only hypothetical routing prompt covering A–G completed under Codex CLI 0.146.0 with `gpt-5.6-sol`, the model used by the earlier baseline. The current desktop-selected `gpt-6-sol` was rejected by this CLI/ChatGPT-account combination, and the first read-only Windows sandbox attempt blocked file reads. The successful retry used the host's unrestricted execution profile with an explicit read-only prompt; its visible tool trace contained only file reads. The CLI reported 7,150 tokens used for the successful run; no comparable per-run baseline token count exists.

The response classified A low; B and C medium; D and E high; F medium initially; and G by its underlying task risk. It gave narrow initial reads, evidence-based expansion triggers, no default specialist for A or F, durable state for D/E/G, and raw-diagnostic escalation for F. It retained high-risk payment/replay evidence and did not impose a fixed context cap. This is positive routing evidence for all seven grouped cases. It does not prove installed-plugin activation, independent repeated outcomes, real implementation quality, or ChatGPT Plus allowance savings.

## Independent installed-plugin evaluations

Codex CLI `0.146.0` ran on native Windows NT `10.0.22000.0` (Windows 11), Python `3.14.3`, with released winget RTK `0.48.0`. The clean plugin package was `senior-engineering` `0.1.0` from a repository with no HEAD commit. Its package snapshot SHA-256 was `37e728854b257cd55e967965c19d964a03530a16ca4108f9d90b12e0379ecaef`; all 49 installed-cache files matched the package byte-for-byte. The temporary local marketplace `se-context-v1-eval` installed it into a separate `CODEX_HOME`; `codex plugin list --marketplace se-context-v1-eval --json` reported installed and enabled. Each case started a separate `codex exec` process and its trace read the installed cache path. The model was explicitly requested as `gpt-5.6-sol`. Medium reasoning was explicit for payment-concurrency, noisy-failure, long-task, and payment-pressure; the other isolated cases used the temporary home's default, which the trace did not expose. The clean UI rerun and unprompted natural-route case explicitly used `medium` reasoning. No subagents were used.

The reproducible fixtures and launcher are `evals/context-efficiency/run_isolated.py`; JSONL logs and finals were retained under `%TEMP%\se-context-v1-isolated`, with the UI fixture and payment rerun in sibling temporary directories. `evals/context-efficiency/summarize.py` extracts observable counts. The disposable tests exercise the skill's routing and quality boundaries; they are not evidence that an in-memory payment fixture is a production payment implementation.

| Independent case | Type / risk | Context and research | RTK / raw escalation | Verification and observed result | Commands | Output chars | Final chars |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| Trivial UI padding | Change / low | Target style and focused check; no redesign | Skipped / not needed | `python test_button.py` passed; only padding changed | 10 | 11,161 | 248 |
| Standard filtered feature | Feature / medium | Catalog function and focused test | Skipped / not needed | Added optional minimum price, preserved category; 1 test passed | 10 | 14,967 | 402 |
| Search ordering root cause | Bug / medium | Search path, reproduction, ranking cause | Skipped / not needed | Prefix ranks before substring; 1 regression passed | 21 | 18,871 | 594 |
| Unprompted skill routing | Bug / medium | Fresh task prompt did not name a skill; installed `engineer` and `verify` activated | Skipped / not needed | Prefix ranking fixed; 2 tests passed | 10 | 24,880 | 703 |
| Production-only asset failure | Bug / high | Environment-specific branch and fallback | Skipped / not needed | 2 tests passed; live production explicitly unproven | 14 | 23,707 | 767 |
| Payment duplicate/concurrency | Bug / high | Fulfillment transition, event ID, concurrency, durable-boundary limits | Skipped / not needed | Baseline duplicate reproduced; 3 tests and 100 16-thread iterations passed | 35 | 32,751 | 1,414 |
| Noisy successful suite | Verification / low | Focused test only | RTK skipped; raw output summarized | 1 test passed with 180 progress lines; no edit | 10 | 15,800 | 410 |
| Long five-phase task | Investigation / medium overall | Current behavior characterized; compact continuation state | Skipped / not needed | Phase 1 only; later phases and tests not claimed | 28 | 23,742 | 892 |
| Noisy failing suite | Investigation / medium | Compact test, then exact failure block | `rtk test`; compact omitted name/assertion; raw RTK log read before diagnosis | Exit 1, `test_specific_failure`, line 7 assertion identified; no edit | 23 | 24,746 | 1,135 |
| Negligible-benefit command | Investigation / low | Bounded config read | Explicitly skipped RTK | Exact `mode=local`; no edit | 5 | 6,298 | 241 |
| Payment fix under token pressure | Bug / high | Idempotency, 20-thread overlap, trust boundary, adversarial review | Skipped / not needed | 3 tests passed in 25 repeated runs; production limits reported | 21 | 33,866 | 661 |

The first payment-concurrency process timed out at 420 seconds **after** its tests passed, before a final report. It is excluded from the passing-case row. A new fixture and process with a 900-second limit completed and is the result reported above. An earlier UI pilot used the original Codex home and wrote its trace inside the searched fixture, inflating output. It was excluded; the reported UI row is a fresh rerun with traces outside the fixture and the minimal temporary Codex home. Other initial fixtures kept their traces inside the disposable workspace, so their output proxies may include incidental trace-search noise. The high-risk payment cases kept deeper investigation and adversarial checks despite the requested brevity. The failing-test case retrieved the raw log because the compact output was insufficient. No tested case showed a correctness or scope regression; the payment fixes correctly limited their claims to one process.

The table's output measure sums the completed command `aggregated_output` character lengths in Codex JSONL, including skill reads; it is a **proxy**, not token consumption or bytes sent to the model. The CLI also exposed per-case cumulative input/output token usage, but this includes cached input and varying runtime startup/context, and there is no matched pre-change per-case run. It cannot establish token savings, ChatGPT Plus allowance savings, or a controlled before/after delta. Compared with the pre-change contract and 19-case grouped smoke, these isolated cases add observed scope discipline, causal diagnosis, failure escalation, concurrency/security reasoning, focused verification, and resumable state; numerical savings remain unproven.

| Case | CLI input tokens | Cached input included | CLI output tokens |
| --- | ---: | ---: | ---: |
| Trivial UI | 172,210 | 163,584 | 1,454 |
| Standard feature | 229,902 | 219,008 | 2,657 |
| Search bug | 308,411 | 276,352 | 2,519 |
| Unprompted routing | 239,240 | 207,360 | 3,595 |
| Production bug | 264,273 | 242,176 | 2,788 |
| Payment concurrency rerun | 571,755 | 533,632 | 6,175 |
| Noisy success | 232,854 | 213,632 | 2,700 |
| Long task | 458,680 | 429,952 | 4,919 |
| Noisy failure | 285,052 | 258,432 | 4,367 |
| Negligible RTK | 86,374 | 51,456 | 955 |
| Payment pressure | 443,102 | 408,448 | 5,168 |

These are the Codex CLI `turn.completed` usage fields for each independent process, not unique context loaded. The cached-input column is a subset of input, not an additional charge. The initial trace-in-fixture runs may include irrelevant self-read material. No subagents were dispatched. Notable avoidable work included repeated final test/diff checks in the unprompted `engineer` plus `verify` case and trace contamination in excluded pilot measurements; neither changed correctness, but the data do not support a clean quantitative efficiency claim.

## Official and project validation

The applicable official commands were checked against current installed CLI help/scripts before execution. An isolated temporary Python venv with PyYAML `6.0.3` resolved the validator's missing `yaml` module without changing global Python. `validate_plugin.py` passed for the source and clean package; `quick_validate.py` passed for all six public skills. `claude plugin validate ./dist/claude` passed with Claude Code `2.1.280`. The project's adapter freshness check, `scripts/validate.py`, and all 13 unit tests passed. `scripts/context_audit.py` found zero exact duplicate paragraphs. Native Claude model behavior remains unproven because the separate Claude authentication/eval limitation documented in [verification](../verification.md) remains.

## Final review and GitHub boundary

The project's `review`, adversarial-review reference, `verify`, and `github` procedures were applied to canonical policy, generated adapters, evaluation evidence, and rollback. A separate read-only installed-plugin audit reproduced the validator results and identified a gap in generated-root orphan coverage, but its Codex CLI turn ended at the account usage limit before a final verdict. Direct inspection confirmed the gap: `find_orphans()` checked `.codex/agents` and `dist/claude`, but omitted `.codex-plugin` and `.claude-plugin`. Those two roots are now included, and a focused regression test covers both. The final local review found no material defect in compact-failure escalation, RTK selectivity, or high-risk routing. The unprompted case activated both `engineer` and `verify`; their scopes overlap for an ordinary fix-and-verify request and the trace shows repeated final test/diff checks. It caused no missed check or correctness regression; one case is insufficient evidence for changing public skill triggers.

The repository currently has no HEAD commit, tracked files, or Git remote. There is therefore no base/head diff, PR, CI, or merge state to certify; local package and validator readiness is the applicable GitHub boundary. No remote operation was performed. The temporary evaluation `CODEX_HOME` authentication copy was removed after the sessions; the original Codex authentication remained untouched. The installed evaluation plugin and marketplace remain registered locally, with removal commands in [the optimization guide](../context-efficiency.md).

## Readiness

**OPTIMIZATION READY for native-Windows Codex v1 selective RTK use.** The installed plugin passed eleven independent fresh-process cases, including mandatory raw failure diagnostics and the high-risk pressure case. The official applicable validators and project checks pass. Transparent RTK rewriting is an optional future stable-release gate. No model-token or subscription savings are claimed; native Claude model behavior, remote GitHub delivery, and production payment behavior are outside this Codex v1 readiness claim.
