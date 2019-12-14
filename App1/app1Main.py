#Project: Project Diamond
#Purpose Details: Retrieve a JSON payload from the internet and send it to App2 using TLS. It will also retrieve an encrypted payload from App4 and save the JSON payload to a text file.
#Course: IST 411
#Author: Team 1
#Date Developed: 10/9/2019
#Last Date Changed:11/04/2019
#Rev: 0


#This will call all other classes created, related to App1.
import sys
from PayloadRetriever import PayloadRetriever
from PayloadSaver import PayloadSaver
from SendPayload import SendPayload
from mongo import MongoDB
from datetime import date
from RabbitReciever import RabbitReciever
import time
''' This will call all other classes created for App1 '''
def main():

    #timestamp = 1545730073
    #startDtObject = date.fromtimestamp(timestamp)
    #client = MongoClient('localhost', 27017)
    #db = client.Team1
    #collection = db.logs
    startTime = time.time()
    mongoDB = MongoDB()

#    print(startDtObject)
    print("Retrieving JSON payload from source.")
    payload = PayloadRetriever().readAndDecodeJSON(mongoDB)

    print("Sending payload to App2.")
    SendPayload().sendPayload(payload,mongoDB)

    print("Saving payload to text file.")
    PayloadSaver().savePayload(payload,mongoDB)

    RabbitReciever.getMessage(startTime)

    endTime = time.time()
    print(str(endTime-startTime) + " seconds")
    #endDtObject = date.fromtimestamp(timestamp)
    
    #print(((endDtObject-startDtObject).microseconds().total_seconds()))

if __name__ == '__main__':
    main()

