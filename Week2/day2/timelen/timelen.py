#!/usr/bin/env python3
#30 May 2018, Lab 46 'import datetime'

from datetime import datetime # required to use datetime
startTime = datetime.now()    # returns the time of right now from the datetime object
# Note that datetime is an object, not a simple string.

## WRITE YOUR OWN CODE TO DO SOMETHING. ANYTHING.
# SUGGESTION: Replace with code to print a question to screen and collect data from user.
# MORE DIFFICULT -- Place the response(s) in a list & continue asking the question until the user enters the word 'quit'

import subprocess
subprocess.call(['ping', '-c', '15', '8.8.8.8'])

## Explore the statrTime object
print('The startTime hour is: ' + str(startTime.hour))
print('The startTime minute is: ' + str(startTime.minute))
print('The startTime day is: ' + str(startTime.day))
print('The startTime year is: ' + str(startTime.year))

## Figure out how long it took to do that something 
print('The code took: ' + str(datetime.now() - startTime) + ' to run.')
