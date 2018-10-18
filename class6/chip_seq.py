#!/usr/bin/env python3

"""
Usage: ./chip_seq.py ctcf_gained.bed ctcf_lost.bed Mus_muculus.GRCm38.94_features.bed

4 ChIP-seq data, input_G1E, CTCF_G1E, input_ER4, CTCF_ER4
the ER4 cell line is the differetiated form of G1E
we used bowtie2-build and bowtie2 to align the reads back to the ref_genome (mm10, chr19)
then we used macs2 to call peaks and got 2 .narrowPeak files
then we used bedtools on the .narrowPeak files to see which CTCF sites were gained in ER4 and lost in ER4 cells
now we want to make 2 bar plots, 1 plots number of sites gained, and other plots if sites are exons, introns, etc.
"""

import sys
import matplotlib.pyplot as plt
import numpy as np

f1 = open(sys.argv[1])
f2 = open(sys.argv[2])
f3 = open(sys.argv[3])

# make dictionary with key as bp and value as exon/intron/promoter
feature_dict = {}
for line in f3:
    fields = line.rstrip("\r\n").split("\t")
    start = int(fields[1])
    end = int(fields[2])
    feature = fields[3]
    #print(start, end, feature)
    for bp in range(start, end):
        feature_dict[bp] = feature
#print(feature_dict)

# plot number of CTCF sites lost and gained in ER4 cells from G1E cells
# also see what that site is by referencing dictionary
sites_gained = 0
features_gained = []
for i, line in enumerate(f1):
    sites_gained += 1
    fields = line.rstrip("\r\n").split("\t")
    g_start = int(fields[1])
    g_end = int(fields[2])
    for bp in range(g_start, g_end):
        if bp in feature_dict:
            g_feat = feature_dict[bp]
            features_gained.append(g_feat)
#print(features_gained)
gained_dict = {i:features_gained.count(i) for i in features_gained}
#print(gained_dict)


sites_lost = 0
features_lost = []
for i, line in enumerate(f2):
    sites_lost += 1
    fields = line.rstrip("\r\n").split("\t")
    l_start = int(fields[1])
    l_end = int(fields[2])
    for bp in range(l_start, l_end):
        if bp in feature_dict:
            l_feat = feature_dict[bp]
            features_lost.append(l_feat)
#print(features_lost)
lost_dict = {i:features_lost.count(i) for i in features_lost}
#print(lost_dict)

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(20,5))
ax1.bar(range(len(gained_dict)), list(gained_dict.values()), align='center', color="r", label="CTCF sites gained in ER4 cells")
ax1.set_xticks(range(len(gained_dict)), list(gained_dict.keys()))
ax1.bar(range(len(lost_dict)), list(lost_dict.values()), align='center', color="b", label="CTCF sites lost in ER4 cells")
#ax1.set_xticks(range(len(lost_dict)), list(lost_dict.keys()))
ax1.set_ylabel("Number of bp")
ax1.set_title("Number of bp for each type of region in ER4 or G1E cells")
ax1.legend()
ax2.bar(0, sites_gained, width=0.1, color="r", align="center", label="CTCF sites gained in ER4 cells")
ax2.bar(.25, sites_lost, width=0.1, color="b", align="center", label="CTCF sites lost in ER4 cells")
ax2.set_xticks([])
#ax2.set_xticklabels("gained", "lost")
ax2.set_ylabel("Number of CTCF sites")
ax2.set_title("Number of CTCF binding sites gained/lost from G1E to ER4 Cells")
ax2.legend()
plt.show()
fig.savefig("chip.png")
plt.close(fig)