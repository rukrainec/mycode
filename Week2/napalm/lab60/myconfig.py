#!/usr/bin/env python3
#1 June 2018, Lab 60 'Napalm changes, validation , and rollback'
# import code from NAPALM
from napalm import get_network_driver
import pprint as pp
import json
    
# Tell NAPALM to speak "eos" commands to our switches (very cisco-like)
driver = get_network_driver('eos')
    
# Hard-code the switch credentials
device = driver('172.16.2.10', 'admin', 'alta3') 
    
#Equates to: ssh into the switch, login, and enable
device.open() 
    
# Print STARTUP, RUNNING, and CANDIDATE configs 
config = device.get_config()

print("UGLY ASS RAW STUFF:\r")
print(config)
print("THIS THAT REAL STUFF:\r")
print(json.dumps(config, indent=4, separators=(',', ': ')))
