# Contributing to the SUpost Antigravity Framework

Team members are encouraged to improve this framework whenever you discover a better workflow, catch a recurring agent mistake, or build a reusable agent or skill.

---

## What Goes Where?

| What you want to add | Where to put it | When it loads |
| :--- | :--- | :--- |
| **Team-wide coding/agent rules** | `.agents/rules/AGENTS.md` | Always on in workspace |
| **Reusable custom subagent** | `.agents/agents/<agent-name>.md` | Discovered in `/agents` & `invoke_subagent` across App, IDE, and CLI |
| **Reusable step-by-step workflow** | `.agents/skills/<skill-name>/SKILL.md` | On demand (progressive disclosure) |
| **Project starter boilerplate** | `template/` | Copied into new projects by `project-bootstrap` |
| **Ecosystem / usage docs** | `ANTIGRAVITY_ECOSYSTEM_GUIDE.md` or `README.md` | Reference documentation |

---

## Adding a Custom Subagent (`.agents/agents/<name>.md`)

1. Create `.agents/agents/<agent-name>.md` with YAML frontmatter:
   ```markdown
   ---
   name: <agent-name>
   description: Clear description so the lead agent knows when to invoke it.
   tools:
     - read_file
     - run_command
   subagent: true
   mainAgent: false
   model: flash # Allowed values: inherit, flash, pro
   commandExecutionPolicy: sandbox
   skills:
     - skills/<paired-skill>
   ---
   ```
2. **Double-check `tools` names**: Only use valid runtime tool names (`read_file`, `edit_file`, `write_file`, `run_command`, `manage_task`, `search_web`). Misspelled tool names can cause subagent processes to hang.
3. **Model values**: Subagents only accept `inherit`, `flash`, or `pro` (`Carbon`, `Argon`, and `Hydrogen` are session/Orchestrator models, not subagent `model` values).

---

## Adding a New Skill

1. Create a folder under `.agents/skills/<skill-name>/` (lowercase, hyphenated).
2. Add `SKILL.md` with required YAML frontmatter (`name` matching folder name, third-person `description`).
3. Keep `SKILL.md` concise. Put long templates/manuals in `references/`, helper scripts in `scripts/`, and sample files in `examples/`.
4. Include a **Verification** section telling the agent how to confirm the workflow succeeded.

---

## Updating Rules (`AGENTS.md`)

- Keep rules actionable, non-redundant, and consistent with skill instructions.
- Antigravity limits: **24,000 bytes** max per rule file; **20,000 tokens** shared aggregate budget across all always-on rules.
- If a rule is only needed for a specific task, turn it into a **Skill** instead.

---

## Testing Your Changes

Before committing improvements:
1. Open the repo in **Antigravity CLI (`agy`)**, **Antigravity IDE**, or **Antigravity App**.
2. Run `/agents` in `agy` (or check Customizations in the App) to confirm `.agents/agents/*.md` and skills load cleanly.
3. Verify no broken relative links, leftover `<placeholders>`, or machine-specific paths exist.
