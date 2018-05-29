#!/usr/bin/env python3
#25 May 2018, Lab 36 'Space APIs; the final frontier'

import urllib
import json
## Trace the ISS
majortom = 'http://api.open-notify.org/astros.json'

## Call the webservice
groundctrl = urllib.request.urlopen(majortom)

## json 2 python data structure
helmetson = json.load(groundctrl.read())

## display our pythonic data
print("Converted python data")
print(helmetson)

print('\n'"People in Space: ", result['number'])
people = result['people']
print(people)
