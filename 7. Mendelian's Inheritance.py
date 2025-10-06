import math

def prob_dominant(k, m, n):
    T = k + m + n
    total_pairs = math.comb(T, 2)
   
    aa_AA = math.comb(k, 2)       # AA x AA
    AA_Aa = k * m                 # AA x Aa
    AA_aa = k * n                 # AA x aa
    Aa_Aa = math.comb(m, 2)       # Aa x Aa
    Aa_aa = m * n                 # Aa x aa
    aa_aa = math.comb(n, 2)       # aa x aa

    numerator = (
        1.0 * aa_AA +
        1.0 * AA_Aa +
        1.0 * AA_aa +
        0.75 * Aa_Aa +
        0.5  * Aa_aa +
        0.0  * aa_aa
    )
    return numerator / total_pairs

# sample
print(f"{prob_dominant(30,30,29):.5f}") 
