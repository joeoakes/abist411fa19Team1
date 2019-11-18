# Project: Project Diamond
# Purpose Details: Secure File Transfer
# Course: IST 411 Fall 2019
# Author: Team 1
# Date Developed: 11/04/19
# Last Date Changed: 11/12/19
# Rev:

#https://pysftp.readthedocs.io/en/release_0.2.9/
import pysftp, sys
import config

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
cinfo = {'cnopts':cnopts, 'host': 'oz-ist-linux-oakes', 'username':'ftpuser','password':'test1234','port':100}

"""This class receives payload from a SFTP server"""
class SFTPReceive:

    """Initialize using config file"""
    def __init__(self):
        self.cnopts = config.cnopts
        cnopts.hostkeys = None
        self.cinfo = config.cinfo

    """Start connection and move files"""
    def connectSFTP(self):
        try:
            with pysftp.Connection(**cinfo) as sftp:
                print("Connection made")
                try:
                        print("getting payloadReceiveTeam1.json file")
                        sftp.get('/home/ftpuser/payloadReceiveTeam1.json')
                        sftp.remove('/home/ftpuser/payloadReceiveTeam1.json')
                except:
                        print("Log exception 1:", sys.exc_info()[0])
        except:
            print("Log exception 2:", sys.exc_info()[0])


