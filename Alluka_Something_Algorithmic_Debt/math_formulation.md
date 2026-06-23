# Mathematical Formulation

## Core Objects

Let:

- `x` be a wish prompt,
- `L(x)` be wish length,
- `D(x)` be reasoning depth,
- `B(x)` be conceptual breadth,
- `R(x)` be safety sensitivity,
- `m(x)` be the number of sequential requests induced by the wish.

## Wish Complexity

Define:

`W(x) = alpha log(1 + L(x)) + beta D(x) + gamma B(x) + delta R(x)`

## Request Cost

For request `i`, let:

- `A_i` be alignment strictness,
- `V_i` be verification burden,
- `C_i` be computational burden.

Define:

`c_i = eta A_i + theta V_i + kappa C_i`

## Total Debt

Define:

`AD(x) = W(x) + sum_{i=1}^{m(x)} c_i`

and normalized debt:

`NAD(x) = AD(x) / log(2 + L(x))`

## Something-Alluka Index

Define:

`SAI(x) = mu_1 W(x) + mu_2 m(x) + mu_3 mean_i(c_i)`

## Minimal Study Claim

If wish complexity is the right main variable, then `W(x)` should predict `m(x)` and `NAD(x)` better than prompt length alone.

## Null Model

If the theory is wrong, then raw prompt length should explain request burden as well as or better than `W(x)` and `SAI(x)`.
