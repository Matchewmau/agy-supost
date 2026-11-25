# SUpost Team Framework — Repository Rules

You are working inside the **SUpost Antigravity Team Framework** repository.

## Purpose
This repository stores reusable Antigravity customizations (rules, skills, plugins, hooks, and project templates) shared across projects and team members.

## Rules for Editing This Repository
1. **Keep Customizations Portable**: Never hardcode machine-specific paths, personal credentials, or project-only secrets inside `.agents/` or `template/`.
2. **Respect Context Budgets**:
   - Keep `AGENTS.md` files concise and high-signal (each rule file is capped at 24,000 bytes; all always-on rules share a 20,000-token budget).
   - Use **skills** (`.agents/skills/<name>/SKILL.md`) for multi-step procedures and put bulky docs in `references/` so they load on demand via progressive disclosure.
3. **Skill Frontmatter**: Every `SKILL.md` must begin with YAML frontmatter containing `name` (lowercase, hyphenated) and `description` (third-person: what it does and when to use it).
4. **Safe Defaults in Templates**: Any `hooks.json` in `template/` must ship with `"enabled": false` unless explicitly tested and safe across Windows, macOS, and Linux.
5. **Follow Contributing Guidelines**: Review [CONTRIBUTING.md](./CONTRIBUTING.md) before adding new plugins, skills, or rules.
