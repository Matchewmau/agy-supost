---
name: token-efficient-agents
description: Selects execution modes and model tiers for coding tasks with token, latency and verification constraints.
---
# Budget by accepted change

Use the built-in Orchestrator for sequential work. Use saved builders for independent work with stable interfaces and separate workspaces. For a larger mechanical batch, use a structured workflow. See [Neon routing](../neon-orchestrator/SKILL.md) when coordinating a build.

Saved agents accept `inherit`, `flash`, or `pro`. Confirm the resolved parent for inherited builders. Use flash for scouting, verification and mechanically checkable edits. Use inherit or pro for domain logic, ambiguous failures and sensitive changes. Reserve flash_lite for workflow workers.

Pass paths, symbols and checks. Reuse the worker holding the relevant context. Return commands, outcomes and the decisive error excerpt. Escalate a repeated failure after two attempts.

## Verification

Compare tokens and elapsed time through accepted changes, including review, integration and retries. Track defects and failed checks alongside savings.
