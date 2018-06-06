#!/usr/bin/env python3
#6 June 2018, Lab 74 'List.sort() vs sorted()'
#written by Robert Ukrainec

vendors = ['cisco', 'juniper', 'big_ip', 'f5', 'arista', 'hp', 'dell']

print('original: ', vendors)
print('sorted but unchanged: ', sorted(vendors))
print('what? ', vendors.sort())
print('look what they did to vendors: ', vendors)
