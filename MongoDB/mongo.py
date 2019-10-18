import sys, datetime
from pymongo import MongoClient

class MongoDB:
    def __init__(self):
        
        try:
            client = MongoClient('localhost', 27017)
            print("Connected to MongoDB")
            db = client.Team1Fall
            print("Got the Database test_database")
            self.collection = db.logs
            print("Got the Collection")

        except Exception as e:
#            e = sys.exc_info()[0]
            print("error:%s"%e)

    def mongoInstance(typer, text):
        try:
#            client = MongoClient('localhost', 27017)
#            print("Connected to MongoDB")
#            db = client.Team1Fall
#            print("Got the Database test_database")
#            collection = db.logs
#            print("Got the Collection")
            post = {"type":typer, 
                    "text":text, 
                    "date": datetime.datetime.utcnow()}
            print("Created the Document Object")
            post_id = self.collection.insert_one(post)
        except Exception as e:
#            e = sys.exc_info()[0]
            print("error:%s"%e)

