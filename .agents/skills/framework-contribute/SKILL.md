---
name: framework-contribute
description: >-
  Use this skill when a user or team member wants to add, update, or refactor
  a custom agent, skill, rule, hook, or template in the SUpost Antigravity Team Framework.
---

# Contribute to the SUpost Antigravity Framework

Guide team members through adding or improving reusable customizations in this repository.

## Steps

1. **Classify the Change**:
   - **Always-on rule** (short, universal constraint) -> `.agents/rules/AGENTS.md`
   - **Reusable specialist subagent** (fixed tools, model tier, paired skills) -> `.agents/agents/<agent-name>.md`
   - **On-demand workflow** (multi-step procedure) -> `.agents/skills/<skill-name>/SKILL.md`
   - **New-project starter** -> `template/`
2. **Author the Change**:
   - **Custom agents (`.agents/agents/<name>.md`)**: Include YAML frontmatter with `name`, `description`, `subagent: true`, `mainAgent: false`, `model` (`inherit`, `flash`, or `pro` only), `commandExecutionPolicy` (`sandbox` recommended), optional `skills: [skills/<skill-name>]`, and an explicit `tools` list using **exact** runtime tool names (`read_file`, `edit_file`, `write_file`, `run_command`, `manage_task`, `search_web` — unmapped/misspelled tool names can cause subagents to hang).
   - **Skills**: Create `<skill-name>/SKILL.md` with lowercase hyphenated `name` matching the folder and third-person `description` in YAML frontmatter. Move lengthy docs to `references/` and helper scripts to `scripts/`.
   - **Rules**: Keep concise (under 24,000 bytes per file; mindful of the 20,000-token aggregate budget) and ensure rules never contradict skill model/tool guidance.
   - **Hooks**: Place in `template/.agents/hooks.json` with `"enabled": false` by default unless cross-platform safe.
3. **Validate**:
   - Check JSON syntax on any modified `.json` files and YAML frontmatter on `.agents/agents/*.md` and `SKILL.md`.
   - Verify no machine-specific paths, secrets, or invalid subagent parameter/model names were introduced.
   - Confirm [README.md](../../../README.md) or [CONTRIBUTING.md](../../../CONTRIBUTING.md) reflects any new files.
