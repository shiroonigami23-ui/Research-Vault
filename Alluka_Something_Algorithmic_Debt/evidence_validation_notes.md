# Evidence and Validation Notes

## What Existing Literature Supports

1. model capability is compute-sensitive,
2. inference-time effort can substitute for or complement larger model scale,
3. repeated sampling and verification can improve answer quality,
4. token count alone is too weak as a full cost descriptor.

## What We Still Need to Prove

1. prompt ambition can be operationalized cleanly,
2. algorithmic debt can be measured consistently across workflows,
3. safety and verification overhead scale in predictable ways,
4. a useful index can be built for comparing tasks.

## Validation Path

- define prompt ambition features,
- log direct inference, repeated sampling, validation, and retrieval cost,
- compare simple and complex task families,
- fit whether overhead grows linearly, sublinearly, or superlinearly.
