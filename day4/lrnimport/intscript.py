#!/usr/bin/env python3
#24 May 2018 lab 30 'from and import'

from subprocess import call
call(["ip", "link", "show", "up"])

print('This program will check your interfaces')

interface = input('Enter an enterface, like \'ens3\': ')
call(['ip', 'addr', 'show', 'dev', interface])


