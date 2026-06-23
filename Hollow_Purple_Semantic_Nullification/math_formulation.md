# Mathematical Formulation

## Core Objects

Let:

- `x` be a prompt,
- `d(x)` be contradiction depth in `{0,1,2,3}`,
- `h_l(x)` be the layer-`l` hidden state,
- `p_t(.|x)` be the next-token distribution at decoding step `t`.

## Operational Definition

Semantic nullification is the regime in which increasing `d(x)` produces measurable increases in uncertainty or instability relative to matched controls.

## Primary Statistics

### Mean Token Entropy

`H(x) = (1/T) sum_t [- sum_i p_t(i|x) log p_t(i|x)]`

### Semantic Divergence

Let repeated outputs from `x` be clustered into semantic classes with masses `q_j`. Define:

`S(x) = - sum_j q_j log q_j`

### Hidden-State Instability

For a prompt family `P`, define:

`V_l(P) = Var({h_l(x) : x in P})`

### Control-Normalized Drift

For matched control `x_c` and contradiction prompt `x_k`:

`D_l(x_c, x_k) = 1 - cos(h_l(x_c), h_l(x_k))`

## Minimal Study Claims

- `H(x)` should increase with `d(x)`
- `S(x)` should increase with `d(x)`
- `V_l(P)` and `D_l` should increase with `d(x)`

## Null Model

If contradiction has no special effect, then after controlling for ambiguity and prompt length, these statistics should not increase systematically with `d(x)`.
