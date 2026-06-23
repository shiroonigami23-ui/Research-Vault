# Benchmark Summary

## Entropy by Condition

| Condition | Mean Entropy | Count |
| --- | ---: | ---: |
| control_coherent | N/A | 3 |
| mild_tension | N/A | 3 |
| explicit_contradiction | N/A | 3 |
| deep_contradiction | N/A | 3 |

## Notes

- `dry-run` mode validates the benchmark pipeline without model inference.
- `hf` mode computes token entropy from generation scores for local Hugging Face causal LMs.
- This script is a first-pass scaffold; semantic entropy and hidden-state variance should be added in later iterations.