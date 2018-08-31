#!/usr/bin/env python3

"""
Usage: ./04-day4-homework-#1.py <samples.csv> <ctab_dir>

Create .csv with FPKMs from all 16 samples in samples.csv formatted differently
"""

import sys
import pandas as pd
import os
import matplotlib.pyplot as plt

df = pd.read_csv(sys.argv[1])
#soi = df.loc[:, "sex"] == sys.argv[3]
#df = df.loc[soi, :]

compiled = {}


for index, sample, sex, stage in df.itertuples():
    filename = os.path.join(sys.argv[2], sample, "t_data.ctab") # join
    ctab_df = pd.read_table(filename, index_col="t_name")
    #fpkms.append(ctab_df.loc[:, "FPKM"])
    compiled[sex + "_" + stage] = ctab_df.loc[:, "FPKM"]

compiled_df = pd.DataFrame(compiled)
    
compiled_df.to_csv(sys.stdout)
#print(compiled_df)


"""
fig, ax = plt.subplots()
ax.plot(fpkms)
fig.savefig("timecourse.png")
plt.close(fig)
"""