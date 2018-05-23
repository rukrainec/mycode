#!/usr/bin/env python3
# 22 May 2018, Lab 15 'Pythong Dictionaries'

## create a dictionary
switch = {'hostname': 'sw1', 'ip': '10.0.1.1', 'version': '1.2', 'vendor': 'cisco'}
    
## display parts of the dictionary
print( switch['hostname'] )
print( switch['ip'] )
    
## request a 'fake' key
# print( switch['lynx'] )

## request a 'fake' key with .get() method
print( "First test - .get()" )
switch.get('lynx')

print( "Second test - .get()" )
switch.get('lynx', "THE KEY IS IN ANOTHER CASTLE!")

print( "Third test - .get()" )
switch.get('version')
    
## request a 'fake' key
# print( switch['lynx'] )

print('Fourth test - .keys()')
switch.keys()

print('Fifth test - .values()')
switch.values()

print( "Sixth test - .pop()" )
switch.pop('version') # removes this key (and value) pair
switch.keys()   # notice the value of version is gone
switch.values() # notice the value 1.2

print( "Seventh test - ADD a new value" )
switch['adminlogin'] = 'karl08'
switch.keys()
switch.values()

print( "Eighth test - ADD a new value" )
switch['password'] = 'qwerty'
switch.keys()
switch.values()
    
## request a 'fake' key
print(switch)
