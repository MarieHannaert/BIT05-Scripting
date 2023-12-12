#!/usr/bin/python3
DNAseq = input("enter a DNA sequence: ")

def calculate_sequence(DNAseq):
    countlist={
        'A':0,
        'G':0,
        'C':0,
        'T':0
    }
    for nucleotide in DNAseq:
           countlist[nucleotide] += 1
    return countlist

result=calculate_sequence(DNAseq)

print("seq = {}\nCounts = {}".format(DNAseq,result))
