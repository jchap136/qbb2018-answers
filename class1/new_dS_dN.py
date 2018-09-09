#!/usr/bin/env python3

"""
Usage: ./aa_to_nt.py <seqs.fa> <aligned_aa.fa>

After converting aa back to nt, get dN and dS values
"""

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import fasta
import itertools

dna_reader = fasta.FASTAReader(open(sys.argv[1]))
aa_reader = fasta.FASTAReader(open(sys.argv[2]))

all_nt = []
all_aa = []

# this first for loop iterates through sequence by sequence
for (dna_id, dna), (aa_id, aa) in zip(dna_reader, aa_reader): # zip iterates through 2 files at once
    nuclist = []
    aa_list = []
    j = 0
    # this for loop iterates through each aa within a sequence
    for i in range(len(aa)):      
        a = aa[i]
        aa_list.append(a)
        nt = dna[j*3:(j*3)+3]
        if a == "-":
            nuclist.append("---")
        else:
            nuclist.append(nt)
            j += 1 # only increase when aa exists, otherwise lose nt
    all_nt.append(nuclist) # append list into bigger list
    all_aa.append(aa_list) # append list into bigger list

# so each nuclist is a list of codons, and it gets appended to all_nt each time, so each list within all_nt list
# is a different sequence
#print(all_nt)
#print(all_aa)

ref_nuc = all_nt[0] # first sublist in list is reference
ref_aa = all_aa[0] # first sublist in list is reference
biglist = [] # list of lists

for protein, seq in zip(all_aa[1:], all_nt[1:]): # iterate through each sequence
    dS = 0
    dN = 0
    none = 0   
    for (amino_acid, codon, ref_amino_acid, ref_codon) in zip(protein, seq, ref_aa, ref_nuc):
        if amino_acid != ref_amino_acid:
            dN += 1
        elif codon != ref_codon:
            dS += 1
        else:
            none += 1          
    biglist.append([dS, dN, none])
       
for i in range(len(biglist)):     
    print("dS: ", str(biglist[i][0]))
    print("dN: ", str(biglist[i][1]))
    print("none: ", str(biglist[i][2]))

values = []
for i in biglist:
    values.append(i[1] / i[0])
    
plt.plot(values)
plt.xlabel('dN/dS')
plt.ylabel('Codon Position')
plt.title('dN/dS for each Sequence')
plt.savefig("dS_dN.png")
plt.close()

