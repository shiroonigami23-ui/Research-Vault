# Something-Alluka Algorithmic Debt Model

## Wish-Request Model

Let:

- `x` be a wish prompt,
- `L(x)` be prompt length,
- `D(x)` be reasoning depth,
- `B(x)` be conceptual breadth,
- `R(x)` be risk or safety sensitivity,
- `m(x)` be the number of sequential requests induced by the wish,
- `Q_i(x)` be the i-th sequential request.

Define wish complexity:

`W(x) = alpha log(1 + L(x)) + beta D(x) + gamma B(x) + delta R(x)`

Define request cost:

`c(Q_i) = eta A_i + theta V_i + kappa C_i`

where:

- `A_i` is alignment strictness of request `i`,
- `V_i` is verification burden of request `i`,
- `C_i` is computational burden of request `i`.

Then the total algorithmic debt is:

`AD(x) = W(x) + S_{i=1}^{m(x)} c(Q_i)`

## Something-Alluka Index

Define:

`SAI(x) = mu_1 W(x) + mu_2 m(x) + mu_3 (1/m(x)) S_i c(Q_i)`

This index is intended to capture both the size of the initial wish and the burden of the compensating requests that follow.

## Normalized Debt

To compare tasks across families, define:

`NAD(x) = AD(x) / log(2 + L(x))`

This separates raw length from sequential request overhead.

## Research Claim

If large wishes generate disproportionate increases in `m(x)` and `NAD(x)`, then prompt burden is not reducible to token count alone and is better understood as sequential request debt.
