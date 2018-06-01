#!/usr/bin/env python3
#25 May 2018, lab 32b 'snippet.split.join'

###goals pt###
#give user a message
#accept an IPv4 address from user
#pass ip addr to a func that will
#remove dot notation
#add 10 to last octet
#return false if ^ >255, otherwise return true
#tell user success/failure

import socket #input validation

print('I\'m a program that will let you reserve a block of IPs 10 at a time \n(ignore the subnetting issues)')

while(True): #lifted from previous lab to ensure input is an IPv4 address
    try:
        ipaddr = input('What is the first IPv4 address in the block of 10 you would like to reserve?: \n')
        socket.inet_aton(ipaddr)
    except socket.error: #if user inputs something other than an IPv4 addr
        print('Invalid input! IPv4 addresses only!')
        continue
    else:
        break

def ipres(ipaddr):
    ipsplit = ipaddr.split('.') #takes ipaddr set above and splits into list
    last8 = int(ipsplit[-1]) #takes last octet
    last8 += 10 #adds 10 to last octet
    if last8 > 255:
        return False
    else:
        return True

ipres(ipaddr) #run the function

if ipres(ipaddr) == False:
    print('That didn\'t work :( ')
if ipres(ipaddr) == True:
    print('IP block reserved! Enjoy your /28(ish) subnet!')

