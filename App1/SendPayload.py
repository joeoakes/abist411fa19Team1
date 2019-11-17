# Project: Project Diamond
# Purpose Details: Send Payload using TLS
# Course: IST 411
# Author: Team 1
# Date Developed: 10/11/19
# Last Date Changed: 10/16/19
# Rev: 2
import socket, ssl, json, datetime, socket
from mongo import MongoDB
#from pymongo import MongoClient

"""Send payload to a different class"""
# To send payload
class SendPayload:

    """Send payload accepting payload and a database"""
    # Connect to server and send payload
    def sendPayload(self, payload,db):
         HOST = 'localhost'
         PORT = 9999
         s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            print("App 1 connecting on port 8080 using TLS")
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ssl_sock = ssl.wrap_socket(s,
                ca_certs="team1tls.crt",
                cert_reqs=ssl.CERT_REQUIRED)
            ssl_sock.connect(('localhost',8080))

            ssl_sock.sendall(json.dumps(payload).encode())
            print("JSON payload sent to _______ using TLS")
            ssl_sock.close()
            s1.connect((HOST, PORT))
            s1.send('App 1 Connected and sent payload'.encode())
            s1.close()


            db.mongoInstance("Test","Sent to app2")
            return True

        except Exception as e:

            db.mongoInstance("Test","Failed to send to app2")
            print(e)
            s1.connect((HOST, PORT))
            s1.send('App 1 Failed to create a connection'.encode())
            s1.close()

            return False
