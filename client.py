import v2
import ip_address
import sys
import logging

#switch_name = raw_input('Please enter switch name: ')

for key in ip_address.switch_list:
    print ("\n\nThe IP Address and port number of the switch is: %s %s \n" % ((ip_address.switch_list.get(key)['HOST']), (ip_address.switch_list.get(key)['port'])))
    obj = v2.NetworkDevice()
    result = obj.telnetToSwitch(ip_address.switch_list.get(key))
    print result
    logging.basicConfig(filename='output.log', filemode='w', level=logging.INFO)
    logging.info(result)

