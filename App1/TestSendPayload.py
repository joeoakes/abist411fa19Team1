# Project: Project Diamond
# Purpose Details: Test of SendPayload
# Course: IST 411
# Author: Team 1
# Date Developed: 10/11/19
# Last Date Changed: 10/12/19
# Rev: 2
import unittest, socket, ssl
from SendPayload import SendPayload
from PayloadRetriever import PayloadRetriever
class TestSendPayload(unittest.TestCase):

   def testSendPayload(self):
        results = SendPayload().sendPayload(PayloadRetriever().readAndDecodeJSON())
        self.assertTrue(results)
        
