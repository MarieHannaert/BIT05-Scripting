#!/usr/bin/python3
day=int(input("what is your day of birth (e.g. 26)? "))
month=input("what is your month of birth (e.g. june)? ")
if month == "october":
    if day > 22: 
        print ("you're a scorpio")
    if day < 23:
        print ("you're a libra")
elif month == "november":
    if day < 22: 
        print ("you're a scorpio")
    if day > 21: 
        print ("you're a sagittarius")
elif month == "december":
    if day < 22: 
        print ("you're a sagittarius")
    if day > 21:
        print ("you're a capricorn")
elif month == "januari":
    if day < 20:
        print("you're a capricorn")
    if day > 19:
        print("you're a aquarius")
elif month == "februari":
    if day < 19:
        print("you're a aquirius")
    if day > 18:
        print ("you're a Picses")
elif month == "march":
    if day < 21:
        print("you're a pisses")
    if day > 20:
        print ("you're a aries")
elif month == "april":
    if day < 20:
        print("you're a aries")
    if day > 19:
        print ("you're a Taurus")
elif month == "may":
    if day < 21:
        print("you're a Taurus")
    if day > 20:
        print ("you're a gemini")
elif month == "june":
    if day < 21:
        print("you're a gemini")
    if day > 20:
        print ("you're a cancer")
elif month == "july":
    if day < 23:
        print("you're a cancer")
    if day > 22:
        print ("you're a leo")
elif month == "august":
    if day < 23:
        print("you're a leo")
    if day > 22:
        print ("you're a virgo")
elif month == "september":
    if day < 23:
        print("you're a virgo")
    if day > 22:
        print ("you're a libra")

