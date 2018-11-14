#!/usr/bin/env python3

"""
Usage: ./cluster.py rna-seq.txt

find position of motif within CTCF peak
"""

import sys
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import pandas as pd
import seaborn as sns


f = open(sys.argv[1])
#df = pd.read_csv(sys.argv[1], index_col=0) # treat first column as index
data = pd.read_csv(f, sep="\t", index_col='gene')
df = pd.DataFrame(data)
#df_array = np.array(df)
#print(df["CFU"])
#cmap = sns.diverging_palette(220, 20, sep=20, as_cmap=True)
#https://python-graph-gallery.com/404-dendrogram-with-heat-map/
ax = sns.clustermap(df, metric="euclidean", standard_scale=1, method="ward", cmap="Reds")
#plt.show()
ax.savefig("cluster.png")
plt.close()

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=4)
kmeans.fit(df)
y_kmeans = kmeans.predict(df)

plt.figure()
plt.title("k-means plot")
plt.scatter(df["CFU"], df['poly'], c=y_kmeans, s=5, cmap='viridis')
plt.ylabel("poly expression")
plt.xlabel("CFU expression")
plt.savefig("kmeans.png")
plt.close()