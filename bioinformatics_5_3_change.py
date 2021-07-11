with open("sequence.nucleotide.fasta", "r") as handle:
    seq = []
    for line in handle:
        if line.strip().startswith(">"):
            continue
        seq.append(line.strip())
    seq = "".join(seq)


def dna_to_protein(seq):
    codon_dic = {
        "TTT": "F",
        "TTC": "F",
        "TTA": "L",
        "TTG": "L",
        "TCT": "S",
        "TCC": "S",
        "TCA": "S",
        "TCG": "S",
        "TAT": "Y",
        "TAC": "Y",
        "TAA": "*",
        "TAG": "*",
        "TGT": "C",
        "TGC": "C",
        "TGA": "*",
        "TGG": "W",
        "CTT": "L",
        "CTC": "L",
        "CTA": "L",
        "CTG": "L",
        "CCT": "P",
        "CCC": "P",
        "CCA": "P",
        "CCG": "P",
        "CAT": "H",
        "CAC": "H",
        "CAA": "Q",
        "CAG": "Q",
        "CGT": "R",
        "CGC": "R",
        "CGA": "R",
        "CGG": "R",
        "ATT": "I",
        "ATC": "I",
        "ATA": "I",
        "ATG": "M",
        "ACT": "T",
        "ACC": "T",
        "ACA": "T",
        "ACG": "T",
        "AAT": "N",
        "AAC": "N",
        "AAA": "K",
        "AAG": "K",
        "AGT": "S",
        "AGC": "S",
        "AGA": "R",
        "AGG": "R",
        "GTT": "V",
        "GTC": "V",
        "GTA": "V",
        "GTG": "V",
        "GCT": "A",
        "GCC": "A",
        "GCA": "A",
        "GCG": "A",
        "GAT": "D",
        "GAC": "D",
        "GAA": "E",
        "GAG": "E",
        "GGT": "G",
        "GGC": "G",
        "GGA": "G",
        "GGG": "G",
    }
    protein_result = []
    for i in range(0, len(seq), 3):
        if i + 3 > len(seq):
            break
        protein_result.append(codon_dic[seq[i : i + 3]])
    protein = "  ".join(protein_result) + "  "
    return protein


print(dna_to_protein(seq))
print(" " + dna_to_protein(seq[1:]))
print("  " + dna_to_protein(seq[2:]))

print(seq)
cmp_seq = seq.lower()
d_base = {"a": "T", "c": "G", "g": "C", "t": "A"}
for k, v in d_base.items():
    cmp_seq = cmp_seq.replace(k, v)
print(cmp_seq)

cmp_rev_seq = cmp_seq[::-1]
print(dna_to_protein(cmp_rev_seq)[::-1])
print("  " + dna_to_protein(cmp_rev_seq[1:])[::-1])
print(" " + dna_to_protein(cmp_rev_seq[2:])[::-1])
