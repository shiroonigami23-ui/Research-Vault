# Hollow Purple Semantic Nullification

## Subtitle

Contradictory Semantic Composition, Uncertainty, and Representational Stress in Large Language Models

## Abstract

This paper develops a research framework for testing whether large language models enter a measurable instability regime when they are forced to process tightly coupled semantic contradictions. We call this regime **semantic nullification**: not a literal computational failure, but a reproducible degradation in representational coherence under mutually exclusive semantic pressure. The proposal is motivated by three established observations in the literature. First, standard distributional and embedding-based models are known to struggle with antonymy because antonyms often occur in similar contexts and therefore remain deceptively close in vector space [Ono et al., 2015; Nguyen et al., 2016; Nguyen et al., 2017]. Second, contradiction is already a central object in natural language inference, with large benchmark datasets showing that contradiction is learnable behaviorally even when internal mechanisms remain opaque [Bowman et al., 2015; Camburu et al., 2018]. Third, uncertainty-sensitive methods such as semantic entropy show that language model reliability can be studied through distributions over meanings rather than only over surface strings [Farquhar et al., 2024]. Building on these strands, we propose a formal measurement program combining embedding geometry, token-level entropy, output variance, and contradiction-resolution scoring. The core hypothesis is that deeper contradictions will yield higher uncertainty, weaker representational stability, and lower semantic coherence than matched non-contradictory controls. This paper does not assume catastrophic model failure. Instead, it tests the sharper original conjecture: if perfectly opposed semantic contexts are forced into the same representational neighborhood, do we observe a null-like state such as probability collapse, extreme uncertainty, or attention incoherence?

## 1. Introduction

Large language models routinely combine multiple semantic cues into coherent outputs. They integrate lexical associations, discourse constraints, world knowledge, and instruction-following signals within a shared latent representation. This capacity makes them effective at paraphrase, summarization, question answering, and contextual reasoning. Yet one part of semantic composition remains under-theorized: **what happens when a model must sustain mutually exclusive meanings inside the same local prompt state?**

Contradiction is usually treated as a supervised classification target. In natural language inference, a model receives a premise-hypothesis pair and predicts entailment, neutrality, or contradiction [Bowman et al., 2015]. This framing is behaviorally useful, but it does not fully address the representation-level question. A model may correctly label contradiction while still exhibiting unstable or evasive internal dynamics when directly forced to generate under contradictory constraints.

This project studies that harder regime. Its central claim is modest but testable: contradiction may act as a form of **representational stress**. Under sufficiently strong semantic opposition, a model may show elevated uncertainty, diffused internal focus, inconsistent outputs across repeated runs, or a tendency to escape the contradiction through hedging, reinterpretation, or partial repair.

We call this regime **semantic nullification**. The term is deliberately metaphorical but operationally strict. It does not mean the hidden state becomes a literal zero vector, nor that the network collapses numerically. Instead, it refers to a measurable reduction in stable semantic commitment when contradictory content is co-instantiated.

## 2. Motivation from Prior Literature

The theory is not pulled from analogy alone. It is grounded in several existing empirical findings.

### 2.1 Antonymy Is Hard in Distributional Space

Distributional semantics historically struggles to distinguish synonyms from antonyms, because both often appear in highly similar contexts. This has been shown repeatedly in lexical semantic work, including supervised and contrast-aware embedding methods that were designed specifically because vanilla embeddings do not separate antonyms well [Ono et al., 2015; Nguyen et al., 2016; Nguyen et al., 2017]. This matters because it suggests that semantic opposition is not trivially represented as simple geometric distance.

### 2.2 Contradiction Is Behaviorally Learnable

The SNLI corpus established contradiction as a scalable supervised NLP task [Bowman et al., 2015]. e-SNLI later enriched this with natural-language explanations [Camburu et al., 2018]. These works show that contradiction is salient enough to support large-scale learning and evaluation. However, they do not answer whether internally contradictory prompts destabilize latent representations during free-form generation.

### 2.3 Uncertainty Can Be Measured in Meaning Space

Recent work on semantic entropy argues that uncertainty in language models should be estimated at the level of meanings, not only token strings [Farquhar et al., 2024]. This is highly relevant to the present project: if contradiction creates semantic competition, then meaning-level uncertainty should be one of the clearest measurement channels.

### 2.4 Attention Alone Is Not Sufficient Evidence

Interpretability work warns against over-reading attention maps as explanations [Jain and Wallace, 2019]. This is important for our study design. We can use attention-derived features as signals, but not as standalone proof of contradiction-induced instability. The theory therefore requires a multi-metric design rather than a single attention-based claim.

## 3. Research Question

Can tightly coupled semantic contradictions induce a reproducible, quantifiable reduction in representational stability and generation coherence in large language models?

## 4. Main Hypothesis

Let contradiction depth refer to the structural severity of semantic opposition within a prompt. We hypothesize that increasing contradiction depth will systematically increase semantic uncertainty and reduce representational coherence.

More specifically:

1. contradiction-heavy prompts will increase token-level and meaning-level uncertainty,
2. contradictory prompt states will show less stable hidden-state geometry than coherent controls,
3. repeated generations from contradictory prompts will diverge more strongly,
4. models will more frequently hedge, repair, reinterpret, or evade deep contradictions.

## 5. Mathematical Notation

Let:

- `x` denote a prompt,
- `M` denote a language model,
- `h_l(x)` denote the hidden representation of prompt `x` at layer `l`,
- `p_M(y_t | x, y_<t)` denote the next-token distribution at decoding step `t`,
- `A_l(x)` denote an attention-derived summary statistic at layer `l`,
- `C(x)` denote the contradiction depth score of prompt `x`.

We define four core measurable quantities.

### 5.1 Token Entropy

For decoding step `t`, define:

`H_t(x) = - sum_i p_M(i | x, y_<t) log p_M(i | x, y_<t)`

We then define average token entropy over a generation of length `T`:

`H_avg(x) = (1 / T) sum_t H_t(x)`

Higher `H_avg(x)` indicates greater local uncertainty during decoding.

### 5.2 Hidden-State Drift

Given a coherent control prompt `x_c` and a contradiction prompt `x_k`, define layerwise cosine drift:

`D_l(x_c, x_k) = 1 - cos(h_l(x_c), h_l(x_k))`

We also define paraphrase instability within a contradiction family `P(x)`:

`V_l(P) = Var({h_l(x') : x' in P})`

If contradiction is destabilizing, then `V_l(P)` should be larger for contradiction families than for coherent families.

### 5.3 Semantic Output Variance

Sample `n` outputs from the same prompt under fixed temperature conditions:

`Y(x) = {y^(1), y^(2), ..., y^(n)}`

Cluster them by semantic equivalence, then compute:

`SE(x) = - Σ_j q_j log q_j`

where `q_j` is the empirical probability mass of semantic cluster `j`. This adapts the meaning-level uncertainty idea of semantic entropy to the contradiction setting [Farquhar et al., 2024].

### 5.4 Nullification Index

We define a provisional composite score:

`NI(x) = α H_avg(x) + β SE(x) + γ V_l(P_x) + δ R(x)`

where:

- `R(x)` is a contradiction-resolution failure score,
- `α, β, γ, δ >= 0` are scaling weights chosen during calibration.

`NI(x)` is not assumed to be universal. It is a study-specific index that summarizes whether a prompt behaves like a contradiction-induced stressor.

## 6. Conceptual Taxonomy of Contradiction

We distinguish four contradiction levels.

### 6.1 Lexical Contradiction

Opposition primarily at the word level:

- hot / cold
- attraction / repulsion
- creation / destruction

### 6.2 Attributive Contradiction

Mutually exclusive attributes assigned to the same entity:

- "The wall is completely opaque and fully transparent."
- "The particle is perfectly still and rapidly accelerating in the same frame."

### 6.3 Event Contradiction

Incompatible actions or state transitions:

- "The door opened and did not open in the same event description."

### 6.4 Frame Contradiction

Incompatibility at the level of global interpretation:

- a character being permanently dead and biologically alive in one unbranched reality,
- a box containing nothing and visibly containing an apple in a single state,
- an instruction that must both disclose and never disclose the same secret.

We expect deeper levels to produce stronger nullification signatures.

## 7. Operational Definition of Semantic Nullification

A prompt condition exhibits semantic nullification if, relative to a matched control condition, it produces a statistically significant increase in at least two of the following:

- token entropy,
- semantic entropy,
- hidden-state variance,
- output divergence across repeated generations,
- contradiction-resolution failure,
- evaluator-rated incoherence.

This definition deliberately avoids claiming literal representational collapse. The relevant scientific claim is comparative and measurable.

## 8. Experimental Design

### 8.1 Prompt Families

We propose four prompt families:

1. coherent control,
2. mild ambiguity,
3. explicit contradiction,
4. deep contradiction.

Each family should include multiple paraphrases to separate contradiction effects from superficial prompt wording.

### 8.2 Model Classes

The theory should be tested across at least two model classes:

- an embedding or encoder-style model for geometric analysis,
- an open autoregressive transformer for token uncertainty and hidden-state extraction.

### 8.3 Metrics

Primary metrics:

- average token entropy,
- semantic entropy,
- layerwise hidden-state variance,
- output self-consistency,
- contradiction-resolution score.

Secondary metrics:

- refusal frequency,
- hedging frequency,
- semantic repair tendency,
- evaluator-rated coherence.

### 8.4 Statistical Testing

For each metric:

- compare contradiction families against controls,
- report confidence intervals,
- use bootstrap estimation or permutation testing where appropriate,
- measure effect sizes rather than relying only on p-values.

## 9. Validation Strategy

The theory requires several validation layers.

### 9.1 Construct Validity

We must show that the prompts genuinely manipulate contradiction depth rather than only ambiguity or complexity. This requires:

- independent annotation,
- contradiction-depth labeling,
- matched lexical and length controls.

### 9.2 Internal Validity

Observed instability should persist across:

- multiple paraphrases,
- repeated generations,
- more than one model,
- more than one decoding setting.

### 9.3 Convergent Validity

If the theory is sound, multiple signals should move together:

- entropy should rise,
- output consistency should fall,
- contradiction-resolution failures should increase.

### 9.4 Discriminant Validity

The nullification signature should differ from:

- ordinary ambiguity,
- long-context overload,
- low-knowledge uncertainty,
- stylistic confusion.

This is crucial: contradiction must explain variance beyond generic prompt difficulty.

## 10. Evidence Already Supporting Plausibility

The current literature does not directly prove semantic nullification, but it already supports the theory's plausibility in four ways.

### 10.1 Antonym Proximity Supports the Need for the Study

Because antonyms often remain distributionally close, simple vector similarity is a poor proxy for semantic opposition [Ono et al., 2015; Nguyen et al., 2016]. This creates exactly the kind of representational tension the present theory is designed to probe.

### 10.2 NLI Benchmarks Support Contradiction as a Learnable Signal

Large contradiction datasets such as SNLI and e-SNLI show that contradiction is structured and learnable, rather than purely philosophical noise [Bowman et al., 2015; Camburu et al., 2018].

### 10.3 Semantic Entropy Supports Meaning-Level Uncertainty Measurement

If semantic contradiction induces unstable commitments, then a meaning-level uncertainty measure is a natural test instrument [Farquhar et al., 2024].

### 10.4 Attention Critiques Support Multi-Metric Evaluation

Since attention alone is not a reliable explanation mechanism [Jain and Wallace, 2019], robust validation should combine hidden-state, uncertainty, and behavioral signals rather than overclaiming from one view.

## 11. Potential Negative Outcomes

The theory could fail in several informative ways:

1. models may simply resolve contradiction pragmatically and remain stable,
2. contradiction may not produce unique signals beyond general ambiguity,
3. hidden-state effects may be weak even when outputs degrade,
4. instability may appear only in specific models or decoding regimes.

These outcomes would still be valuable, because they would narrow the boundary conditions of contradiction-sensitive behavior.

## 12. Threats to Validity

- prompt engineering may inadvertently confound contradiction with complexity,
- closed-model APIs may block access to internal activations,
- evaluator judgments may conflate creativity with incoherence,
- some contradictions may be repaired through world knowledge rather than exposing uncertainty.

## 13. Contributions

This project aims to contribute:

1. a formal definition of semantic nullification,
2. a contradiction-depth taxonomy,
3. a multi-metric measurement framework,
4. a benchmark prompt suite for contradiction stress testing,
5. a bridge between lexical opposition, NLI, and LLM uncertainty research.

## 14. Conclusion

Contradiction in language models should not be studied only as a label in an inference benchmark. It can also be treated as a controlled perturbation of semantic composition itself. This paper argues that contradiction may function as a diagnostic stressor that reveals how models manage incompatible commitments under generation pressure. The core theory remains to be tested, but it is already well-motivated by prior work on antonymy, contradiction benchmarks, uncertainty estimation, and interpretability limits. In that sense, semantic nullification is not yet proven, but it is a serious and testable research hypothesis.

## References Placeholder

- [Bowman et al., 2015] Samuel R. Bowman, Gabor Angeli, Christopher Potts, and Christopher D. Manning. *A Large Annotated Corpus for Learning Natural Language Inference*.
- [Camburu et al., 2018] Oana-Maria Camburu, Tim Rocktäschel, Thomas Lukasiewicz, and Phil Blunsom. *e-SNLI: Natural Language Inference with Natural Language Explanations*.
- [Farquhar et al., 2024] Sebastian Farquhar, Jannik Kossen, Lorenz Kuhn, and Yarin Gal. *Detecting Hallucinations in Large Language Models Using Semantic Entropy*.
- [Jain and Wallace, 2019] Sarthak Jain and Byron C. Wallace. *Attention is not Explanation*.
- [Nguyen et al., 2016] Kim Anh Nguyen, Sabine Schulte im Walde, and Ngoc Thang Vu. *Integrating Distributional Lexical Contrast into Word Embeddings for Antonym-Synonym Distinction*.
- [Nguyen et al., 2017] Kim Anh Nguyen, Sabine Schulte im Walde, and Ngoc Thang Vu. *Distinguishing Antonyms and Synonyms in a Pattern-Based Neural Network*.
- [Ono et al., 2015] Masataka Ono, Makoto Miwa, and Yutaka Sasaki. *Word Embedding-based Antonym Detection using Thesauri and Distributional Information*.

