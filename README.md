# SUpost Antigravity Team Framework

A reusable, team-maintained framework for building projects and custom agents consistently across **Antigravity App (2.0)**, **Antigravity IDE**, and **Antigravity CLI (`agy`)**.

> New to Antigravity? Start with [ANTIGRAVITY_ECOSYSTEM_GUIDE.md](./ANTIGRAVITY_ECOSYSTEM_GUIDE.md) for how the App, IDE, CLI, and Python SDK work together.

---

## Repository Structure

```text
.
├── AGENTS.md                                      # Rules for agents working inside this framework repo
├── ANTIGRAVITY_ECOSYSTEM_GUIDE.md                 # Full guide to App, IDE, CLI, and agent features
├── TOKEN_EFFICIENCY_GUIDE.md                      # $50/mo playbook: model tiering, skills, subagents
├── CONTRIBUTING.md                                # How team members add/improve skills, rules, and plugins
├── .agents/
│   └── plugins/
│       └── supost-framework/                      # Shareable Antigravity plugin (auto-discovered here)
│           ├── plugin.json
│           ├── rules/AGENTS.md                    # Shared team engineering & token-efficiency rules
│           └── skills/
│               ├── codebase-explorer/SKILL.md     # Skill: fast read-only search & file mapping
│               ├── frontend-dev/SKILL.md          # Skill: token-efficient frontend development
│               ├── backend-dev/SKILL.md           # Skill: token-efficient backend development
│               ├── token-efficient-agents/SKILL.md# Skill: model tiering & subagent delegation
│               ├── project-bootstrap/SKILL.md     # Skill: bootstrap any repo with this framework
│               └── framework-contribute/SKILL.md  # Skill: add/update framework skills, rules, hooks
└── template/                                      # Copy-paste starter kit for new projects
    ├── AGENTS.md
    └── .agents/
        ├── hooks.json
        └── skills/
            └── example-workflow/SKILL.md
```

---

## Using This Framework in Another Project

### Option 1: Copy the Starter Template (Recommended for New Projects)
1. Copy everything inside `template/` into the root of your target project.
2. Edit `<your-project>/AGENTS.md` with your project's tech stack, build/test commands, and conventions.
3. Open `<your-project>` in **Antigravity App**, **Antigravity IDE** (`antigravity-ide .`), or **Antigravity CLI** (`agy`). All three surfaces automatically discover `AGENTS.md` and `.agents/`.

### Option 2: Share the Plugin Across Projects
Copy `.agents/plugins/supost-framework/` into:
- **A specific project**: `<your-project>/.agents/plugins/supost-framework/` (team-shared via Git).
- **Your global config**: `~/.gemini/config/plugins/supost-framework/` (applies to all projects on your machine).

### Option 3: Bootstrap with the Agent
Open this repo (or copy the `project-bootstrap` skill) and ask the agent:
> *"Use the `project-bootstrap` skill to set up Antigravity customizations for `<path-to-project>`."*

---

## Improving the Framework

This framework is meant to evolve with the team. See [CONTRIBUTING.md](./CONTRIBUTING.md) for how to add new skills, refine team rules, or contribute lifecycle hooks and plugins.
