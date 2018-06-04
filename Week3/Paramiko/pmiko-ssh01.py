#!/usr/bin/env python3
#4 June 2018, lab 64 'Introducing Paramiko"

import paramiko
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.WarningPolicy())
client.connect('localhost', username='student', password='alta3')
while(True):
    cmd = input('\n\nEnter the linux-friendly command you want to run on the remote machine.\nExamples include: \n      "ls -l"\n      "ping -c 5 8.8.8.8"\n      "sudo rm -rf ~"\nPress q to quit\n>')
    if cmd.lower() == 'q':
        print('Thanks for playing!')
        break
    else:
        stdin, stdout, stderr = client.exec_command(cmd)
        print('result ' + cmd)
        for line in stdout:
            print(' ' + line.strip('\n'))
print('Terminating connection to remote host.')
client.close()
