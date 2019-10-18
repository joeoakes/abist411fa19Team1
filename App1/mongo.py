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
            print("error:%s"%e)

    def mongoInstance(self, typer, text):
        try:
            post = {"type":typer, 
                    "text":text, 
                    "date": datetime.datetime.utcnow()}
            print("Created the Document Object")
            post_id = self.collection.insert_one(post)
            return True
        except Exception as e:
            print("error:%s"%e)
            return False

