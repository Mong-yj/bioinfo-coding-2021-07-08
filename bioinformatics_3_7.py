with open("sequence.protein.2.fasta","r") as handle:
    content = handle.readlines()
seq = ""
for i in range(len(content)):
    if i == 0:
        title = content[i].strip()
    else:
        seq += content[i].strip()

while 1:
    in_pos = input("Position: ")
    if in_pos == "XXX":
        print("Okay, I will stop.")
        break
    else:
        in_pos = int(in_pos)
        print(seq[in_pos-1:in_pos+2])



