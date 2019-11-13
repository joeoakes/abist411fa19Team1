# Project: Project Diamond
# Purpose Details: Test SFTP receiving
# Course: IST 411
# Author: Team 1
# Date Developed: 11/11/19
# Last Date Changed:
# Rev:

import sys, pysftp, unittest
import config

from app3SFTP import SFTPReceive

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
cinfo = {'cnopts':cnopts, 'host':'oz-ist-linux-oakes','username':'ftpuser','password':'test1234','port':100}

def start_sftp(cls):
    sftp.start_server('localhost', 3373, 'oz-ist-linux-oakes', 'INFO')

def setUp(cls):
    cls.process=start_process(target=cls.sart_sftp)
    cls.transport.connect(username='ftpuser', password='test1234', pkey=pkey)

def tearDown(cls):
    cls.sftp.close()
    cls.transport.close()
