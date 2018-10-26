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
#features_gained = []
biglist_gained = []
for i, line in enumerate(f1):
    features_gained = []
    sites_gained += 1
    fields = line.rstrip("\r\n").split("\t")
    g_start = int(fields[1])
    g_end = int(fields[2])
    for bp in range(g_start, g_end):
        if bp in feature_dict:
            g_feat = feature_dict[bp] # get value from dictionary
            if g_feat not in features_gained:
                features_gained.append(g_feat)
    biglist_gained.append(features_gained)
    #features_gained = []    
#print((biglist_gained))
exons_gained = 0
introns_gained = 0
promoter_gained = 0
for i in biglist_gained:
    if len(i) == 0:
        continue
    for sublist in i:
        if sublist == "intron":
            introns_gained += 1
        if sublist == "exon":
            exons_gained += 1
        if sublist == "promoter":
            promoter_gained += 1
# print("gained")
# print(exons_gained)
# print(introns_gained)
# print(promoter_gained)

#gained_dict = {i:biglist_gained.count(i) for i in biglist_gained} # from stackoverflow
#print(gained_dict)
sites_lost = 0
biglist_lost = []
for i, line in enumerate(f2):
    features_lost = []
    sites_lost += 1
    fields = line.rstrip("\r\n").split("\t")
    l_start = int(fields[1])
    l_end = int(fields[2])
    for bp in range(l_start, l_end):
        if bp in feature_dict:
            l_feat = feature_dict[bp] # get value from dictionary
            if l_feat not in features_lost:
                features_lost.append(l_feat)
    biglist_lost.append(features_lost)
      
#print((biglist_gained))
exons_lost = 0
introns_lost = 0
promoter_lost = 0
for i in biglist_lost:
    if len(i) == 0:
        continue
    for sublist in i:
        if sublist == "intron":
            introns_lost += 1
        if sublist == "exon":
            exons_lost += 1
        if sublist == "promoter":
            promoter_lost += 1
            
# print("lost")
# print(exons_lost)
# print(introns_lost)
# print(promoter_lost)

#print(features_lost)
#lost_dict = {i:features_lost.count(i) for i in features_lost} # from stackoverflow
#print(lost_dict)
#counts = [sites_gained, sites_lost]
ticks = [0, 0.25]
ticks2 = [0, 1, 2]
tick_labels = ["gained", "lost"]
tick_labels2 = ["exons", "introns", "promoter"]
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(20,5))
ax1.bar(0, exons_gained, color="red", label="CTCF sites gained in ER4 cells")
ax1.bar(1, introns_gained, color="red")
ax1.bar(2, promoter_gained, color="red")
ax1.bar(0, exons_lost, color="blue", label="CTCF sites lost in ER4 cells")
ax1.bar(1, introns_lost, color="blue")
ax1.bar(2, promoter_lost, color="blue")
ax1.set_xticks(ticks2)
ax1.set_xticklabels(tick_labels2)
#ax1.bar(range(len(gained_dict)), list(gained_dict.values()), align='center', color="r", label="CTCF sites gained in ER4 cells")
#ax1.set_xticks(range(len(gained_dict)), list(gained_dict.keys()))
#ax1.bar(range(len(lost_dict)), list(lost_dict.values()), align='center', color="b", label="CTCF sites lost in ER4 cells")
#ax1.set_xticks(range(len(lost_dict)), list(lost_dict.keys()))
ax1.set_ylabel("Number of CTCF binding sites")
#ax1.xticks(range(len(gainied_dict)), range(len(lost_dict)), ("introns", "promotor", "exons"))
ax1.set_title("Number of CTCF binding sites for each type of region in ER4 or G1E cells")
ax1.legend()
ax2.bar(0, sites_gained, width=0.1, color="r", align="center", label="CTCF sites gained in ER4 cells")
ax2.bar(0.25, sites_lost, width=0.1, color="b", align="center", label="CTCF sites lost in ER4 cells")
ax2.set_xticks(ticks)
ax2.set_xticklabels(tick_labels)
ax2.set_ylabel("Number of CTCF binding sites")
ax2.set_title("Number of CTCF binding sites gained/lost from G1E to ER4 Cells")
ax2.legend()
#plt.show()
fig.savefig("chip.png")
plt.close(fig)
