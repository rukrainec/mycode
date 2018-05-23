#!/usr/bin/env python3
#22 May 2018, lab 18 pt 2

vendors = ['cisco', 'juniper', 'big_ip', 'f5', 'arista', 'alta3', 'zach', 'stuart'] #list 1
approved_vendors = ['cisco', 'juniper', 'big_ip'] #list 2
for x in vendors:
    print("\nThe vendors is " + x, end="") #print entries in list 1
    if x not in approved_vendors:
        print(" - NOT AN APPROVED VENDOR!", end="") #adds message if item in list 1 is NOT in list 2
print("\nOur loop has ended.")
