
import sys, datetime
from pymongo import MongoClient

class MongoDB:
    def mongoInstance(type, text):
        try:
            client = MongoClient(self,'localhost', 27017)
            print("Connected to MongoDB")
            db = client.Team1Fall
            print("Got the Database test_database")
            collection = db.logs
            print("Got the Collection")
            post = {"type":type, "text":text, "date": datetime.datetime.utcnow()}
            print("Created the Document Object")
            post_id = collection.insert_one(post)
        except:
            e = sys.exc_info()[0]
            print("error:%s"%e)
