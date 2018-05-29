#!/usr/bin/env python3
#29 May 2018 Lab 42, 'Making Excel Sheets'

import pyexcel
import socket

# Request data from user
def get_ip_data():
    while(True):
        try:
            input_ip = input("\nWhat is the IP address? ")
            socket.inet_aton(input_ip)
        except socket.error:
            print('Not a valid IP address!!!!')
            continue
        else: break
    input_driver = input("What is the driver associated with this device? ")
#this would be another good spot for input validation, verify presence of driver in list of auth. drivers
    input_loc = input('Where is this device located?')
    input_deadline = input('When does this need to happen?')
    d = {"1) IP": input_ip, "2) Driver": input_driver, "3) Location": input_loc, "4) Deadline": input_deadline}
    return d

## This code is left turned off, but might help visualize how pyexcel works with data sets.
## IP is the first column, whereas driver is the second column.
## mylistdict = [ {"IP": "172.16.2.10", "driver": "arista_eos"}, {"IP": "172.16.2.20", "driver": "arista_eos"} ]
## pyexcel.save_as(records=mylistdict, dest_file_name="ip_list.xls")


# Runtime
mylistdict = []  # this will be our list we turn into a *.xls file

print("Hello! This program will make you a *.xls file")

while(True):
    mylistdict.append(get_ip_data()) # add an item to the list returned by get_ip_data() {"IP": value, "driver": value}
    keep_going = input("\nWould you like to add another value? Enter to continue, or enter 'q' to quit: ")
    if (keep_going.lower() == 'q'):
        break

filename = input("\nWhat is the name of the *.xls file? ")

pyexcel.save_as(records=mylistdict, dest_file_name= filename + str('.xls'))

print("The file " + filename + ".xls should be in your local directory")
