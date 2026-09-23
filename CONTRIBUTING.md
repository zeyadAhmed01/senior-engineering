# Contributing

Keep contributions narrow, evidence-backed, and aligned with the Codex-only v1 scope.

1. Read `AGENTS.md` and the relevant design or research document.
2. Change canonical sources, not generated adapters.
3. Add or update an eval case when behavior changes.
4. Regenerate adapters and run the validation commands in `AGENTS.md`.
5. Record any new upstream source, commit pin, license, and adaptation in `THIRD_PARTY_NOTICES.md`.

Public skills are a constrained interface. Prefer an internal reference module over adding a new public skill. Keep Codex metadata in the canonical Codex manifest or the generated Codex files; do not add another agent-runtime adapter to v1.
