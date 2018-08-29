#!/usr/bin/env python3

# run this python command followed by 

import sys

if len(sys.argv) > 1:
    f = open(sys.argv[1])
else:
    f = sys.stdin
    
interest = 21378950
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
    if fields[2] == "gene" and fields[0] == "3R":
        start = int(fields[3])
        end = int(fields[4])
        
        if "protein_coding" in line:
            if start > interest:
                my_dist = start - interest
            elif end < interest:
                my_dist = interest - end
            if my_dist < closest_dist:
                closest_dist = my_dist
                closest_name = fields[13]
        if "protein_coding" not in line:
            if start > interest:
                my_dist_n = start - interest
            elif end < interest:
                my_dist_n = interest - end
            if my_dist < closest_dist:
                closest_dist_n = my_dist_n
                closest_name_n = fields[13]

print("Closest protein coding gene and distance: ", closest_name, my_dist)
print("Closest non-protein coding gene and distance: ", closest_name_n, my_dist_n)
    
        