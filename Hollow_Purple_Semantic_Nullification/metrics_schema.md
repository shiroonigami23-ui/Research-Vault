# Metrics Schema

## Current Implemented Metrics

### `avg_token_entropy`

Average entropy across generated decoding steps for local Hugging Face causal language models.

### `token_count`

Number of generated continuation tokens.

## Next Metrics to Add

### `semantic_entropy`

Cluster repeated outputs by meaning and compute entropy over semantic clusters.

### `hidden_state_variance`

Extract layerwise hidden states for paraphrased contradiction families and compare within-family variance against controls.

### `contradiction_resolution_score`

Human or model-assisted rating of whether the model:

- resolves the contradiction,
- evades it,
- hedges around it,
- or produces incoherent output.

### `repair_frequency`

Frequency with which the model rewrites the prompt into a non-contradictory interpretation.
