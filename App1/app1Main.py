
#Project: Project Diamond
#Purpose Details: Retrieve a JSON payload from the internet and send it to App2 using TLS. It will also retrieve an encrypted payload from App4 and save the JSON payload to a text file.
#Course: IST 411
#Author: Team 1
#Date Developed: 10/9/2019
#Last Date Changed:10/12/2019
#Rev: 0


#This will call all other classes created, related to App1.
import sys
from PayloadRetriever import PayloadRetriever
from PayloadSaver import PayloadSaver
from SendPayload import SendPayload
from pymongo import MongoClient


def main():
    client = MongoClient('localhost', 27017)
    db = client.Team1
    collection = db.logs
    print("Retrieving JSON payload from source.")
    payload = PayloadRetriever().readAndDecodeJSON()

    print("Sending payload to App2.")
    SendPayload().sendPayload(payload)

    print("Saving payload to text file.")
    PayloadSaver().savePayload(payload)



if __name__ == '__main__':
    main()



