# SUpost Team Shared Rules

These rules apply whenever `.agents/rules/AGENTS.md` is present in a workspace.

## Engineering & Code Integrity
- **Quality First**: Never compromise correctness, security, or maintainability to save tokens. Use higher-capability models and effort for complex, security-sensitive, or architectural work.
- **Inspect Before Editing**: Read the relevant files/line ranges before proposing or applying changes.
- **Verify Real Diffs & Tests**: Inspect `git diff` and run targeted tests while iterating, then run the relevant build/lint/test suite after the final edit; never rely solely on a subagent's self-reported summary.
- **Minimal, Focused Diffs**: Keep changes scoped to the task; preserve unrelated comments, docstrings, and formatting.
- **No Secrets in Config**: Never commit API keys, tokens, or machine-local credentials into `AGENTS.md`, agents, skills, hooks, or `mcp_config.json`.

## Context & Multi-Agent Hygiene
- **Keep Rules Lean**: Put detailed workflows in `.agents/skills/` and reusable specialist roles in `.agents/agents/` rather than expanding `AGENTS.md`.
- **Right-Size Models**:
  - Single-thread work: Prefer the built-in **`Orchestrator`** model (e.g., `Orchestrator (Neon)`) when available so the planner delegates routine execution automatically.
  - Subagents (`invoke_subagent` accepts `inherit`, `flash`, or `pro`): Use `flash` for read-only exploration (`explorer`), independent test/diff checks (`verifier`), and strictly mechanical boilerplate; use `inherit` or `pro` for feature logic, UI state, APIs, DB migrations, auth, and debugging.
- **Isolate Parallel Edits**: When running 2+ builder subagents concurrently, set `workspace: "share"` or `"branch"` so builds, lockfiles, and test runs never collide.
- **Persist Multi-Session State**: Keep `PLAN.md` and `TASKS.md` updated at the repo root on multi-slice projects so fresh chat sessions resume without losing context.
