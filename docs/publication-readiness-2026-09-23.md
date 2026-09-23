# Publication Readiness — 2026-09-23

## Verdict

**NOT READY TO PUBLISH**

The current package supports local/private dogfood. The expanded 19-case smoke, two agent-run seeded fixtures, and one successful installed-Codex-plugin case improve behavioral evidence, but neither packaged runtime has completed its full behavioral suite.

## Current evidence

- Nineteen behavioral contracts each have a distinct Claude-native fixture, prompt, criteria grader, and skill-fired grader.
- A qualitative Codex routing smoke passed 19/19 across two grouped prompts. It is not an independent run per case or an installed-plugin evaluation.
- Fresh Codex-run typo fixture: one-function rename only; Codex ran the focused test (1 passed) and inspected the final diff/status. An independent rerun also passed.
- Installed-plugin smoke: temporarily registered the local package as a Codex marketplace plugin, confirmed Codex loaded the installed `engineer` skill, then completed the isolated low-risk rename fixture. The focused unittest passed, the typo was absent, and only the requested source file changed. The temporary plugin and marketplace registrations were removed afterward. This is one case, not a full 19-case packaged-Codex suite.
- Fresh Codex-run payment fixture: regression failed before the fix due to a new UUID per attempt; Codex changed to a stable checkout-scoped key; the regression then passed (1 test), as did a distinct-checkout invariant check. An independent rerun also passed.
- Codex CLI 0.146.0 / `gpt-5.6-sol` completed both seeded tasks under the host's unrestricted execution profile after its bundled workspace-write sandbox failed to launch. It read canonical source skills directly; this was not plugin-loader evaluation.
- Fresh probe: Claude Code `2.1.280`; local `claude auth status` reported `loggedIn: false`, while the user reported `loggedIn: true` and `authMethod: oauth_token`. Their eval subprocess reported `Not logged in` and the grader reported insufficient credit balance. The discrepancy remains unresolved. No model eval was run because the user chose Codex-only validation.
- Current deterministic recheck: `python scripts/generate_adapters.py --check` PASS; `python scripts/validate.py` PASS; `python -m unittest discover -s tests -v` PASS (13 tests); Claude distribution static validation PASS. Codex-specific validators passed earlier via `uv run --with pyyaml`.
- Independent source review identified missing packaged Claude eval fixtures, a review-case skill-grader mismatch, and stale Claude runtime claims. The fixtures are now generated into `dist/claude/evals/`; a regression test covers all 19; the case now requests missing evidence before edits and grades the engineer route; current runtime claims were refreshed. Focused checks pass.
- Codex manifest and all six skill validators were rerun successfully via `uv run --with pyyaml`.
- Version provenance still needs a release-time decision: the manifest is `0.1.0`, while the changelog has both an `[Unreleased]` section and a dated `[0.1.0]` entry. No commit, tag, remote, or public release exists to establish which exact source state 0.1.0 would identify.
- The repository has no remote, commit, tag, release, marketplace publication, deployment, or pull request.

## Exit criteria

1. COMPLETE: Codex edited, tested, and inspected both seeded fixtures in isolation.
2. Run the remaining 18 prompts as isolated packaged-Codex evaluations and record versions, outputs, and grades; a grouped qualitative smoke is not a substitute. The one completed plugin-loader smoke does not establish broad case coverage.
3. DEFERRED per user choice: no Claude model evaluation is authorized in this Codex-only pass. Run the native suite against `dist/claude` only if the user later chooses cross-runtime behavioral certification and approves its billing/authentication setup.
4. Re-run deterministic validators and tests after any behavioral fixes.
5. A fresh independent review was completed and its three actionable findings were fixed with focused regression/validation checks. A second full review after those narrow fixes has not been run.
6. Reassess publication only after all material failures are resolved or explicitly accepted. Codex-only evidence must not be presented as Claude behavioral certification.

Public repository creation, push, tag, release, and marketplace submission remain separate actions requiring user authorization.
