# Project: Project Diamond App 2
# Purpose: Test App 2
# Course: IST 411-001
# Author: Team 1, Teresa Barker and Asraa Alkurdi
# Date Developed: October 9, 2019
# Last Date Revised: October 16, 2019
# Rev: 2

import unittest, socket, ssl
from SendPayload import sendPayload


class TestApp2(unittest.TestCase):

    def testApp2(self):
        payload = "message"
        SendPayload().sendPayload(payload)
        self.assertEqual(serverssl_socket.recv(1024).decode(), "reply")
