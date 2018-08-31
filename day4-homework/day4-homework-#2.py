#!/usr/bin/env python3

"""
Usage: ./day4-homework-#2.py <gene_name> <samples.csv> <ctab_dir>

"""

import sys
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv(sys.argv[2])
compiled = {}

for index, sample, sex, stage in df.itertuples():
    #name = (sample + "_" + stage)
    filename = os.path.join(sys.argv[3], sample, "t_data.ctab") # join
    ctab_df = pd.read_table(filename, index_col="t_name")
    #compiled[sex + "_" + stage] = ctab_df.loc[sys.argv[1], "FPKM"]
    #fpkms.append(ctab_df.loc[sys.argv[1], "FPKM"])
    gene_id = sys.argv[1]
    roi = ctab_df.loc[:, "gene_name"] == sys.argv[1]
    #values = df.loc["FPKM", roi]
    compiled = ctab_df.loc[roi, "FPKM"]
    compiled_df = pd.DataFrame(compiled)
    #return compiled_df
print(compiled_df)
average = compiled_df.mean(axis = 1)


#f_value = females.loc["FBtr0331261", :]
#m_value = males.loc["FBtr0331261", :]

fig, ax = plt.subplots()
ax.scatter(list(compiled_df.index), list(average), alpha = 0.5, color="red")
#ax.plot(list(males), m_value, alpha = 0.5, color="blue")
ax.set_title(gene_id)
ax.tick_params(bottom=False, left=False)
plt.xticks(rotation=90)
plt.xlabel("Transcript")
plt.ylabel("Average mRNA abundance (FPKM)")
plt.tight_layout()
fig.savefig("gene.png")
plt.close(fig)