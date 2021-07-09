with open("sequence.nucleotide.fasta","r") as handle:
    seq =[]
    for line in handle:
        if line.strip().startswith(">"):
            continue
        seq.append(line.strip())
    seq = "".join(seq)
for i in range(0,len(seq),3):
    print(seq[i:i+3])
