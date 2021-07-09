with open("sequence.protein.fasta","r") as handle:
    content = handle.readlines()

with open("sequence.protein.2.fasta","w") as handle:
    for line in content:
        handle.write(line)

