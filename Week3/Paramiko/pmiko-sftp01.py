#!/usr/bin/env python3
#4 June 2018, Lab 66 'Paramiko and SFTP'

import paramiko
import os

def sftpput():
    oldfile = input('What file do you want to send to the remote host?\n>')
    while not os.path.isfile(oldfile):
        print('Can\'t find that file, try the full path (or spellcheck)')
        oldfile = input('What file do you want to send to the remote host?')
    newfile = input('\n\n\nWhat do you want the new file to be called?\nRemember, this is Linux, no spaces or other weirdstuff\n' + uname + '@' + dest + '>')
    sftp.put(oldfile, newfile)

def sftpget():
    oldfile = input('What file do you want to retrieve from the remote host?\n' + uname + '@' + dest + '>')
    newfile = input('\n\n\nWhat do you want the new file to be called?\nRemember, this is Linux, no spaces or other weirdstuff\n>')
    sftp.get(oldfile, newfile)

dest = input('What is the IP address of the host you want to connect to?\n>')
uname = input('What is the user you want to log in as?\n>')
t = paramiko.Transport((dest, 22))
t.connect(username=uname, password="alta3")
sftp = paramiko.SFTPClient.from_transport(t)
sftp.listdir()

while(True):
    action = input('What would you like to do today?\n    Type GET to get a file from remote host\n    Type PUT to add a file to the remote host\n    Type Q to quit\n' + uname + '@' + dest + '>')
    if action.lower() == 'q':
        print('Thanks for playing!')
        break
    elif action.lower() == 'get':
        sftpget()
    elif action.lower() == 'put':
        sftpput()
    else:
        print("I'm sorry, I didn't get that")
t.close()
