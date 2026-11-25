# SUpost Team Shared Rules

These rules apply whenever `.agents/rules/AGENTS.md` is present in a workspace.

## Engineering & Code Integrity
- **Quality First**: Never compromise correctness, security, or maintainability to save tokens. Use higher-capability models and effort for complex, security-sensitive, or architectural work.
- **Inspect Before Editing**: Read the relevant files/line ranges before proposing or applying changes.
- **Verify After Changes**: Run targeted tests while iterating and the relevant build/lint/test check after your final edit; report only observed results.
- **Minimal, Focused Diffs**: Keep changes scoped to the task; preserve unrelated comments, docstrings, and formatting.
- **No Secrets in Config**: Never commit API keys, tokens, or machine-local credentials into `AGENTS.md`, skills, hooks, or `mcp_config.json`.

## Context & Budget Hygiene
- **Keep Rules Lean**: Put detailed workflows in `.agents/skills/` (progressive disclosure) rather than expanding `AGENTS.md`.
- **Right-Size Subagents**: Use `flash`/`flash_lite` for read-only codebase exploration, and balanced/high models (`inherit`/`pro`) for implementation and debugging.
- **Concise Handoffs**: Ask subagents to return exact file paths, line numbers, and verified test results.
