# Project: Project Diamond
# Purpose Details: Save JSON payload to a file
# Course: IST 411
# Author: Team 1
# Date Developed: 10/10/2019
# Last Date Changed:
# Rev:


import sys, json, datetime
#from mongo import MongoDB
#from pymongo import MongoClient

# To save payload
class PayloadSaver:

    #Writes payload to TEXT file
    def savePayload(self,payload):
        try:
            with open('jsonPayload.txt', 'w') as outFile:
                outFile.write(json.dumps(payload))
                #Logging
             #   MongoDB.mongoInstance("test","Saved Payload")
                return True

        except Exception as e:
            print("Error: %s" % e)

            #Logging
            #MongoDB.mongoInstance("test","Failed to Save Payload")


            return False

