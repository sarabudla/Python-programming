"""calculating the length of protien sequence with the given lenght"""



import sys

# asking the user for the gene name

GENE_NAME = input("Please enter a name for the DNA sequence:")
print("your sequence name is:", GENE_NAME)

# asking the user for the number of nucleotides in its coding sequence

NUMBER_OF_NUCLEOTIDES = float(input("please enter the lenght of the sequence:"))
print("The length of the DNA sequence:", NUMBER_OF_NUCLEOTIDES)

# calculating the number of amino acids in resulting protien

if NUMBER_OF_NUCLEOTIDES % 3==0 :
    RESULTING_PROTEIN = NUMBER_OF_NUCLEOTIDES//3
    print("The length of the decoded protein is:", RESULTING_PROTEIN)

# average molecular weight of each amino acid
    AVERAGE_MOLECULAR_WEIGHT = 110

# molecular weight of the protein in daltons
    WEIGHT_IN_DALTONS = RESULTING_PROTEIN * AVERAGE_MOLECULAR_WEIGHT

# estimated molecular weight of protein in kilodaltons
    ESTIMATED_MW_IN_KD = WEIGHT_IN_DALTONS/1000

    print("The average weight of the protein sequence is:", ESTIMATED_MW_IN_KD)
else:
    print("The DNA sequence is not divisible by 3", file=sys.stderr)
    sys.exit(1)
