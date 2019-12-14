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
import socket
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
            # Use SFTP to send the payload to App 3

            # specifying connection options
            cnopts = pysftp.CnOpts()
            cnopts.hostkeys = None
            cinfo = {'cnopts': cnopts,
                     'host': 'oz-ist-linux-oakes',
                     'username': 'ftpuser',    # FIXME add username
                     'password': 'test1234',    # FIXME add password
                     'port': 100}
            with pysftp.Connection(**cinfo) as sftp:
                print("Connection made")
                try:
                    print("Getting payloadTeam1.json file")
                    #sftp.get('/home/ftpuser/payloadTeam1.json')
                    json = sftp.get('payloadTeam1.json')

                    #sftp.get('/home/ftpuser/payloadTeam1.json')
                    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s2.connect(('localhost', 9999))
                    s2.send(b'App 3 recieved payload via SFTP')
                    s2.close()
                except Exception as e:
                    print(e)
        except Exception as e:
            print("Log exception: ", sys.exc_info()[0])

