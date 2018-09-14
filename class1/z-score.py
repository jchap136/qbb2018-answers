#!/usr/bin/env python3

"""
Usage: ./z-score.py <seqs.fa> <seqs_pep_mafft.fa>

After converting aa back to nt, get dN and dS values, and print out nice tabbed list
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

class FindMutations:
    def __init__(self):
        self.dN = 0
        self.dS = 0
        self.none = 0
    def add_dN(self):
        self.dN += 1
    def add_dS(self):
        self.dS += 1
    def add_none(self):
        self.none += 1

ref_nuc = all_nt[0] # first sublist in list is reference
ref_aa = all_aa[0] # first sublist in list is reference
biglist = [FindMutations() for i in range(len(ref_aa))]

for protein, seq in zip(all_aa[1:], all_nt[1:]): # iterate through each sequence   
    for (amino_acid, codon, ref_amino_acid, ref_codon, entry) in zip(protein, seq, ref_aa, ref_nuc, biglist):
        if amino_acid != ref_amino_acid:
            entry.add_dN()
        elif codon != ref_codon:
            entry.add_dS()
        else:
            entry.add_none()

print("codon" + "\t" + "dS" + "\t" + "dN" + "\t" + "no change")
for i in range(len(biglist)):
    print(str(i) + "\t" + str(biglist[i].dS) + "\t" + str(biglist[i].dN) + "\t", str(biglist[i].none))
# for i in range(len(biglist)):
#     print("dS: ", str(biglist[i].dS))
#     print("dN: ", str(biglist[i].dN))
#     print("none: ", str(biglist[i].none))

"""
y_values = []
x_values = []
for i, line in enumerate(biglist):
    if line.dS == 0:
        line.dS = line.dS + 0.000001
    y_values.append(line.dN / line.dS)
    x_values.append(i)
   
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, alpha = 0.2, color="red")
#plt.clim(0,3)
#plt.plot(y_values)
#ax.set_title('z score for each codon')
plt.ylabel('z score')
plt.xlabel('Codon Position')
plt.title('z score for each codon')
fig.savefig("zscore.png")
plt.close(fig)
"""