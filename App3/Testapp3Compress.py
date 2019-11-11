# Project: Project Diamond
# Purpose Details: Test compression for app3
# Course: IST 411
# Author: Team 1
# Date Developed: 11/11/19
# Last Date Changed:
# Rev:

import unittest, json, zlib
from app3Compress import CompressPayload

class CompressPayloadTest(unittest.TestCase):
    def setUp(self):
        payload = open('payloadTeam1.py', 'rb')
        self.data = payload.read()
        payload.close()
        self.checksum = zlib.crc32(data)
    def testPayloadCompressed(self):
        compressed = CompressPayload(self.data)
        newChecksum = zlib.crc32(compressed)
        self.assertEqual(self.checksum, newChecksum)
