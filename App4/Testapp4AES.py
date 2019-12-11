# Project: Project Diamond
# Purpose Details: Unit test methods for App 4
# Course: IST 411
# Author: Team 1
# Date Developed: 11/30/19
# Last Date Changed: 12/12/19
# Rev:

import unittest
from app4AES import App4AES

class App4AESTest(unittest.TestCase):
    def testAES(self):
        test = App4AES()
        self.assertTrue(test)
