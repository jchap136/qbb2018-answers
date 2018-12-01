#!/usr/bin/env python

"""
Usage: ./hic_ctcf.py CTCF_peaks.txt

find all bins that contain at least 1 CTCF peak
"""

import sys
#import matplotlib.pyplot as plt
import numpy
import hifive


f1 = open(sys.argv[1])
#f2 = open(sys.argv[2])

midpoint = []
for i, line in enumerate(f1):
    if i == 0:
        continue
    fields = line.rstrip("\r\n").split("\t")
    chrom = fields[0]
    start = int(fields[1])
    end = int(fields[2])
    if chrom == "chr17" and start >= 15000000 and end <= 17500000:
        mid = ((end - start) / 2) + start
        midpoint.append(mid)
#print(midpoint)
#print(len(midpoint))

hic = hifive.HiC('hic_ex.hcp')

data = hic.cis_heatmap(chrom='chr17', start=15000000, stop=17500000, binsize=10000, datatype='fend', arraytype='full')
data[:, :, 1] *= numpy.sum(data[:, :, 0]) / numpy.sum(data[:, :, 1])
where = numpy.where(data[:, :, 1] > 0)
data[where[0], where[1], 0] /= data[where[0], where[1], 1]
# where says know position in matrix that satisfy what I say
data = data[:, :, 0]
#print(data)
#print(data.shape)
#print(data[0][0])

# convert midpoint values to which bins they are in in the data matrix
bin_list = []
for j in midpoint:
    val = (j-15000000)/10000
    bin_list.append(val)
ctcf_list = numpy.unique(bin_list)
#print(unique_bin_list)
#print(len(unique_bin_list))

enriched_values = []
for i in range(len(ctcf_list)):
    for j in range(i, len(ctcf_list)):
        if data[ctcf_list[i],ctcf_list[j]] > 1:
            enriched_values.append((ctcf_list[i], ctcf_list[j], data[ctcf_list[i],ctcf_list[j]]))
#print(enriched_values)
#print(len(enriched_values))

#genomic_pos = []
print "bin1", "\t", "bin2", "\t", "genomic_pos1", "\t" "genomic_pos2", "\t" "enrichment_value"
for x, y, val in enriched_values:
    x_pos = (x * 10000) + 15000000
    y_pos = (y * 10000) + 15000000
    #genomic_pos.append((x_pos, y_pos))
    print x, "\t", y, "\t", x_pos, "\t", y_pos, "\t", val
#print(genomic_pos)
#print(len(genomic_pos))

    


        
    
    

