---
name: release
description: Explicit-only release readiness and publication workflow. Use only when the user directly asks to assess, prepare, tag, publish, deploy, or otherwise manage a release.
license: MIT
disable-model-invocation: true
---

# Release

Separate readiness, publication, deployment, and production verification. A user asking whether a repository is ready has not authorized a tag, release, package publication, or deployment.

## Readiness

Read [release readiness](references/release-readiness.md). Inspect repository-specific versioning, branch policy, required checks, changelog/release notes, artifacts, migrations, compatibility, secrets, operations, rollback, and known limitations. Do not assume semantic versioning, a `v` tag, generated notes, or a particular release branch.

Issue one verdict:

- GO - required evidence is current and no release blocker remains;
- CONDITIONAL GO - named external/CI evidence must complete;
- NO-GO - a material requirement failed or is absent;
- BLOCKED - assessment cannot safely proceed.

## Publication

Read [publication](references/publication.md) only when the user explicitly authorizes the named release action. Reconfirm target repository/environment, version, commit SHA, artifacts, credentials, rollback, and concurrency state immediately before mutation.

## Verify

After publication, read back the tag/release/artifact/deployment and verify the next downstream boundary. Report exactly what is proven. A GitHub release is not a deployment; a deployment record is not production health.
