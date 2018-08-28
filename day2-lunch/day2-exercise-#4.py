#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    f = open(sys.argv[1])
else:
    f = sys.stdin

list = []
for i, line in enumerate(f):
    if line.startswith("@"):
        continue
    cut = line.strip("\r\n").split("\t")
    list.append(cut[2])
    if len(list) >= 10:
        print(list)
        break
        