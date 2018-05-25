#!/usr/bin/env python3
#25 May 2018, lab 28

import netifaces
print('The list of interfaces is: \n' + str(netifaces.interfaces()) + '\n  [0]    [1]    [2]      [3]')



for i in netifaces.interfaces():
    print('\n**************Details of Interface - ' + i + ' *********************')
    try:
        print('MAC: ', end='')
        print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr'])
        print('IP: ', end='')
        print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
    except:
        print('could not collect adapter information')

### create a function that returns just the ip address (& another for just MAC)
