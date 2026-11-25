---
name: codebase-explorer
description: >-
  Use this skill when searching a codebase, mapping architecture, or locating
  symbols/files before making edits, especially in the read-only explorer custom agent or a flash subagent.
---

# Codebase Explorer (Token-Efficient)

Quickly locate exact files, symbols, and call sites without bloating the main agent's context window.

## Steps

1. **Search Before Reading**:
   - Use fast text/file search (`rg -n`, `Get-ChildItem`, or grep) to find definitions and call sites.
   - Read only the specific line ranges needed (under ~150 lines per read).
2. **Return a Compact Map**:
   - Do not paste entire files back to the caller.
   - Report only:
     - Exact file paths and line ranges
     - Key symbol names, signatures, and data flow
     - Build/test commands observed in config files
