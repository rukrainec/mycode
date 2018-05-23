#!/usr/bin/env python3
#23 May 2018, Afternoon Exercise

###GOALS###
# establish a dictionary detailing a networking device
# iterate through the dictionary (for loop)
# display message preceding dictionary value
# only write message once
###########

#establish dictionary
cisco_ios = {'1)device_type': 'cisco_ios_ssh', '2)ip': '10.10.10.27', '3)username': 'admin', '4)password': 'passwd', '5)port': 22} # added #) to keys to allow for sorting
for x in sorted(cisco_ios): # sorting dictionary for constant, predictable output
    print('CISCO LOGIN INFO - ' + str(cisco_ios[x])) # iterate dictionary, display values as strings to allow concatenation
