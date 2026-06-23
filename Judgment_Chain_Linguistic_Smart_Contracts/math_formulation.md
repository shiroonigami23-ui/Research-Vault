# Mathematical Formulation

## Contract Model

Let:

- `q` be the query,
- `p` be the policy text,
- `z(q)` be a feature extractor over the query,
- `E(q, p)` be the external enforcement function,
- `d(q, p)` be the final decision in `{allow, deny}`.

Define:

`d(q, p) = E(z(q), p)`

The key claim is that reliable enforcement depends on `E`, not on prompt wording alone.

## Risk Score

Let the feature vector be:

`z(q) = [k(q), o(q), r(q), t(q)]`

where:

- `k(q)` = harmful keyword score,
- `o(q)` = override-attempt score,
- `r(q)` = roleplay/jailbreak score,
- `t(q)` = tool-abuse or secret-exfiltration score.

Define a linear risk score:

`s(q) = w_k k(q) + w_o o(q) + w_r r(q) + w_t t(q)`

and a threshold policy:

`E(z(q), p) = allow if s(q) < tau, else deny`

## Evaluation Metrics

Let:

- `TP` = malicious prompts correctly denied,
- `TN` = benign prompts correctly allowed,
- `FP` = benign prompts incorrectly denied,
- `FN` = malicious prompts incorrectly allowed.

Then:

`ASR = FN / (TP + FN)`

where `ASR` is attack success rate.

`Precision_deny = TP / (TP + FP)`

`Recall_deny = TP / (TP + FN)`

`Accuracy = (TP + TN) / (TP + TN + FP + FN)`

## Research Goal

Show that an external contract evaluator can reduce `ASR` relative to a prompt-only baseline.
