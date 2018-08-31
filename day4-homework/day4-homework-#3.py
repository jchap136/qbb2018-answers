#!/usr/bin/env python3

"""
Usage: ./day4-homework-#3.py <gene_name> <gene_name> ...

"""

import sys
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("~/qbb2018/samples.csv")

for i in range(1, len(sys.argv)):
    compiled = {}
    
    for index, sample, sex, stage in df.itertuples():
        #name = (sample + "_" + stage)
        filename = os.path.join("~/data/results/stringtie", sample, "t_data.ctab") # join
        ctab_df = pd.read_table(filename, index_col="t_name")
        #compiled[sex + "_" + stage] = ctab_df.loc[sys.argv[1], "FPKM"]
        #fpkms.append(ctab_df.loc[sys.argv[1], "FPKM"])
        roi = ctab_df.loc[:, "gene_name"] == sys.argv[i]
        #values = df.loc["FPKM", roi]
        compiled = ctab_df.loc[roi, "FPKM"]
        compiled_df = pd.DataFrame(compiled)
        #return compiled_df

        average = compiled_df.mean(axis = 1)
    

        fig, ax = plt.subplots()
        ax.scatter(list(compiled_df.index), list(average), alpha = 0.5, color="red")
        #ax.plot(list(males), m_value, alpha = 0.5, color="blue")
        ax.set_title(sys.argv[i])
        ax.tick_params(bottom=False, left=False)
        plt.xticks(rotation=90)
        plt.xlabel("Transcript")
        plt.ylabel("mRNA abundance (FPKM)")
        plt.tight_layout()
        fig.savefig("".join(["gene_", sys.argv[i], ".png"]))
        plt.close(fig)