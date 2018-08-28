#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    f = open(sys.argv[1])
else:
    f = sys.stdin
    
count = 0
for i in f:
    if i == 0:
        continue
    elif "NH:i:1" in i:
        count += 1

print(count)