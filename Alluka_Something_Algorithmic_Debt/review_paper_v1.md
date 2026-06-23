# Alluka Something Algorithmic Debt

## Subtitle

Iterative Prompting Dynamics, Sequential Safety Requests, and the Something-Alluka Index

## Abstract

This review-style paper proposes **algorithmic debt** as a framework for studying the exact theory in the original pitch: a large "wish" prompt forces a larger sequence of compensating "requests" needed to keep the model stable, aligned, and reliable. The central object is not generic workflow cost. It is the mapping from **wish complexity** to the **strictness and number of sequential safety-alignment requests** that must follow. Classical scaling-law work shows that capability depends strongly on data, parameters, and compute [Kaplan et al., 2020; Hoffmann et al., 2022]. More recent work shows that performance can also be improved by additional inference-time effort [Wang et al., 2022; Snell et al., 2024]. We use these foundations to define a Something-Alluka Index: a mathematical measure of how the complexity of an initial prompt predicts the number, intensity, and computational burden of the follow-up control steps required for stable generation. The publishable contribution is therefore a theory of **iterative prompting debt**, not merely a general accounting of tooling cost.

## 1. Core Thesis

A large "wish" prompt does not incur only generation cost. It may force a chain of compensating requests such as:

- alignment clarification requests,
- safety verification requests,
- decomposition requests,
- repeated reasoning passes,
- and stricter follow-up control prompts.

The sum of these sequential burdens is the study target.

## 2. Supporting Literature

### 2.1 Scaling Laws

Language model performance has strong relationships with training compute and model scale [Kaplan et al., 2020; Hoffmann et al., 2022]. This supports the broader idea that capability is resource-sensitive rather than free.

### 2.2 Iterative Effort at Test Time

Self-consistency and test-time scaling results show that additional inference-time effort can improve performance [Wang et al., 2022; Snell et al., 2024]. This is directly relevant to the theory that a larger wish may require more sequential control effort after the original ask.

### 2.3 Reliability Requires Sequential Requests

When decomposition, verification, or repeated safety checks are needed, the cost of a prompt is no longer well-approximated by token count alone. This supports the wish-request debt framing.

## 3. Formal Framing

Let:

- `x` be a prompt,
- `W(x)` be wish complexity,
- `Q_i(x)` be the i-th compensating request after the wish,
- `m(x)` be the number of required sequential requests,
- `c(Q_i)` be the computational/alignment cost of request `Q_i`.

Define:

`AD(x) = W(x) + sum_{i=1}^{m(x)} c(Q_i)`

The theory claims that `m(x)` and the aggregate request cost can grow nonlinearly with wish complexity.

## 4. Something-Alluka Index

Define a normalized index:

`SAI(x) = lambda_1 W(x) + lambda_2 m(x) + lambda_3 (1/m(x)) sum_i c(Q_i)`

where `W(x)` can itself be decomposed into prompt length, conceptual breadth, ambiguity, risk level, and reasoning depth.

## 5. Defensible Present Claim

The current literature does not yet prove a universal algorithmic debt law. It does justify this narrower claim:

> the burden of a large prompt should be modeled as the complexity of the initial wish plus the sequential cost of the requests required to keep the system stable.

## References Placeholder

- [Kaplan et al., 2020] *Scaling Laws for Neural Language Models*.
- [Hoffmann et al., 2022] *Training Compute-Optimal Large Language Models*.
- [Wang et al., 2022] *Self-Consistency Improves Chain of Thought Reasoning in Language Models*.
- [Snell et al., 2024] *Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters*.

