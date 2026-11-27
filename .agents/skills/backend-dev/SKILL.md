---
name: backend-dev
description: Guides implementation and verification of APIs, authentication, services and database changes.
---
# Implement

Start at supplied handlers and tests. Trace affected callers, validators and data access. Reuse existing auth and database helpers, validate inputs at boundaries, handle errors and protect credentials. Preserve supported clients and existing data.

## Verification

Exercise the changed contract, failure paths and relevant migration or retry behavior with targeted tests. The integration owner runs required final lint, typecheck, build and tests on the integrated revision.
