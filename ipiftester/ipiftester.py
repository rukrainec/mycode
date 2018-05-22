#!/usr/bin/env python3
# 22 May 2018, PM exercise
# Goal: take an ip address, determine if it matches gateway (10.10.3.1)
# if it matches dns server
# otherwise, add it to list
avail_ip = [ '192.168.0.1', '127.0.0.1']
ipaddr = ''
while ipaddr != 'q':
	ipaddr = input('What IP address would you like to add to the list of available IP\'s? (press q/Q to quit): ')
	if ipaddr == '10.10.3.1':
		print('That is the default gateway. That is not an available IP address.')
	elif ipaddr == '8.8.8.8':
		print('That is the DNS server.  That is not an available IP address.')
	else:
		avail_ip.append(ipaddr)
print('The current list of available IPv4 addresses is: '+ str(avail_ip))
