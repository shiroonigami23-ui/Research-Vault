# Related Work Notes

## Priority Literature Areas

- vector semantics and compositionality
- natural language inference and contradiction detection
- representation geometry in transformers
- entropy and uncertainty in language generation
- interpretability through hidden-state and attention analysis
- adversarial prompting and semantic stress testing

## Core Papers to Cite

1. Bowman et al. (2015) on SNLI for large-scale contradiction benchmarking
2. Camburu et al. (2018) on e-SNLI for contradiction explanations
3. Ono et al. (2015) on antonym detection in embeddings
4. Nguyen et al. (2016) on lexical contrast in embeddings
5. Nguyen et al. (2017) on antonym-synonym distinction with pattern-based neural methods
6. Farquhar et al. (2024) on semantic entropy for meaning-level uncertainty
7. Jain and Wallace (2019) on limits of attention as explanation

## Questions for Review

1. How well do current embeddings encode antonymy versus similarity?
2. What methods already exist for measuring representational instability?
3. How often do contradiction tasks focus only on outputs rather than internals?
4. Which open models expose the cleanest hidden-state and attention interfaces?

## Literature Use in This Project

- SNLI and e-SNLI justify contradiction as an established supervised object.
- antonym papers justify the claim that semantic opposition is geometrically nontrivial.
- semantic entropy justifies meaning-level uncertainty as a primary metric.
- attention critique justifies using attention only as a secondary signal.
