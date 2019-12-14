# Project: Project Diamond
# Purpose Details: Use Pyro ORB to send an object for App3 to use
# Course: IST 411
# Author: Team 1
# Date Developed: 11/10/19
# Last Date Changed: 12/13/19
# Rev: 


import Pyro4, datetime, socket

''' Receive Pyro object from App3 and provide pyro methods for App3 to use '''
class App4Pyro:
    ''' Methods interacting with Pyro4 '''
    def __init__(self):
        self.payload = []

    ''' To get the URI for later use '''
    def getURI(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
            print(self.payload)
            print("")

            # Logging success
            s.connect('localhost', 9999)
            s.send('App 4 created Pyro object'.encode())
            s.close()

            return self.payload
        except Exception as e:
            print("Error: %s" % e)

            # Logging
            s.connect('localhost', 9999)
            s.send('App 4 failed to create object'.encode())
            s.close()



