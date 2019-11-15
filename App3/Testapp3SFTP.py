# Project: Project Diamond
# Purpose Details: Test SFTP receiving
# Course: IST 411
# Author: Team 1
# Date Developed: 11/11/19
# Last Date Changed:
# Rev:

import sys, pysftp, unittest
import config
from App1 import *

from app3SFTP import SFTPReceive

"""Test app3SFTP.py"""
class TestSFTP(unittest.TestCase):

    """Start an sftp server"""
    def start_sftp(cls):
        sftp.start_server('localhost', 100, 'oz-ist-linux-oakes', 'INFO')

    """Set up and initiation for sftp connection"""
    def setUp(cls):
        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None
        cinfo = {'cnopts':cnopts, 'host':'oz-ist-linux-oakes','username':'ftpuser','password':'test1234','port':100}

        cls.process=start_process(target=cls.sart_sftp)
        cls.transport.connect(username='ftpuser', password='test1234', pkey=pkey)

        with pysftp.Connnection(**cinfo) as sftp:
            try:
                sftp.get('/home/ftpuser/payloadReceiveTeam1.json')

                payload = open("payloadReceiveTeam1.json", "rb")
                assertEquals(payload.read(), App1.jsonPayload.txt.read())
            except Exception as e:
                print(e)

    """Close all running servers after tests"""
    def tearDown(cls):
        cls.sftp.close()
        cls.transport.close()
