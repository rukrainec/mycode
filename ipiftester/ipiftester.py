#!/usr/bin/env python3
# 22 May 2018, PM exercise
# Goal: take an ip address 
# determine if it matches gateway (10.10.3.1) or dns server
# otherwise, add it to list
# continue prompting for more ip addresses until user enters 'q'

avail_ip = [] # declare empty list to add ip addresses to
ipaddr = '' # declare variable for user input, starts out blank
while ipaddr != 'q': # establishes loop that continues until user inputs 'q'
	ipaddr = input('What IP address would you like to add to the list of available IP\'s? (press q to quit):\n') # initial user prompt
	if ipaddr == '10.10.3.1': # prevent user from selecting default gw
		print('That is the default gateway. That is not an available IP address.')
	elif ipaddr == '8.8.8.8': # prevent user from selecting DNS server
		print('That is the DNS server.  That is not an available IP address.')
	elif ipaddr != 'q': # add user's input to the list as long as it isn't 'q'
		avail_ip.append(ipaddr)
	else: # closeout messages
		print('The current list of available IPv4 addresses is: ')
		print(str(avail_ip))
		print('Thank you!')
