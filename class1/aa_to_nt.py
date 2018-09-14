#!/usr/bin/env python3

"""
Usage: ./aa_to_nt.py <seqs.fa> <seqs_pep_mafft.fa>

convert aa to nt
"""

import sys
import pandas as pd
import fasta
import itertools

dna_reader = fasta.FASTAReader(open(sys.argv[1]))
aa_reader = fasta.FASTAReader(open(sys.argv[2]))

# these will be the list of lists
all_nt = []
all_aa = []

# this first for loop iterates through sequence by sequence
for (dna_id, dna), (aa_id, aa) in zip(dna_reader, aa_reader): # zip parses 2 files at once
    nuclist = []
    aa_list = []
    #print(aa)
    j = 0
    # this for loop iterates through each aa within a sequence
    for i in range(len(aa)):      
        a = aa[i]
        aa_list.append(a) # append aa's to a list
        nt = dna[j*3:(j*3)+3] # nt will be codons
        if a == "-":
            nuclist.append("---")
        else:
            nuclist.append(nt) # append nt's to list
            j += 1 # only increase when aa exists, otherwise lose nt
    all_nt.append(nuclist) # append list into bigger list
    all_aa.append(aa_list) # append list into bigger list

# so each nuclist is a list of codons, and it gets appended to all_nt each time, so each list within all_nt list
# is a different sequence
print(all_nt)
#print(all_aa)