with open("sequence.protein.gb","r") as handle:
    content = handle.readlines()

for i in range(len(content)):
    if i == 0:
        title = content[i].strip()
    elif content[i].startswith("ORIGIN"):
        seq = [i.lstrip() for i in content[i+1:]]
seq = "".join(seq)

seq_line = seq.split("\n")
seq_result = ""
for line in seq_line:
    seq_list = line.split(" ")
    if len(seq_list) < 2:
        continue
    seq_result += "".join(seq_list[1:])
print(seq_result)
