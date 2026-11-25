# Quality-First Token & Cost Guide ($50/Month Playbook)

Practical guidelines for staying within a **$50/month** budget **without sacrificing code integrity, architecture quality, or test coverage**. Fixing buggy output from an underpowered model costs more tokens than doing it right the first time.

---

## 1. Match Model & Effort to Task Risk (Quality First)
Use the full range of available models (e.g., **Neon**, **Carbon**, **Argon**, **Hydrogen**, `pro`, `flash`) and tune **reasoning effort** to match the complexity and risk of the work:

| Work Type | Recommended Model & Effort | Why |
| :--- | :--- | :--- |
| **Architecture, Security, DB Migrations, Hard Bugs** | High-capability (`pro`, Neon/Carbon/Argon) at **High** effort | Minimizes subtle bugs, security flaws, and costly rework loops |
| **Feature Implementation (Frontend & Backend)** | Balanced (`inherit` / Hydrogen / Carbon) at **Medium** effort | Strong code quality and conventions at reasonable cost |
| **Codebase Search & File Mapping** | Fast (`flash` / `flash_lite`) at **Low** effort | Read-only exploration doesn't need heavy reasoning |
| **Routine Boilerplate & Formatting** | Fast (`flash`) at **Low–Medium** effort | Low-risk edits with clear patterns |

> **Rule of Thumb**: Never force a weak model onto complex logic, auth, state management, or data-integrity code. Escalate model/effort whenever errors or ambiguity appear.

---

## 2. Save Tokens Through Clean Context (Not Weak Models)
- **Keep `AGENTS.md` lean**: Always-on rules load on every turn (20,000-token aggregate budget). Keep `AGENTS.md` under ~50–80 lines.
- **Use Skills (`.agents/skills/`)**: Progressive disclosure keeps domain instructions (`frontend-dev`, `backend-dev`, `codebase-explorer`, `token-efficient-agents`) out of context until needed.
- **One task = one fresh conversation**: Every turn re-sends the full history. Start a new chat per feature/bug, or use `/compact` on long threads.
- **Use IDE Tab & `Ctrl+I` for small edits**: Autocomplete and inline commands avoid full multi-turn agent overhead for localized changes.

---

## 3. Isolate Context with Focused Subagents (`define_subagent`)
Subagents run in their own context window, preventing intermediate file reads and test logs from bloating the main session. For a full Neon-led delegation protocol (4-tier model routing, skill pairing, and 2-strike escalation), see [neon-orchestrator/SKILL.md](./.agents/skills/neon-orchestrator/SKILL.md).

1. **Explorer Subagent** (`flash` / `flash_lite`, `EnableWriteTools: false`): Uses `codebase-explorer` to return exact file paths, line ranges, and key symbols.
2. **Frontend Subagent** (`inherit` or `pro` for complex state/UI, `EnableWriteTools: true`): Uses `frontend-dev`, edits UI files, and runs targeted UI checks + build.
3. **Backend Subagent** (`inherit` or `pro` for API/DB/auth, `EnableWriteTools: true`): Uses `backend-dev`, edits server/DB files, and runs targeted backend tests.

---

## 4. Verification Keeps Errors (and Rework) Minimal
- Run targeted tests while iterating (`pytest tests/test_auth.py`), then run the full relevant lint/typecheck/test suite before finishing.
- Review diffs carefully—catching a bug in one verification pass is far cheaper than debugging it across 10 follow-up turns.
