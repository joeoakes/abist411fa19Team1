# Project: Project Diamond
# Purpose Details: Use Pyro ORB to send an object for App3 to use
# Course: IST 411
# Author: Team 1
# Date Developed: 11/10/19
# Last Date Changed: 
# Rev: 


import Pyro4

''' Receive Pyro object from App3 and provide pyro methods for App3 to use '''
class App4Pyro:
    ''' Methods interacting with Pyro4 '''
    def __init__(self):
        self.payload = []

    ''' To get the URI for later use '''
    def getURI(self):
        @Pyro4.expose
        class SendPayload(object):
            ''' Setting up variables to be used '''
            def __init__(self, payload):
                self.payload = payload

            ''' Adds payload to constructor variable '''
            def sendPyro(self, payloadSent):
                try:
                    self.payload.append(payloadSent)

                    # Logging

                except Exception as e:
                    print("Error: %s" % e)

                    # Logging
        try:

            daemon = Pyro4.Daemon()
            uri = daemon.register(SendPayload(self.payload))
            print("Ready. Object uri = ", uri)
            print("Waiting for pyro object to send")
            daemon.requestLoop()
            daemon.close()
            print("Daemon closed.\n")
            print("Payload contents: ")
            print(self.payload[0])
            print("")

            # Logging

            return True
        except Exception as e:
            print("Error: %s" % e)

            # Logging

            return False



