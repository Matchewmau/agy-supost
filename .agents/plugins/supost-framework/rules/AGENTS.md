# SUpost Team Shared Rules

These rules apply whenever the `supost-framework` plugin is enabled.

## Engineering & Agent Standards
- **Inspect Before Editing**: Read the relevant files and understand existing patterns before proposing or applying changes.
- **Verify After Changes**: Run the project's build, lint, or test command after your final edit and report only observed results.
- **Minimal, Focused Diffs**: Keep changes scoped to the task; preserve unrelated comments, docstrings, and formatting.
- **No Secrets in Config**: Never commit API keys, tokens, or machine-local credentials into `AGENTS.md`, skills, hooks, or `mcp_config.json`.
