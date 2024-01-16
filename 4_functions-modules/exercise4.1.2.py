#!/usr/bin/python3
def string_reverse(str1):
    rstr1=""
    index = len(str1)
    while index > 0: 
        rstr1 += str1[index-1]
        index = index-1
    return rstr1


str1=input("Give an input string: ")
rstr1=string_reverse(str1)
print("the reverse string is: {}".format(rstr1))