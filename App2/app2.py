# Project: Project Diamond App 2
# Purpose: Implement App 2 to receive secure payload using TLS
# Course: IST 411-001
# Author: Team 1, Teresa Barker and Asraa Alkurdi
# Date Developed: October 9, 2019
# Last Date Revised: November 13, 2019
# Rev: 9

import hmac
import socket
import ssl
from mongo import MongoDB
import pysftp
import hashlib
import sys
import os
# import base64


class App2:

    def __init__(self):
        self.dataRecieved = None

    def tls_connection(self):
        try:
            # Receive the secure payload using TLS
            print("App 2 connecting on port 8080 using SSL (TLS)")
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s2.connect(('localhost', 9999))
            s2.send(b'App 2 got connection from app 1')
            s2.close()
            ssl_socket = ssl.wrap_socket(s,
                                         server_side=True,
                                         certfile="team1tls.crt",
                                         keyfile="team1tls.key")

            # Listen on port 8080
            ssl_socket.bind(('localhost', 8080))
            ssl_socket.listen(5)
            mongoDB = MongoDB()
            condition = True
            while condition:
                print("Accept connections from outside")
                (clientSocket, address) = ssl_socket.accept()
                #print(clientSocket.recv(1024))
                self.dataRecieved = clientSocket.recv(1024)
                print(self.dataRecieved)
                mongoDB.mongoInstance("Test", "Got Connection")
                if(clientSocket.recv(1024) is None):
                    condition = False
                    #print(dataRecieved)
                    #hash_payload_hmac(dataRecieved)
        except Exception as e:
            print(e)

    #@staticmethod
    def hash_payload_hmac(self):
        try:
            # Hash the JSON payload and append it to the message (HMAC SHA-256)
            #cur_path = os.path.dirname(__file__)
            #print(cur_path)
            #os.chdir("../App1")
            #print(os.path.abspath(os.curdir))
            #new_path = os.path.relpath('~/abist411fa19Team1/jsonPayload.txt', cur_path)

            #payload = open('jsonPayload.txt', 'rb')
            #data = payload.read()
            #data = bytes(data, 'UTF-8')
            print(self.dataRecieved)
            checksum = hashlib.md5(self.dataRecieved.encode()).hexdigest()

            checksum = hashlib.sha256(self.dataRecieved.encode()).hexdigest()
            print("SHA256: ", checksum)

            # create a message and a key
            message = "This is a message"
            key = "This is a key"

            # put message and key in byte format
            message = bytes(message, 'UTF-8')
            key = bytes(key, 'UTF-8')

            # create HMAC digester object
            digesterObject = hmac.new(key, message, hashlib.sha1)

            # call digest() to create signature
            signature = digesterObject.digest()
            print('signature: ', signature)

            s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s2.connect('localhost', 9999)
            s2.send('App 2 hashed message')
            s2.close()

            '''         *** could possibly be deleted ***
            # perform base64 encoding on the signature
            encodedSignature = base64.urlsafe_b64encode(signature)
            print('signature encoded in base64: ', encodedSignature)

            # compare two digests using compare_digest()
            compareDigests = hmac.compare_digest(signature, encodedSignature)
            print('signature and encodedSignature comparison: ', compareDigests)
            '''
        except Exception as e:
            print(e)

    #@staticmethod
    def send_payload_sftp(self):
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
                    sftp.put('payloadTeam1.json')

                    #sftp.get('/home/ftpuser/payloadTeam1.json')
                    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s2.connect(('localhost', 9999))
                    s2.send(b'App 2 sent payload via SFTP')
                    s2.close()

                except Exception as e:
                    print(e)
        except Exception as e:
            print("Log exception: ", sys.exc_info()[0])



