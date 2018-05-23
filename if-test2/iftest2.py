#!/usr/bin/env python3
#22 May 2018 Lab 12: IPv4 Testing with If
ipchk = input('Please provide an IP address: ') #changed to prompt user for input

if ipchk == '192.168.70.1': # hypothetical default gateway address
	print('That (' + ipchk + ') looks a lot like the default gateway, you sure about this?') # to prevent entering the default gw
elif ipchk == '': #added consequences for not putting anything in
	print('You didn\'t provide any input!')
else:
	print('Looks like the IP address was set: ' + ipchk)

