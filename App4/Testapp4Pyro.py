# Project: Project Diamond
# Purpose Details: Unit test methods for App 4
# Course: IST 411
# Author: Team 1
# Date Developed: 11/10/18
# Last Date Changed: 
# Rev: 


import unittest
from app4Pyro import App4Pyro

class App4PyroTest(unittest.TestCase):
    def testURI(self):
        test = App4Pyro()
        self.assertTrue(test.getURI())
