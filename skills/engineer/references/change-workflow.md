# Bounded Change Workflow

## Characterize first

For refactors, configuration, documentation, dependency, and maintenance work, state whether behavior must remain identical or intentionally change. Locate all consumers of the changed contract and the repository's existing convention.

## Choose the smallest coherent edit

- Keep behavior preservation separate from new behavior where practical.
- Avoid repository-wide mechanical churn unless the request requires it.
- Do not update generated files by hand when a canonical generator exists.
- For dependency changes, inspect lockfiles, compatibility, advisories, and build impact; do not change dependencies without authority.
- For docs, verify claims against current code and change only surfaces made stale.

## Evidence

Use characterization tests for refactors, parsing/build validation for configuration, link or example validation for docs, and consumer compatibility checks for shared contracts. Inspect the final diff for accidental scope growth.

