#!/usr/bin/env python3
#6 June 2018, lab 70 'Custom sorted() with key'
#written by Robert Ukrainec

iplist = ['10.8.2.1', '1.1.1.1', '255.255.255.255', '10.1.2.1', '10.2.1.2', '10.2.3.2', '10.7.2.1', '192.168.23.1', '192.168.66.1', '10.42.2.1', '10.11.10.2', '10.25.32.2', '10.27.21.1', '192.168.55.1']

print('Currently iplist looks like this: ', iplist)
print('This is what it looks like default sorted(): ', sorted(iplist))

iplistkeyed = sorted(iplist, key=len)
print('iplist sorted by length: ', iplistkeyed)
revkeyiplist = sorted(iplist, key=len, reverse=True)
print('Reverse sorted by length: ', revkeyiplist)

dnsrecord_types = [ 'a', 'MX', 'AAAA', 'CNAME', 'naptr', 'ns', 'svr', 'SOA' ]
print('Results of sorting dns record list by str.lower; ', sorted(dnsrecord_types, key=str.lower))
