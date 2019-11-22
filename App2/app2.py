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
# import base64


class App2:

    def tls_connection(self):
        try:
            # Receive the secure payload using TLS
            print("App 2 connecting on port 8080 using SSL (TLS)")
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ssl_socket = ssl.wrap_socket(s,
                                         server_side=True,
                                         certfile="team1tls.crt",
                                         keyfile="team1tls.key")

            # Listen on port 8080
            ssl_socket.bind(('localhost', 8080))
            ssl_socket.listen(5)
            mongoDB = MongoDB()
            while True:
                print("Accept connections from outside")
                (clientSocket, address) = ssl_socket.accept()
                print(clientSocket.recv(1024))

                mongoDB.mongoInstance("Test", "Got Connection")

                mongoDB.mongoInstance("Test", "Got Connection")
        except Exception as e:
            print(e)

    @staticmethod
    def hash_payload_hmac(self):
        try:
            # Hash the JSON payload and append it to the message (HMAC SHA-256)
            payload = open('payload.json', 'rb')
            data = payload.read()
            data = bytes(data, 'UTF-8')
            checksum = hashlib.md5(data.encode()).hexdigest()

            checksum = hashlib.sha256(data.encode()).hexdigest()
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

    @staticmethod
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
                    sftp.get('/home/ftpuser/payloadTeam1.json')
                    sftp.put('/home/ftpuser/payloadTeam1.json')
                except Exception as e:
                    print(e)
        except Exception as e:
            print("Log exception: ", sys.exc_info()[0])



