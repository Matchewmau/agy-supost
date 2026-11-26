---
name: project-bootstrap
description: >-
  Use this skill when setting up, initializing, or bootstrapping either a
  brand-new (greenfield) project or an existing repository with the SUpost
  Antigravity Team Framework.
---

# Project Bootstrap (Greenfield & Existing Repos)

Equip any new or existing project with working build/lint/test commands, tailored `AGENTS.md` rules, and the framework's `.agents/` custom agents and skills.

## Steps

### 1. Detect Mode: Greenfield vs. Existing Repo
- **Existing Repo**: Inspect manifests (`package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`, `Makefile`, CI workflows) to find the exact install, build, lint, typecheck, and test commands.
- **Brand-New / Empty Folder (Greenfield)**:
  1. Confirm the target stack and package manager with the user (or read `PLAN.md` if already drafted via `/grill-me` or `/plan`).
  2. Initialize Git (`git init`) if `.git` is missing, and create a sensible `.gitignore`.
  3. Initialize the project manifest/toolchain (e.g., `npm init`, `uv init`, `cargo init`, `go mod init`) so build, lint, and test commands actually exist before agents start coding.

### 2. Install Framework Customizations
- Copy `template/AGENTS.md` into `<target-project>/AGENTS.md` (if `AGENTS.md` already exists, merge missing sections without clobbering project rules).
- Copy `.agents/agents/`, `.agents/rules/`, and `.agents/skills/` into `<target-project>/.agents/` (plus `template/.agents/hooks.json` with `"enabled": false` if desired).

### 3. Tailor `AGENTS.md` & Persistent Trackers
- Replace **every** `<placeholder>` in `<target-project>/AGENTS.md` with verified stack details, directory boundaries, and exact install/build/lint/test commands.
- For greenfield or multi-milestone projects, create `PLAN.md` (architecture, shared contracts, milestones), `TASKS.md` (ordered slice checklist), and `PROGRESS.md` (current build snapshot & next step) at `<target-project>/` so progress persists across sessions.

### 4. Verify & Baseline Checkpoint
- Run at least one verification command (e.g., test runner or build/typecheck) to confirm the toolchain works.
- Confirm `<target-project>/AGENTS.md` has zero `<...>` placeholders and all `.json` files in `.agents/` are valid JSON.
- On a greenfield repo, recommend committing this baseline (`git add -A && git commit -m "chore: bootstrap project and agent config"`) before running `neon-orchestrator` on feature slices.
