# Project: Project Diamond
# Purpose Details: Send Payload using TLS
# Course: IST 411
# Author: Team 1
# Date Developed: 10/11/19
# Last Date Changed:
# Rev:
import socket, ssl, json, datetime
from pymongo inport MongoClient

# To send payload
class SendPayload:

   # Connect to server and send payload
   def sendPayload(self, payload):
      try:
         print("App 1 connecting on port 443 using TLS")
         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         ssl_sock = ssl.wrap_socket(s,
            ca_certs="team1Server.crt",
            cert_reqs=ssl.CERT_REQUIRED)
         ssl_sock.connect(('localhost',443))
         ssl_sock.sendall(payload)
         print("JSON payload sent to _______ using TLS")
         ssl_sock.close()
         print(ssl_sock.cipher())

         client = MongoClient('localhost', 27017)
         db = client.Team1
         collection = db.logs

         # Logging
         post_id = collection.insert_one({"Type": "Test","Time": datetime.datetime.utcnow(), "Action": "Sent Payload"})
         return True

      except Exception as e:
         print(e)

         #Logging
         post_id = collection.insert_one({"Type": "Test","Time": datetime.datetime.utcnow(), "Action": "Failed to Send Payload"})
         return False
