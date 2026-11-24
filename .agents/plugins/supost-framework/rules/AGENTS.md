# SUpost Team Shared Rules

These rules apply whenever the `supost-framework` plugin is enabled.

## Engineering & Agent Standards
- **Inspect Before Editing**: Read only the relevant files/line ranges before proposing or applying changes.
- **Verify After Changes**: Run targeted tests while iterating and the relevant build/lint/test check after your final edit; report only observed results.
- **Minimal, Focused Diffs**: Keep changes scoped to the task; preserve unrelated comments, docstrings, and formatting.
- **No Secrets in Config**: Never commit API keys, tokens, or machine-local credentials into `AGENTS.md`, skills, hooks, or `mcp_config.json`.

## Token & Cost Efficiency
- **Keep Rules Lean**: Put detailed workflows in `.agents/skills/` (progressive disclosure) rather than expanding `AGENTS.md`.
- **Tier Subagents**: Use `flash_lite`/`flash` subagents for codebase exploration and routine frontend/backend implementation; reserve heavier models for planning and complex debugging.
- **Stay Concise**: Ask subagents to return exact file paths, line numbers, and test results instead of verbose summaries.
