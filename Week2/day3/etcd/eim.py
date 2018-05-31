#!/usr/bin/env python3
#31 May 2018, Lab 52 'Construct a ...HTTP Client'

import http.client
import re

conn = http.client.HTTPConnection("localhost", 9021) #(host, port, timeout, source_address=None)

while(True):
    print('Welcome to Grok\'s paleolithic webclient!\nWhat would you like to do?\nA- test connection (HEAD)\nB- Retrieve info (GET)\nQ- quit')
    action = input('>')
    if action.lower() == 'q':
        print('Thank you!')
        break
    if action.lower() == 'a':
        conn.request('HEAD', '/') #HEAD isn't a CRUD but will still get a response
        res = conn.getresponse() #define response
        print(res.status, res.reason)
    if action.lower() == 'b':
        conn.request('GET', '/') # this time we'll issue GET
        res = conn.getresponse() # res is equal to the response associated wtih conn
        print(res.status, res.reason) # print the response status code and reason  
        page_data = res.read()  # page_data is all of the data associated with res 
        print(str(page_data), file=open('http_readin.txt', 'w')) # this will print out all of the data assocaited with res
        print('The output of GET request has been dropped off in \"http_readin.txt\" if you really want to look at it')
    if not re.match("[a,b,q]", action):
        print('Invalid input!')
