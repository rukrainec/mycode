#!/usr/bin/env python3
#6 June 2018, Lab 71 'Custom sorted ...myFunct'
#written by Robert Ukrainec

firewallports = [ 5060, 5061, 80, 443, 22, 25565 ]

def modTen(x):
    return x%10

print('Currently firewallports looks like: ', firewallports)
print('\nSorting that using the function we made as a key: ', sorted(firewallports, key=modTen))

simpsons = [ ('Lisa', 8), ('Bart', 10), ('Maggie', 2), ('Homer', 36), ('Marge', 34) ]

def byAge(x):
    return x[1]
simpsonsage = sorted(simpsons, key=byAge)

print('Now sort the touples by using a function as the key: ', simpsonsage)

def secondLetter(x):
    return x[0][1]

print('made a new function to call second letter in 1st part of touple, now use it as a key!:\n', sorted(simpsons, key=secondLetter))
