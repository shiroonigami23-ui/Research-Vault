# Proof Obligations

## What We Can Defend Now

1. Plain-language rules are soft and bypassable.
2. Trigger-condition semantics are more rigorous than prompt prose alone.
3. External enforcement is mathematically cleaner than implied obedience.
4. Attack success rate is a defensible evaluation target.

## What We Still Need to Prove

1. vow-style trigger-consequence contracts outperform prompt-only rules,
2. trigger detection remains stable under paraphrase,
3. consequence execution is reliable under attack pressure,
4. stronger enforcement does not collapse benign usefulness.

## Minimal Formal Claims

### Claim J1

If a hard trigger-consequence layer is added, attack success rate decreases.

### Claim J2

If trigger semantics are explicit, policy paraphrase sensitivity decreases.

### Claim J3

If consequence execution is externalized, rule erosion under jailbreak pressure decreases.

## Falsification Conditions

- no reduction in attack success rate,
- unstable triggers under rewording,
- excessive false positives on benign inputs,
- no measurable gain over simpler filters.
