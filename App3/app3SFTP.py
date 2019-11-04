# Project: Project Diamond
# Purpose Details: Secure File Transfer
# Course: IST 411 Fall 2019
# Author: Team 1
# Date Developed: 11/04/19
# Last Date Changed:
# Rev:

#https://pysftp.readthedocs.io/en/release_0.2.9/
import pysftp, sys
import config

class app3SFTP:
    # Initialize using config file
    def __init__(self):
        self.cnopts = config.cnopts
        cnopts.hostkeys = None
        self.cnopts = config.cinfo

    # Start connection and move files
    def connectSFTP(self, db):
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


