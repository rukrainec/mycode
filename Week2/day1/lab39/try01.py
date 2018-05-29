#!/usr/bin/env python3
#29 May 2018, lab 39 'try and except 01'

try:
    print('Enter a file name: ')
    name = input()
    file = open(name, 'w')
except:
    print('Error with that file name!')
    print('Enter a file name: ')
    name = input()
    file = open(name, 'w')
finally:
    print('This code will always execute')
