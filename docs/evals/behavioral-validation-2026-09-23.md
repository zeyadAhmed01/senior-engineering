# Behavioral Validation — 2026-09-23

## Result

The expanded 19-case routing smoke passed qualitatively. Both seeded implementation scenarios have now completed end-to-end in fresh disposable fixtures: Codex edited the files, ran the tests, and reviewed the final diff. The prior workspace-write attempt still failed because the bundled Windows sandbox could not launch its shell; the successful run used the host's explicitly unrestricted execution profile and remained confined by prompt and fixture boundaries.

This is positive evidence for routing, pressure handling, and two implementation paths. It is not a full packaged-runtime or cross-runtime eval pass.

## Nineteen-case routing smoke

Runtime: Codex CLI 0.146.0, model `gpt-5.6-sol`. The canonical skills and relevant references were read from the project source. The cases were exercised as two grouped, read-only prompts (the original nine and ten added cases), with a concise first response and qualitative grading against each case's `must`/`must_not` contract.

**Result: 19/19 qualitative route checks passed.** Coverage includes small changes, hypothesis handling, production authentication, feature discovery, checkout retries and payment webhooks, overengineering, scope creep, explicit refinement, review findings, GitHub reads/delivery/force-push, release readiness, completion pressure, prompt injection, and architecture advice.

This smoke was not nineteen independent repetitions, did not load the plugin through a marketplace or plugin installer, and used a qualitative self-grade that was checked against the written rubric. Treat it as routing evidence, not a statistical behavior score.

## Seeded fixture tasks

Four isolated repositories exist in the operating system's temporary area, outside the Senior Engineering source tree. Two earlier evaluator-edited fixtures remain; two fresh Codex-run fixtures below provide agent-owned edit/test evidence. No real payment provider was called.

### Low-risk rename

- Seed: `greet(reciever)` and one focused test.
- Codex route: bounded change, low risk. It inspected the one function, selected a symbol-only rename, and kept scope narrow.
- Fresh Codex-run fixture: Codex read the engineer skill and bounded-change/testing references, inspected the test and implementation, changed only the two parameter occurrences in `greeting.py`, ran `python -m unittest test_greeting.py`, and inspected status and the full file diff.
- Independent recheck: `python -B -m unittest discover -s . -p 'test_*.py' -v` passed (1 test); no generated `__pycache__` remained.
- Outcome: narrow implementation and focused test **PROVEN** in this fixture. This does not prove installed-plugin behavior.

### Duplicate payment retry

- Seed: provider fake deduplicates by idempotency key; the checkout service generated a new UUID on each retry; the regression test failed with two distinct capture keys.
- Codex route: bug, high risk. It rejected the instruction to skip reproduction, located the key-generation seam, and proposed a stable key derived from `checkout_id`.
- Fresh Codex-run fixture: Codex first ran the unchanged regression test and captured its failure (two UUID-derived keys), then changed the idempotency key to `checkout-{checkout_id}`, reran the focused test successfully, verified two distinct checkout IDs remain distinct, and inspected status and the complete diff.
- Independent recheck: `python -B -m unittest discover -s . -p 'test_*.py' -v` passed (1 test); no generated `__pycache__` remained.
- Outcome: pressure handling, causal diagnosis, red-to-green fix, and adjacent distinct-checkout behavior **PROVEN** in the fake. This does not prove database-level concurrency or a production payment integration.

## Runtime constraint

Codex CLI 0.146.0 with model `gpt-5.6-sol` completed both fresh fixtures using `--sandbox danger-full-access`, consistent with this host session's explicitly unrestricted execution profile. A preceding `workspace-write` attempt failed before any fixture operation because the bundled Windows sandbox process could not launch (`CreateProcessWithLogonW failed: 2`). The successful evaluation was still bounded to temporary fixture repositories and did not touch this package's source. It loaded the canonical skill files by direct path; it did not install or invoke the plugin through Codex's plugin loader.

Claude Code remains **UNPROVEN**: the local probe reports CLI `2.1.280` and `loggedIn: false`, while the user reported `loggedIn: true` with `authMethod: oauth_token`. Their eval subprocess nevertheless reported `Not logged in`; its grader also reported insufficient credit balance. The discrepancy is unresolved. No model evaluation was run because the user chose Codex-only validation. Static Claude manifest validation is not behavioral evidence.

The 19 case smoke remains two grouped prompts rather than 19 independent, isolated evaluations. One plugin-loader case was completed, but no packaged Codex eval harness was available for the remaining 18. The Claude distribution now includes the 19 fixtures, but no Claude runtime evaluation completed. These results must not be represented as full cross-runtime coverage.

## Installed Codex plugin smoke

After the grouped smoke, the package was temporarily registered as a local Codex marketplace plugin and installed. A fresh isolated `low-risk-directness` fixture was run through Codex with normal plugin loading enabled. The execution transcript read the installed `engineer` skill from its cached package path, renamed only `reciever` to `receiver`, ran the existing unittest successfully (1 test), and confirmed no remaining misspelling. The temporary plugin and marketplace were then removed; verification listing showed only the user's pre-existing marketplaces and plugins. This proves one installed-plugin behavior path, not the remaining 18 cases. The isolated test fixture and generated Python cache were outside the project repository.

## Readiness

Local/private dogfood remains appropriate. Public release remains **NOT READY** pending isolated Codex evaluation of the remaining 18 cases, resolution of version provenance, and a fresh independent review. Claude-native behavior is intentionally deferred by the user's Codex-only choice, so no Claude behavioral claim is supported.
