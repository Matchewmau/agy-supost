---
name: backend-dev
description: >-
  Use this skill when building, editing, or debugging backend APIs, routes,
  services, database schemas/migrations, auth, or backend tests.
---

# Backend Development (Token-Efficient)

Follow this workflow for server, API, database, and integration tasks while minimizing token spend.

## Steps

1. **Locate Only Relevant Files**:
   - Search for the target route/controller, service, and schema/model first.
   - Read only the relevant handler, validator, and data-access layer—avoid scanning unrelated modules.
2. **Implement Safely**:
   - Validate inputs at boundaries, handle errors explicitly, and reuse existing DB/auth helpers.
   - Never hardcode secrets or log sensitive credentials/tokens.
3. **Verify with Targeted Checks**:
   - Run the specific test file or endpoint test while iterating (e.g., `pytest tests/test_users.py`).
   - Run lint/typecheck and the relevant test suite after the final edit.
4. **Concise Handoff (if running as a subagent)**:
   - Return only: modified file paths, endpoint/schema changes, and exact test results.
