#!/usr/bin/env python3

"""
Usage: ./day4-homework-#1.1.py <t_name> <samples.csv> <ctab_dir> <replicates.csv>

Create a timecourse of a given transcript (FBtr0331261) for females
"""

import sys
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

def sex_ab(gender):
    #df1 = pd.read_csv(sys.argv[2])
    #df2 = pd.read_csv(sys.argv[4])
    #df = pd.concat([df1, df2]) # combining both files together
    df = pd.read_csv(sys.argv[2])
    compiled = {}
    soi = df.loc[:, "sex"] == gender
    df = df.loc[soi, :]
    #fpkms = []
    for index, sample, sex, stage in df.itertuples():
        name = stage
        #name = (sample + "_" + stage)
        filename = os.path.join(sys.argv[3], sample, "t_data.ctab") # join
        ctab_df = pd.read_table(filename, index_col="t_name")
        #compiled[sex + "_" + stage] = ctab_df.loc[sys.argv[1], "FPKM"]
        #fpkms.append(ctab_df.loc[sys.argv[1], "FPKM"])
        transcript_id = sys.argv[1]
        roi = ctab_df.index == transcript_id
        compiled[name] = ctab_df.loc[roi, "FPKM"]
    compiled_df = pd.DataFrame(compiled)
    return compiled_df

females = sex_ab("female")
print(females)
males = sex_ab("male")
print(males)

f_value = females.loc["FBtr0331261", :]
m_value = males.loc["FBtr0331261", :]

fig, ax = plt.subplots()
ax.plot(list(females), f_value, alpha = 0.5, color="red")
ax.plot(list(males), m_value, alpha = 0.5, color="blue")
ax.set_title("Sxl")
ax.tick_params(bottom=False, left=False)
plt.xticks(rotation=90)
plt.xlabel("developmental stage")
plt.ylabel("mRNA abundance (FPKM)")
#red = mpatches.Patch(color='red', label='Females')
#blue = mpatches.Patch(color='blue', label='Males')
#plt.legend(handles=[red])
#plt.legend(handels=[blue])
ax.legend(bbox_to_anchor=(1.05,0.5), loc=2, borderaxespad=0, labels=['female','male'])
plt.tight_layout()
fig.savefig("Sxl.png")
plt.close(fig)
