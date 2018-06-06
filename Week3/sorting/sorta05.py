#!/usr/bin/env python3
#6 June 2018, lab 73 'Sort stability and complex sorts'
#written by Robert Ukrainec

company_gear = [('cisco', '2015', '192.168.10.14'), ('cisco', '2011', '192.168.11.14'), ('cisco', '1999', '10.10.10.14'), ('cisco', '2018', '10.1.6.14'), ('juniper', '2018', '10.7.6.10'), ('dell', '2007', '10.55.2.12'), ('juniper', '2014', '192.168.30.44'), ('cisco', '2008', '10.0.2.1'), ('cisco', '2009', '10.2.3.77'), ('dell', '2009', '10.6.77.1'), ('juniper', '2004', '192.168.66.19'), ('arista', '2016', '192.168.88.22'), ('arista', '2016', '192.68.88.11'), ('cisco', '2001', '10.12.1.7'), ('juniper', '2002', '10.0.0.2')]

def byName(x):
    return x[0]
def byYear(x):
    return x[1]
def byIP(x):
    return x[2]

vendor_name = sorted(company_gear, key=byName)
vendor_name_year = sorted(vendor_name, key=byYear)
vendor_name_year_HtL = sorted(vendor_name, key=byYear, reverse=True)
vendor_name_IP = sorted(vendor_name, key=byIP)


print('Original:\n', company_gear)
print('\n\nBy name only:\n', vendor_name)
print('\n\nBy name AND year:\n', vendor_name_year)
print('\n\nBy name AND year, most recent year first:\n', vendor_name_year_HtL) 
print('\n\nBy name AND IP:\n', vendor_name_IP)
