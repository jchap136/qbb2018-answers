#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    f = open(sys.argv[1])
else:
    f = sys.stdin

# first idea, but didn't work
#total = 0
#junk = 0
#for i in f:
#    if i.startswith("@"):
#        junk += 1
#    cut = i.strip("\r\n").split("\t")
#    total += cut[4]
    
#avg = total / (i - junk)

#print(avg)

listf = []  
for i in f:
    if i.startswith("@"):
        continue
    cut = i.strip("\r\n").split("\t")
    listf.append(int(cut[4]))

avg = sum(listf)/len(listf)
print("Average MAPQ Score: " + str(avg))
    

    