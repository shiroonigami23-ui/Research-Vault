# Alluka Something Algorithmic Debt

## Subtitle

Prompt Complexity, Test-Time Compute, and Safety Overhead as a Unified Burden Model for Language Systems

## Abstract

This review-style paper proposes **algorithmic debt** as a framework for studying how ambitious prompts create downstream burdens beyond raw token generation. The theory is inspired by a wish-cost metaphor: larger requests trigger larger compensating requirements. In language model systems, these compensating requirements may include longer inference, repeated sampling, verification passes, tool orchestration, retrieval overhead, or safety review. Existing literature already supports several building blocks. Classical scaling-law work shows that capability depends strongly on data, parameters, and compute [Kaplan et al., 2020; Hoffmann et al., 2022]. More recent work shows that performance can also be improved by spending additional **test-time compute**, including repeated reasoning and search-like inference [Wang et al., 2022; Snell et al., 2024]. These findings motivate a broader claim: prompt difficulty should be modeled not only by input length, but by the full burden of achieving reliable answers. This paper frames that burden as algorithmic debt and argues for a review paper or empirical program that estimates how task ambition drives inference cost, verification cost, and alignment overhead together rather than in isolation.

## 1. Core Thesis

A user request does not incur only generation cost. It may also create:

- reasoning cost,
- sampling cost,
- validation cost,
- retrieval cost,
- policy review cost,
- and human-oversight cost.

The sum of these burdens is the study target.

## 2. Supporting Literature

### 2.1 Scaling Laws

Language model performance has strong relationships with training compute and model scale [Kaplan et al., 2020; Hoffmann et al., 2022]. This supports the broader idea that capability is resource-sensitive rather than free.

### 2.2 Test-Time Compute

Self-consistency and test-time scaling results show that additional inference-time effort can improve performance [Wang et al., 2022; Snell et al., 2024]. This is directly relevant to the theory that harder prompts trigger compensating post-prompt costs.

### 2.3 Reliability Requires More Than One Pass

When verification, multiple samples, or external tools are needed, the cost of a prompt is no longer well-approximated by token count alone. This supports the algorithmic debt framing.

## 3. Formal Framing

Let:

- `x` be a prompt,
- `I(x)` be direct inference cost,
- `S(x)` be sampling or repeated-generation cost,
- `V(x)` be verification cost,
- `R(x)` be retrieval or tool-use cost,
- `A(x)` be alignment and safety overhead.

Define:

`AD(x) = I(x) + S(x) + V(x) + R(x) + A(x)`

The theory claims that for some task families, `AD(x)` grows faster than prompt length and may scale nonlinearly with task ambition.

## 4. Defensible Present Claim

The current literature does not yet prove a universal algorithmic debt law. It does justify this narrower claim:

> prompt burden should be modeled as a multi-component systems cost rather than as raw token count alone.

## References Placeholder

- [Kaplan et al., 2020] *Scaling Laws for Neural Language Models*.
- [Hoffmann et al., 2022] *Training Compute-Optimal Large Language Models*.
- [Wang et al., 2022] *Self-Consistency Improves Chain of Thought Reasoning in Language Models*.
- [Snell et al., 2024] *Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters*.
