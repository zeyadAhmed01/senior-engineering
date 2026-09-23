# Repository Discovery

## Establish authority

1. Read instructions from the repository root toward the target path and resolve their precedence.
2. Inspect the current branch, status, diff, remotes, and relevant worktrees without modifying them.
3. Preserve uncommitted and untracked user work. Do not reset, clean, switch, pull, merge, or broadly stage to simplify the task.
4. Identify authoritative architecture, contributor, test, CI, release, schema, and dependency files.

## Trace the real path

Start from the user-visible or external entry point and follow routing, controllers/components, services/actions, models/storage, configuration, and tests. Search for actual consumers before changing a shared helper or contract.

Prefer iterative retrieval:

1. Locate candidate entry points.
2. Read the smallest relevant body and its delegates.
3. Test one hypothesis about control or data flow.
4. Expand only when evidence points outward.

Do not substitute filenames, naming intuition, or an issue description for execution-path evidence.

## Dirty or unsafe checkout

Work around unrelated changes. Use an isolated worktree only when the task needs a clean or independent branch and worktree creation is in scope. Never delete or overwrite an ambiguous existing worktree.

## Current documentation

For time-sensitive frameworks, APIs, platform commands, policies, and security behavior, use authoritative current documentation. Record material version assumptions.

