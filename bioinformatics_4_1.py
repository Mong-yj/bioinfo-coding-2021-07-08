with open("sequence.protein.gb","r") as handle:
    content = handle.readlines()

for i in range(len(content)):
    if i == 0:
        title = content[i].strip()
    elif content[i].startswith("ORIGIN"):
        seq = [i.lstrip() for i in content[i+1:]]
seq = "".join(seq)

print("title:",title)
print("seq:",seq)

