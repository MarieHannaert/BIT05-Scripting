#!/usr/bin/python3
firstnumber=0
secondnumber=1
print (firstnumber)
print (secondnumber)
while secondnumber < 50:
    newnumber = firstnumber + secondnumber
    print (firstnumber, "+", secondnumber, "=", newnumber)
    firstnumber = secondnumber
    secondnumber = newnumber
    
import random
guess=int(input("Guesse a number between 1 and 9: "))
number = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(number)
while guess != number:
    print("wrong! try again")
    guess = int(input("take a new guess: "))

print("Hooray, you're right! The number is ", guess)
    



     


