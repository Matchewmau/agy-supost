---
name: token-efficient-agents
description: >-
  Use this skill when choosing between Antigravity's built-in Orchestrator model,
  saved custom subagents, and dynamic workflows to minimize token spend while
  keeping code quality and verification strict.
---

# Quality-First Agent & Subagent Efficiency

Optimize token spend through the right execution mode, clean context, and right-sized models—never by skipping verification or forcing weak models onto complex code.

## 1. Session Models vs. Subagent `model` Tiers
- **Single-Thread Sessions**: Use the built-in **`Orchestrator` model** (`agy --model "Orchestrator (Neon)"` or `/model` on Pro/Ultra/Enterprise) when working sequentially—Neon/Carbon plans and reviews while Hydrogen executes searches, edits, and tests automatically. Or pick standalone **Neon / Carbon / Argon** (High effort) for hard architecture/security work and **Hydrogen** (Medium effort) for standard tasks.
- **Subagent `model` Values (`invoke_subagent` / `.agents/agents/*.md`)**: Only **`inherit`**, **`flash`**, and **`pro`** are valid across CLI, App, and IDE (`flash_lite` is only for `run_workflow` Python scripts):
  - **`inherit` or `pro`**: Feature implementation, UI state, APIs, DB schemas, auth, and bug fixes.
  - **`flash`**: Read-only exploration (`explorer`), independent diff/test verification (`verifier`), and low-risk mechanical boilerplate.
  - **Escalate After 2 Failures**: Stop retrying on `flash` if a check fails twice; escalate to `inherit`/`pro` or the lead session.

## 2. Prefer Saved Custom Agents Over Ad-Hoc `define_subagent`
Use the pre-configured agents in `.agents/agents/` directly via `invoke_subagent`:
- **`explorer`** (`model: flash`, tools: `read_file`, `run_command`): Read-only scout paired with `codebase-explorer`.
- **`frontend-builder`** (`model: inherit`, write-enabled): Paired with `frontend-dev`.
- **`backend-builder`** (`model: inherit`, write-enabled): Paired with `backend-dev`.
- **`verifier`** (`model: flash`, tools: `read_file`, `run_command`, `manage_task`): Audits `git diff` and runs tests with **no** file-edit tools.

*(If `.agents/agents/` is absent and you use transient `define_subagent`, pass `enable_write_tools: false/true`—note that `define_subagent` has no `model` parameter and `enable_write_tools` gates shell commands and file writes together.)*

## 3. Workspace Isolation & Real Verification
- Pass file paths, line numbers, and acceptance criteria—never paste whole files into subagent prompts.
- Set `workspace: "share"` or `"branch"` whenever 2+ builders run in parallel.
- Verify real changes (`git diff` + actual lint/typecheck/test runs via the lead agent or `verifier`) before marking any slice complete.
