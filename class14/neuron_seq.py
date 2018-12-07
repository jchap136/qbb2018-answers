#!/usr/bin/env python3

"""
Usage: ./neuron_seq.py

analyze RNA-seq data
"""

import sys
#import matplotlib.pyplot as plt
import numpy
import matplotlib
matplotlib.use("Agg")
import scanpy.api as sc

sc.settings.autoshow = False

# Read 10x dataset
adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
# Make variable names (in this case the genes) unique
adata.var_names_make_unique()

sc.tl.pca(adata)
#sc.pl.pca(adata, save="_unfiltered.png")

# filter adata
filtered = sc.pp.recipe_zheng17(adata, copy=True)
#sc.pl.pca(adata, save="_filtered.png")
### this is what sc.pp.recipe_zheng17 does ###
# sc.pp.filter_genes(adata, min_counts=1)  # only consider genes with more than 1 count
# sc.pp.normalize_per_cell(                # normalize with total UMI count per cell
#      adata, key_n_counts='n_counts_all')
# filter_result = sc.pp.filter_genes_dispersion(  # select highly-variable genes
#     adata.X, flavor='cell_ranger', n_top_genes=n_top_genes, log=False)
# adata = adata[:, filter_result.gene_subset]     # subset the genes
# sc.pp.normalize_per_cell(adata)          # renormalize after filtering
# if log: sc.pp.log1p(adata)               # log transform: adata.X = log(adata.X + 1)
# sc.pp.scale(adata)                       # scale to unit variance and shift to zero mean
###
sc.pp.neighbors(filtered, n_neighbors=15, n_pcs=50)
sc.tl.louvain(filtered)
sc.tl.tsne(adata)
sc.pl.tsne(adata, save="_tsne.png")
sc.tl.umap(adata)
sc.pl.umap(adata, save="_umap.png")

sc.tl.rank_genes_groups(filtered, groupby='louvain', method='t-test')
sc.pl.rank_genes_groups(filtered, save='_ttest.png')
sc.tl.rank_genes_groups(filtered, groupby='louvain', method= 'logreg')
sc.pl.rank_genes_groups(filtered, save='_logreg.png')

# generate cluster maps based on highest gene in each cluster in t-test
sc.tl.tsne(filtered)
sc.pl.tsne(filtered, color = ["louvain", "Igfbpl1"], save="_tsne0.png")
sc.pl.tsne(filtered, color = ["louvain", "Tmsb10"], save="_tsne1.png")
sc.pl.tsne(filtered, color = ["louvain", "Tuba1a"], save="_tsne2.png")
sc.pl.tsne(filtered, color = ["louvain", "Dbi"], save="_tsne3.png")
sc.pl.tsne(filtered, color = ["louvain", "Tmsb10"], save="_tsne4.png")
sc.pl.tsne(filtered, color = ["louvain", "Gm42418"], save="_tsne5.png")
sc.pl.tsne(filtered, color = ["louvain", "Tuba1a"], save="_tsne6.png")
sc.pl.tsne(filtered, color = ["louvain", "mt-Atp6"], save="_tsne7.png")
sc.pl.tsne(filtered, color = ["louvain", "Malat1"], save="_tsne8.png")
sc.pl.tsne(filtered, color = ["louvain", "Tmsb4x"], save="_tsne9.png")
sc.pl.tsne(filtered, color = ["louvain", "Tuba1a"], save="_tsne10.png")



