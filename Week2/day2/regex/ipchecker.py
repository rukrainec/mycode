#!/usr/bin/env python3
#30 May 2018, Lab 48 'User RegEx ...IP Address'

import urllib.request
import re
import netifaces

def get_external_ip():
    url = 'http://checkip.dyndns.org'
    requesty = urllib.request.urlopen(url).read().decode('utf-8')
    externalIP = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', requesty)
    return externalIP

print('Your public IP address is: ' + str(get_external_ip()))
for i in netifaces.interfaces():
    try:
        print('Your local IP address is: ' +str(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr']))
    except: break
