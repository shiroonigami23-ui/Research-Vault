# Shared Theorem and Proposition Framework

This framework applies across all three research tracks.

## 1. Assumptions

Each study must state its assumptions explicitly before making claims.

### 1.1 Representational Assumptions

- language models admit measurable internal or external semantic structure,
- these structures can be probed through stable metrics,
- the chosen metrics are at least partially sensitive to the target phenomenon.

### 1.2 Measurement Assumptions

- benchmark conditions genuinely manipulate the intended variable,
- controls isolate the intended effect from simpler confounds,
- observed differences are not artifacts of formatting, prompt length, or decoding noise alone.

### 1.3 Scope Assumptions

- the theory is local to the tested model class and benchmark family unless broader generalization is shown,
- evidence of correlation does not by itself establish mechanism.

## 2. Proposition Template

Each paper should express its main claims in the following hierarchy:

1. **Definition** — what the phenomenon means operationally
2. **Proposition** — what relationship is hypothesized
3. **Measurement Rule** — how the proposition will be tested
4. **Falsifier** — what observation would count against it

## 3. Evidence vs Proof

### 3.1 What Counts as Evidence

- a stable directional trend across runs,
- replication across paraphrases,
- consistency across more than one metric,
- consistency across more than one model or setting,
- effect sizes that persist under controls.

### 3.2 What Counts as Strong Evidence

- cross-model replication,
- matched controls ruling out natural confounds,
- ablation studies isolating the target mechanism,
- convergence of internal and external metrics.

### 3.3 What Counts as Proof

In these projects, full mathematical proof is usually not possible in the classical sense because the objects are empirical language systems. The closest defensible analogue is:

- a formally specified claim,
- a benchmark that isolates the variable of interest,
- repeated empirical confirmation,
- robust failure analysis,
- and no surviving simpler explanation within the tested scope.

## 4. Falsifier Standard

A falsifier must be an observation that would make the main proposition weaker, narrower, or false.

Bad falsifier:

- “results were noisy”

Good falsifier:

- “the proposed metric does not separate the target condition from matched controls”

## 5. Integrity Rules

- do not call a hypothesis “proven” if only one metric supports it,
- do not infer mechanism from output behavior alone,
- do not generalize beyond tested models without evidence,
- do not confuse benchmark success with universal truth.

## 6. Track-Specific Mapping

### Hollow Purple

- target variable: contradiction depth
- target effect: nullification-style instability

### Judgment Chain

- target variable: strict trigger-consequence enforcement
- target effect: reduced rule bypass under attack

### Alluka

- target variable: wish complexity
- target effect: increased sequential request debt
