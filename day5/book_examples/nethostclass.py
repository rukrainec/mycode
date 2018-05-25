#!/usr/bin/env python3
#class examples

class Nethost:
    dhcp = []
    def __init__(self, name, mac, ip):
        self.name = name
        self.mac = mac
        self.ip = ip

    def addDHCP(self, dhcp):
        self.dhcp.append(dhcp)

    def __str__(self):
        return self.name + ' ' + self.mac + ' ' + self.ip
    def showDHCP(self):
        sdhcp = ''
        for x in self.dhcp:
            sdhcp += str(x) + ' '
        return sdhcp
User1 = Nethost('WS01', 'a1:b2:c3:d4', '192.168.1.1')
User1.addDHCP(3)
User1.addDHCP(4)
User1.addDHCP(12)
User1.addDHCP(15)
User1.addDHCP(42)

print(User1)
print(User1.showDHCP())

