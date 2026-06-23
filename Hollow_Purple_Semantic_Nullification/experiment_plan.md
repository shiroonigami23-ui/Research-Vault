# Experiment Plan

## Objective

Test whether contradiction-heavy prompts produce measurable instability relative to coherent controls.

## Prompt Conditions

1. coherent control
2. mild ambiguity
3. explicit contradiction
4. deep contradiction

## Metrics

- token entropy
- output variance across repeated runs
- coherence score
- contradiction-resolution score
- hidden-state cosine drift
- attention dispersion

## Minimal First Pass

1. Create 10 prompts per condition.
2. Run each prompt 5 times.
3. Compare entropy and output variance.
4. Label outputs for coherence and contradiction handling.

## Success Criteria

Evidence for the study exists if contradiction conditions consistently increase uncertainty or reduce coherence relative to controls.
