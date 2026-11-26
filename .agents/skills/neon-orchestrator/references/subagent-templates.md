# Subagent Templates, Workflows & Persistent Project Files

Reference templates for `neon-orchestrator`.

---

## 1. Invoking Saved Custom Subagents (Preferred)

When `.agents/agents/` is present in the workspace (or `~/.gemini/config/agents/`), you do **not** need `define_subagent`. Call `invoke_subagent` directly with the saved agent's `name` (`explorer`, `frontend-builder`, `backend-builder`, `verifier`, `doc-writer`):

- **Model selection happens at invocation** (`model`: `"inherit"`, `"flash"`, or `"pro"`) or defaults to the `.agents/agents/<name>.md` frontmatter.
- **Workspace isolation** (`workspace`):
  - `"inherit"`: Read-only `explorer`, `verifier`, or a **single** sequential builder.
  - `"share"` or `"branch"`: **Required** whenever 2+ builders run in parallel so lockfiles, build artifacts, and test runs stay isolated.

### Task Brief Template (`invoke_subagent` `prompt`)
Subagents start with an empty conversation history—your prompt is all they see:

```text
Assigned files (strict boundary): <path1>, <path2>
Context map:
- <path:line-range — symbol/interface notes from explorer>
Goal: <single-sentence objective>
Acceptance criteria:
- <criterion 1>
- <criterion 2>
Verification command: <exact lint/typecheck/test command from AGENTS.md>
Handoff: Return (1) modified files, (2) <=5 bullet summary, (3) exact command outputs.
```

---

## 2. Fallback Transient `define_subagent` Schema (Only When `.agents/agents/` Is Absent)

If orchestrating in a workspace without `.agents/agents/*.md`, note these parameter rules:
- `define_subagent` sets capability flags (`name`, `description`, `system_prompt`, `enable_write_tools`, `enable_mcp_tools`, `enable_subagent_tools` — PascalCase in App/IDE tool declarations, `snake_case` in CLI). It has **no `model` parameter**.
- `enable_write_tools` gates **both** file edits and `run_command` together (all-or-nothing). Unlike `.agents/agents/verifier.md`, a transient subagent cannot allow shell test runs while blocking file edits except via prompt instructions.

---

## 3. Escalation Handoff Template (2-Strike Rule)

When a subagent fails twice or hits an interface blocker:

```text
Escalated from: <agent-name> (<prior model>)
Files involved: <paths + line ranges>
What was tried: <1-2 bullets>
Observed error: <exact minimal error / failing test output>
Goal: Fix the root cause cleanly and verify with `<command>`.
```

---

## 4. `run_workflow` Template (For Fan-Outs > 3–4 Slices)

Use `run_workflow` when fanning out across many files/modules and enforcing a JSON result schema (`flash_lite` is valid here):

```python
RESULT_SCHEMA = {
    "type": "object",
    "properties": {
        "files_modified": {"type": "array", "items": {"type": "string"}},
        "summary": {"type": "string"},
        "tests_passed": {"type": "boolean"},
    },
    "required": ["files_modified", "summary", "tests_passed"],
}

slices = [
    {"role": "Slice A", "files": "src/a.ts", "goal": "..."},
    {"role": "Slice B", "files": "src/b.ts", "goal": "..."},
]

phase("Parallel implementation")
results = await parallel(
    slices,
    lambda s: agent(
        f"Follow backend-dev skill. Edit ONLY {s['files']}. Goal: {s['goal']}. Run targeted tests.",
        schema=RESULT_SCHEMA,
        role=s["role"],
        type_name="backend-builder",
        workspace="branch",
        model="inherit",
    ),
)
print(results)
```

---

## 5. Persistent Project Files (For Greenfield & Multi-Session Builds)

Keep sessions lean ("one slice = one fresh chat") **without** losing project memory by maintaining `PLAN.md`, `TASKS.md`, and `PROGRESS.md` in the project root:

### `PLAN.md` (Architecture & Milestones)
```markdown
# <Project Name> — Implementation Plan

## Stack & Commands
- Stack: <runtime, framework, DB, test runner>
- Commands: see `AGENTS.md`

## Architecture & Shared Contracts
- <Directory layout and module boundaries>
- <Core types / API schemas / DB tables agreed upfront>

## Milestones
1. M0 — Foundation skeleton, shared interfaces, test harness
2. M1 — <Core vertical slice>
3. M2 — <Secondary features & hardening>
```

### `TASKS.md` (Session-to-Session Checklist)
```markdown
# Task Tracker

- [x] M0.1: Bootstrap repo, toolchain, `AGENTS.md`, initial skeleton (`commit <sha>`)
- [ ] M1.1: `[backend-builder]` Implement auth & user schema (`src/db/`, `src/auth/`) — Verify: `npm test -- auth`
- [ ] M1.2: `[frontend-builder]` Build login/session UI (`src/features/auth/`) — Verify: `npm test -- Login`
```

### `PROGRESS.md` (Living Handoff — Updated Each Phase via `doc-writer` / `/phase-handoff`)
```markdown
# Build Progress & Session Handoff

## Current Snapshot
- **Branch**: `main` | **Last Verified Commit**: `<sha>`
- **Health**: Build passing, `<N>` tests passing (`<test command>`)

## Latest Phase Summary
- Completed `<task IDs>`: <1-3 bullets on routes, components, or schemas added>
- **Env / Config Changes**: <new env vars, migrations, or `None`>

## Key Decisions & Caveats
- <Important contract, constraint, or edge case the next session must preserve>

## Next Up (Resume Here)
- **Next Slice**: `M1.2` — Build login/session UI in `src/features/auth/`
- **Verify With**: `npm test -- Login`
```
