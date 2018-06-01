#!/usr/bin/env python3
#22 May 2018, lab 11
hostname = input('What is your hostname?: ') # get user input
if hostname.upper() == 'MTG':
	print('The hostname was found to be MTG (or some derivative of that)') # success message
	print('Stay classy San Diego!') # closing message
else: 
	print('huh?') # if it doesn't match
