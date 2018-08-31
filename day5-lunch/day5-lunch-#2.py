#!/usr/bin/env python3

"""
Usage: ./day5-lunch-#2.py <ctab_file>

Get  +/-500bp from transcription start sites
Store columns as chromosomes, start, end, t_name
"""

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


compiled = {}

f = open(sys.argv[1])
for i, line in enumerate(f):
    if i == 0:
        continue
    fields = line.rstrip("\r\n").split("\t")
    ch = fields[1]
    strand = fields[2]
    start = int(fields[3])
    end = int(fields[4])
    t_name = fields[5]
    
    if strand == "+":
        start -= 500
        end = start + 1000
    if strand == "-":
        end += 500
        start = end - 1000
    if start < 0 or end < 0:
        continue
    print("{0}\t{1}\t{2}\t{3}".format(ch, start, end, t_name))

# pandas fail
"""
values = ["chr", "start", "end", "t_name"]
df = pd.read_csv(sys.argv[1], sep="\t")
for index, row in df.itertuples():
    
    if "strand" == "+":
        start = row.loc[:, "start"]
        t_start = int(start) - 500
        df.loc[index, "start"] = t_end
        end = row.loc[:, "end"]
        t_end = int(end) + 500
        df.loc[index, "end"] = t_end
    if "strand" == "-":
        start = row.loc[:, "start"]
        t_start = int(start) + 500
        df.loc[index, "start"] = t_start
        end = row.loc[:, "end"]
        t_end = int(end) - 500
        df.loc[index, "end"] = t_end

compiled[df.index] = df.loc[:, values]
"""