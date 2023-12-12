#!/usr/bin/python3
import math
largest=None
thelist = [1, 2, 3, 9, 40, 4, 5, 6, 9, 0]
print("Before: ", largest)
print("-------------------")
for number in thelist:
    listtwo=[]
    listtwo.append(number)
    print("Loop:    ",number,"  ",max(listtwo))
print("-------------------")
print("The largest is:",max(thelist))

listofnumbers=[]

numbers = None

while numbers != 0:
 numbers=input("Give some numbers: ")
 for number in numbers:
    listofnumbers.append(number)
print(listofnumbers)

sumlist=int(sum(listofnumbers))
print(sumlist)
count=int(len(listofnumbers))
print(count)

print("the average is: ",average= sumlist / count)








    