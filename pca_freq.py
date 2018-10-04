#!/usr/bin/env python3

"""
Usage: ./pca_freq.py plink.eigenvec file.vcf

make PCA plot from eigenvec file and allele frequency histogram from vcf file
"""

import sys
import matplotlib.pyplot as plt
import numpy as np

f1 = open(sys.argv[1])

p1_val = []
p2_val = []
for line in f1:
    fields = line.rstrip("\r\n").split(" ")
    p1 = fields[2]
    p1_val.append(float(p1))
    p2 = fields[3]
    p2_val.append(float(p2))

fig, ax = plt.subplots()
ax.scatter(p1_val, p2_val, color="red", alpha="0.5")
ax.set_xlabel("pca_1")
ax.set_ylabel("pca_2")
fig.savefig("pca.png")
plt.close(fig)

f2 = open(sys.argv[2])
af_val = []
for line in f2:
    if line.startswith("#"):
        continue
    fields = line.rstrip("\r\n").split("\t")
    info = fields[7]
    for id_val in info.split(";"): # why doesn't this work without ; split???
        id, val = id_val.split("=")
        if id == "AF":
            af_val.append(float(val.split(",")[0]))
    # af = fields[7].split("=")
#     af_num = af[1]
#     af_val.append(float(af_num[0]))
# for i in af_val:
#     if "," in i:
#         print(i)
    
fig, ax = plt.subplots()
ax.hist(af_val, bins=100, color="red")
fig.savefig("allele_freq.png")
plt.close(fig)