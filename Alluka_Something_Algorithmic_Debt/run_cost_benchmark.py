import csv
import json
import math
from pathlib import Path
from typing import Dict, List


ROOT = Path(__file__).resolve().parent
TASK_PATH = ROOT / "task_suite.json"
RESULTS_DIR = ROOT / "results"


ALPHA = 1.0
BETA = 1.4
GAMMA = 1.6
DELTA = 1.8
EPSILON = 2.0
ZETA = 0.9
ETA = 0.5


def load_tasks() -> List[Dict]:
    return json.loads(TASK_PATH.read_text(encoding="utf-8"))


def ensure_results_dir() -> None:
    RESULTS_DIR.mkdir(exist_ok=True)


def direct_inference(task: Dict) -> float:
    return ALPHA * math.log(1 + task["prompt_tokens"]) + BETA * task["reasoning_depth"]


def orchestration_cost(task: Dict) -> float:
    return GAMMA * task["tool_steps"] + DELTA * task["verification_steps"]


def safety_overhead(task: Dict) -> float:
    return EPSILON * task["safety_sensitivity"] + ZETA * task["reasoning_depth"] * task["safety_sensitivity"]


def algorithmic_debt(task: Dict) -> float:
    return (
        direct_inference(task)
        + orchestration_cost(task)
        + safety_overhead(task)
        + ETA * task["tool_steps"] * task["verification_steps"]
    )


def normalized_debt(task: Dict) -> float:
    return algorithmic_debt(task) / math.log(2 + task["prompt_tokens"])


def write_results(tasks: List[Dict]) -> Path:
    ensure_results_dir()
    path = RESULTS_DIR / "cost_benchmark_results.csv"
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            [
                "id",
                "task_family",
                "prompt_tokens",
                "reasoning_depth",
                "tool_steps",
                "verification_steps",
                "safety_sensitivity",
                "direct_inference",
                "orchestration_cost",
                "safety_overhead",
                "algorithmic_debt",
                "normalized_debt",
            ]
        )
        for task in tasks:
            writer.writerow(
                [
                    task["id"],
                    task["task_family"],
                    task["prompt_tokens"],
                    task["reasoning_depth"],
                    task["tool_steps"],
                    task["verification_steps"],
                    task["safety_sensitivity"],
                    round(direct_inference(task), 4),
                    round(orchestration_cost(task), 4),
                    round(safety_overhead(task), 4),
                    round(algorithmic_debt(task), 4),
                    round(normalized_debt(task), 4),
                ]
            )
    return path


def write_summary(tasks: List[Dict]) -> Path:
    ensure_results_dir()
    ranked = sorted(tasks, key=algorithmic_debt, reverse=True)
    path = RESULTS_DIR / "cost_benchmark_summary.md"
    lines = [
        "# Cost Benchmark Summary",
        "",
        "| Task | Debt | Normalized Debt |",
        "| --- | ---: | ---: |",
    ]
    for task in ranked:
        lines.append(
            f"| {task['task_family']} | {algorithmic_debt(task):.3f} | {normalized_debt(task):.3f} |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- Debt includes direct inference, orchestration, safety, and interaction costs.",
            "- Normalized debt helps show whether burden grows beyond prompt length alone.",
            "- This benchmark is a mathematical scaffold for later real logging against actual workflows.",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def main() -> None:
    tasks = load_tasks()
    csv_path = write_results(tasks)
    summary_path = write_summary(tasks)
    print(f"Wrote {csv_path}")
    print(f"Wrote {summary_path}")


if __name__ == "__main__":
    main()
