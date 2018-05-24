#!/usr/bin/env python3
#24 May 2018, lab 23 'outputting data to files' part 2

# take a bunch of stuff from a csv and output it to other stuff

import csv
f = open('csv_users.txt', 'r') #created file object from source csv file
i = 0 # set counter to 0

for row in csv.reader(f): # csv.reader is a function to read each line of the file
    i = i + 1
    filename = 'admin.rc%d'%(i,) #establishes output file, which changes name as value of i changes on each iteration of the loop
    rcfile = open(filename, 'w')
    print('export OS_AUTH_URL= ' + row[0], file=rcfile)
    print('export OS_IDENTITY_API_VERSION= 3', file=rcfile)
    print('export OS_PROJECT_NAME= ' + row[1], file=rcfile)
    print('export OS_PROJECT_DOMAIN_NAME= ' + row[2], file=rcfile)
    print('export OS_USERNAME= ' + row[3], file=rcfile)
    print('export OS_USERNAME_DOMAIN_NAME= ' + row[4], file=rcfile)
    print('export OS_PASSWORD= ' + row[5], file=rcfile)
    rcfile.close()

