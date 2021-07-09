with open("sequence.protein.2.fasta","r") as handle:
    content = handle.readlines()
seq = ""
for i in range(len(content)):
    if i == 0:
        title = content[i].strip()
    else:
        seq += content[i].strip()
print("title:",title)
print("seq:",seq)
