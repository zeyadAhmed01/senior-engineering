# Publication Readiness — 2026-09-22

Historical snapshot. Superseded by the behavioral validation report dated 2026-09-23.

## Verdict

**NOT READY TO PUBLISH**

The package is ready for local/private dogfood, but public publication would overstate cross-runtime behavioral evidence.

## Proven

- The Agent Plugins 1.0 root manifest passes the Codex plugin validator.
- All six canonical skills pass the Codex skill validator.
- The generated Claude distribution passes `claude plugin validate`.
- Adapter generation is reproducible and detects stale managed files.
- Ten unit/contract/validation tests pass.
- Nine behavioral contracts have matching Claude-native fixtures.
- An independent Codex review and completion audit were run; all four actionable review findings were remediated.
- License, provenance, contribution, security, changelog, migration, and usage documentation exist.
- The repository has no configured remote, commit, tag, release, or marketplace publication.

## Blocking evidence

1. Claude Code behavior is unproven because the installed CLI is unauthenticated and too old for the current native plugin-eval workflow.
2. The nine-case suite has not been executed through both packaged runtimes after the final adapter fixes.
3. No seeded fixture repository has exercised a complete investigation-to-implementation-to-verification route.
4. A final independent review should be repeated after those behavioral runs because eval-driven fixes can alter the package.

## Exit criteria

- Authenticate and upgrade Claude Code, then run the native eval suite against `dist/claude`.
- Run the cross-runtime cases against the packaged Codex and Claude forms and record model/runtime versions, repetitions, results, and failures.
- Complete at least one seeded low-risk change and one high-risk bug scenario without external writes.
- Resolve or explicitly accept every failure, rerun deterministic checks, and repeat independent review/verification.
- Only then reassess public repository creation, marketplace submission, tag, and release as separately authorized actions.
