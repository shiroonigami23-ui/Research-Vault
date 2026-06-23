# Contract Benchmark Summary

| System | Accuracy | Attack Success Rate | Deny Precision | Deny Recall |
| --- | ---: | ---: | ---: | ---: |
| Baseline | 0.333 | 1.000 | 0.000 | 0.000 |
| Contract | 1.000 | 0.000 | 1.000 | 1.000 |

## Interpretation

- Baseline simulates prompt-only behavior with no external enforcement.
- Contract simulates a simple external rule evaluator over attack features.
- This is a first empirical scaffold, not a final proof of robust safety.