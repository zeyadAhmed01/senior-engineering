# GitHub Capability Selection

## Order

1. Official GitHub MCP for structured reads/writes when available.
2. `gh` for deterministic supported GitHub operations.
3. Local `git` for commits, refs, branches, diffs, remotes, and worktrees.
4. Browser automation only when structured capabilities cannot complete an authorized action.

Do not assume capability names. Discover available tools or command help. Current official docs outrank copied command recipes.

## MCP

Prefer read-only mode during discovery and the smallest toolset, such as repositories, issues, pull requests, Actions, code security, or secret protection. Lockdown and push protection are defense in depth, not authorization or proof that content is safe.

## CLI

Use explicit repository arguments when the current checkout may not match the target. Read complete bodies/comments and paginate APIs where relevant. Inspect command help for current flags rather than preserving stale limitations.

## Local git

Validate refs before shell use. Fetch only when needed and without overwriting local work. Do not pull, rebase, reset, clean, switch, force-push, or delete branches/worktrees merely to simplify reconciliation.

## Fallback

If no structured capability can perform an authorized action, report the exact missing capability and provide a safe manual command or step. Do not silently replace a read with a scrape or a write with browser clicking.

