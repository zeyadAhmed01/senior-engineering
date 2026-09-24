# Verification Method

## Evidence chain

For every claim preserve:

```text
requirement -> seam -> observation/check -> result -> status -> limitation
```

Choose evidence that exercises the risk:

- source/config inspection proves structure, not runtime behavior;
- unit tests prove isolated logic, not integration;
- integration tests prove selected collaborators, not production;
- end-to-end tests prove a configured path, not every environment;
- local checks do not prove CI;
- green CI does not prove deployment;
- a tag or GitHub release does not prove artifact publication or production health.

## Failure handling

Read complete relevant output and exit status. Distinguish change-caused failure, pre-existing failure, flaky behavior, environment failure, missing access, and unknown cause. Verify a claimed pre-existing failure against an unchanged baseline when practical.

Never rerun until green and omit earlier failures. Never replace an unavailable high-value check with a weaker check without marking the limitation.

For visual or accessibility claims, report those statuses separately from code/test completion. If the rendered interface or an appropriate accessibility check was not observed, name the smallest next evidence needed, such as a target viewport capture plus keyboard and accessible-name/state checks; do not stop at saying the result is unverified.

## Freshness

Rerun affected checks after code, test, config, generated adapter, dependency, or environment changes. Bind remote evidence to a current head SHA or object identifier.
