# Project: Project Diamond App 2
# Purpose: Implement App 2 to receive secure payload using TLS
# Course: IST 411-001
# Author: Team 1, Teresa Barker and Asraa Alkurdi
# Date Developed: October 9, 2019
# Last Date Revised: October 13, 2019
# Rev: 2

import socket, datetime, ssl, logging
from pymongo import MongoClient
logger = logging.getLogger('app 5')

try:

    #part here as example
    HOST = 'localhost'
    PORT = 9999
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.send('App 2 Started'.encode())
    s.close()

    # Receive the secure payload using TLS
    print("App 2 connecting on port 8080 using SSL (TLS)")
    ssl_sock = ssl.wrap_socket(s, ca_certs="server.crt", cert_reqs=ssl.CERT_REQUIRED)
    ssl_sock.connect(('localhost', 8080))
    client = MongoClient('localhost', 27017)
    db = client.Team1
    collection = db.logs

    while True:
        print("Accept connections from outside")
        (clientSocket, address) = ssl_sock.accept()
        print(clientSocket.recv(1024))

    # Log pass/fail workflow actions into the MongoDB database with timestamp
        client = MongoClient('localhost', 27017)
        db = client.Team1
        collection = db.logs
        post_id = collection.insert_one({"Type": "Test","Time": datetime.datetime.utcnow(), "Action": "Connection Accepted"})
        s.connect(('localhost', 9999))
        s.send('App 2 accepted connection'.encode())
        s.close()


    # Unit tests for methods

except Exception as e:
    print(e)
    client = MongoClient('localhost', 27017)
    db = client.Team1
    collection = db.logs

    post_id = collection.insert_one({"Type": "Test","Time": datetime.datetime.utcnow(), "Action": "Error in Connecting"})
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 9999))
    s.send('App 2 failed to accept connection'.encode())
    s.close()

