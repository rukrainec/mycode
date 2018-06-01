#!/usr/bin/env python3
#1 June 2018, lab 61 load/replace, compare, commit
#format: py3 script.py driver ip uname pw filename

import sys
import napalm
    
if len(sys.argv) != 5:
   print("You supplied ", len(sys.argv)-1, " arguments but 5 are needed")
   print("getrun.py requires: OS, IP, USER, PW, restore_file_name of device")
   print("example: python3  getrun.py  eos  a.b.c.d  username  password filename.run")
   sys.exit()
os = sys.argv[1]
ip = sys.argv[2]
user = sys.argv[3]
passwd = sys.argv[4]

from napalm import get_network_driver
import pprint as pp
driver = get_network_driver(os)
device = driver(ip,user,passwd)
device.open()

device.rollback()
print('Changes rolled back!')
device.close()
exit()
