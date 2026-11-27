"""Offline scenario model. Run with Python 3.9+ from any directory."""

import argparse
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Step:
    model: str
    inputs: int
    outputs: int
    tool_seconds: int = 0

    def seconds(self):
        # Assumed output tokens/s. Input processing is folded into fixed latency.
        speed = {"Neon": 45, "Hydrogen": 90, "flash": 90, "flash_lite": 100}
        return 2 + self.outputs / speed[self.model] + self.tool_seconds


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / ".agents" / "skills"


def prompt_size(path):
    return (len(path.read_text(encoding="utf-8")) + 3) // 4


def role_prompt(role, skill=None):
    size = prompt_size(ROOT / ".agents" / "agents" / (role + ".md"))
    if skill:
        size += prompt_size(SKILLS / skill / "SKILL.md")
    return size


# Work per slice (input, output, tool seconds), common to every route.
UI = ("frontend-builder", "frontend-dev", 5000, 1400, 55)
API = ("backend-builder", "backend-dev", 6000, 1800, 65)
FIX = ("backend-builder", "backend-dev", 2200, 550, 20)
DOC = ("doc-writer", "phase-handoff", 1300, 250, 5)
CASES = [
    ("Small fix", [FIX], False),
    ("Independent UI + API", [UI, API], True),
    ("API then UI", [API, UI], False),
    ("Eight independent doc edits", [DOC] * 8, True),
]


def stages(strategy, slices, independent):
    overlay = strategy == "Neon skill"
    route = "native" if strategy == "Built-in" else "saved"
    if overlay:
        if len(slices) > 4:
            route = "workflow"
        elif not independent:
            route = "native"
    overhead = prompt_size(SKILLS / "neon-orchestrator" / "SKILL.md") if overlay else 0
    yield [Step("Neon", 2400 + overhead, 320)]
    native = route == "native"
    scout = "Hydrogen" if native else "flash"
    scout_prompt = role_prompt("explorer", "codebase-explorer") if route == "saved" else 0
    yield [Step(scout, 3000 + scout_prompt, 300, 10)]
    work = []
    for role, skill, inputs, outputs, seconds in slices:
        if native:
            work.append(Step("Hydrogen", inputs, outputs, seconds))
        elif route == "workflow":
            work.append(Step("flash_lite", inputs + 300, outputs + 80, seconds))
        else:
            model = "flash" if role == "doc-writer" else "Neon"
            work.append(Step(model, inputs + role_prompt(role, skill) + 300,
                             outputs + 80, seconds))
    if not native:
        yield [Step("Neon", 400 + 200 * len(work), 120 * len(work), 5)]
    width = 4 if independent and not native else 1
    for start in range(0, len(work), width):
        yield work[start:start + width]
    verify_prompt = role_prompt("verifier") if route == "saved" else 0
    yield [Step(scout, 2400 + verify_prompt, 300, 35)]
    yield [Step("Neon", 1200, 220)]
    docs_prompt = role_prompt("doc-writer", "phase-handoff") if route == "saved" else 0
    yield [Step(scout, 800 + docs_prompt, 180, 4)]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--detail", action="store_true", help="show tokens by model")
    args = parser.parse_args()
    # Invented sensitivity weights per 1k input/output. No provider rate implied.
    weights = {"Neon": (4, 20), "Hydrogen": (2, 10), "flash": (1, 5),
               "flash_lite": (0.5, 2.5)}
    print("| Workload | Strategy | Input | Output | Seconds | Weighted units |")
    print("|---|---|---:|---:|---:|---:|")
    for name, slices, independent in CASES:
        for strategy in ("Built-in", "Saved agents", "Neon skill"):
            rounds = list(stages(strategy, slices, independent))
            inputs, outputs = Counter(), Counter()
            for batch in rounds:
                for step in batch:
                    inputs[step.model] += step.inputs
                    outputs[step.model] += step.outputs
            elapsed = sum(max(step.seconds() for step in batch) for batch in rounds)
            units = sum((inputs[m] * weights[m][0] + outputs[m] * weights[m][1])
                        / 1000 for m in inputs)
            print(f"| {name} | {strategy} | {sum(inputs.values())} | {sum(outputs.values())}"
                  f" | {elapsed:.0f} | {units:.1f} |")
            if args.detail:
                print("  " + ", ".join(f"{m} {inputs[m]} in/{outputs[m]} out" for m in inputs))


if __name__ == "__main__":
    main()
