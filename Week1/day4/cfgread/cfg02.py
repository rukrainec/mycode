#!/usr/bin/env python3
#24 May 2018, lab 25

## create file object in "r"ead mode
configfile = open(input('what file do you want to run this script on?'), 'r')

## display file to the screen - .read()
configblog = configfile.read()
print(configblog)

## break configblog across line boundaries (strips out \n)
configlist = configblog.splitlines()

## display list with no '\n'
print(configlist)

## Always close your file
configfile.close()

## display how many lines are in the overall file
print('\n''There are ' + str(configlist.__len__()) + ' lines in the file you ran this script on.')
