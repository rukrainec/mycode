#!/usr/bin/env python3
#24 May 2018, Afternoon exercise


###GOALS###
#prompt user for values for cnumber(count) and ipaddress
#pass both to function icmpsender
#icmpsender issues ping -c <cnumber> <ipaddress>
#hints: import subprocess, subprocess.call(cmd)

import subprocess
import socket #found on stackoverflow for verifying input as ipv4 addr

# while loops enable input checking, we only want IPv4 and integers!
while(True):
    try:
        tgt = input('Who would you like to ping today? \n[enter IPv4 address]: ')
        socket.inet_aton(tgt) #found on s/o
    except socket.error: #if user inputs something other than an IPv4 addr
        print('Invalid input! IPv4 addresses only!')
        continue
    else:
        break
while(True):
    try:
        hahaha = int(input('How many times would you like to ping them?: '))
    except ValueError: # if user inputs something other than an integer
        print('Invalid input! Whole numbers only!')
        continue
    else:
        break
subprocess.call(['ping', '-c', str(hahaha), tgt]) # executes ping command hahaha times on tgt ip addr
