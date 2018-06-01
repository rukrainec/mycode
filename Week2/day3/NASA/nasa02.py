#!/usr/bin/env python3
import urllib.request
import json
import webbrowser
import re

## Define NEO parameters 
neourl = 'https://api.nasa.gov/neo/rest/v1/feed?'
startd = input('What is your desired start date? (YYYY-MM-DD or \'enter\' for today)\n>')
startdate = 'start_date=' + str(startd)
endd = input('What is the end date? (YYYY-MM-DD only or \'enter\' for 7 days after start date)\n>')
enddate = '&end_date=' + str(endd)
mykey = '&api_key=fuux1BQoy7PKOF5CLUDcgqkNaJJW1oZuVJPReuzF'    

neourl = neourl + startdate + enddate + mykey

## Call the webservice
neourlobj = urllib.request.urlopen(neourl)

## read the file-like object
neoread = neourlobj.read()

## decode json to python data structure
decodeneo = json.loads(neoread.decode('utf-8'))

#create a function that will print miss_distance converted to moon-lengths for each neo above

def moon_lens(miss_distance):
    return float(miss_distance) / 238900

for key in decodeneo['near_earth_objects'].keys():
    neo = 0 #to set number of iterations
    while neo < decodeneo['near_earth_objects'][key].__len__(): #loop through neo list
        print('NEO ID = ' + decodeneo['near_earth_objects'][key][neo]['name'], end='')
        print('  Close Approach Date: ' + str(decodeneo['near_earth_objects'][key][neo]['close_approach_data'][0]['close_approach_date']))
        print('    Miss Distance (in miles): ' + decodeneo['near_earth_objects'][key][neo]['close_approach_data'][0]['miss_distance']['miles'])
        print('    Miss Distance (in moon lengths): ' + str(round(moon_lens(decodeneo['near_earth_objects'][key][neo]['close_approach_data'][0]['miss_distance']['miles']), 2)))
        neo += 1

## display our pythonic data
#print("\n\nConverted python data")
print('Information retrieved from :\n' + neourl) #to verify outputted data straight from the source


    
