# Project: Project Diamond
# Purpose Details: Test of SendPayload
# Course: IST 411
# Author: Team 1
# Date Developed: 10/11/19
# Last Date Changed: 10/12/19
# Rev: 2
import unittest, socket, ssl
from SendPayload import sendPayload

class TestSendPayload(unittest.TestCase):

   def setUp(self):
        s = socket(AF_INET, SOCK_STREAM)
        serverssl_socket = ssl.wrap_socket(s, server_side=True, certfile="team1tls.crt", keyfile="team1tls.key")
        serverssl_socket.bind(('localhost', 443))
        serverssl_socket.listen(5)
        while True:
             client, address = serverssl_socket.accept()

   def tearDown(self):
        serverssl_socket.close()

   def testSendPayload(self):
        payload = "message"
        SendPayload().sendPayload(payload)
        self.assertEqual(serverssl_socket.recv(1024).decode(), "reply")
