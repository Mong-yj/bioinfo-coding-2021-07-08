with open("sequence.protein.2.fasta","r") as handle:
    content = handle.readlines()

seq = ""
for i in range(len(content)):
    if i == 0:
        title = content[i].strip()
    else:
        seq += content[i].strip()

while 1:
    in_amino = input("Searching for: ")
    if in_amino == "XXX":
        print("Okay, I will stop.")
        break
    else:
        amino_list = []
        for a in range(len(seq)):
            if seq[a] == in_amino:
                amino_list.append(str(a+1))
        print("Found at:",",".join(amino_list))


