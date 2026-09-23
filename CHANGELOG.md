# Changelog

This project follows Semantic Versioning. Changes are listed for tagged releases only.

## [1.0.0] - 2026-09-24

Initial public release for OpenAI Codex.

- Publish six Codex skills for prompt refinement, engineering, review, verification, GitHub work, and release readiness.
- Keep prompt refinement explicit: return an improved prompt and do not execute it.
- Add risk-proportional, repository-grounded engineering workflows and evidence-based completion guidance.
- Package Codex plugin metadata and local/Git marketplace installation instructions.
- Add 43 Codex behavior contracts (including 14 direct prompt-refinement cases), 11 context-efficiency scenarios, and deterministic repository checks.
- Document the v1 support boundary: Codex only; Windows validated; other operating systems unverified.

The release does not claim that model-behavior evaluations passed unless their current installed-copy runs and grading are recorded in the release-readiness report.
