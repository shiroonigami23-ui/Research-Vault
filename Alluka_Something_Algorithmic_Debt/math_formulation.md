# Mathematical Formulation

## Algorithmic Debt Model

Let:

- `x` be a task prompt,
- `T(x)` be prompt token count,
- `D(x)` be reasoning depth,
- `U(x)` be tool-use steps,
- `V(x)` be verification steps,
- `S(x)` be safety sensitivity.

Define direct inference cost:

`I(x) = alpha * log(1 + T(x)) + beta * D(x)`

Define orchestration cost:

`O(x) = gamma * U(x) + delta * V(x)`

Define safety overhead:

`H(x) = epsilon * S(x) + zeta * D(x) * S(x)`

Then the total algorithmic debt is:

`AD(x) = I(x) + O(x) + H(x) + eta * U(x) * V(x)`

The interaction term `eta * U(x) * V(x)` models the intuition that multi-tool workflows become more expensive when verification must also scale.

## Normalized Debt

To compare tasks across families, define:

`NAD(x) = AD(x) / log(2 + T(x))`

This separates raw length from systems overhead.

## Research Claim

If complex tasks generate disproportionate increases in `NAD(x)`, then prompt burden is not reducible to token count alone.
