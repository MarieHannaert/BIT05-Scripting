#!/usr/bin/python3
var1="live desserts"
legelist=[]
rstr=""
letters=len(var1)
index=letters-1
print("string is {}\nThere are {} letters.".format(var1,letters))
while(index>=0):
  print(var1[index],end="")
  index = index-1
print("\n")
  

def string_reverse(str1):
    reversedstr=""
    letters=len(str1)
    while(letters>0):
        #print(str1[letters-1])
        reversedstr += str1[letters-1]
        letters = letters-1
    return reversedstr

str1=input("give me a string." )
print("the string is {}".format(str1))
print(string_reverse)



    


