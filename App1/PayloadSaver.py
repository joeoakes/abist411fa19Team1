# Project: Project Diamond
# Purpose Details: Save JSON payload to a file
# Course: IST 411
# Author: Team 1
# Date Developed: 10/10/2019
# Last Date Changed:
# Rev:


import sys, json, datetime, socket
#from mongo import MongoDB
#from pymongo import MongoClient

''' To save payload '''
class PayloadSaver:

    ''' Writes payload to TEXT file '''
    def savePayload(self,payload,db):

        HOST = 'localhost'
        PORT = 9999
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            with open('jsonPayload.txt', 'w') as outFile:
                outFile.write(json.dumps(payload))
                #Logging
                db.mongoInstance("test","Saved Payload")
                s.connect((HOST, PORT))
                s.send('App 1 Saved Payload'.encode())
                s.close()
                return True

        except Exception as e:
            print("Error: %s" % e)

            #Logging
            db.mongoInstance("test","Failed to Save Payload")
            s.connect((HOST, PORT))
            s.send('App 1 Failed to save Payload'.encode())
            s.close
            return False

