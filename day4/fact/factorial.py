#!/usr/bin/env python3
#24 May 2018, lab 21 'for loops and range()'

x = int(input('Enter a number: \n')) # create a variable for integers from the user
f= 1

for i in range(1, x+1):
    f = f * i
print(str(x) + '! = ' + str(f))

