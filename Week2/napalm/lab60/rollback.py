#!/usr/bin/env python3
#1 June 2018, lab 60 rollback a change
from napalm import get_network_driver
driver = get_network_driver('eos')
device = driver('172.16.2.20', 'admin', 'alta3')
device.open()
device.rollback()
