#!/usr/bin/env python3
#6 June 2018, Lab 72 'sorting lists of dictionaries'
#written by Robert Ukrainec

us_invasion = [{'ip':'10.10.1.2', 'un':'john', 'pw':'allstar'}, {'ip':'10.10.1.3', 'un':'paul', 'pw':'iils20s3'}, {'ip':'10.10.1.4', 'un':'george', 'pw':'hunkydoryzory'}, {'ip':'10.10.1.5', 'un':'stuart', 'pw':'alta3'}, {'ip':'10.10.1.6', 'un':'pete', 'pw':'a8dd827z3'}]

def byUserName(x):
    return x['un']

def byIP(x):
    return x['ip']

def byPass(x):
    return x['pw']

def byLastPass(x):
    return x['pw'][-1]

listbyusername = sorted(us_invasion, key=byUserName)

print('\nTrying to sort my list of dictionaries: ', listbyusername)

print('New function to sort by ip:\n', sorted(us_invasion, key=byIP))

print('\n\nAnd by password:\n', sorted(us_invasion, key=byPass))

print('\n\nAnd by last letter of password:\n', sorted(us_invasion, key=byLastPass))
