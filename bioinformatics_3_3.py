with open("sequence.protein.fasta","r") as handle:
    for line in handle:
        print(line.strip())
