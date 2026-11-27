# SUpost orchestration benchmark

**Offline simulation, 27 November 2026.** On the independent UI/API workload, saved builders finish 38 seconds sooner than the built-in pair while consuming 3,595 more tokens. Give those same builders a dependency and they finish 52 seconds later than the built-in pair. Slice independence is the most consequential routing decision in these cases.

## What the three strategies execute

| Strategy | Routing used in the simulation | Evidence |
|---|---|---|
| Built-in Orchestrator | Gemini 4 Neon plans and reviews. Hydrogen scouts, implements, tests and records the handoff in one conversation. We model sequential execution. | Google documents automatic planner/executor handoffs. The personal paid CLI pairs the selected planner with Hydrogen. The App also offers executor selection. Enterprise uses Carbon/Hydrogen. [Models](https://antigravity.google/docs/models?app=antigravity), [Enterprise](https://antigravity.google/docs/enterprise) |
| Saved agents, dispatched directly | Standalone Neon leads. The frontend and backend builders inherit that parent. Explorer, verifier and doc-writer use the flash tier. Independent builders receive separate workspaces. | All five [agent definitions](../.agents/agents) declare these defaults. Google documents inherited and explicit subagent tiers and isolated sessions. [Custom subagents](https://antigravity.google/docs/subagents?app=cli) |
| SUpost Neon Orchestrator skill | Load the skill once. Route sequential work to built-in, the independent pair to saved agents, and eight independent edits to a dynamic workflow with lightweight workers. | The [skill](../.agents/skills/neon-orchestrator/SKILL.md) supplies routing, isolation, two-failure escalation, independent verification and checkpoints. Google supplies the execution mechanisms. [Dynamic workflows](https://antigravity.google/docs/dynamic-workflows) |

Two details affect interpretation. The repository mentions Sonnet as an executor alongside a CLI example. The App and CLI have different executor choices. Also, an inherited builder under a standalone Neon lead has a known parent. The repository itself calls for checking the resolved model when dispatching from an Orchestrator session. The simulation uses the standalone lead for its saved-agent route. A live comparison should record the resolved builder model.

## Simulated results

Each row represents one completed synthetic job. Seconds are critical-path wall time. Weighted units estimate relative model consumption under the illustrative weights below.

| Workload | Strategy | Input tokens | Output tokens | Seconds | Weighted units |
|---|---|---:|---:|---:|---:|
| Small fix | Built-in | 12000 | 1870 | 108 | 55.3 |
| Small fix | Saved agents | 14383 | 2070 | 125 | 65.2 |
| Small fix | Neon skill | 12482 | 1870 | 108 | 57.2 |
| Independent UI + API | Built-in | 20800 | 4520 | 239 | 99.4 |
| Independent UI + API | Saved agents | 23995 | 4920 | 201 | 160.6 |
| Independent UI + API | Neon skill | 24477 | 4920 | 201 | 162.5 |
| API then UI | Built-in | 20800 | 4520 | 239 | 99.4 |
| API then UI | Saved agents | 23995 | 4920 | 291 | 160.6 |
| API then UI | Neon skill | 21282 | 4520 | 239 | 101.3 |
| Eight independent doc edits | Built-in | 20200 | 3320 | 158 | 86.2 |
| Eight independent doc edits | Saved agents | 31691 | 4920 | 129 | 95.6 |
| Eight independent doc edits | Neon skill | 25082 | 4920 | 129 | 77.4 |

The leaner routing prompt costs an estimated 482 tokens, down from 2,010. On the independent UI/API case, the Neon route now uses 29,397 total tokens, down from 31,984. Holding the work stages fixed isolates the effect of smaller instructions. The simulator gives no speed or token credit for skipping optional scouts or batching milestone handoffs. For the independent UI/API pair, an extra 38 seconds of unmodeled integration or queue time would erase the parallel speedup.

## Assumptions and reproduction

Run `python benchmarks/orchestration.py` from the repository root to reproduce the table. Add `--detail` to see the input and output totals attributed to each model in each row. The runner uses the Python standard library and local prompt files.

- All strategies receive the same implementation workload and the same final diff/test and documentation workload. The saved route adds dispatch and worker summaries. The workflow uses eight small Markdown changes eligible for mechanical implementation. Each batch has up to four workers.
- Local prompt size is estimated as one token per four characters, rounded up per file. The skill adds approximately 482 input tokens at this revision. The simulator reads the actual files, so edits can change the results. Task context, generated tokens, tool times and speeds are assumed. The model counts one prompt load per modeled invocation and omits cache discounts, long-conversation replay and variable reasoning effort.
- Each stage takes two seconds of fixed latency plus tool time and output generation time. Assumed output speeds are 45 tokens/s for Neon, 90 for Hydrogen and flash, and 100 for flash_lite. Parallel batches take as long as their slowest worker. Input length has no separate latency term, which explains the equal times for two strategies that execute the same route.
- Costs use illustrative input/output weights per 1,000 tokens of 4/20 for Neon, 2/10 for Hydrogen, 1/5 for flash and 0.5/2.5 for flash_lite. These weights are editable in the runner. The flash labels identify routing tiers. Their deployed model versions require runtime inspection.
- The model assumes first-pass success, negligible merge cost and warm workspaces. It prices a single review and handoff, abstracts individual tool calls, and excludes checkpoint I/O. Correctness, defect detection and escalation frequency require real patches and test outcomes. No quality score is assigned.

## AI credits

This offline run consumed **zero Antigravity AI credits**. For a live personal Pro or Ultra run fully covered by baseline quota, the purchased-credit debit is also zero. Once eligible quota is exhausted, the balance and overage setting determine whether execution continues on credits. Google specifies standard Gemini Enterprise consumption pricing for overages. The weighted-unit column cannot be read as a predicted account debit. [Antigravity plans and overages](https://antigravity.google/docs/plans?hl=en)

For a measured follow-up, start each route from the same commit with the same task, acceptance tests, plan, effort and cache conditions. Record the resolved models, time until acceptance tests pass, model-level input/output/cache counts where exposed, retry and merge time, and credit balance before and after each isolated run. Record whether baseline quota covered any steps. Use repeated runs in varied order and report failures alongside median elapsed time and debit per successful task.
