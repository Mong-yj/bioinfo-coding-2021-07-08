with open("sequence.nucleotide.gb","r") as handle:
    l = 0
    seq = []
    seq_line = 100
    for line in handle:
        l+=1
        if line.startswith("ORIGIN"):
            seq_line = l+1
            seq = []
        if l >= seq_line:
            seq.append(line.lstrip())
        if "CDS" in line and ".." in line:
            info = ""
            for i in line:
                if i.isnumeric() or i == ".":
                    info += i
start, end = info.split("..")

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

seq = "".join(seq)
seq_line = seq.split("\n")
seq_result = ""
for line in seq_line:
    seq_list = line.split(" ")
    if len(seq_list) < 2:
        continue
    seq_result += "".join(seq_list[1:])
seq_result = seq_result.upper()

cds_seq = seq_result[int(start)-1:int(end)]
for i in range(0,len(cds_seq),3):
    if i+3 > len(cds_seq):
        break
    print(codon_dic[cds_seq[i:i+3]],end="")
print()
