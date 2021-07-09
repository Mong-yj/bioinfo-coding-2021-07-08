fasta_file = input("Enter input file: ")
fasta_output = input("Enter output file: ")

print("Option-1) Read a FASTA format DNA sequence file and make a reverse sequence file.")
print("Option-2) Read a FASTA format DNA sequence file and make a reverse complement sequence file.")
print("Option-3) Convert GenBank format file to FASTA format file.")
option = int(input("Select the option: "))

seq = []
with open(fasta_file,"r") as handle:
    for line in handle:
        if line.startswith(">"):
            header = line
        else:
            seq.append(line.strip())
    seq = "".join(seq)
    rev_seq = seq[::-1]

if option == 1:
    with open(fasta_output,"w") as handle:
        handle.write(header)
        for i in range(0,len(rev_seq),70):
            handle.write(rev_seq[i:i+70])
            handle.write("\n")
elif option == 2:
    d_comp = {"a":"T","g":"C","c":"G","t":"A"}
    cmp_rev_seq = rev_seq.lower()
    for k,v in d_comp.items():
        cmp_rev_seq = cmp_rev_seq.replace(k,v)
    with open(fasta_output,"w") as handle:
        handle.write(header)
        for i in range(0,len(cmp_rev_seq),70):
            handle.write(cmp_rev_seq[i:i+70])
            handle.write('\n')
elif option == 3:
    with open(fasta_file,"r") as handle:
        content = handle.readlines()

    for i in range(len(content)):
        if i == 0:
            title = content[i]
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

    with open(fasta_output,"w") as handle:
        handle.write(title)
        for i in range(0,len(seq_result),70):
            handle.write(seq_result[i:i+70])
            handle.write('\n')
