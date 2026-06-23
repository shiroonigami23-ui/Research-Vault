# Proof Obligations

## What We Can Defend Now

1. prompt burden is not exhausted by raw token count,
2. harder tasks often require repeated reasoning or verification,
3. compute-sensitive scaling theory supports resource-aware modeling,
4. a wish-request debt model is mathematically definable.

## What We Still Need to Prove

1. larger wishes induce more sequential requests in a measurable way,
2. sequential request strictness scales with wish complexity,
3. Something-Alluka Index predicts burden better than token count alone,
4. the effect generalizes across task families.

## Minimal Formal Claims

### Claim A1

If wish complexity increases, expected request count increases.

### Claim A2

If wish complexity increases, normalized debt increases faster than token length alone predicts.

### Claim A3

If safety sensitivity is high, request strictness contributes superlinearly to debt.

## Falsification Conditions

- request count is unrelated to wish complexity,
- token count explains burden just as well as the full index,
- no stable relationship across task families,
- sequential controls fail to add measurable explanatory power.
