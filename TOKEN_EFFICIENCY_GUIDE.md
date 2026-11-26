# Quality-First Token & Cost Guide ($50/Month Playbook)

Practical guidelines for staying within a **$50/month** budget **without sacrificing code integrity, architecture quality, or test coverage**. Fixing buggy output from an underpowered model costs more tokens than doing it right the first time.

---

## 1. Pick the Right Execution Mode & Model

Antigravity separates **session models** (selected via `/model` or `agy --model`) from **subagent `model` tiers** (`inherit`, `flash`, `pro`):

| Work Type | Recommended Mode / Model | Why |
| :--- | :--- | :--- |
| **Single-thread feature or bug fix** | **Built-in `Orchestrator` model** (`Orchestrator (Neon)` on Pro/Ultra; `Carbon + Hydrogen` on Enterprise) | Zero setup: planner (Neon/Carbon) plans & reviews while fast executor (Hydrogen) runs searches, edits, and tests |
| **Architecture, Security, DB Migrations, Hard Bugs** | Standalone **Neon / Carbon / Argon** (High effort), or subagent `model: "pro"` / `"inherit"` | Minimizes subtle bugs, security flaws, and costly rework loops |
| **Parallel Independent Feature Slices (2–4)** | **`neon-orchestrator` + saved `.agents/agents/`** (`inherit` / `pro` builders in `workspace: "share"` or `"branch"`) | Parallel progress with isolated workspaces, per-agent skills, and clean context |
| **Codebase Scouting & Independent Verification** | Saved **`explorer`** / **`verifier`** custom agents (`model: "flash"`) | Read-only scouting and diff/test auditing don't need heavy reasoning |
| **Large Per-File Fan-Outs (>4 items)** | **`run_workflow`** (`model="flash_lite"` or `"flash"` with JSON `schema`) | Enforces structured results across many items in one script |

> **Rule of Thumb**: Never force `flash` onto complex logic, auth, state management, or data-integrity code. If a subagent fails twice, escalate immediately (2-strike rule).

---

## 2. Save Tokens Through Clean Context & Persistent State
- **Keep `AGENTS.md` lean**: Always-on rules load every turn (20,000-token shared budget). Keep `AGENTS.md` under ~50–80 lines.
- **Use Skills (`.agents/skills/`)**: Progressive disclosure keeps domain instructions (`frontend-dev`, `backend-dev`, `neon-orchestrator`) out of context until needed.
- **One slice = one fresh chat + `PLAN.md` / `TASKS.md` / `PROGRESS.md`**: Every turn re-sends conversation history. Keep architecture in `PLAN.md`, slice checklists in `TASKS.md`, and rolling phase handoffs (<120 lines) in `PROGRESS.md` via `/phase-handoff` so each fresh chat starts small without re-exploring the codebase (or run `/compact` on long threads).
- **Use IDE Tab & `Ctrl+I` for small edits**: Inline commands avoid full multi-turn agent overhead for localized changes.

---

## 3. Use Saved Custom Subagents (`.agents/agents/`)
Instead of redefining transient subagents with `define_subagent` (`enable_write_tools`) every session, invoke the saved workspace agents in `.agents/agents/`:
1. **`explorer`** (`model: flash`, `tools: [read_file, run_command]`): Uses `codebase-explorer` to return exact file paths, line ranges, and symbols.
2. **`frontend-builder`** (`model: inherit`, write-enabled): Uses `frontend-dev`; run with `workspace: "share"` or `"branch"` when parallelized.
3. **`backend-builder`** (`model: inherit`, write-enabled): Uses `backend-dev`; run with `workspace: "share"` or `"branch"` when parallelized.
4. **`verifier`** (`model: flash`, `tools: [read_file, run_command, manage_task]`): Audits real `git diff` and runs tests independently—cannot edit files.
5. **`doc-writer`** (`model: flash`, `tools: [read_file, edit_file, write_file, run_command]`): Runs `phase-handoff` to refresh `PROGRESS.md`, `TASKS.md`, and `AGENTS.md` cheaply after verification so your main session doesn't spend top-tier tokens writing docs.

---

## 4. Independent Verification & Git Checkpoints
- Never rely solely on a builder subagent's own summary: inspect `git diff` and rerun lint/typecheck/tests in the lead session or via `verifier`.
- Commit each verified slice (`git commit`) so regressions can be rolled back in one command instead of debugged across 10 turns.
