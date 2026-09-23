# Context Efficiency Evaluation — historical measurements from 2026-09-23

## Policy

For native Windows v1, use released RTK selectively. RTK is optional: wrap commands only when it materially reduces noisy output, prefer compact summaries for successful tests/builds, and inspect compact failure output first. If failure names, stack traces, or diagnostic evidence are missing, retrieve `rtk recall` or focused raw output before diagnosing. Direct/raw commands remain authoritative. A missing transparent Codex hook is not a readiness blocker; hooking remains a future stable-release gate.

Do not claim account-level ChatGPT Plus savings from RTK command-output measurements. No Spec Kit, Caveman, Headroom, token-router, or other optimization framework is part of this implementation.

## Historical before/after measurement

One synthetic bounded-task comparison against the saved baseline recorded:

| Measure | Baseline | Optimized | Difference |
| --- | ---: | ---: | ---: |
| Commands | 5 | 4 | 20% fewer |
| Aggregated command-output characters | 16,062 | 8,442 | 47.5% fewer |
| Codex-reported input tokens | 156,258 | 99,015 | 36.6% lower in this run |
| Codex-reported output tokens | 1,760 | 1,587 | 9.8% lower in this run |

This is one synthetic observation, not a repeated benchmark. Token telemetry includes runtime and cached context, so it is not attributable solely to the plugin and is not a Plus-billing savings claim. Command-output characters and command count are proxies.

Earlier successful/noisy output examples and their event-level token fields are preserved in the historical evaluation archive. Runs performed with `danger-full-access` are not safe behavioral evidence and are excluded from current release readiness.

## Current package and environment

At the time of this historical run, a clean package copy at version `0.1.0` was installed through the local Codex marketplace workflow. Source and installed cache each contained 302 files with zero hash differences. The host was Windows 11 Pro build `10.0.22000`, Codex CLI `0.156.1`, Python `3.14.3`, and released RTK `0.48.0`. Across the then-current 29 behavior contracts and 11 context-efficiency scenarios, **0 executions completed under proven isolation** because the elevated Windows permission profile had not been shown to deny access to the authenticated `.codex` directory. These results are historical and do not certify v1.0.0; see the current [release-readiness report](../release-readiness-v1.0.0.md).

## Verification limits

The official package/skill validators, repository validator, 19 unit/contract tests, adapter freshness check, and context audit passed for the package state at that time. These static checks did not replace the blocked independent installed-plugin behavior suite.
