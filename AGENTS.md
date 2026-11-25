# SUpost Team Framework — Repository Rules

You are working inside the **SUpost Antigravity Team Framework** repository.

## Purpose
This repository stores reusable Antigravity customizations (custom subagents, rules, skills, hooks, and project templates) shared across projects and team members.

## Rules for Editing This Repository
1. **Keep Customizations Portable**: Never hardcode machine-specific paths, personal credentials, or project-only secrets inside `.agents/` or `template/`.
2. **Respect Context Budgets**:
   - Keep `AGENTS.md` files concise and high-signal (each rule file is capped at 24,000 bytes; all always-on rules share a 20,000-token budget).
   - Use **skills** (`.agents/skills/<name>/SKILL.md`) for multi-step procedures and put bulky docs in `references/` so they load on demand via progressive disclosure.
   - Put reusable specialist roles in **custom subagents** (`.agents/agents/<name>.md`) so sessions do not need to redefine them with `define_subagent`.
3. **Frontmatter & Tool Validity**:
   - Every `SKILL.md` must begin with YAML frontmatter containing `name` (lowercase, hyphenated, matching folder) and `description` (third-person: what it does and when to use it).
   - Every `.agents/agents/<name>.md` must specify valid `model` (`inherit`, `flash`, or `pro` only) and valid runtime `tools` (`read_file`, `edit_file`, `write_file`, `run_command`, `manage_task`, `search_web`).
4. **Safe Defaults in Templates**: Any `hooks.json` in `template/` must ship with `"enabled": false` unless explicitly tested and safe across Windows, macOS, and Linux.
5. **Follow Contributing Guidelines**: Review [CONTRIBUTING.md](./CONTRIBUTING.md) before adding new plugins, skills, or rules.
