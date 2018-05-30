#!/usr/bin/env python3
#30 May 2018, Lab 45 'Import time'

import time # This is required to include time module

## Count the number of ticks from the epoch
ticks = time.time()
print("Number of ticks since 12:00am, January 1, 1970: " + str(ticks))

## Show how we can convert ticks into a useful time tuple
myTime = time.localtime(ticks) # pass ticks to localtime
print("The local time touple is: " + str(myTime))
print("The local time touple year is: " + str(myTime[0]))
print("The local time touple month is: " + str(myTime[1]))
print("The local time touple day is: " + str(myTime[2]))
print("The local time touple hour is: " + str(myTime[3]))
print("The local time touple minute is: " + str(myTime[4]))
print("The local time touple second is: " + str(myTime[5]))
print("The local time touple week is: " + str(myTime[6]))
print("The local time touple year is: " + str(myTime[7]))
print("The local time touple daylight savings is: " + str(myTime[8]))
