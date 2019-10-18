import unittest

#from pymongo import MongoClient
from mongo import MongoDB

class MongoTest(unittest.TestCase):
#    def testInstance(self):
#        mongoDB = MongoDB()
        

    #testing readAndDecodeJSON method
    def testInsertOne(self):
        mongoDB = MongoDB()
        self.assertTrue(mongoDB.mongoInstance("Unit test", "testing unit"))
        #self.assertEqual(("Unit test", "testing unit"), collection.find({"Type": "Unit test"}))

