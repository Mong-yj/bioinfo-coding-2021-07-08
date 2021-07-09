with open("sequence.nucleotide.gb","r") as handle:
    content = handle.readlines()    

title = []
for i in range(len(content)):
    if "TITLE" in content[i]:
        t = [content[i].rstrip()]
        ws_idx = content[i].index("T")
        for line in content[i+1:]:
            if line[:ws_idx+1] == " "*(ws_idx+1):
                t.append(" "+content[i+1].strip())
            else:
                break
        title.append("".join(t))
for t in range(len(title)):
    if t == 0:
        continue
    else:
        title[t] = " "*(ws_idx+5)+title[t][ws_idx+5:]

title = "\n".join(title)
print(title)
