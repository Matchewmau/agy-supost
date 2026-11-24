---
name: framework-contribute
description: >-
  Use this skill when a user or team member wants to add, update, or refactor
  a skill, rule, hook, or template in the SUpost Antigravity Team Framework.
---

# Contribute to the SUpost Antigravity Framework

Guide team members through adding or improving reusable customizations in this repository.

## Steps

1. **Classify the Change**:
   - **Always-on rule** (short, universal constraint) -> `.agents/plugins/supost-framework/rules/AGENTS.md`
   - **On-demand workflow** (multi-step procedure) -> `.agents/plugins/supost-framework/skills/<skill-name>/SKILL.md`
   - **New-project boilerplate** -> `template/`
2. **Author the Change**:
   - For skills: create `<skill-name>/SKILL.md` with lowercase hyphenated `name` and third-person `description` in YAML frontmatter. Move lengthy docs to `references/` and helper scripts to `scripts/`.
   - For rules: keep total size concise (under 24,000 bytes per file; mindful of the 20,000-token aggregate budget).
   - For hooks: place in `hooks.json` at the plugin root (or `template/.agents/hooks.json` with `"enabled": false` by default).
3. **Validate**:
   - Check JSON syntax on any modified `.json` files (`plugin.json`, `hooks.json`, `mcp_config.json`).
   - Verify no machine-specific paths or secrets were introduced.
   - Confirm [README.md](../../../../README.md) or [CONTRIBUTING.md](../../../../CONTRIBUTING.md) reflects any new top-level structure.
