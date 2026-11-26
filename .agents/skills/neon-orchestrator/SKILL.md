---
name: neon-orchestrator
description: >-
  Use this skill as the process and coordination layer when planning, building
  a project from scratch, or delegating parallel feature slices across saved
  custom subagents, the built-in Orchestrator model, or dynamic workflows.
---

# Neon Orchestrator — Process & Multi-Agent Coordination Layer

Treat this skill as the **process layer** (plan, bootstrap, slice, isolate, verify, checkpoint, escalate) while letting Antigravity's native features handle execution mechanics.

---

## 1. Choose the Right Execution Mechanism First

Do not spawn subagents when a simpler or stronger built-in mode fits better:

| Scenario | Best Antigravity Mechanism | How It Works |
| :--- | :--- | :--- |
| **Single-thread feature or bug fix** | **Built-in `Orchestrator` model** (`agy --model "Orchestrator (Neon)"` or `/model`) | Zero setup. Neon plans and reviews while a fast executor (**Hydrogen** / Sonnet 5.5) runs searches, edits, and tests in one thread. Load domain skills (`frontend-dev`, `backend-dev`) directly. |
| **2–4 independent parallel slices** | **Saved custom subagents** (`.agents/agents/*.md` via `invoke_subagent`) | Parallel execution with per-agent skills, strict tool lists, and isolated workspaces (`workspace: "share"` or `"branch"`). |
| **Large fan-out (>4 slices / per-file pipeline)** | **`run_workflow`** (Python script) | Uses `parallel()` / `pipeline()` with `model="flash_lite"` / `"flash"` / `"pro"` and enforces structured JSON output via `schema`. |
| **Broad parallel work on a shared board** | **`/swarm`** *(user-invoked only)* | User starts `/swarm`; workers coordinate on a shared message board with dedicated verifiers. (Workers stay on the coordinator's model.) |
| **Multi-day / multi-milestone system** | **`/teamwork`** *(paid plans)* | Runs a scoping interview, persistent project folder, and dedicated explorer/worker/auditor roles. |

---

## 2. Valid Subagent Models & Saved Agents

Subagents (`invoke_subagent` and `.agents/agents/*.md`) accept **only** `inherit`, `flash`, or `pro` for `model` (`Carbon`, `Argon`, and `Hydrogen` are session/Orchestrator models, not subagent `model` values; `flash_lite` is for `run_workflow` scripts, not CLI subagents).

| Custom Agent (`.agents/agents/`) | Default `model` | `workspace` | Allowed Tools | Role & Paired Skill |
| :--- | :--- | :--- | :--- | :--- |
| **`explorer`** | `flash` | `inherit` | `read_file`, `run_command` | Read-only scout (`codebase-explorer`) |
| **`frontend-builder`** | `inherit` (override to `flash` only for low-risk boilerplate, or `pro`) | `share` or `branch` (parallel) / `inherit` (solo) | `read_file`, `edit_file`, `write_file`, `run_command`, `manage_task` | UI/state builder (`frontend-dev`) |
| **`backend-builder`** | `inherit` (or `pro`) | `share` or `branch` (parallel) / `inherit` (solo) | `read_file`, `edit_file`, `write_file`, `run_command`, `manage_task` | API/DB/auth builder (`backend-dev`) |
| **`verifier`** | `flash` | `inherit` (or target branch) | `read_file`, `run_command`, `manage_task` | Independent diff & test auditor (no file-write tools) |
| **`doc-writer`** | `flash` | `inherit` | `read_file`, `edit_file`, `write_file`, `run_command` | Updates `PROGRESS.md`, `TASKS.md`, and `AGENTS.md` (`phase-handoff`) |

> **Note on `inherit` with the built-in `Orchestrator` model**: `inherit` uses the parent session's model. If your main session is running on `Orchestrator (Neon)` rather than standalone `Neon`, verify what `inherit` resolves to in `/agents` before relying on it, or pass `model: "pro"` / `"flash"` explicitly.

---

## 3. Orchestration Workflow

### Phase 0: Entry Gate — Greenfield vs. Existing Repo

**Path A: Starting a New Project from Scratch (Greenfield)**
Do **not** fan out parallel builders into an empty folder. Execute sequentially first:
1. **Align & Spec**: Recommend `/grill-me` or `/plan` if requirements are open. Write **`PLAN.md`** (stack, architecture, milestones, acceptance criteria), **`TASKS.md`** (ordered checklist of slices), and an initial **`PROGRESS.md`** at the repo root so progress persists across fresh chat sessions (templates in [subagent-templates.md](./references/subagent-templates.md)).
2. **Bootstrap Repo & Toolchain**: Initialize Git (`git init`), scaffold the project manifest/toolchain, and run the **`project-bootstrap`** skill so `AGENTS.md` contains real, working install/build/lint/test commands and `.agents/` is installed.
3. **Foundation Slice + First Checkpoint**: Have a single builder (or the lead session) create the directory skeleton, shared types/interfaces, DB/config baseline, and a passing smoke test. Commit this baseline (`git commit -m "chore: initial project skeleton"`) **before** any parallel work begins.

**Path B: Working in an Existing Repo**
1. Read `AGENTS.md` first, plus `PROGRESS.md`, `TASKS.md`, and `PLAN.md` if present—`PROGRESS.md` gives you the latest build state, caveats, and next slice without re-scanning old work. If `AGENTS.md` is missing or still has `<placeholder>` commands, run `project-bootstrap` first.
2. Invoke the saved **`explorer`** subagent (`model: "flash"`, `workspace: "inherit"`) to map only the files, line ranges, and symbols needed for the current task.

### Phase 1: Decompose & Isolate Workspaces
1. Split work into independent slices with **non-overlapping file ownership** (update `TASKS.md` for multi-slice features).
2. Choose `model` per `invoke_subagent` call:
   - `inherit` or `pro`: Feature logic, state management, APIs, DB migrations, auth, tricky bugs.
   - `flash`: Read-only scouting, independent test runs, or strictly mechanical boilerplate with clear patterns.
3. **Isolate parallel builders**: Whenever 2+ builders run concurrently, set **`workspace: "share"`** (separate working copy sharing Git storage) or **`"branch"`** (isolated clone)—never let parallel builders share `workspace: "inherit"`, where lockfiles, build outputs, and test runs collide.

### Phase 2: Dispatch & 2-Strike Circuit Breaker
- Invoke the saved agents (`explorer`, `frontend-builder`, `backend-builder`) using the compact prompt format in [subagent-templates.md](./references/subagent-templates.md). Pass file paths and line ranges—never paste whole files.
- Use `send_message` to follow up with an idle subagent that already holds slice context instead of spawning a new one.
- **2-Strike Escalation**: If a subagent fails the same check twice or hits cross-slice ambiguity, stop retrying at that level—escalate `flash` -> `inherit`/`pro`, or resolve directly in the lead session.

### Phase 3: Independent Verification, Docs Sync & Git Checkpoints
**Never mark a slice done based only on the builder's own summary:**
1. Integrate changes from `share` / `branch` workspaces into the working branch.
2. **Audit the real diff & rerun checks**: Either inspect `git status -s` + `git diff` and run the lint/typecheck/test commands directly in the lead session, or invoke the read-only **`verifier`** subagent (`model: "flash"`) to check `git diff` against acceptance criteria and execute the test suite.
3. **Update Living Build Docs (`phase-handoff`)**: Invoke **`doc-writer`** (`model: "flash"`)—or follow `phase-handoff` directly—to refresh `PROGRESS.md` (what changed, new env vars/migrations, caveats, exact next step), check off `TASKS.md`, and sync `AGENTS.md` if commands/layout changed.
4. **Checkpoint**: Create a clean Git checkpoint commit per verified slice/phase (including the updated `PROGRESS.md` and `TASKS.md`) so any later regression can be rolled back cleanly and the next session resumes immediately.

---

## Verification
Confirm orchestration succeeded when:
1. `git diff` has been independently reviewed (by the lead or `verifier`) with no out-of-scope edits or leftover placeholders.
2. Target lint, typecheck, build, and test commands pass and observed outputs are reported.
3. `PROGRESS.md` and `TASKS.md` (plus `AGENTS.md` if commands changed) are updated so the next session can pick up with zero guesswork.
