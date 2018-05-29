#!/usr/bin/env python3
#29 May 2018, lab 40 'try and except 02'
try: # code we want to try to run goes under the try
    print('Enter a numerator: ')
    numerator = int(input())
    print('Enter a denominator: ')
    denominator = int(input())
    print(numerator / denominator)
except ZeroDivisionError:  # Only catches div by zero errors
    print('**Not a legal entry**\nEnter a numerator: ')
    numerator = int(input())
    print('Enter a denominator: ')
    denominator = int(input())
    print(numerator / denominator)
except:
    print("We're sorry, something unexpected happened. See your IT department.")
