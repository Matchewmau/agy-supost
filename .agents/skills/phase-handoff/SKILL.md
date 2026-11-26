---
name: phase-handoff
description: >-
  Use this skill at the end of a task, slice, or milestone (or via /phase-handoff)
  to update PROGRESS.md, TASKS.md, and AGENTS.md so the next chat session or
  teammate can pick up the build immediately with minimal token cost.
---

# Phase Handoff & Living Build Docs

Capture verified build progress, architectural decisions, and exact next steps in repository Markdown files so fresh chat sessions resume in seconds without re-exploring the codebase.

## When to Run
- Automatically at the end of **Phase 3** in `neon-orchestrator` after verification passes.
- Whenever finishing a feature, milestone, migration, or debugging session.
- Explicitly when the user runs `/phase-handoff`.

> **Token-Efficiency Tip**: When the main session runs on a high-tier model (Neon, Carbon, Argon), invoke the saved **`doc-writer`** custom subagent (`model: "flash"`, `workspace: "inherit"`) to perform this update cheaply.

## Steps

### 1. Gather Ground-Truth Repo State
Run one compact command (`git status -s`, `git log -n 3 --oneline`, `git diff --stat`) and read existing `PROGRESS.md`, `TASKS.md`, and `AGENTS.md` if present. Never invent file paths, commands, or commit SHAs.

### 2. Update `PROGRESS.md` (Keep Under ~120 Lines)
Create or update `PROGRESS.md` at the repo root. **Overwrite** stale status sections instead of endlessly appending—keep only the 5 most recent phase entries so `PROGRESS.md` stays tiny in future context windows:
- **Current Snapshot**: Branch, latest verified commit SHA, and build/test status.
- **Latest Changes**: Completed slice(s), key files/routes/components added or changed, and any new env vars or DB migrations required.
- **Decisions & Caveats**: Non-obvious constraints, contracts, or known limitations future sessions must respect.
- **Next Up**: The exact next task ID from `TASKS.md`, target files, and verification command so a new session can start immediately.

### 3. Sync `TASKS.md` & `AGENTS.md`
- **`TASKS.md`**: Mark verified slices `[x]` (with commit SHA if committed) and add newly discovered follow-up slices under the right milestone.
- **`AGENTS.md`** *(edit only if needed)*: Update `Key Commands` or `Architecture & Conventions` if new scripts, package managers, test commands, or top-level directories were introduced. Keep `AGENTS.md` concise.

## Verification
Confirm handoff succeeded when:
1. `PROGRESS.md` is concise (<120 lines) and accurately reflects observed `git` state and test results.
2. `TASKS.md` checkboxes match actual verified work.
3. No application source or test files were modified during the doc pass.
