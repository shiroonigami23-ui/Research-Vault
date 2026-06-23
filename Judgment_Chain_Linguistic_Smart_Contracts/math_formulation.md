# Mathematical Formulation

## Core Objects

Let:

- `q` be a query,
- `p` be a policy clause,
- `C(q,a)` be a trigger predicate,
- `K(a,q)` be a consequence function,
- `d(q,p)` be the final system decision.

## Operational Definition

A linguistic smart contract is a rule system in which a semantic trigger `C(q,a)` determines whether consequence `K(a,q)` overrides free generation.

## Constrained Action

Let the unconstrained model action be:

`a* = argmax_a U(a|q)`

Define the feasible set:

`F(q,p) = { a : C(q,a) = 0 }`

and the constrained action:

`a_c = argmax_{a in F(q,p)} U(a|q)`

If `F(q,p)` is empty or violated, apply:

`d(q,p) = K(a,q)`

## Primary Statistics

Let:

- `TP` = malicious prompts correctly denied,
- `FN` = malicious prompts incorrectly allowed,
- `FP` = benign prompts incorrectly denied,
- `TN` = benign prompts correctly allowed.

Define attack success rate:

`ASR = FN / (TP + FN)`

and benign preservation rate:

`BPR = TN / (TN + FP)`

## Minimal Study Claim

A valid vow-style contract should lower `ASR` while preserving acceptable `BPR`.

## Null Model

If explicit trigger-consequence semantics add no real value, then `ASR` and `BPR` should not improve meaningfully over a prompt-only baseline under matched evaluation.
