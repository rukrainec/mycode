#!/usr/bin/env python3
# 22 May 2018
# goal: prompt and collect an IP and MAC addr from a user and store in a variable then print out ip and mac on same line along with a message

user_ip = input('What is your IP address?: ')
user_mac = input('What is your MAC address?: ')
print('You said your IP address is ' + user_ip + ' and your MAC address is ' + user_mac)

# basic thing to confirm the user provided input
confirm = input('Is this correct (y/n?) ')

if confirm == 'y':
	print('Thank you')
else:
	print('Please try again')
# need to figure out how to get it to automatically restart the script if confirm != 'y'
