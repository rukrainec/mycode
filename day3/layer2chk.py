#!/usr/bin/env python3
# 23 May 2018, while loop exercise
# prompt user for L2 protocols, restart loop if not recognized, if input matches to protocol end script with message

while(True): # set up an infinite loop to practice 'continue' and 'break'
	l2p = input('What protocol would you like to use?: \n')
	
	if l2p == 'eth':
		print('Ethernet protocol allowed \nThank you!')
		break
	elif l2p == 'fc':
		print('Fiber channel is NOT allowed! >:( ')
		break
	elif l2p == 'ifb':
		print('Infiniband NOT allowed! >:( ')
		break
	elif l2p == 'otn':
		print('Optical Network allowed \nThank you!')
		break
	else:
		print('No idea what that tehcnology is')
#		continue #not required, already an infinite loop
