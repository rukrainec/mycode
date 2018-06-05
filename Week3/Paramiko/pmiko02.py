#!/usr/bin/env python3
#4 June 2018, Lab 65 'Paramiko SSH to Remote Host'

import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.WarningPolicy())

while(True):
    computter = input('What is the ip address you want to connect to?\nOr press q to quit\n>')
    if computter.lower() == 'q': break
    uzor = input('What is the username you want to log in as?\n>')
    client.connect(computter, username=uzor, password='alta3')
    while(True):
        cmd = input('\n\nEnter the linux-friendly command you want to run on the remote machine.\nExamples include: \n      "ls -l"\n      "ping -c 5 8.8.8.8"\n      "sudo rm -rf ~"\nPress q to quit\n\n' + str(uzor) + '@' + str(computter) + '>')
        if cmd.lower() == 'q':
            print('Terminating connection to remote host.')
            client.close()
            break
        else:
            stdin, stdout, stderr = client.exec_command(cmd)
            print('result ' + cmd)
            for line in stdout:
                print(' ' + line.strip('\n'))   
print('Thanks for playing!')
