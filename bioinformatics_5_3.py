with open("sequence.nucleotide.fasta","r") as handle:
    seq =[]
    for line in handle:
        if line.strip().startswith(">"):
            continue
        seq.append(line.strip())
    seq = "".join(seq)

codon_dic = {
            'TTT':'F', 'TTC':'F', 'TTA':'L', 'TTG':'L',
            'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S',
            'TAT':'Y', 'TAC':'Y', 'TAA':'*', 'TAG':'*',
            'TGT':'C', 'TGC':'C', 'TGA':'*', 'TGG':'W',
            'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L',
            'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
            'CAT':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Q',
            'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R',
            'ATT':'I', 'ATC':'I', 'ATA':'I', 'ATG':'M',
            'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
            'AAT':'N', 'AAC':'N', 'AAA':'K', 'AAG':'K',
            'AGT':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R',
            'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
            'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
            'GAT':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E',
            'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
            }

for i in range(0,len(seq),3):
    if i+3 > len(seq):
        break
    print(codon_dic[seq[i:i+3]],end="  ")
print()

print(" ",end="")
for i in range(1,len(seq),3):
    if i+3 > len(seq):
        break
    print(codon_dic[seq[i:i+3]],end="  ")
print()

print("  ",end="")
for i in range(2,len(seq),3):
    if i+3 > len(seq):
        break
    print(codon_dic[seq[i:i+3]],end="  ")
print()

print(seq)
cmp_seq = seq.lower()
d_base = {"a":"T","c":"G","g":"C","t":"A"}
for k,v in d_base.items():
    cmp_seq = cmp_seq.replace(k,v)
print(cmp_seq)

rev_1 = []
for i in range(len(cmp_seq)-1,0,-3):
    if i-3 < 0:
        if i == 2:
            rev_1.append(codon_dic[cmp_seq[i::-1]])
        break
    rev_1.append(codon_dic[cmp_seq[i:i-3:-1]])
stop = (len(cmp_seq) % 3)+2
print(" "*stop + "  ".join(rev_1[::-1]))

for i in range(len(cmp_seq)-2,-1,-3):
    if i-3 < 0:
        if i == 2:
            rev_1.append(codon_dic[cmp_seq[i::-1]])
        break
    rev_1.append(codon_dic[cmp_seq[i:i-3:-1]])
stop = ((len(cmp_seq)-1) % 3)+2
print(" "*stop + "  ".join(rev_1[::-1]))

for i in range(len(cmp_seq)-3,-1,-3):
    if i-3 < 0:
        if i == 2:
            rev_1.append(codon_dic[cmp_seq[i::-1]])
        break
    rev_1.append(codon_dic[cmp_seq[i:i-3:-1]])
stop = ((len(cmp_seq)-2) % 3)+2
print(" "*stop + "  ".join(rev_1[::-1]))

