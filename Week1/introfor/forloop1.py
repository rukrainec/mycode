#!/usr/bin/env python3
#22 May 2018, lab 18 'Looping with for'

vendors = ['cisco', 'juniper', 'big_ip', 'f5', 'arista'] #initial list of vendors
for x in vendors: # start for loop
    print("The vendor is: " + x.upper()) #print entries in list 'vendors' until complete
print("\nOur loop has ended.")
