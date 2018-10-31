#!/usr/bin/env python3

"""
Usage: ./motif_pos.py intersect2.out

find position of motif within CTCF peak
"""

import sys
import numpy as np
import matplotlib.pyplot as plt

f = open(sys.argv[1])

motif_pos = []
motif_pos_end = []
motif_percent = []
for line in f:
    fields = line.rstrip("\r\n").split()
    peak_start = int(fields[1])
    peak_end = int(fields[2])
    motif_start = int(fields[13])
    motif_end = int(fields[14])
    d_start = motif_start - peak_start
    d_end = peak_end - motif_end
    percent_start = (d_start) / (peak_end - peak_start)
    motif_pos.append(d_start)
    motif_pos_end.append(d_end)
    motif_percent.append(percent_start)
    
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(20,5))
ax1.hist(motif_pos, bins=150, color="blue", alpha=0.5, label="distance from start")
ax1.hist(motif_pos_end, bins=150, color="red", alpha=0.2, label="distance from end")
ax1.set_ylabel("frequency")
ax1.set_xlabel("motif position within CTCF binding site (nt)")
ax1.legend()
ax2.hist(motif_percent, bins=150, color="blue", label="bins = 150")#label="bins = 150")
ax2.set_ylabel("frequency")
ax2.set_xlabel("motif position within CTCF binding site (%)")
ax2.legend()
plt.show()
fig.savefig("motif_pos.png")
plt.close(fig)