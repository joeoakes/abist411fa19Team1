# Project: Project Diamond
# Purpose Details: To test the app3Email file
# Course: IST 411
# Author: Team 1
# Date Developed: 11/10/2019
# Last Date Changed:
# Rev:


import unittest, urllib.request, json
from app3Email import EmailPayload

''' Test EmailPayload class '''
class EmailPayloadTest(unittest.TestCase):
    ''' Setting up payload to use for testing '''
    def setUp(self):
        with urllib.request.urlopen('https://jsonplaceholder.typicode.com/posts/1') as payload:
            self.jsonPayload = json.loads(payload.read().decode('utf-8'))

    ''' Testing sendEmail method '''
    def testEmailisSent(self):
        email = EmailPayload(self.jsonPayload)
        self.assertTrue(email.sendEmail())
