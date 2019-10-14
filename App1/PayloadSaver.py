# Project: Project Diamond
# Purpose Details: Save JSON payload to a file
# Course: IST 411
# Author: Team 1
# Date Developed: 10/10/2019
# Last Date Changed:
# Rev:


import sys, json, datetime
from mongo import MongoClient

# To save payload
class PayloadSaver:

    #Writes payload to TEXT file
    def savePayload(self,payload):
        try:
            with open('jsonPayload.txt', 'w') as outFile:
                outFile.write(json.dumps(payload))
                client = MongoClient('localhost', 27017)
                db = client.Team1
                collection = db.logs
                #Logging
                post_id = collection.insert_one({"Type": "Test","Time": datetime.datetime.utcnow(), "Action": "Saved Payload"})
                return True

        except Exception as e:
            print("Error: %s" % e)

            #Logging
            post_id = collection.insert_one({"Type": "Test","Time": datetime.datetime.utcnow(), "Action": "Failed to Save Payload"})

            return False

