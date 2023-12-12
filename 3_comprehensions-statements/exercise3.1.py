#!/usr/bin/python3
given=[1,4,9,16,25,36,49,64,81,100]
even=[]
for number in given:
    if number%2==0:
        even.append(number)
print(given)
print(even)
    
current=input("what is the current year? (e.g. 2023)")
years=[1990, 1995, 2000, 2005, 2010, 1990, 1992]
ages=[]
for year in years: 
    age=int(current)-year
    ages.append(age)
print(ages)
