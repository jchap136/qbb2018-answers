#!/usr/bin/env python3

# run this python command followed by file

import sys

if len(sys.argv) > 1:
    f = open(sys.argv[1])
else:
    f = sys.stdin
    
    
gene_type = {}

for line in f:
    fields = line.rstrip("\r\n").split()
    if line.startswith("#"):
        continue
    if fields[2] != "gene":
        continue
    for i, column in enumerate(fields):
        if column  == "gene_biotype":
            typ = fields[i+1]
            if typ in gene_type:
                gene_type[typ] += 1
            else:
                gene_type[typ] = 1

for name, value in gene_type.items():
    print(name, value)
        