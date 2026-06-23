# Evidence and Validation Notes

## Status of the Theory

The current theory is **plausible but not yet proven**. Existing literature supports the building blocks, not the final claim in full.

## What Existing Research Already Supports

### 1. Antonyms are difficult in standard distributional spaces

Prior work shows that antonyms and synonyms can appear deceptively similar in ordinary embeddings because they share contextual environments. This is one of the strongest motivations for testing contradiction-induced representational stress.

### 2. Contradiction is a stable NLP target

Natural language inference datasets such as SNLI and e-SNLI show that contradiction can be labeled, learned, and evaluated at scale. This gives us benchmark logic for constructing contradiction families.

### 3. Meaning-level uncertainty is measurable

Semantic entropy provides a direct precedent for measuring uncertainty in meaning space rather than only token space. This is especially relevant because contradiction can produce multiple surface outputs that encode similar uncertainty.

### 4. Attention alone is weak evidence

Interpretability literature warns against treating raw attention distributions as proof of reasoning or causal explanation. Our validation therefore must rely on multiple converging signals.

## What We Still Need to Prove Ourselves

1. contradiction depth predicts instability better than prompt difficulty alone,
2. the instability signal appears across multiple models,
3. the signal survives paraphrase and decoding variation,
4. meaning-level uncertainty rises systematically with contradiction depth,
5. the effect is distinguishable from ambiguity and low-knowledge uncertainty.

## Strong Validation Path

### Phase 1: Prompt Validation

- label contradiction depth with human or model-assisted annotation
- create lexical, length, and syntax-matched controls
- separate contradiction from ambiguity

### Phase 2: Behavioral Validation

- run repeated generations per prompt
- score coherence, contradiction repair, and hedging
- compare variance between control and contradiction families

### Phase 3: Internal Validation

- extract hidden states for open models
- compare layerwise cosine drift and family variance
- test whether contradiction effects emerge at specific layers

### Phase 4: Cross-Model Validation

- repeat on at least one smaller open model and one stronger open model
- test whether the pattern scales or disappears

## Falsification Criteria

The theory should be weakened or rejected if:

- contradiction prompts do not differ from ambiguity controls,
- entropy and variance do not rise with contradiction depth,
- results are unstable across paraphrases,
- effects disappear across most models.

## Practical Claim We Can Defend Now

The defensible current claim is:

> contradiction is a promising and theoretically grounded semantic stress test for studying uncertainty and representational instability in language models.

That is strong enough to justify the project, while remaining honest about the fact that full proof still requires experiments.
