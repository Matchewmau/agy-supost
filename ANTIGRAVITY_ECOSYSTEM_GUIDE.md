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

### Multi-Agent & Workflow Patterns
- **Subagents (`invoke_subagent` / `define_subagent`)**: Delegate focused tasks (e.g., codebase research, isolated test debugging). Supports workspace modes: `inherit` (same workspace), `branch` (isolated clone), or `share` (shared repo, separate working copy).
- **Swarms**: Spawn named workers on a shared board for parallel implementation across independent modules or files.
- **Dynamic Python Workflows (`run_workflow`)**: Orchestrate `parallel`, `pipeline`, and `phase` agent fan-outs in Python when a task splits cleanly across many files, modules, or review angles.

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

## 5. Recommended Blueprint for `D:\agy-supost`

When you are ready to turn `D:\agy-supost` into a full project workspace, organize customizations like this so the **App**, **IDE**, and **CLI** all behave consistently:

```text
D:\agy-supost\
├── AGENTS.md                         # Project overview, conventions, build/test commands
└── .agents\
    ├── skills\
    │   └── <workflow-name>\
    │       ├── SKILL.md              # Step-by-step runbook (YAML frontmatter: name, description)
    │       ├── scripts\              # Helper scripts for the agent to run
    │       └── references\           # Detailed docs loaded only when needed
    ├── hooks.json                    # Optional: PreToolUse / PostToolUse linters or safety checks
    └── plugins\                      # Optional: Team-shareable bundles
```

### Official Documentation Index
- **Full Docs Sitemap**: `https://antigravity.google/llms.txt` (append `.md` to any docs URL for its Markdown version)
- **CLI Reference & Best Practices**: `https://antigravity.google/docs/cli/reference.md` | `https://antigravity.google/docs/cli/best-practices.md`
- **Customizations**: `https://antigravity.google/docs/skills.md` | `https://antigravity.google/docs/rules.md` | `https://antigravity.google/docs/hooks.md` | `https://antigravity.google/docs/plugins.md` | `https://antigravity.google/docs/mcp.md`
- **Permissions & Sandbox**: `https://antigravity.google/docs/permissions.md` | `https://antigravity.google/docs/sandbox.md`
