#!/usr/bin/env python3
#1 June 2018 lab 61 'NAPALM basic python script'

import sys
import napalm
from napalm import get_network_driver
import pprint as pp  
  
if len(sys.argv) != 5:
   print("You supplied ", len(sys.argv)-1, " arguments but 4 are needed")
   print("getrun.py requires: OS, IP, USER and PW of device")
   print("example: python3  getrun.py  eos  a.b.c.d  username  password")
   sys.exit()

os = sys.argv[1]
ip = sys.argv[2]
user = sys.argv[3]
passwd = sys.argv[4]

driver = get_network_driver(os)
device = driver(ip,user,passwd)
device.open()

config = device.get_config()
running_config = config['running']
print(running_config)
device.close()
