d_codon = {}
while 1:
    in_key = input("Enter three-base codon to build: ")
    if in_key == "XXX":
        print("Okay, I will switch.")
        break
    else:
        in_value = input("Enter amino acid: ")
    d_codon[in_key] = in_value

while 1:

    in_codon = input("Enter three-base codon to search: ")
    if in_codon == "XXX":
        print("Okay, I will stop.")
        break
    else:
        print("Amino acid for %s: %s"%(in_codon,d_codon[in_codon]))
