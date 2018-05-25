#!/usr/bin/env python3
#24 May 2018, lab 22 'parsing log files'

#Goals: make a script that reads through a file and counts occurences of desired string (failed logins in this case)

loginfail = 0 #establish counted variable and set count to 0
loginpass = 0 #counter for good logins
ipfail = [] #list for ip's of failed login attempts

keystone_file = open('/home/student/mycode/day4/attemptlogin/keystone.common.wsgi', 'r') #creates file object for desired file in read only mode
keystone_file_lines=keystone_file.readlines() #creates a list where each item is a line from the file
keystone_file.close() #stop reading the file, we've extracted what we need

#begin the loop
for i in range(len(keystone_file_lines)): #sets range as total number of lines in original file
    if "- - - - -] Authorization failed" in keystone_file_lines[i]: #sets condition for failed login
        loginfail +=1 #increment counter

        keystone_file_ip=keystone_file_lines[i] #new list of lines that meet if criteria
        ip_split=keystone_file_ip.split() #new list of individual words from _ip list
        ipfail.append(ip_split[-1])
    elif '-] Authorization failed' in keystone_file_lines[i]:
        loginpass +=1
print('The number of failed login attempts is ' + str(loginfail))
print('The source(s) of the failed login attempts: ' + str(ipfail))
print('The number of successful login attempts is ' + str(loginpass))
    
