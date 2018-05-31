#!/usr/bin/env python3
import urllib.request
import json
import webbrowser
import re

######GOALS#######
#create a python client that can query APIs across a WAN
#in this case, grab nasa's astronomy picture of the day

#base URL and my nasa api key:
apodurl = 'https://api.nasa.gov/planetary/apod?api_key=fuux1BQoy7PKOF5CLUDcgqkNaJJW1oZuVJPReuzF'

#Customization request 1: allow user to input date of apod they want to see, default to today
while(True):
    apoddate = input('Date of picture you want to see? (format in YYYY-MM-DD, or hit \'Enter\' for today\'s APOD)\n>')
    if re.match("\d{4}-\d{2}-\d{2}", str(apoddate)):
        print('Thanks! Finding APOD for ' + str(apoddate) + '...')
        break
    if apoddate == '':
        print('Thanks! Finding APOD for today...')
        break
    else:
        print('Invalid date! That won\'t work!')

#Customization request 2: allow user option to retrieve HD picture data
hdef = input('Would you like your image in HD? (1 for yes, 2 for no)')
if hdef == 1: hdef = True
else: hdef = ''

#New URL with all the options addedls
newapodurl = str(apodurl) + '&date=' + str(apoddate) + '&hd=' + str(hdef)

#open the url
apodobj = urllib.request.urlopen(newapodurl)

apodread = apodobj.read()

decodeapod = json.loads(apodread.decode('utf-8'))

print('\n\nConverted python data')
#Customization request 3: fix the print statement so it doesn't print entire json response, ONLY display explanation, date, and title
print('Date: ' + str(decodeapod["date"]) + '\nDescription: ' + str(decodeapod["explanation"]))

input('\nPress Enter to open NASA Picture of the Day in Firefox')
webbrowser.open(decodeapod['url'])





