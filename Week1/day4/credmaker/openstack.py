#!/usr/bin/env python3
#24 May 2018, lab 23 'outputting data to files'

outfile = open('admin.rc', 'a') # establish file where results are printed, in append mode

# now get some input and append to the file
print('What is the OS_AUTH_URL?')
osauth = input()
print('export OS_AUTH_URL= ' + osauth, file=outfile) #actually appends to the file

print('export OS_IDENTITY_API_VERION=3', file=outfile)

print('What is the OS_PROJECT_NAME?')
osproj = input()
print('export OS_PROJECT_NAME= ' + osproj, file=outfile)

print('What is the OS_PROJECT_DOMAIN_NAME?')
osdom = input()
print('export OS_PROJECT_DOMAIN_NAME= ' + osdom, file=outfile)

print('What is the OS_USERNAME?')
osuname = input()
print('export OS_USERNAME= ' + osuname, file=outfile)

print('What is the USER_DOMAIN_NAME?')
osudom = input()
print('export USER_DOMAIN_NAME= ' + osudom, file=outfile)

print('What is the OS_PASSWORD?')
ospass = input()
print('export OS_PASSWORD= ' + ospass, file=outfile)

outfile.close()
