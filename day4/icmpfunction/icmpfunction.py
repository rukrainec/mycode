#!/usr/bin/env python3
#24 May 2018, Afternoon exercise


###GOALS###
#prompt user for values for cnumber(count) and ipaddress
#pass both to function icmpsender
#icmpsender issues ping -c <cnumber> <ipaddress>
#hints: import subprocess, subprocess.call(cmd)

import subprocess

tgt = input('Who would you like to ping today? \n[enter IPv4 address]: ')
hahaha = input('How many times would you like to ping them?: ')

subprocess.call(['ping', '-c', str(hahaha), tgt])
