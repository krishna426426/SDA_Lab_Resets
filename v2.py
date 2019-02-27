#!/usr/bin/python
#
# Copyright (c) 2018  Krishna Kotha <krkotha@cisco.com>
# All rights reserved.

# import the requests library

import sys
import time
import datetime
import re
import paramiko
import yaml
import logging
import pprint
import traceback
from pprint import pprint as pp
from fileinput import filename
import json
import requests
import telnetlib
import ip_address
import commands


class NetworkDevice:
    def telnetToSwitch(self, switch):
        str_return_val = " "
        try:
            #creates a telnet connection to the switch
            tn = telnetlib.Telnet(switch['HOST'], switch['port'], timeout=1)
            time.sleep(2)
            tn.write("\r")
            time.sleep(3)

            access_verify = '\r\n\r\nUser Access Verification\r\n\r\nUsername: '

            # if switch prompts username then enter the username if not skip
            if tn.read_until("Username: ", 3) == access_verify:
                tn.write(switch['user'] + "\r")
                tn.read_until("Password: ", 3) == "Password"
                tn.write(switch['password'] + "\r")

            # typing in the enable secret password
            tn.write('enable' + "\r")
            time.sleep(2)
            tn.write(switch['enable_password'] + '\r')
            time.sleep(2)

            # for the IOS XE device to get rid of the '---More---'
            tn.write("terminal length 0" + "\r")
            time.sleep(2)

            # execute the command from the command file
            tn.write(commands.exec_command1 + "\r")
            time.sleep(4)

            # exit out of the switch
            tn.write("exit\r")
            time.sleep(3)

            #read the whatever output it displayed to the main function
            str_return_val = tn.read_very_eager()
            time.sleep(3)
            return str_return_val

        #if any of the device is not reachable, it skips that device and continue on other devices
        except Exception:
            pass
            print ("\n\nThis switch is not reachable: %s %s \n" % (switch['HOST'], switch['port']))
