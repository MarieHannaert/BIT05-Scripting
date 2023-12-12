#!/usr/bin/python3
countries={'Belgium':'Brussels', 'England':'London', 'France':'Paris', 'Spain':'Madrid'}

print("List of capitals:\n=================")
for k, v in countries.items():
    print("{}".format(v))

n=5
for i in range(n):
    for j in range(i):
        print('*', end="")
    print('')
for i in range(n,0,-1):
    for j in range(i):
        print('*', end="")
    print('')
    



    
