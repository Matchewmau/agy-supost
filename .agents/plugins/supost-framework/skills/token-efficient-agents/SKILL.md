---
name: token-efficient-agents
description: >-
  Use this skill when orchestrating multi-step coding tasks with subagents on a
  strict token budget, assigning model tiers and specialized frontend/backend/explorer roles.
---

# Token-Efficient Agent & Subagent Orchestration

Keep token usage low by routing work to the cheapest capable model tier and isolating context per role.

## 1. Model Tiering
- **Coordinator (Main Agent — `inherit` / Medium)**: Plans the task, decomposes work, reviews final diffs.
- **Explorer (`flash_lite` or `flash`)**: Runs read-only searches via `codebase-explorer` and returns exact file paths + line ranges.
- **Builders (`flash`)**: Executes scoped `frontend-dev` or `backend-dev` tasks. Escalate to `pro` only for complex architecture or hard bugs.
- **Avoid swarms / `/boost`** for routine single-feature work.

## 2. Defining Focused Subagents (`define_subagent`)
When delegating recurring roles, define narrow subagents with `EnableWriteTools: false` for exploration and `EnableWriteTools: true` for builders:
- **`codebase-explorer`**: Read-only (`EnableWriteTools: false`). Instruct it to follow `codebase-explorer/SKILL.md` and return only file paths, line numbers, and a 5–10 line summary.
- **`frontend-builder`**: Write-enabled (`EnableWriteTools: true`). Instruct it to follow `frontend-dev/SKILL.md`, touch only UI files, and run targeted UI tests.
- **`backend-builder`**: Write-enabled (`EnableWriteTools: true`). Instruct it to follow `backend-dev/SKILL.md`, touch only server/DB files, and run targeted backend tests.

## 3. Delegation Rules
- Give each subagent exact target paths and a strict output format.
- Never pass huge file dumps in prompts—pass file paths and let the subagent read only the needed line range.
- Run targeted tests during iteration; run the broader check once at the end.
