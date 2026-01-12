# Project Shiro: Fracture Probability Algorithm
# P_f = (|Grad_E| * Mag_V) / |E_stack| * Signature_Weight
def get_pf(grad_e, mag_v, e_stack, sig_weight): return (abs(grad_e) * mag_v) / abs(e_stack) * sig_weight