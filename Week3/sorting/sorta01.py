#!/usr/bin/env python3
#more list sorting practices
vendors = ['cisco', 'juniper', 'big_ip', 'f5', 'arista', 'hp']

print('Current value of vendors: ', vendors)

print('\nSort that stuff: ', sorted(vendors))

print('\nSorted() doesn\'t change the list: ', vendors)

filething = open('/home/student/mycode/Week3/Paramiko/pmiko02.py')
newlist = filething.readlines()
outputfile = open('results.txt', 'w')

print(newlist)
print('Let\'s see if this works!', sorted(newlist), file=outputfile)


