import argparse
import csv
import json
import math
import statistics
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional


ROOT = Path(__file__).resolve().parent
BENCHMARK_PATH = ROOT / "benchmark_suite.json"
OUTPUT_DIR = ROOT / "results"


@dataclass
class BenchmarkResult:
    prompt_id: str
    condition: str
    contradiction_depth: int
    run_index: int
    provider: str
    model: str
    output_text: str
    avg_token_entropy: Optional[float]
    token_count: int


def load_benchmark() -> List[Dict]:
    with BENCHMARK_PATH.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def ensure_results_dir() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)


def entropy_from_probs(probabilities: List[float]) -> float:
    return -sum(p * math.log(p) for p in probabilities if p > 0)


def dry_run_generate(prompt: str) -> str:
    return f"[DRY_RUN] {prompt}"


def try_hf_generate(prompt: str, model_name: str, max_new_tokens: int) -> Dict:
    try:
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer
    except ImportError as exc:
        raise RuntimeError(
            "transformers and torch are required for --provider hf"
        ) from exc

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token_id = tokenizer.eos_token_id

    inputs = tokenizer(prompt, return_tensors="pt")
    with torch.no_grad():
        generated = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=False,
            return_dict_in_generate=True,
            output_scores=True,
            pad_token_id=tokenizer.pad_token_id,
        )

    generated_tokens = generated.sequences[0][inputs["input_ids"].shape[1]:]
    output_text = tokenizer.decode(generated_tokens, skip_special_tokens=True).strip()

    step_entropies: List[float] = []
    for score in generated.scores:
        probs = torch.softmax(score[0], dim=-1)
        step_entropies.append(float(entropy_from_probs(probs.tolist())))

    avg_entropy = statistics.mean(step_entropies) if step_entropies else None
    return {
        "output_text": output_text,
        "avg_token_entropy": avg_entropy,
        "token_count": int(generated_tokens.shape[0]),
    }


def run(provider: str, model_name: str, repeats: int, max_new_tokens: int) -> List[BenchmarkResult]:
    benchmark = load_benchmark()
    results: List[BenchmarkResult] = []

    for item in benchmark:
        for run_index in range(repeats):
            if provider == "dry-run":
                output_text = dry_run_generate(item["prompt"])
                avg_entropy = None
                token_count = 0
            elif provider == "hf":
                generated = try_hf_generate(
                    prompt=item["prompt"],
                    model_name=model_name,
                    max_new_tokens=max_new_tokens,
                )
                output_text = generated["output_text"]
                avg_entropy = generated["avg_token_entropy"]
                token_count = generated["token_count"]
            else:
                raise ValueError(f"Unsupported provider: {provider}")

            results.append(
                BenchmarkResult(
                    prompt_id=item["id"],
                    condition=item["condition"],
                    contradiction_depth=item["contradiction_depth"],
                    run_index=run_index,
                    provider=provider,
                    model=model_name,
                    output_text=output_text,
                    avg_token_entropy=avg_entropy,
                    token_count=token_count,
                )
            )
    return results


def write_results(results: List[BenchmarkResult]) -> Path:
    ensure_results_dir()
    output_path = OUTPUT_DIR / "benchmark_results.csv"
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            [
                "prompt_id",
                "condition",
                "contradiction_depth",
                "run_index",
                "provider",
                "model",
                "avg_token_entropy",
                "token_count",
                "output_text",
            ]
        )
        for result in results:
            writer.writerow(
                [
                    result.prompt_id,
                    result.condition,
                    result.contradiction_depth,
                    result.run_index,
                    result.provider,
                    result.model,
                    result.avg_token_entropy,
                    result.token_count,
                    result.output_text,
                ]
            )
    return output_path


def write_summary(results: List[BenchmarkResult]) -> Path:
    ensure_results_dir()
    output_path = OUTPUT_DIR / "benchmark_summary.md"
    grouped: Dict[str, List[Optional[float]]] = {}
    for result in results:
        grouped.setdefault(result.condition, []).append(result.avg_token_entropy)

    lines = [
        "# Benchmark Summary",
        "",
        "## Entropy by Condition",
        "",
        "| Condition | Mean Entropy | Count |",
        "| --- | ---: | ---: |",
    ]

    for condition, values in grouped.items():
        numeric = [value for value in values if value is not None]
        mean_value = f"{statistics.mean(numeric):.4f}" if numeric else "N/A"
        lines.append(f"| {condition} | {mean_value} | {len(values)} |")

    lines.extend(
        [
            "",
            "## Notes",
            "",
            "- `dry-run` mode validates the benchmark pipeline without model inference.",
            "- `hf` mode computes token entropy from generation scores for local Hugging Face causal LMs.",
            "- This script is a first-pass scaffold; semantic entropy and hidden-state variance should be added in later iterations.",
        ]
    )
    output_path.write_text("\n".join(lines), encoding="utf-8")
    return output_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Hollow Purple benchmark.")
    parser.add_argument("--provider", default="dry-run", choices=["dry-run", "hf"])
    parser.add_argument("--model", default="gpt2")
    parser.add_argument("--repeats", type=int, default=2)
    parser.add_argument("--max-new-tokens", type=int, default=64)
    args = parser.parse_args()

    results = run(
        provider=args.provider,
        model_name=args.model,
        repeats=args.repeats,
        max_new_tokens=args.max_new_tokens,
    )
    csv_path = write_results(results)
    summary_path = write_summary(results)
    print(f"Wrote {csv_path}")
    print(f"Wrote {summary_path}")


if __name__ == "__main__":
    main()
