#!/usr/bin/env python3

# match kmers

import sys
import fasta

target = open(sys.argv[1]) # subset.fa
query = open(sys.argv[2]) # droYak2_seq.fa
k = int(sys.argv[3]) # use 11

reader = fasta.FASTAReader(target) # use target file (subset.fa)

target_dict = {}

for ident, sequence in reader:
    for i in range(0, len(sequence)-k):
        kmer = sequence[i:i+k]
        if kmer not in target_dict:
            target_dict[kmer] = [(ident, i)] # kmer as key, gene name and start pos as value 
        else:
            target_dict[kmer].append((ident, i)) # add tuple in list
            
# for key in target_dict:
#    print(key, target_dict[key])

reader2 = fasta.FASTAReader(query) # use query file (droYak2_seq)
for ident, sequence in reader2:
    for j in range(0, len(sequence)-k):
        kmer2 = sequence[j:j+k]
        if kmer2 in target_dict.keys(): # find matching kmers from dictonary
            for hit in target_dict[kmer2]:
                print(hit[0], hit[1], j, kmer2) # print gene name, start pos, query start, kmer 