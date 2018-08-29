#!/usr/bin/env python3

# run this python command followed by file

import sys

if len(sys.argv) > 1:
    f = open(sys.argv[1])
else:
    f = sys.stdin
    
interest = 21378950 # region of interest

#protein coding
closest_dist = 100000000000
my_dist = 0
closest_name = ""
#non protein coding
closest_dist_n = 1000000000000
my_dist_n = 0
closest_name_n = ""

for line in f:
    fields = line.rstrip("\r\n").split()
    if line.startswith("#"):
        continue
    if fields[2] == "gene" and fields[0] == "3R": # only looking for genes in chromosome 3R
        start = int(fields[3]) # start position
        end = int(fields[4]) # end position
        
        if "protein_coding" in line: # protein coding genes
            if start > interest:
                my_dist = start - interest # my_dist is a number now
            elif end < interest:
                my_dist = interest - end # my_dist is a number now
            if my_dist < closest_dist:
                closest_dist = my_dist # now we will override closest_dist with my_dist if lower
                closest_name = fields[13] # list gene name is my_dist is lower
                
        if "protein_coding" not in line: # non-protien coding genes, same thing as above
            if start > interest:
                my_dist_n = start - interest
            elif end < interest:
                my_dist_n = interest - end
            if my_dist_n < closest_dist_n:
                closest_dist_n = my_dist_n
                closest_name_n = fields[13]

print("Closest protein coding gene and distance: ", closest_name, closest_dist)
print("Closest non-protein coding gene and distance: ", closest_name_n, closest_dist_n)
    
        