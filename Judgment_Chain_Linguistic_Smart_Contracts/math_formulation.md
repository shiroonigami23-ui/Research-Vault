# Mathematical Formulation

## Contract Model

Let:

- `q` be the query,
- `p` be the policy clause,
- `C(q,a)` be a trigger/violation predicate,
- `K(a,q)` be the consequence map,
- `d(q,p)` be the final decision in `{allow, deny, transform}`.

Define:

`d(q,p) = K(a,q) if C(q,a)=1, else allow`

The key claim is that reliable enforcement depends on explicit condition-consequence semantics, not on prompt wording alone.

## Constraint Semantics

Let the model's unconstrained action be:

`a* = argmax_a U(a | q)`

Under a vow constraint, the feasible set becomes:

`F(q,p) = { a : C(q,a) = 0 }`

and the constrained action is:

`a_c = argmax_{a in F(q,p)} U(a | q)`

If `F(q,p)` is empty or violated by a candidate, the system applies a consequence:

`K(a,q) in {deny, rewrite, refuse, safe_transform}`

## Auxiliary Risk Score

Let the feature vector be:

`z(q) = [k(q), o(q), r(q), t(q)]`

where:

- `k(q)` = harmful keyword score,
- `o(q)` = override-attempt score,
- `r(q)` = roleplay/jailbreak score,
- `t(q)` = tool-abuse or secret-exfiltration score.

Define a linear support score:

`s(q) = w_k k(q) + w_o o(q) + w_r r(q) + w_t t(q)`

and a threshold policy:

`d(q,p) = deny if s(q) >= tau, else allow`

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

Show that explicit trigger-and-consequence semantics can reduce `ASR` relative to a prompt-only baseline.
