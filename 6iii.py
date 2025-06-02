def dna_to_rna(dna):
    transcription = {'A': 'U', 'T': 'A', 'C': 'G', 'G': 'C'}
    rna = ''
    for nucleotide in dna:
        if nucleotide in transcription:
            rna += transcription[nucleotide]
    return rna


test_cases = ["ACGTTGCA", "ACG TGCA", "GATTACA", "A42%"]
for dna in test_cases:
    print(f"Input: {dna} Output: {dna_to_rna(dna)}")
# Output
# PS C:\Users\HP\OneDrive\Desktop\computer-assignments> & C:/Python313/python.exe c:/Users/HP/OneDrive/Desktop/computer-assignments/6iii.py
# Input: ACGTTGCA Output: UGCAACGU
# Input: ACG TGCA Output: UGCACGU
# Input: GATTACA Output: CUAAUGU
# Input: A42% Output: U