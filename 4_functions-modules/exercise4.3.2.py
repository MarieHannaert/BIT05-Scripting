#!/usr/bin/python3
def DNA_counter(DNA_sequence):
    total_nt=len(DNA_sequence)
    counter = ({'A':0, 'G':0, 'C':0, 'T':0})
    for nt in DNA_sequence:
        if nt == 'A':
            counter[nt] += 1
        elif nt == 'G':
            counter[nt] += 1
        elif nt == 'T':
            counter[nt] += 1
        elif nt == 'C':
            counter[nt] += 1
        else: 
            print("this {} is not a nucleotide".format(nt))
    frequencies=dict()
    for nt2 in counter:
        frequencies[nt2]= counter[nt2]/total_nt
    return counter, frequencies          


#DNA_sequence="ATGCATAGAGCTACGTACTATACTCTACTACGG"
DNA_sequence = input("Give a DNA sequence: ")
counter=DNA_counter(DNA_sequence)
print("Calculate base counts: \n{}".format(counter[0]))
frequencies=DNA_counter(DNA_sequence)
print("Calculate base frequencies: \n{}".format(frequencies[1]))

