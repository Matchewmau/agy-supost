---
name: frontend-dev
description: >-
  Use this skill when building, editing, or debugging frontend UI components,
  styling, client-side state, routing, or frontend tests.
---

# Frontend Development (Token-Efficient)

Follow this workflow for UI, styling, state, and client-side tasks while minimizing token spend.

## Steps

1. **Locate Only Relevant Files**:
   - Search for the target component, route, or style file first (`rg -n` / `grep`).
   - Read only the relevant component and its direct types/hooks (avoid reading unrelated pages or `node_modules`).
2. **Implement Cleanly**:
   - Reuse existing design-system components, utilities, and state patterns in the repo.
   - Keep components small, typed, and accessible; avoid duplicating styles or markup.
3. **Verify with Targeted Checks**:
   - Run the narrowest check first (e.g., single test file or typecheck/lint on changed files).
   - Only run the full frontend build after all edits are complete.
4. **Concise Handoff (if running as a subagent)**:
   - Return only: modified file paths, props/state/route changes, and exact test/build output.
