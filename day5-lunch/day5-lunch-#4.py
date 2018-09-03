#!/usr/bin/env python3

"""
Usage: ./day5-lunch-#4.py <tab_file1> <tab_file2> <tab_file3> <tab_file4> <tab_file> <ctab_file>

Generate a model to see relationship between histone methylation and FPKMs
"""

import sys
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf

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

tabs = {name1 : tab1, name2 : tab2, name3 : tab3, name4 : tab4, name5 : tab5, name6 : fpkms}
tabs_df = pd.DataFrame(tabs)

#print(tabs_df)


mod = smf.ols(formula="{} ~ {} + {} + {} + {} + {}".format(name6, name1, name2, name3, name4, name5), data=tabs_df)
res = mod.fit()
print(res.summary())