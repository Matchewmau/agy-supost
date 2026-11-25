---
name: neon-orchestrator
description: >-
  Use this skill when running a Neon (or top-tier) orchestrator session that
  delegates work to lower-tier subagents (Carbon, Argon, Hydrogen, flash,
  flash_lite) equipped with specialized skills to minimize token usage while
  maintaining high code quality.
---

# Neon Orchestrator — Skill-Powered Tiered Subagent Protocol

Use **Neon** as the strategic planner, reviewer, and integrator—not the workhorse for every file read or routine edit. Delegate bounded tasks to lower-tier models equipped with domain skills so each model punches above its weight at a fraction of the token cost.

## 1. Model-to-Task Routing Matrix

| Tier | Models (`invoke_subagent` / Swarm) | Role | Skills to Load | Best For |
| :--- | :--- | :--- | :--- | :--- |
| **Tier 0 (Lead)** | **Neon** (`inherit` / `pro`) | Orchestrator & Reviewer | `neon-orchestrator`, `token-efficient-agents` | Architecture, task decomposition, security/DB decisions, final diff review, resolving blockers |
| **Tier 1 (Complex Build)** | **Carbon / Argon** (`inherit` / `pro`) | Senior Builder | `backend-dev` or `frontend-dev` | Auth, DB migrations, complex state, tricky bug fixes, multi-file refactors |
| **Tier 2 (Standard Build)** | **Hydrogen / `flash`** | Focused Builder | `frontend-dev`, `backend-dev` | Standard UI components, CRUD endpoints, unit tests, wiring known patterns |
| **Tier 3 (Fast / Read-Only)** | **`flash_lite` / `flash`** | Explorer & Scout | `codebase-explorer` | Codebase search, symbol mapping, log triage, boilerplate scaffolding |

> **Core Principle**: A lower model with **clean context + a loaded skill + exact file paths** outperforms an unguided model with a bloated context window.

## 2. Orchestration Workflow

### Step 1: Scout First (Tier 3 — Parallel Read-Only)
Before planning edits, dispatch a read-only `explorer` subagent (`flash_lite` or `flash`, `EnableWriteTools: false`) instructed to read and follow `codebase-explorer/SKILL.md`.
- Require it to return only: **exact file paths, line ranges, key symbols, and test/build commands**.
- Never let Neon scan 20 files directly when `flash_lite` can map them in an isolated context.

### Step 2: Decompose & Assign Skills (Tier 0 — Neon)
Break the task into independent, non-overlapping slices:
1. Assign each slice the **lowest model tier** that can reliably complete it on the first try.
2. Pair every subagent with its **exact skill** (`frontend-dev`, `backend-dev`, `codebase-explorer`, etc.) so it inherits team conventions and verification steps automatically.
3. Define **strict file ownership** so parallel builders never edit the same file.

### Step 3: Dispatch & Fan-Out (Tier 1 / Tier 2)
- Define reusable specialist subagents with `define_subagent` (see [subagent-templates.md](./references/subagent-templates.md) for copy-pasteable prompts and handoff schemas).
- Launch independent subagents in **parallel** in a single turn.
- Pass **file paths, line ranges, and acceptance criteria**—never paste large file dumps into subagent prompts.

### Step 4: Escalation & Circuit Breaker
Prevent cheap models from burning tokens in retry loops:
- **2-Strike Rule**: If a Tier 2/3 subagent fails the same check twice or reports ambiguity, **stop retrying on that tier**.
- **Escalate Up**: Re-dispatch the narrowed problem (with the exact error output) to Tier 1 (Carbon/Argon/`pro`) or handle it directly in Neon.

### Step 5: Integrate & Verify (Tier 0 — Neon)
- Review the concise handoff reports (modified files + test outputs) from each subagent.
- Run one final cross-cutting build/lint/test check if multiple slices touched shared interfaces.
- Report only observed results to the user.

## 3. Token-Efficiency Guardrails
- **Isolate noisy logs**: Run verbose test suites, builds, and grep searches inside subagents so raw logs stay out of Neon's context.
- **Reuse active subagents**: If a slice needs a follow-up fix, use `send_message` to the existing subagent instead of spawning a new one from scratch.
- **No redundant reads**: Trust verified subagent file maps; only read full files in Neon when reviewing critical or ambiguous diffs.

## Verification
Confirm orchestration succeeded when:
1. All subagent slices report passing targeted checks/tests.
2. No overlapping/conflicting edits exist across slices.
3. Final build/lint/test verification passes with zero regressions.
