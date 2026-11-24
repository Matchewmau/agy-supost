---
name: token-efficient-agents
description: >-
  Use this skill when orchestrating multi-step coding tasks with subagents on a
  budget, matching model tiers and reasoning effort to task risk while keeping code quality high.
---

# Quality-First Agent & Subagent Orchestration

Optimize token spend through clean context and right-sized model/effort selection—never by compromising code integrity or skipping verification.

## 1. Model & Effort Selection by Risk
- **High-Risk / Complex Work** (architecture, auth, DB migrations, tricky bugs, code review): Use high-capability models (`pro`, Neon, Carbon, Argon) with **Medium–High** effort.
- **Standard Feature Work** (UI components, API endpoints, unit tests): Use balanced models (`inherit` / Medium effort) so code quality stays high with minimal errors.
- **Read-Only Exploration & Boilerplate** (searching files, mapping symbols, simple scaffolding): Use `flash` or `flash_lite` with **Low** effort.
- **Escalate Early**: If a lighter model hits errors or ambiguity, immediately escalate to a higher model/effort rather than burning turns retrying.

## 2. Defining Focused Subagents (`define_subagent`)
- **`codebase-explorer`**: Read-only (`EnableWriteTools: false`, `flash`/`flash_lite`). Follows `codebase-explorer/SKILL.md` and returns exact file paths, line numbers, and a concise map.
- **`frontend-builder`**: Write-enabled (`EnableWriteTools: true`, `inherit` or `pro`). Follows `frontend-dev/SKILL.md`, edits UI files, and runs targeted UI tests/lint.
- **`backend-builder`**: Write-enabled (`EnableWriteTools: true`, `inherit` or `pro`). Follows `backend-dev/SKILL.md`, edits server/DB files, and runs targeted backend tests.

## 3. Context & Verification Rules
- Pass file paths and clear acceptance criteria to subagents instead of pasting large file dumps.
- Require every builder subagent to verify its changes with tests/typechecks before reporting back.
