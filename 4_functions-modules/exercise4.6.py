#!/usr/bin/python3
import re
password=input("give a valid password: ")
""" x = True
while x:
    if(len(password)<6 or len(password)>12):
        break
    else:
        print("valid password")
        x = False
        break """

if(len(password)<6 or len(password)>12):
    print("invalid password, is the wrong lenght")
elif not (re.search("[0-9]",password)):
    print("invalid password, does not include a number")
elif not (re.search("[a-z]",password)):
    print("invalid password, does not include lowercase letter")
elif not (re.search("[A-Z]",password)):
    print("invalid password, does not include a uppercase letter")
elif not (re.search("[$#@]]",password)):
    print("invalid password, does not include a character")
else:
    print("valid password")