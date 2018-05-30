#!/usr/bin/env python3
#30 May 2018, Lab 47 'import cal'

import calendar
import time
ticks = time.time()
myTime = time.localtime(ticks)

#lilcal = calendar.month(2018, 1)
#print('Here is a tiny calendar:')
#print(lilcal)

#figure out if it's a leap year
if calendar.isleap(myTime[0]) == True:
    print('\n      It\'s a leap year! Time to replace the hard drives!')
    calendar.prcal(myTime[0])
else:
    print('\n      It is not a leap year! Keep saving money for more hard drives!')
    calendar.prcal(myTime[0])

