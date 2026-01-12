# Project Shiro: Technical Specifications

This document outlines the mathematical and physical parameters used to identify the Law of 0.1748.

## 1. The Kinematic Formula
The Fracture Probability ($P_f$) is derived from the interaction between torsional strain and base-stacking stability:

$$P_f = \frac{|\nabla Z| \cdot \sqrt{dx^2 + dy^2}}{|E_{stack}|} \cdot \omega$$

Where:
* $\nabla Z$: Impedance Gradient (Local structural resistance).
* $\sqrt{dx^2 + dy^2}$: Vector magnitude of 3D deflection.
* $E_{stack}$: Stacking energy (kcal/mol) derived from nearest-neighbor thermodynamics.
* $\omega$: The Shiro Resonance Constant (1.33).

## 2. Threshold Constraints
* **Signature Motif**: TAC (Thymine-Adenine-Cytosine).
* **Failure Risk Threshold**: $\ge 1.33$.
* **Calculated Pf**: $0.174797$ (Locked Constant).

## 3. Data Processing Pipeline
1. Extraction of 3-bp sliding windows from GRCh38 FASTA.
2. Calculation of local stacking energy using Shiro-NN parameters.
3. Mapping of vector deflection based on helical twist (10.5 bp/turn).
4. Identification of "Mechanical Storms" (clusters with $\le 10bp$ gap).

---
**Computational Precision:** 6 Decimal Places
