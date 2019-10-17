# Project: Project Diamond App 2
# Purpose: Test App 2
# Course: IST 411-001
# Author: Team 1, Teresa Barker and Asraa Alkurdi
# Date Developed: October 9, 2019
# Last Date Revised: October 16, 2019
# Rev: 2

import unittest, socket, ssl
#from SendPayload import SendPayload
import app2

class TestApp2(unittest.TestCase):

    def testApp2(self):
        payload = "message"
        self.assertEqual(app2.getConnection(), True)
