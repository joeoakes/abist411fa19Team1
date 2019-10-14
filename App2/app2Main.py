# Project: Project Diamond App 2
# Purpose: Implement App 2 to receive secure payload using TLS
# Course: IST 411-001
# Author: Team 1, Teresa Barker and Asraa Alkurdi
# Date Developed: October 9, 2019
# Last Date Revised: October 13, 2019
# Rev: 2

import socket
import ssl

try:
    # Receive the secure payload using TLS
    print("App 2 connecting on port 8080 using SSL (TLS)")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssl_sock = ssl.wrap_socket(s, ca_certs="server.crt", cert_reqs=ssl.CERT_REQUIRED)
    ssl_sock.connect(('localhost', 8080))

    while True:
        print("Accept connections from outside")
        (clientSocket, address) = ssl_sock.accept()
        print(clientSocket.recv(1024))

    # Log pass/fail workflow actions into the MongoDB database with timestamp

    # Unit tests for methods

except Exception as e:
    print(e)
