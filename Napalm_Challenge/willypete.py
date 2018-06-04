#!/usr/bin/env python3
#1 June 2018, Napalm Challenge, final version

######GOALS######
#write a script that will, given a list of device IP addresses, 1) archive current configs 2) merge new configs with devices, and 3) offer them a chance to rollback
# Other files required: ip list (devices in GNS3), config changes to merge
# Script assumes use will only be dealing with arista eos devices, since that's all we've done so far
# Things to add to improve this tool:
#    - any kind of relevant API call, for practice
#    - input format flexibility, i.e. reading from .txt, .xls, .csv
#    - validation function
#################

#import the things:
from napalm import get_network_driver
import os
import sys

####make functions:####
#these functions are only ever called in 'for' loops
def archive_old():
    device = driver(devlist[ip].strip('\n'), 'admin', 'alta3')
    device.open()
    config = device.get_config()
    running_config = config['running']
    output = devlist[ip].strip('\n') + '.conf'
    o = open(output, 'w')
    print(running_config, file= o)
    device.close()

def merge_new():
    device = driver(devlist[ip].strip('\n'), 'admin', 'alta3')
    device.open()
    device.load_merge_candidate(mergefile)
    device.commit_config()

def rollback():
    device = driver(devlist[ip].strip('\n'), 'admin', 'alta3')
    device.open()
    device.rollback()
#######################

iplist = input('what is the full path of the file containing the list of ip addresses of the devices you want to change?\n>')
while not os.path.isfile(iplist):
    print('Can\'t find that in the current path, try again')
    iplist = input('What is the full path to the file you want to read from?')

mergefile = input('What is the full path of the file containing your config changes?\n>')
while not os.path.isfile(mergefile):
    print('Can\'t find that in the current path, try again')
    mergefile = input('What is the full path to the file you want to read from?')

devlist = open(iplist).readlines()
driver = get_network_driver('eos')

for ip in range(len(devlist)):      
    archive_old()
    merge_new()

print('Just so you\'re completely sure, you just made the following change:')
merg = open(mergefile)
print (merg.read())
print('To the following devices:')
devs = open(iplist)
print (devs.read())

chk = input('Press "R" to rollback these changes, hit any other key to continue: \n>')
if chk.lower() == 'r':
    for ip in range(len(devlist)):
        rollback()
    print('Changes reverted!/nConfigs still saved to your current directory.')
else:
    print('Thank you!  Changes have been applied, old configs are saved to your current directory')



