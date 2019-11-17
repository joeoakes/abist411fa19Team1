# Project: Project Diamond
# Purpose Details: Retrieve a JSON payload from the internet
# Course: IST 411
# Author: Team 1
# Date Developed: 10/9/2019
# Last Date Changed:10/13/2019
# Rev:


import sys, urllib.request, json, datetime
import config, socket
from mongo import MongoDB

''' Retrieve Payload '''
class PayloadRetriever:
    ''' Default constructor declaring URL and PARAM going to be used '''
    def __init__(self):
        self.url = config.URL
        self.param = config.PARAM

    ''' Gets JSON payload using URL and PARAM '''
    def readAndDecodeJSON(self, db):
        HOST = 'localhost'
        PORT = 9999
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            with urllib.request.urlopen(self.url + self.param) as payload:
                jsonPayload = json.loads(payload.read().decode('utf-8'))
                # Log to App5 Success

                s.connect((HOST, PORT))
                s.send('App 1 Payload created'.encode())
                s.close()

                db.mongoInstance("Test", "Got Payload")
                return jsonPayload


        except Exception as e:
            print("error: %s" % e)
            # Log to App5 Failure
            db.mongoInstance("Test", "Failed to get Payload")
            s.connect((HOST, PORT))
            s.send('App 2 Failed to create payload'.encode())
            s.close()

            return null
