# Bounded Change Workflow

## Characterize first

For refactors, configuration, documentation, dependency, and maintenance work, state whether behavior must remain identical or intentionally change. Locate all consumers of the changed contract and the repository's existing convention.

## Choose the smallest coherent edit

- Keep behavior preservation separate from new behavior where practical.
- When a request pairs a specific small change with a broad, undefined add-on (for example, “modernize the whole component”), complete the concrete change and defer the add-on unless a demonstrated dependency makes it necessary and its scope is clear. Ask what outcome the broader request should achieve; do not treat it as permission to add opportunistic formatting, annotations, or refactors.
- Avoid repository-wide mechanical churn unless the request requires it.
- Do not update generated files by hand when a canonical generator exists.
- For dependency changes, inspect lockfiles, compatibility, advisories, and build impact; do not change dependencies without authority.
- For docs, verify claims against current code and change only surfaces made stale.

## Evidence

Use characterization tests for refactors, parsing/build validation for configuration, link or example validation for docs, and consumer compatibility checks for shared contracts. For a clear one-file low-risk edit, run its focused check and inspect only that path's concise diff (for example, `git --no-pager diff -- <path>`); do not repeat a repository-wide search after the target is established. Then report the result briefly. For broader changes, inspect the final diff for accidental scope growth.
