#!/usr/bin/env python3
#1 June 2018 Napalm challenge part I: config gathering

####GOAL####: make config files for all devices listed in a file
import sys
import napalm
import os

#10-19 ensures file with list of dev ip addr's can be read
if len(sys.argv) != 2:
   print("!!!!Bad argument(s)!!!!")
   print("example: /getconfs.py filename")
   sys.exit()

iplist = sys.argv[1]

while not os.path.isfile(iplist):
    print('Can\'t find that in the current path, try again')
    iplist = input('What is the full path to the file you want to read from?')

from napalm import get_network_driver

#make a list from file object that can be iterated through in a for loop
devlist = open(iplist).readlines()
driver = get_network_driver('eos')

#for loop to get and print to unique file running config for every dev in list
for ip in range(len(devlist)):
    device = driver(devlist[ip].strip('\n'), 'admin', 'alta3')
    device.open()
    config = device.get_config()
    running_config = config['running']
    output = devlist[ip].strip('\n') + '.conf'
    o = open(output, 'w')
    print(running_config, file= o)
    device.close()
    ip += 1

print('Running configs saved to directory!')

