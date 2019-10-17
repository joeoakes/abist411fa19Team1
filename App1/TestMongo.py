import unittest
#from pymongo import MongoClient
from mongo import MongoDB

class MongoTest(unittest.TestCase):

    #testing readAndDecodeJSON method
    def testInsertOne(self):
        MongoDB.mongoInstance("Unit test", "testing unit")
        self.assertEqual(("Unit test", "testing unit"), collection.find({"Type": "Unit test"}))

