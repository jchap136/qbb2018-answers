#!/usr/bin/env python3

"""
Usage: ./day5-lunch-#5.py <tab_file1> <tab_file2> <tab_file3> <tab_file4> <tab_file> <ctab_file>

Generate a model to see relationship between histone methylation and FPKMs
"""

import sys
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.sandbox.regression.predstd import wls_prediction_std

name1 = sys.argv[1].split(os.sep)[-1].split('.')[0] # second split by . to exclude ".tab"
tab1 = pd.read_csv(sys.argv[1], sep="\t").iloc[:, 4]

name2 = sys.argv[2].split(os.sep)[-1].split('.')[0]
tab2 = pd.read_csv(sys.argv[2], sep="\t").iloc[:, 4]

name3 = sys.argv[3].split(os.sep)[-1].split('.')[0]
tab3 = pd.read_csv(sys.argv[3], sep="\t").iloc[:, 4]

name4 = sys.argv[4].split(os.sep)[-1].split('.')[0]
tab4 = pd.read_csv(sys.argv[4], sep="\t").iloc[:, 4]

name5 = sys.argv[5].split(os.sep)[-1].split('.')[0]
tab5 = pd.read_csv(sys.argv[5], sep="\t").iloc[:, 4]

name6 = sys.argv[6].split(os.sep)[-2]
fpkms = pd.read_csv(sys.argv[6], sep="\t").iloc[:, -1]
log_fpkms = np.log(fpkms+1)

tabs = {name1 : tab1, name2 : tab2, name3 : tab3, name4 : tab4, name5 : tab5, name6 : log_fpkms}
tabs_df = pd.DataFrame(tabs)

#print(tabs_df)


mod = smf.ols(formula="{} ~ {} + {} + {} + {} + {}".format(name6, name1, name2, name3, name4, name5), data=tabs_df)
res = mod.fit()
print(res.summary())

res2 = res.resid
print(res2)

#prstd, iv_l, iv_u = wls_prediction_std(res)
fig, ax = plt.subplots()
#ax.plot(x, y, "o", label="data")
#ax.plot(x, y_true, "b-", label="True")
#ax.plot(x, res.fittedvalues, "r--.", label="OLS")
#ax.plot(x, iv_u, "r--")
#ax.plot(x, iv_l, "r--")
#ax.legend(loc="best")
n, bins, patches = plt.hist(res2, 1000, density=True, facecolor="g", alpha=0.75)
ax.set_xlim(-5,5)
ax.set_ylim(0,13)
#sns.residplot(x, y, lowess=True, color="g")
plt.xlabel("log Histone Modification Load")
plt.ylabel("mRNA Transcription (FPKM)")
fig.savefig("histone_logFPKM.png")
plt.close()





