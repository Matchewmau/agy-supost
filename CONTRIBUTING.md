# Contributing to the SUpost Antigravity Framework

Team members are encouraged to improve this framework whenever you discover a better workflow, catch a recurring agent mistake, or build a reusable skill.

---

## What Goes Where?

| What you want to add | Where to put it | When it loads |
| :--- | :--- | :--- |
| **Team-wide coding/agent rules** | `.agents/rules/AGENTS.md` | Always on in workspace |
| **Reusable step-by-step workflow** | `.agents/skills/<skill-name>/SKILL.md` | On demand (progressive disclosure) |
| **Project starter boilerplate** | `template/` | Copied into new projects |
| **Ecosystem / usage docs** | `ANTIGRAVITY_ECOSYSTEM_GUIDE.md` or `README.md` | Reference documentation |

---

## Adding a New Skill

1. Create a folder under `.agents/skills/<skill-name>/` (lowercase, hyphenated).
2. Add `SKILL.md` with required YAML frontmatter:
   ```markdown
   ---
   name: <skill-name>
   description: >-
     Clear third-person description of what this skill does and when the agent should use it.
   ---
   ```
3. Keep `SKILL.md` concise. Put long manuals in `references/`, helper scripts in `scripts/`, and sample files in `examples/`.
4. Include a **Verification** section telling the agent how to confirm the workflow succeeded.

---

## Updating Rules (`AGENTS.md`)

- Keep rules actionable and non-redundant (don't repeat general coding advice the model already knows).
- Remember Antigravity limits:
  - **24,000 bytes** max per rule file.
  - **20,000 tokens** shared aggregate budget across all always-on rules.
- If a rule is only needed for a specific task, turn it into a **Skill** instead.

---

## Testing Your Changes

Before committing improvements:
1. Open `D:\agy-supost` in **Antigravity CLI (`agy`)**, **Antigravity IDE**, or **Antigravity App**.
2. Verify your skill is discovered and triggers cleanly from a natural prompt.
3. If you modified `template/`, test copying it to a sample directory and confirm no broken relative links or machine-specific paths exist.
