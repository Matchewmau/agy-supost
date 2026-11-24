# Token & Cost Efficiency Guide ($50/Month Playbook)

Practical rules for running Antigravity App, IDE, and CLI (`agy`) with subagents on a strict **$50/month** budget.

---

## 1. Tier Your Models by Role
When invoking subagents (`invoke_subagent`) or choosing a model in the App/IDE:
- **Coordinator / Architect (`inherit` / Medium)**: Plans the task, decomposes work, and reviews final diffs.
- **Explorer / Researcher (`flash_lite` or `flash`)**: Searches files, greps symbols, and returns a short summary with exact file paths and line numbers—so the main agent doesn't burn context reading 15 files itself.
- **Frontend & Backend Builders (`flash`)**: Handles routine components, endpoints, migrations, and unit tests. Escalate to `pro` only for complex architecture or hard bugs.
- **Skip `/boost` and large swarms** for routine tasks—they multiply turns and parallel token spend.

---

## 2. Use Skills (Progressive Disclosure) Instead of Big `AGENTS.md` Files
`AGENTS.md` is injected on **every turn** (up to the 20,000-token aggregate rules budget). Keep project `AGENTS.md` files under ~50–80 lines (stack, build/test commands, hard constraints).

Put domain workflows into **Skills**—only their `name` and `description` sit in context until triggered. This repo includes four ready-to-use skills in `.agents/plugins/supost-framework/skills/`:
- [`codebase-explorer`](./.agents/plugins/supost-framework/skills/codebase-explorer/SKILL.md) — Fast, read-only search & mapping.
- [`frontend-dev`](./.agents/plugins/supost-framework/skills/frontend-dev/SKILL.md) — Scoped UI, styling, state, and targeted frontend tests.
- [`backend-dev`](./.agents/plugins/supost-framework/skills/backend-dev/SKILL.md) — Scoped APIs, DB/schemas, auth, and targeted backend tests.
- [`token-efficient-agents`](./.agents/plugins/supost-framework/skills/token-efficient-agents/SKILL.md) — How the coordinator defines and delegates to `flash`/`flash_lite` subagents.

---

## 3. Isolate Context with Focused Subagents (`define_subagent`)
Each subagent runs in its own conversation, so intermediate file reads and failed test logs **never bloat the parent agent's context window**:
1. **Explorer Subagent** (`flash_lite` / `flash`, `EnableWriteTools: false`): Uses `codebase-explorer` and returns only file paths, line ranges, and key symbols.
2. **Frontend Subagent** (`flash`, `EnableWriteTools: true`): Uses `frontend-dev`, edits only UI files, and returns modified paths + test results.
3. **Backend Subagent** (`flash`, `EnableWriteTools: true`): Uses `backend-dev`, edits only server/DB files, and returns modified endpoints/schemas + test results.

---

## 4. Daily Token-Saving Habits
- **Use IDE Tab & `Ctrl+I` for small edits**: Autocomplete and inline commands cost a fraction of a multi-turn Agent Mode loop.
- **One task = one fresh conversation**: Every turn re-sends the entire history. Start a new chat per feature/bug, or run `/compact` when a thread gets long.
- **Run targeted tests**: Run the specific test file (e.g., `pytest tests/test_auth.py`) while iterating, and run the full suite once at the end.
- **Batch reads & edits**: Ask the agent to read/edit related files in parallel rather than one file per turn.
