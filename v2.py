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
            tn = telnetlib.Telnet(switch['HOST'], switch['port'], timeout=1)
            time.sleep(2)
            tn.write("\r")
            time.sleep(3)

            access_verify = '\r\n\r\nUser Access Verification\r\n\r\nUsername: '

            if tn.read_until("Username: ", 3) == access_verify:
                tn.write(switch['user'] + "\r")
                tn.read_until("Password: ", 3) == "Password"
                tn.write(switch['password'] + "\r")

            tn.write('enable' + "\r")
            time.sleep(2)
            tn.write(switch['enable_password'] + '\r')
            time.sleep(2)
            tn.write("terminal length 0" + "\r")
            time.sleep(2)
            tn.write(commands.exec_command1 + "\r")
            time.sleep(4)
            tn.write("exit\r")
            time.sleep(3)
            str_return_val = tn.read_very_eager()
            time.sleep(3)
            return str_return_val
        except Exception:
            pass
            print ("\n\nThis switch is not reachable: %s %s \n" % (switch['HOST'], switch['port']))
