#!/bin/bash

grep "SRR072893" ~/qbb2018-answers/day1-homework/SRR072893/SRR072893_map > ~/qbb2018-answers/day1-homework/SRR072893/grep.sam
grep -v "^@" ~/qbb2018-answers/day1-homework/SRR072893/grep.sam | grep -v 2110000 | cut -f 3 | sort | uniq -c > ~/qbb2018-answers/day1-homework/SRR072893/align.sam
