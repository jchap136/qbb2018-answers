#!/bin/bash

GENOME=~/qbb2018-answers/genomes/BDGP6
ANNOTATION=~/qbb2018-answers/genomes/BDGP6.Ensembl.81.gtf

for SAMPLE in SRR072893 SRR072903 SRR072905 SRR072915
do
    echo "running mkdir"
    mkdir $SAMPLE # make directory in day1-homework
    cd $SAMPLE # change directory so we're in the new directory under day1-homework
    echo "running fastqc"
    fastqc ~/data/rawdata/${SAMPLE}.fastq #go to this directory and get fastq file but outputs in homework/sample1
    echo "running hisat2"
    hisat2 -x $GENOME -U ~/data/rawdata/${SAMPLE}.fastq -S ${SAMPLE}_mapped
    echo "running samtools sort"
    samtools sort -o ${SAMPLE}_mapped.bam ${SAMPLE}_mapped
    echo "running samtools index"
    samtools index -b ${SAMPLE}_mapped.bam
    echo "running stringtie"
    stringtie ${SAMPLE}_mapped.bam -p -e -G $ANNOTATION -B -o ${SAMPLE}.gtf
    cd ../
done

