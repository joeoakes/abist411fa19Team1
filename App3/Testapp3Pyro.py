# Project: Project Diamond
# Purpose Details: Test App3Pyro
# Course: IST 411
# Author: Team 1
# Date Developed: 11/10/2019
# Last Date Changed:
# Rev:

import urllib.request, json, unittest, Pyro4
from app3Pyro import App3Pyro

class TestApp3Pyro(unittest.TestCase):
    def setUp(self):
        with urllib.request.urlopen('https://jsonplaceholder.typicode.com/posts/1') as payload:
            self.jsonPayload = json.loads(payload.read().decode('utf-8'))

    def testPyroPayload(self):
        self.assertTrue(App3Pyro.pyroPayload(self.jsonPayload))
