#!/usr/bin/env python3
#24 May 2018, lab 26 'Conjunction Function'

# function to push commands
def commandpush(devicecmd): # devicecmd==list 
    for coffeetime in devicecmd.keys():
        print('Handshaking. .. ... connecting with ' + coffeetime )
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[coffeetime]:
            print('Attempting to sending command --> ' + mycmds + '\n')
            # we'll learn to write code that sends cmds to device here

def devreboot(iplist):
    for x in iplist:
        print('Connecting to ' + x) #would use same code from above to connect
        print('...... \nREBOOTING NOW!\n') #would use same code from above to issue reboot command

### Start our script
work2do = {"10.1.0.1":["interface eth1/2", "no shut"], "10.2.0.1":["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]} # data that replaces data stored in file

# make work2do create dictionary from file key:value odd_lines:even_lines
# or create from csv of ip addrs and commands?

devlist = ['10.1.0.1', '10.2.0.1', '10.3.0.1']

print("Welcome to the network device command pusher") # welcome message

## get data set
print("\nData set found\n") # replace with function call that reads in data from file

## run 
commandpush(work2do) # call function to push commands to devices
devreboot(devlist)
