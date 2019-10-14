import unittest
from pymongo import MongoClient

class MongoTest(unittest.TestCase):

    #testing readAndDecodeJSON method
    def testInsertOne(self):
        client = MongoClient('localhost', 27017)
        db = client.Test_DataBase
        collection = db.test_collection
        person={"Name": "Bob", "Job": "Builder"}
        post_id = collection.insert_one(person)
        self.assertEqual(person, collection.find({"Name": "Bob"}))
