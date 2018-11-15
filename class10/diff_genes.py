#!/usr/bin/env python3

"""
Usage: ./cluster.py rna-seq.txt rna-seq.txt

get most upregulated gene with p-val < 0.05, then get genes from that cluster
"""

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans

f = open(sys.argv[1])

name_list = []
upregulated_num = 0
upregulated_gene = "none"
for i, line in enumerate(f):
    if i == 0:
        continue
    fields = line.rstrip("\r\n").split("\t")
    name = fields[0]
    cfu = float(fields[1])
    mys = float(fields[5])
    poly = float(fields[2])
    unk = float(fields[3])
    late_avg = (poly+unk)/2
    early_avg = (cfu+mys)/2
    fold_change = late_avg / early_avg
    t_test, p_val = stats.ttest_ind([cfu, mys], [poly, unk])
    if fold_change > 2 or fold_change < 0.5 and p_val < 0.05:
        name_list.append([name, p_val])
        if fold_change > upregulated_num:
            upregulated_num = fold_change
            upregulated_gene = name
        # print(p_val)
#print(name_list)
#print(len(name_list))
file1 = open('diff_genes.txt','w')
for i, word in enumerate(name_list):
    if i == 0:
        #print("gene name", "\t", "p-value")
        file1.write("gene name")
        file1.write("\t")
        file1.write("p-value")
        file1.write("\n")
    #print(name_list[i][0], "\t", name_list[i][1])
    file1.write(str(name_list[i][0]))
    file1.write("\t")
    file1.write(str(name_list[i][1]))
    file1.write("\n")
file1.close()
    
### up to this point, > to .txt file, then start code below ###
    
#print("\n", "gene: ", upregulated_gene, "\n", "fold change: ", upregulated_num)

# kmeans code from cluster.py, so I can get genes with similar expression from kmeans output
f2 = open(sys.argv[2])
data = pd.read_csv(f2, sep="\t", index_col='gene')
df = pd.DataFrame(data)
kmeans = KMeans(n_clusters=4)
kmeans.fit(df)
y_kmeans = kmeans.predict(df)
ribo_cluster = y_kmeans[2] # cluster 2 is the cluster that upregulated_gene is in
sim_genes = df.index[y_kmeans == ribo_cluster] # pull out genes in that cluster
#print(sim_genes)
#print(df.index)
sim_list = []
for j in sim_genes:
    sim_list.append(j)
# print(sim_list)
# print(len(sim_list))
file2 = open('similar_genes.txt','w')
file2.write("most upregulated gene: ")
file2.write(str(upregulated_gene))
file2.write("\n")
file2.write("fold change: ")
file2.write(str(upregulated_num))
file2.write("\n")
file2.write("genes in same kmeans cluster (n_clusters=4)")
file2.write("\n")
for k in sim_list:
    #print(k)
    file2.write(k)
    file2.write("\n")
file2.close()

    