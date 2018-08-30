#!/usr/bin/env python3

"""
Usage: ./day4-lunch-#1.py <threshold> <ctab1> <ctab2> ...

combine FPKM values from >= 2 ctab files and report transcripts when total FPKM is > threshold
"""

import sys
import os
import pandas as pd
import numpy as np


arg = len(sys.argv)
my_dict = {}

for i in range(2, arg):
    fpkm = pd.read_csv(sys.argv[i], sep="\t", index_col="t_name").loc[:, "FPKM"]
    name = sys.argv[i].split(os.sep)[-2]
    my_dict[name] = fpkm
    
fpkms = pd.DataFrame(my_dict)
#fpkms.to_csv(sys.stdout)


total = fpkms.sum(axis = 1)
#print(total)

threshold = float(sys.argv[1])
with_threshold = total > threshold

results = total.index[with_threshold==True]
print(total, results)

#total.loc[:, roi].to_csv(sys.stdout, sep="\t", index=False)




    