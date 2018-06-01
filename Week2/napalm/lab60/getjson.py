#!/usr/bin/env python3
#1 June 2018, Lab 60 'Napalm changes, validation , and rollback'
# import code from NAPALM
from napalm import get_network_driver
import os.path
import sys
import json

if len(sys.argv) != 2:
    print('You supplied ' + str(len(sys.argv)-1) + ' arguments but 1 is needed')
    print('getjson.py requires: IPv4 address')
    print('example: python3 getjson.py a.b.c.d')
    sys.exit()
ip = sys.argv[1]

driver = get_network_driver('eos')
device = driver('172.16.2.10', 'admin', 'alta3') 
device.open() 
config = device.get_config()

print(device.get_config())
