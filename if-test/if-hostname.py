#!/usr/bin/env python3
#22 May 2018, lab 11
hostname = input('What is your hostname?: ') # get user input
if hostname == 'MTG' or hostname == 'mtg' or hostname == 'mtG' or hostname == 'mTg' or hostname == 'Mtg' or hostname == 'MTg' or hostname == 'MtG' or hostname == 'mTG':
	print('The hostname was found to be MTG (or some derivative of that)') # success message
	print('Stay classy San Diego!') # closing message
else: 
	print('huh?') # if it doesn't match
