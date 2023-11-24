#!/usr/bin/python3
import math
a=int(input("what is the lengt of the first side of the triangle? "))
b=int(input("what is the lengt of the second side of the triangle? "))
c=int(input("what is the lengt of the thirth side of the triangle? "))
s=(((a+b+c))/2)
A=math.sqrt((s*((s-a)*(s-b)*(s-c))))
print("the area is ", round(A,2))