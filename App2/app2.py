# Project: Project Diamond App 2
# Purpose: Implement App 2 to receive secure payload using TLS
# Course: IST 411-001
# Author: Team 1, Teresa Barker and Asraa Alkurdi
# Date Developed: October 9, 2019
# Last Date Revised: October 16, 2019
# Rev: 4

import socket
import ssl
from mongo import MongoDB

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

    while True:
        print("Accept connections from outside")
        (clientSocket, address) = ssl_socket.accept()
        print(clientSocket.recv(1024))
<<<<<<< HEAD
        MongoDB.mongoInstance("Test", "Got Connection")
=======
        

>>>>>>> f19ffca418e9c9091489ddd434c1ddb9b12a67bf
    # Log pass/fail workflow actions into the MongoDB database with timestamp

    # Unit tests for methods

except Exception as e:
    print(e)
    MongoDB.mongoInstance("Test", "Failed to Get Connection")
