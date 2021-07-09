with open("sequence.protein.2.fasta",'r') as handle:
    content = handle.readlines()
print("The second line is: "+content[1].strip())
