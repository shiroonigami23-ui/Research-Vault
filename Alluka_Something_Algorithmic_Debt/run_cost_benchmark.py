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
GAMMA = 1.2
DELTA = 1.8
EPSILON = 2.0
ZETA = 1.1
ETA = 0.5


def load_tasks() -> List[Dict]:
    return json.loads(TASK_PATH.read_text(encoding="utf-8"))


def ensure_results_dir() -> None:
    RESULTS_DIR.mkdir(exist_ok=True)


def wish_complexity(task: Dict) -> float:
    return (
        ALPHA * math.log(1 + task["wish_length"])
        + BETA * task["reasoning_depth"]
        + GAMMA * task["conceptual_breadth"]
        + DELTA * task["safety_sensitivity"]
    )


def request_cost(task: Dict) -> float:
    return (
        EPSILON * task["expected_request_count"]
        + ZETA * task["request_strictness"]
        + ETA * task["expected_request_count"] * task["request_strictness"]
    )


def algorithmic_debt(task: Dict) -> float:
    return wish_complexity(task) + request_cost(task)


def normalized_debt(task: Dict) -> float:
    return algorithmic_debt(task) / math.log(2 + task["wish_length"])


def write_results(tasks: List[Dict]) -> Path:
    ensure_results_dir()
    path = RESULTS_DIR / "cost_benchmark_results.csv"
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            [
                "id",
                "task_family",
                "wish_length",
                "reasoning_depth",
                "conceptual_breadth",
                "safety_sensitivity",
                "expected_request_count",
                "request_strictness",
                "wish_complexity",
                "request_cost",
                "algorithmic_debt",
                "normalized_debt",
            ]
        )
        for task in tasks:
            writer.writerow(
                [
                    task["id"],
                    task["task_family"],
                    task["wish_length"],
                    task["reasoning_depth"],
                    task["conceptual_breadth"],
                    task["safety_sensitivity"],
                    task["expected_request_count"],
                    task["request_strictness"],
                    round(wish_complexity(task), 4),
                    round(request_cost(task), 4),
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
        "| Task | Wish Complexity | Request Cost | Debt | Normalized Debt |",
        "| --- | ---: | ---: | ---: | ---: |",
    ]
    for task in ranked:
        lines.append(
            f"| {task['task_family']} | {wish_complexity(task):.3f} | {request_cost(task):.3f} | {algorithmic_debt(task):.3f} | {normalized_debt(task):.3f} |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- Wish complexity is the main input-side variable.",
            "- Request cost models the burden of the compensating requests that follow the wish.",
            "- Normalized debt tests whether burden grows beyond wish length alone.",
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
