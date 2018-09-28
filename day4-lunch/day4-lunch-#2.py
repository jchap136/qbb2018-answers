#!/usr/bin/env python3

"""
Usage: ./day4-lunch-#2.py <ctab1> <ctab2>

plot FPKM1 on x-axis and FPKM2 on y-axis
"""

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

df1 = pd.read_csv(sys.argv[1], sep="\t", index_col="t_name")
df2 = pd.read_csv(sys.argv[2], sep="\t", index_col="t_name")

fpkm1 = df1.loc[:, "FPKM"]
fpkm1_m = fpkm1 + 0.25
fpkm2 = df2.loc[:, "FPKM"]
fpkm2_m = fpkm2 + 0.25

fig, ax = plt.subplots()
ax.scatter(fpkm1_m, fpkm2_m, alpha = 0.025, color="red")
plt.yscale("log")
plt.xscale("log")
#plt.xlim(xmin=1)
#plt.ylim(ymin=1)
ax.set_title("FPKM2 vs FPKM1") # y vs x
plt.xlabel("log(FPKM1)")
plt.ylabel("log(FPKM2)")
#plt.axis([0.001, 10000, 0.001, 10000])
#axes = plt.gca()
# polyfit stuff
x = fpkm1_m
y = fpkm2_m
coef = np.polyfit(x, y, 1) # 1 is the degree, so this is linear
fit = np.poly1d(coef) # returns the usable function
space = np.linspace(0,10000) # range of data
plt.plot(space, fit(space), '-', color='b') # plot data
plt.text(900, 30, str(fit))

fig.savefig("fpkm.png")
plt.close(fig)