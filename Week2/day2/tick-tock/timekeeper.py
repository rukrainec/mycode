#!/usr/bin/env python3
#30 May 2018, Lab 45 pt 2

###GOALS###
#determine how many seconds I've been alive
#show time 500 days from now in human friendly and epoch format

import time
ticks = time.time() #epoch time in seconds
myTime = time.localtime(ticks) #local time touple setup
#0=year
#1=month
#2=day of month
#3=hour
#4=minute
#5=second
#6=day of week
#7=julian date
#8=dst thing -1 - 1
#make touple for birthday to mktime
lifeTime = int(1988), int(8), int(17), myTime[3], myTime[4], myTime[5], myTime[6], myTime[7], myTime[8]
mymktime = time.mktime(lifeTime)

TimeWasted = ticks - mymktime
dtimewasted = TimeWasted // 86400
ytimewasted = dtimewasted // 365
print('You have been alive for ' + str(TimeWasted) + ' seconds. \nThis is ' + str(round(dtimewasted)) + ' days or ' +str(round(ytimewasted)) + '(ish) years.')

sfuture = ticks + 500
dfuture = ticks + (500 * 86400)
sfc = time.ctime(sfuture)
dfc = time.ctime(dfuture)

print('\nin 500 seconds the epoch time will be:\n\n         ' + str(sfuture))
print('\nin 500 seconds the readable time will be:\n\n         ' + sfc)
print('\nin 500 days the epoch time will be :\n\n         ' + str(dfuture))
print('\nin 500 days the readable time will be:\n\n         ' + dfc)
