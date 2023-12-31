"""CALCULATED THE ESTIMATED MOLECULAR WEIGHT OF THE PROTEIN (IN KILODALTONS) """


PROTEIN_SEQUENCE = """MADPAAGPPPSEGEESTVRFARKGALRQKNVHEVKNHKFTARFFKQPTFCSHCTDFIWGFGKQGFQCQVC
CFVVHKRCHEFVTFSCPGADKGPASDDPRSKHKFKIHTYSSPTFCDHCGSLLYGLIHQGMKCDTCMMNVH
KRCVMNVPSLCGTDHTERRGRIYIQAHIDREVLIVVVRDAKNLVPMDPNGLSDPYVKLKLIPDPKSESKQ
KTKTIKCSLNPEWNETFRFQLKESDKDRRLSVEIWDWDLTSRNDFMGSLSFGISELQKAGVDGWFKLLSQ
EEGEYFNVPVPPEGSEGNEELRQKFERAKIGQGTKAPEEKTANTISKFDNNGNRDRMKLTDFNFLMVLGK
GSFGKVMLSERKGTDELYAVKILKKDVVIQDDDVECTMVEKRVLALPGKPPFLTQLHSCFQTMDRLYFVM
EYVNGGDLMYHIQQVGRFKEPHAVFYAAEIAIGLFFLQSKGIIYRDLKLDNVMLDSEGHIKIADFGMCKE
NIWDGVTTKTFCGTPDYIAPEIIAYQPYGKSVDWWAFGVLLYEMLAGQAPFEGEDEDELFQSIMEHNVAY
PKSMSKEAVAICKGLMTKHPGKRLGCGPEGERDIKEHAFFRYIDWEKLERKEIQPPYKPKARDKRDTSNF
DKEFTRQPVELTPTDKLFIMNLDQNEFAGFSYTNPEFVINV""".replace('\n', '')

# length of protien sequence

NO_OF_AMINOACIDS = len(PROTEIN_SEQUENCE)

# Average molecular weight of each amino acid

AVERAGE_MOLECULAR_WEIGHT = 110

#Average molecular weight of protein in daltons

AVERAGE_WEIGHT_DALTONS = NO_OF_AMINOACIDS * AVERAGE_MOLECULAR_WEIGHT

#Estimated molecular weight of protein in kilodaltons

ESTIMATED_MW_KD = AVERAGE_WEIGHT_DALTONS/1000

print("The length of Protein kinase C beta type is:", NO_OF_AMINOACIDS)

print("The average weight of this protein sequence kilodaltons is:", ESTIMATED_MW_KD)
