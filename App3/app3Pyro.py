# Project: Project Diamond
# Purpose Details: To transform the JSON message into a python object and use Pyro ORB to send the python object to app4
# Course: IST 411
# Author: Team 1
# Date Developed: 11/10/2019
# Last Date Changed:
# Rev:


import Pyro4

''' To create and send a pyro object to App4 '''
class App3Pyro:
    ''' Create and send pyro object '''
    def pyroPayload(payload):
        try:
            message = Pyro4.Proxy(input("Please enter the URI: ").strip())
            message.sendPyro(message)
            
            # Logging

            return True
            
        except Exception as e:
            print("Error: %s" % e)
            
            # Logging

            return False
