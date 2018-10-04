#!/usr/bin/env python3

"""
Usage: ./multi_plot_variants.py annotated_calls.vcf summary.txt

get DP score, GQ score, and AF score in each line in vcf file, then plot 3 plots in one panel
"""

import sys
import matplotlib.pyplot as plt
import numpy as np

f = open(sys.argv[1])

x_value = []
dp_value = []
af_value = []
gq_value = []
i=1
for line in f:
    if line.startswith("#"):
        continue
    fields = line.rstrip("\r\n").split("\t")
    column7 = fields[7].split(";")
    dp = column7[7].split("=")
    dp_num = (dp[1]) # get dp value
    dp_value.append(dp_num) # put dp value into list
    af = column7[3].split("=")
    af_num = af[1] # get af value
    af_value.append(af_num) # put af value into list
    x_value.append(i)
    # now we need to get the GQ score
    column9 = fields[9].split(":")
    try:
        gq = column9[1]
    except IndexError:
        i += 1
    #gq = column9[1]
    gq_value.append(float(gq))
    i += 1
    
    ### Peter's class instruction ###
    # # another way
#     for id_val in column7:
#         id, val = id_val.split("=")
#         if id == "AF":
#             af_value.append(float(val.split(",")[0]))
#         if id == "DP":
#             dp_value.append(float(val))
#     #another way
#     column7 = dict([x.split("=") \
#         for x in fields[7].split(";")])
#     af = float(column7["AF"])
#     dp = float(column7["DP"])
    #########################################
    # get ann and count each type of variation
    # ann = column7[-1].split("|")
#     ann_type = ann[1]
#     print(ann_type)
    
#print(sorted(gq_value))
#print(len(x_value))

# get rid of repeat values in scores
dp_value_new = []
for line in dp_value:
    dp_new = line.split(",")[0]
    dp_value_new.append(float(dp_new))
#print((dp_value_new))
#print(len(dp_value))
#print(len(dp_value_new))
af_value_new = []
for line in af_value:
    #sep = ","
    af_new = line.split(",")[0]
    af_value_new.append(float(af_new))
#print(len(af_value))
#print(len(af_value_new))
#print(af_value_new)

f2 = open(sys.argv[2])
predict_effect = []
predict_value =[]
for line in f2:
    field = line.rstrip("\r\n").split("\t")
    predict_effect.append(field[0])
    predict_value.append(int(field[1]))
    
#print(predict_effect)
#print(predict_value)
# now we have 3 lists of y values - I want to make 3 different plots but on the same panel

fig, axes = plt.subplots(nrows=2, ncols=2) #fig, (ax1, ax2, ax3) = plt.subplots(3, sharex=True)
axes = axes.flatten()
#ax.scatter(x_value, y_value, alpha=0.25, s=1, color="red")
fig.set_size_inches(20,12)
axes[0].hist(np.log10(dp_value_new), bins=100, color="violet") #, alpha=0.25, s=0.5, color="violet")
axes[2].hist(af_value_new, bins=100, color="sienna") #, alpha=0.25, s=0.5, color="sienna")
axes[1].hist(gq_value, bins=100, color="green") #, alpha=0.25, s=1, color="green")
axes[3].bar(predict_effect, predict_value, color="red")
axes[3].set_xticklabels(predict_effect, rotation=90)
plt.tight_layout(pad=2.5, w_pad=2.5, h_pad=2.5)
# ax1.set_yticklabels([])
# ax2.set_yticklabels([])
# ax3.set_yticklabels([])
#axes[0].set_title("depth")
axes[0].set_xlabel("position")
axes[0].set_ylabel("log depth")
#axes[2].set_title("allele frequency")
axes[2].set_xlabel("position")
axes[2].set_ylabel("allele frequency")
axes[1].set_xlabel("position")
axes[1].set_ylabel("genotype quality")
axes[3].set_ylabel("frequency of variant")
fig.savefig("multi_plot_variants.png")
plt.close(fig)


