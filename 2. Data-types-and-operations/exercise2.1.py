#!/usr/bin/python3
################################################################################
#Write a Python script that takes input from the user and displays that input back in upper and lower cases
########################################################################################
text=input("geef uw naam:\n")

print(text.capitalize())
print(text.upper())
print(text.lower())
#############################################################################################
#Write a Python script that takes a sequence and a motif, searches the motif and shows the position (not index) of the motif in the sequence
##########################################################################################
sequence=input("what is the sequence?\n ")
motif=input("what is the motif?\n ")
print(sequence.find(motif)+1)
############################################################################################
#Write a Python script that takes a sequence and a cleavage site (split)and displays the sequence fragments after cleavage (split)
################################################################################
sequence2=input("what is the second sequence?\n")
cleavage=input("what is the cleavage site?\n")
print(sequence2.split())
