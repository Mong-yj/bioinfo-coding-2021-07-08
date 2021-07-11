file_name = "sequence.nucleotide.fasta"

# sequence

# file_name =input('your sequence file? : ')
def FES(file_name):
    # FES : fasta extact sequence
    seq = list()
    with open(file_name, "r") as handle:
        for line in handle:
            if line.startswith(">"):
                continue
            line = line.strip()
            seq.append(line)
        seq_j = "".join(seq)
        return seq_j


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


def FtoAA(seq_j):
    # FtoAA : fasta to Amino Acid
    AA_li = ""
    i = 0
    while i <= len(seq_j):
        codon = seq_j[i : i + 3]
        if len(codon) == 0:
            break
        if len(codon) % 3 == 0:
            AA = codon_dic[codon]
            AA_li += AA + " " + " "
        if len(codon) % 3 != 0:
            blank = len(codon)
            AA_li += (" ") * blank
            print(blank)
        i += 3
    return AA_li


def FtoCS(seq_j):
    # FtoCS : fasta to complement sequence
    trans_seq = ""
    mrna_dict = {"A": "T", "G": "C", "C": "G", "T": "A"}
    for i in seq_j:
        trans_seq += mrna_dict[i]
    return trans_seq


# file_name = sequence.nucleotide.fasta
seq_j = FES(file_name)
seq_j_rev = FtoCS(seq_j)

print(FtoAA(seq_j))
print(" " + FtoAA(seq_j[1:]))
print(" " + " " + FtoAA(seq_j[2:]))

print(seq_j)
print(seq_j_rev)

print(FtoAA(seq_j_rev[::-1])[::-1])
print(FtoAA(seq_j_rev[::-1][1:])[::-1])
print(FtoAA(seq_j_rev[::-1][2:])[::-1])
