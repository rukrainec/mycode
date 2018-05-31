#!/usr/bin/env python3
#30 May 2018, Lab 49 'use RegEx to search text'

import urllib.request
import re

###Customization 1: accept strings until quit is entered (while loop if .lower() == 'q')

while(True):
    url = input('Where should we search? (or hit q to quit)\n>')
    if url.lower() == 'q':
        print('Thank you for playing!')
        break

    print("Great! Let's see what " + str(url) + ' has for us!')
    searchFor = input('What do you want to find?\n>')
    searchme = urllib.request.urlopen(url).read().decode('utf-8')

    if re.search(searchFor, searchme):
        print('Found a match! :-)')
########Customization 2: return total number of matches:
        print('The thing you searched for was found ' + str(len(re.findall(searchFor, searchme))) + ' times.')
    else:
        print('No match ¯\_(*-*)_/¯ ')

######Customization 3: allow user to pass several words as input, determine how many lines in searchme contain any combination of the words input by user  
######I don't know where to start on this one      
