#!/usr/bin/python3
"""A slice operation can specify a third number also following a colon.  In the sequence string: MNKMDLVADVAEKTDLSKAKATEVIDAVFA
 Take the slice [0:9:3]. What does the third number indicate?
 What will be the output when you obtain the slice [16:0:-4]?
 Explain what happens using the slice [:25:-1].
"""
sequence="MNKMDLVADVAEKTDLSKAKATEVIDAVFA"
print(sequence)
slice1 = sequence[0:9:3]
print(slice1)
slice2=sequence[16:0:-4]
print(slice2)
slice3=sequence[:25:-1]
print(slice3)