#!/usr/bin/env python3

"""
Usage: ./day4-homework-#4.1.py <samples.csv> <ctab_dir> <replicates>

Create a timecourse of a given transcript (FBtr0331261) for females
"""

import sys
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

def sex_ab(gender):
    df1 = pd.read_csv(sys.argv[1])
    df2 = pd.read_csv(sys.argv[2])
    df = pd.concat([df1, df2]) # combining both files together
    #df = pd.read_csv(sys.argv[1])
    compiled = {}
    soi = df.loc[:, "sex"] == gender
    df = df.loc[soi, :]
    #fpkms = []
    for index, sample, sex, stage in df.itertuples():
        #name = stage
        name = (sample + "_" + stage)
        filename = os.path.join(sys.argv[3], sample, "t_data.ctab") # join
        ctab_df = pd.read_table(filename, index_col="t_name")
        #compiled[sex + "_" + stage] = ctab_df.loc[sys.argv[1], "FPKM"]
        #fpkms.append(ctab_df.loc[sys.argv[1], "FPKM"])
        #transcript_id = sys.argv[1]
        #roi = ctab_df.index == transcript_id
        compiled[name] = ctab_df.loc[:, "FPKM"]
    compiled_df = pd.DataFrame(compiled)
    return compiled_df

females = sex_ab("female")
f_value = females.iloc[:, 2]
f_value += 0.5
print(females)
males = sex_ab("male")
m_value = males.iloc[:, 2]
m_value += 0.5
print(males)

#f_value = s_females.loc["FBtr0331261", :]
#m_value = s_males.loc["FBtr0331261", :]

y_axis = np.log2(f_value/m_value)
x_axis = np.log10(np.sqrt(m_value + f_value))

fig, ax = plt.subplots()
ax.scatter(x_axis, y_axis, alpha = 0.1, color="red")

ax.set_title("MA Plot")
plt.xlabel("Average log10 mRNA abundance (FPKM)")
plt.ylabel("log2 Ratio")
fig.savefig("ma.png")
plt.close(fig)
