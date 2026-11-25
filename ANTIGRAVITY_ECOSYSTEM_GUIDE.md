# Antigravity Ecosystem Guide: App, IDE, CLI & Agent Building

A practical reference for using **Antigravity App (2.0)**, **Antigravity IDE**, and **Antigravity CLI (`agy`)** together for fast, structured software development and custom agent workflows.

---

## 1. Your Installed Setup

All three surfaces are already installed and available on your `PATH`:

| Surface | Version | Command / Executable | Primary Role |
| :--- | :--- | :--- | :--- |
| **Antigravity App (2.0)** | `2.35.1` | `antigravity` (`D:\Antigravity\bin\antigravity.cmd`) | Parallel orchestration, multi-project management, scheduled tasks, policy controls |
| **Antigravity IDE** | `2.8.0` | `antigravity-ide` (`C:\Users\Admin\AppData\Local\Programs\Antigravity IDE\bin\antigravity-ide.cmd`) | Active coding, inline edits, autocomplete, visual diffs, diagnostic auto-fix |
| **Antigravity CLI** | `1.5.16` | `agy` (`C:\Users\Admin\AppData\Local\agy\bin\agy.exe`) | Fast terminal-native agent sessions, quick runs, plugin management |

### Shared Configuration Locations
- **Global config**: `C:\Users\Admin\.gemini\config\` (`config.json`, `mcp_config.json`, `plugins/`, `projects/`, `sidecars/`) — applies across all workspaces.
- **CLI settings**: `C:\Users\Admin\.gemini\antigravity-cli\settings.json`.
- **Project-scoped customizations**: `<project-root>\.agents\` + `AGENTS.md` / `GEMINI.md` — shared automatically across the App, IDE, and CLI when you open the same folder.

---

## 2. Using the Ecosystem Together Efficiently

Instead of treating the App, IDE, and CLI as separate tools, route each kind of work to the surface built for it:

1. **Plan & Orchestrate in the Antigravity App (`antigravity`)**
   - Manage multiple workspaces under **Projects** in the left sidebar.
   - Run long-running tasks, **Scheduled Tasks** (recurring cron jobs or one-time timers), and parallel agent sessions without blocking your editor.
   - Use **Settings** to set global and per-project guardrails (execution policy, terminal sandbox, file/network access).
   - Drag-and-drop screenshots/media and use `@` mentions (files, folders, previous conversations, terminal sessions, rules, MCP tools).

2. **Build & Refine in Antigravity IDE (`antigravity-ide <folder>`)**
   - **Antigravity Tab (Passive)**: Context-aware **Autocomplete**, **Supercomplete** (multi-line diff suggestions), **Tab-to-Jump** (predicts your next cursor location), and **Tab-to-Import** (auto-adds missing imports). Accept with `Tab`, cancel with `Esc`, or accept word-by-word with `Ctrl+→`.
   - **Inline Command (`Ctrl+I`) (Targeted)**: Highlight a block to refactor, document, or fix it in place—or invoke with no selection to generate code at the cursor.
   - **Sidebar Chat & Agent / Planning Mode (Collaborative)**: Multi-file edits, terminal builds/tests, **Inline Code Lenses** above symbols, **Visual Diff Overlays**, and **Diagnostic Auto-Fix** directly from compiler/lint errors.

3. **Move Fast in the Terminal with `agy`**
   - Run `agy` inside any project directory for lightweight terminal sessions without launching a full GUI.
   - Run `agy --help` for CLI flags and subcommands, or type `/help` inside `agy` to view TUI slash commands.
   - Exit with `Ctrl+D Ctrl+D`, `/exit`, or `/quit`.

### Recommended Daily Loop
1. **Align & Plan**: Open the project in **Antigravity App** (or IDE Sidebar) and use `/plan` or `/grill-me` to lock down architecture and edge cases.
2. **Implement**: Open the repo with `antigravity-ide .` and use **Tab**, **`Ctrl+I`**, and **Visual Diff Overlays** for tight, high-speed coding.
3. **Verify & Automate**: Use **`agy`** in your terminal for quick test/debug loops, and **Antigravity App** for background **Scheduled Tasks** or multi-agent swarms.

---

## 3. Built-In Features for Building Projects

### High-Leverage Slash Commands
Type `/` in the chat canvas to trigger specialized workflows:
- `/plan` — Create a step-by-step plan before making edits on complex tasks.
- `/grill-me` — Run an interactive Q&A interview to resolve design decisions early.
- `/goal` — Extra-thorough, long-running execution until the objective is fully met.
- `/teamwork` — Coordinate multiple autonomous agents on large projects.
- `/boost` — Deep thinking, multi-perspective planning, and rigorous verification for hard coding/research problems.
- `/schedule` — Set up recurring cron jobs or one-time timers.
- `/browser` — Web browsing, testing, and interacting with web apps.
- `/compact` — Summarize and free up context in long sessions.
- `/learn` — Persist corrections or complex setups so future sessions follow them.

### Multi-Agent & Orchestration Options
Pick the simplest built-in mechanism that fits the shape of the work:
- **Built-in `Orchestrator` Model (`agy --model "Orchestrator (Neon)"` or `/model`)**: Best for **single-thread tasks**. A strong planner (Neon by default, or Carbon / Argon / Opus 5.5 on Pro/Ultra; Carbon + Hydrogen on Enterprise) directs a faster executor (Hydrogen / Sonnet 5.5) automatically in one conversation with zero setup.
- **Custom Subagents (`.agents/agents/<name>.md` + `invoke_subagent`)**: Best for **2–4 parallel slices** or isolated scouting/verification. Subagents accept `model` (`inherit`, `flash`, or `pro`) and `workspace` (`inherit`, `share` for separate working copy, or `branch` for isolated clone). Pair with the `neon-orchestrator` skill for greenfield setup (`PLAN.md` / `TASKS.md`), workspace isolation, independent diff/test verification (`verifier`), and Git checkpoints.
- **Dynamic Python Workflows (`run_workflow`)**: Best for **fan-outs >4 items** or staged pipelines (`parallel`, `pipeline`, `phase`) where every agent (`flash_lite`, `flash`, `pro`, `inherit`) returns a JSON-schema-validated result.
- **Swarms (`/swarm`)**: User-invoked shared message board with named workers and dedicated verifiers for broad parallel tasks (available on all plans).
- **Teamwork (`/teamwork`)**: Multi-milestone, long-horizon autonomous teams with scoping interviews, persistent project directories, and critic/auditor gates (paid plans).
- **Boost (`/boost`)**: Multi-round deep reasoning and adversarial verification when a problem is hard rather than broad (paid plans).

### Safety, Permissions & Sandboxing
Configure these globally or per-project in **Antigravity App → Settings**:
- **Tool Execution Policy**: `always-proceed`, `request-review`, `strict`, or `proceed-in-sandbox`.
- **Terminal Sandbox**: Isolates agent shell commands.
- **File & Internet Access Policies**: `allow`, `ask`, or `deny` for non-workspace files and network requests.
- **Allowlists / Denylists**: Explicitly permit or block specific terminal commands and browser domains (`browserAllowlist.txt`).

---

## 4. Features for Building Custom Agents & Team Workflows

Antigravity discovers customizations automatically from your project (`.agents/` walking up to the Git root) and globally (`~/.gemini/config/`). Project-level rules override global defaults.

| Feature | Location | Purpose |
| :--- | :--- | :--- |
| **Rules** | `AGENTS.md`, `GEMINI.md`, `.agents/rules/*.md` | Always-on coding standards, architecture constraints, and repo conventions. (Capped at 24,000 bytes/file; 20,000-token aggregate rules budget.) |
| **Custom Agents** | `.agents/agents/<name>.md` | Saved specialist subagents (`explorer`, `frontend-builder`, `backend-builder`, `verifier`) with explicit `tools`, `model` (`inherit`/`flash`/`pro`), `skills`, and `commandExecutionPolicy`. Discovered in App, IDE, and `agy` (`/agents`). |
| **Skills** | `.agents/skills/<name>/SKILL.md` | On-demand runbooks loaded via **progressive disclosure** (only `name` & `description` are in context until triggered). Can include `scripts/`, `references/`, `examples/`, and `resources/`. |
| **Plugins** | `.agents/plugins/<name>/plugin.json` | Shareable bundles packaging `skills/`, `rules/AGENTS.md`, `hooks.json`, and `mcp_config.json` into one unit. |
| **Lifecycle Hooks** | `.agents/hooks.json` | Run shell commands on `SessionStart`, `PreToolUse`, `PostToolUse`, `PreInvocation`, `PostInvocation`, and `Stop` (e.g., auto-linting, formatting, safety gates). |
| **MCP Servers** | `~/.gemini/config/mcp_config.json` (or plugin `mcp_config.json`) | Connect local tools (**Stdio**: `command`, `args`, `env`) or remote services (**Streamable HTTP**: `url`) via the Model Context Protocol. |

### Programmatic Agents with the Python SDK
When you want to embed Antigravity agents inside scripts, CI pipelines, or custom apps:
```sh
pip install google-antigravity
```
```python
import asyncio
import sys
from google.antigravity import Agent, LocalAgentConfig, CapabilitiesConfig

async def main():
    config = LocalAgentConfig(
        system_instructions="You are an expert assistant for codebase navigation.",
        capabilities=CapabilitiesConfig(),  # Enables write/command tools (omit for read-only)
    )
    async with Agent(config) as agent:
        response = await agent.chat("Summarize the repository structure.")
        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()

asyncio.run(main())
```
You can also stream `response.thoughts` and `response.tool_calls`, or use `run_interactive_loop(agent)` for a terminal loop.

---

## 5. Recommended Workspace Blueprint

Organize project workspaces like this so the **App**, **IDE**, and **CLI** all discover rules, custom agents, and skills identically:

```text
<project-root>/
├── AGENTS.md                         # Project overview, conventions, verified build/test commands
├── PLAN.md                           # Architecture & milestones (for greenfield / multi-session builds)
├── TASKS.md                          # Slice checklist & Git checkpoints across sessions
└── .agents/
    ├── agents/                       # Saved custom subagents (explorer, frontend-builder, backend-builder, verifier)
    ├── rules/
    │   └── AGENTS.md                 # Shared team engineering & verification rules
    ├── skills/
    │   └── <workflow-name>/
    │       ├── SKILL.md              # Step-by-step runbook (YAML frontmatter: name, description)
    │       ├── scripts/              # Helper scripts for the agent to run
    │       └── references/           # Detailed docs loaded only when needed
    └── hooks.json                    # Optional: PreToolUse / PostToolUse linters or safety checks
```

### Official Documentation Index
- **Full Docs Sitemap**: `https://antigravity.google/llms.txt` (append `.md` to any docs URL for its Markdown version)
- **CLI Reference & Best Practices**: `https://antigravity.google/docs/cli/reference.md` | `https://antigravity.google/docs/cli/best-practices.md`
- **Customizations**: `https://antigravity.google/docs/skills.md` | `https://antigravity.google/docs/rules.md` | `https://antigravity.google/docs/hooks.md` | `https://antigravity.google/docs/plugins.md` | `https://antigravity.google/docs/mcp.md`
- **Permissions & Sandbox**: `https://antigravity.google/docs/permissions.md` | `https://antigravity.google/docs/sandbox.md`
