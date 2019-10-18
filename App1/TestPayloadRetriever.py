# Project: Project Diamond
# Purpose Details: Unit test methods for Payload Reciever
# Course: IST 411
# Author: Team 1
# Date Developed 10/10/2019
# Last Date Changed: 
# Rev: 0

import unittest
from PayloadRetriever import PayloadRetriever
from mongo import MongoDB

class PayloadRetrieverTest(unittest.TestCase):
    
    #testing readAndDecodeJSON method
    def testReadAndDecodeJSON(self):
        db = MongoDB()
        payloadToCompare = {"userId": 1, "id": 1, "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit", "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"}
        self.assertEqual(PayloadRetriever().readAndDecodeJSON(db), payloadToCompare)
