---
name: project-bootstrap
description: >-
  Use this skill when the user asks to set up, initialize, or bootstrap a new
  or existing project with the SUpost Antigravity Team Framework.
---

# Project Bootstrap

Set up any target repository with Antigravity rules, skills, and hook templates tailored to its tech stack.

## Steps

1. **Inspect the Target Project**:
   - Check the root directory of the target project for language/framework markers (e.g., `package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`, `.git`).
   - Identify the actual build, lint, and test commands used by the project.
2. **Install Project Customizations**:
   - Copy `template/AGENTS.md` from the framework into `<target-project>/AGENTS.md` (if one does not already exist; otherwise merge sections carefully).
   - Copy `template/.agents/` into `<target-project>/.agents/`.
   - Optionally copy `.agents/rules/` and `.agents/skills/` into `<target-project>/.agents/` if the team wants the shared rules and skills bundled in the repo.
3. **Tailor `AGENTS.md`**:
   - Fill in the project's tech stack, directory layout, and verified build/test/lint commands.
   - Remove placeholder comments that no longer apply.
4. **Verify**:
   - Confirm `<target-project>/AGENTS.md` and `<target-project>/.agents/` exist and contain valid Markdown/JSON.
   - Summarize the created files and remind the user they can open the project in Antigravity App, Antigravity IDE (`antigravity-ide`), or `agy`.
