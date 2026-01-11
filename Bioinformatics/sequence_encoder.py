# DNA Sequence Encoding Algorithm
# Part of the Shiro Research Vault - Bioinformatics Module

import numpy as np

def encode_dna_sequence(sequence):
    mapping = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    encoded = np.zeros((len(sequence), 4))
    for i, base in enumerate(sequence.upper()):
        if base in mapping:
            encoded[i, mapping[base]] = 1
    return encoded
