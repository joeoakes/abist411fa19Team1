# Project: Project Diamond
# Purpose Details: Unit test methods for Payload Saver
# Course: IST 411
# Author: Team 1
# Date Developed 10/10/2019
# Last Date Changed: 
# Rev: 0

import unittest
from PayloadSaver import PayloadSaver
from PayloadRetriever import PayloadRetriever

class PayloadSaverTest(unittest.TestCase):

    #testing savePayload method
    def testSavePayload(self):
        self.assertTrue(PayloadSaver().savePayload(
            PayloadRetriever().readAndDecodeJSON()))

