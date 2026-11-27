# SUpost Antigravity Team Framework

A reusable, team-maintained framework of **custom subagents**, **skills**, **shared rules**, and **project templates** that works consistently across **Antigravity App (2.0)**, **Antigravity IDE**, and **Antigravity CLI (`agy`)**.

> New to Antigravity? Start with [ANTIGRAVITY_ECOSYSTEM_GUIDE.md](./ANTIGRAVITY_ECOSYSTEM_GUIDE.md) for how the App, IDE, CLI, built-in Orchestrator model, custom subagents, and workflows fit together.

---

## Start a project in an empty folder

Open the folder in Antigravity, replace `<your project idea>` with what you want to build, and paste this prompt into the chat.

```text
Start a new project in this folder. Use project-bootstrap from https://github.com/Matchewmau/agy-supost.git to install all agents, skills, and rules here. Then use neon-orchestrator to set up the tooling, build the first working version, and verify it runs.

Project: <your project idea>
```

### Roblox game with live Rojo sync

```text
Set up this folder as a Roblox game. Use project-bootstrap from https://github.com/Matchewmau/agy-supost.git to install all agents, skills, and rules here. Connect Rojo to Roblox Studio and verify live sync by checking that a local Luau edit appears in Studio. Then use neon-orchestrator to build the first playable version of <your game idea>.
```

## Quick Onboarding (Which Doc to Read)

| If you want to... | Read this |
| :--- | :--- |
| **Learn how Antigravity works** (App, IDE, CLI, Orchestrator model, `/swarm`, `/teamwork`) | [ANTIGRAVITY_ECOSYSTEM_GUIDE.md](./ANTIGRAVITY_ECOSYSTEM_GUIDE.md) |
| **Stay on budget without losing code quality** (model selection, context hygiene, `PLAN.md`/`TASKS.md`/`PROGRESS.md`) | [TOKEN_EFFICIENCY_GUIDE.md](./TOKEN_EFFICIENCY_GUIDE.md) |
| **Coordinate greenfield builds or parallel slices** (saved agents, isolated workspaces, real verification) | [neon-orchestrator/SKILL.md](./.agents/skills/neon-orchestrator/SKILL.md) |
| **Keep living build/handoff docs updated at milestones and session boundaries** (`PROGRESS.md`, `TASKS.md`, `doc-writer`) | [phase-handoff/SKILL.md](./.agents/skills/phase-handoff/SKILL.md) |
| **Add or improve custom agents, skills, rules, or templates** | [CONTRIBUTING.md](./CONTRIBUTING.md) |

### Choosing How to Run Work
- **Single-thread feature or bug fix**: Select the built-in **`Orchestrator` model** (`agy --model "Orchestrator (Neon)"` or `/model`) so Neon plans/reviews and Hydrogen executes automatically, and let the agent load `frontend-dev` / `backend-dev` skills.
- **Starting a brand-new project from scratch**: Run `/grill-me` or `/plan`, then prompt *"Use `neon-orchestrator` and `project-bootstrap` to initialize this project"* — sets up `PLAN.md`, `TASKS.md`, verified `AGENTS.md` commands, and an initial skeleton commit before parallel slices begin.
- **Parallel feature slices** — agree shared contracts first, then dispatch disjoint files to isolated builders. Scout only when needed. Review the integrated diff and run required final checks.
- **Milestones and session boundaries** — batch durable tracker updates with `/phase-handoff` or the saved doc-writer.
- **Large fan-outs (>4 files/modules)** or **multi-day builds**: Use `run_workflow` (schema-checked Python fan-out) or `/teamwork`.

---

## Repository Structure

```text
.
├── AGENTS.md                                      # Rules for contributors editing this framework repo
├── ANTIGRAVITY_ECOSYSTEM_GUIDE.md                 # Guide to App, IDE, CLI, Orchestrator, and multi-agent modes
├── TOKEN_EFFICIENCY_GUIDE.md                      # $50/mo playbook: Orchestrator vs subagents, context & checkpoints
├── CONTRIBUTING.md                                # How team members add/improve agents, skills, and rules
├── .agents/
│   ├── agents/                                    # Saved custom subagents (auto-discovered in App, IDE, and CLI)
│   │   ├── explorer.md                            # Read-only codebase scout (flash, sandbox, codebase-explorer)
│   │   ├── frontend-builder.md                    # Scoped UI/state builder (inherit, frontend-dev)
│   │   ├── backend-builder.md                     # Scoped API/DB/auth builder (inherit, backend-dev)
│   │   ├── verifier.md                            # Independent diff & test auditor (flash, no file-edit tools)
│   │   └── doc-writer.md                          # Low-cost handoff & docs updater (flash, phase-handoff)
│   ├── rules/
│   │   └── AGENTS.md                              # Shared team engineering, verification & multi-agent rules
│   └── skills/
│       ├── codebase-explorer/SKILL.md             # Skill: fast read-only search & file mapping
│       ├── frontend-dev/SKILL.md                  # Skill: token-efficient frontend development
│       ├── backend-dev/SKILL.md                   # Skill: token-efficient backend development
│       ├── token-efficient-agents/SKILL.md        # Skill: model selection, workspace isolation & verification
│       ├── neon-orchestrator/                     # Skill: greenfield + parallel process & coordination layer
│       │   ├── SKILL.md
│       │   └── references/subagent-templates.md
│       ├── phase-handoff/SKILL.md                 # Skill: update PROGRESS.md, TASKS.md & AGENTS.md after phases
│       ├── project-bootstrap/SKILL.md             # Skill: bootstrap greenfield or existing repos
│       └── framework-contribute/SKILL.md          # Skill: add/update framework agents, skills, rules, hooks
└── template/                                      # Starter kit copied into target projects by project-bootstrap
    ├── AGENTS.md
    └── .agents/
        ├── hooks.json                             # Optional disabled PostToolUse + Stop phase-handoff reminder
        └── skills/
            └── example-workflow/SKILL.md
```

---

## Using This Framework in Another Project

### Option 1: Install Directly into One Project from GitHub (Recommended)
Run from the root of `<your-project>` to install `.agents/` (`agents/`, `rules/`, `skills/`) for **that project only**:

**PowerShell (Windows):**
```powershell
git clone --depth 1 https://github.com/Matchewmau/agy-supost.git _tmp_agy
Copy-Item -Recurse -Force _tmp_agy/.agents .agents
if (!(Test-Path AGENTS.md)) { Copy-Item _tmp_agy/template/AGENTS.md AGENTS.md }
Remove-Item -Recurse -Force _tmp_agy
```

**Bash (macOS / Linux):**
```bash
git clone --depth 1 https://github.com/Matchewmau/agy-supost.git _tmp_agy && \
cp -r _tmp_agy/.agents .agents && \
[ -f AGENTS.md ] || cp _tmp_agy/template/AGENTS.md AGENTS.md && \
rm -rf _tmp_agy
```
*(After copying, fill in `<your-project>/AGENTS.md` with your real build/lint/test commands—or ask the agent to run `project-bootstrap`.)*

### Option 2: Link via Git Submodule (Stay Synced with `main` Per Project)
1. Add this repo as a submodule:
   ```bash
   git submodule add https://github.com/Matchewmau/agy-supost.git .agents/vendor/agy-supost
   ```
2. Copy or symlink `.agents/agents/` and `.agents/rules/`, and register skills in `<your-project>/.agents/skills.json`:
   ```json
   {
     "skills": [
       "./vendor/agy-supost/.agents/skills"
     ]
   }
   ```
3. Pull updates anytime with:
   ```bash
   git submodule update --remote .agents/vendor/agy-supost
   ```

### Option 3: Install Globally (Applies to All Projects)
Copy `.agents/agents/`, `.agents/rules/`, and `.agents/skills/` into `~/.gemini/config/`.

### Option 4: Bootstrap a Greenfield or Existing Project with the Agent
Open this repo (or install `.agents/` first) and prompt:
> *"Use the `project-bootstrap` skill to set up `<path-to-project>`."*

---

## Improving the Framework

See [CONTRIBUTING.md](./CONTRIBUTING.md) (or use the `framework-contribute` skill) to add new custom subagents, refine team rules, or contribute skills and hooks.
