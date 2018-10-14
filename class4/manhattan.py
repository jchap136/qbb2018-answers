#!/usr/bin/env python3

"""
Usage: ./manhattan.py *.qassoc

make manhattan plots from .qassoc
"""

import sys
import matplotlib.pyplot as plt
import numpy as np
from cycler import cycler


for fname in sys.argv[1:]:
    treatment = fname.split('.')[1]
    #print(treatment)
    with open(fname) as f:
    #f = open(sys.argv[1])
        chrom_list = []
        bp_list = []
        p_list = []
        for i, line in enumerate(f):
            if i == 0:
                continue
            fields = line.split() # file split by random amount of whitespace, this ignores amount of whitespace
            chrom = fields[0]
            bp = fields[2]
            p = fields[-1]
            if "NA" not in p:
                p = np.log(float(p))
                p = -p
                chrom_list.append(chrom)
                bp_list.append(int(bp))
                p_list.append(p)
        #print(len(chrom_list))
        #print(bp_list[0])
        #print(len(p_list))

        # now we have 3 lists and want to iterate over them at the same time to make plot
        # need to shift plot over and change colors every time 'chrom_list' changes
        plt.rc('axes', prop_cycle=(cycler('color', ['r', 'g', 'b', 'y', 'm', 'c',\
         'salmon', 'darkviolet', 'tomato', 'chocolate', 'aqua', \
         'deeppink', 'lime', 'crimson', 'darkgreen', 'orchid'])))
        fig, ax = plt.subplots(figsize=(20,5))
        curr_chr = 1
        #biglist = [[[bp_list[0]]]] # collection of sublists
        biglist = []
        sublist = [[], []] # list of 2 lists - bp and p
        offset = 0
        x_ticks = ["chrI"]
        x_tick_pos = []
        for i in range(len(chrom_list)):
            chrom = chrom_list[i]
            bp = bp_list[i]
            p = p_list[i]

            if i == 0 or chrom == chrom_list[i-1]:
                # add bp and p to sublist
                sublist[0].append(bp) # x value  
                sublist[1].append(p) # y value
                # if using biglist from line 47 and appending sublist: [[[1074]], [[x1], [y1]], [[x2], [y2]]]
            else:
                # set tmp value, plot values in same chr, then set offset values for next chr
                x_ticks.append(chrom)
                max_sub = max(sublist[0])
                x_tick_pos.append(offset + max_sub/2)
                tmp = sublist[0][0] 
                for i, val in enumerate(sublist[0]):
                    sublist[0][i] = (val - tmp) + offset
                    # if i > len(sublist[0]):
#                         ax.set_xticklabels(str(curr_chr))
                offset = sublist[0][-1] # add last value of previous chr to next chr series
                plt.scatter(sublist[0], sublist[1], alpha=0.1, s=10) # then hopefully it changes color next time
                #biglist.append(sublist) # add sublist to biglist
                #print(sublist[0][0])    
                sublist = [[], []] # empty sublist to prep for next series of chr
                curr_chr += 1
                sublist[0].append(bp)
                sublist[1].append(p)
                
        #print(x_ticks)
        ax.set_xticks(x_tick_pos)
        ax.set_xticklabels(x_ticks)
        ax.axhline(5, color='black', linewidth=1, linestyle='--', label="significance cutoff")
        ax.set_title("{} Manhattan Plot".format(treatment))
        ax.set_xlabel("genome position")
        ax.set_ylabel("-log10(p-value)")
        ax.legend()
        #fig.savefig("test.png")
        fig.savefig("manhattan_{}.png".format(treatment))
        plt.close(fig)


### fail, too slow ###
        # for i, (chrom, bp, p) in enumerate(zip(chrom_list, bp_list, p_list)):
        #     print(i)
        #     if i == 0 or (bp < bp_list[i-1] and chrom != chrom_list[i-1]): # when chromosome changes
        #         bp_new = bp_list[i-1] + 1
        #         print(bp_new)
        #         ax.scatter(bp_new, p, alpha=0.5)#use color changer here
        #         #ax.set_xticklabels(chrom)
        #     elif bp < bp_list[i-1]: # after chromosome change, bp values need to be adjusted
        #         bp_new = bp_list[i-1] + bp
        #         print(bp_new)
        #         ax.scatter(bp_new, p, alpha=0.5)#use current color
        #         #ax.set_xticklabels(chrom)
        #     else: # this would be only for chr1
        #         print(bp)
        #         ax.scatter(bp, p, alpha=0.5, color="green")
        #         #ax.set_xticklabels(chrom)


