#!/usr/bin/env python3

"""
Usage: ./z-score2.py <z-score.out>

get z scores for each codon from
z = (Dc - Dn) / SE
Dc = dN - dS
Dn = 0 (null hypothesis)
std.error = std.dev / sqrt(amount of codons)
"""

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import fasta
import itertools



df = pd.read_csv(sys.argv[1], sep="\t")
#print(df)
df["dN-dS"] = df["dN"] - df["dS"]
#print(df)
diff = df.iloc[:,4]
#print(diff)
diff_std = diff.std()
#print(diff_std)
n = 6279
sqrt_n = np.sqrt(n)
std_error = diff_std / sqrt_n
z_test = diff / std_error
#print(z_test)
df["z_test"] = z_test
#print(df)

x_values = df.iloc[:,0]
y_values = df.iloc[:,5]

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, alpha = 0.2, color="red")
plt.ylabel('z score')
plt.xlabel('codon position')
plt.title('z score for each codon')
fig.savefig("zscores.png")
plt.close(fig)
