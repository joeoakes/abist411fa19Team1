#Project: Project Diamond
#Purpose Details: Send with RabbitMQ
#Course: IST 411
#Author: Team 1
#Date Developed: 11/29/2019
#Last Date Changed: 12/11/2019
#Rev: 0

import pika, Pyro4, zlib, sys
from Crypto.Cipher import AES
from app4AES import app4AES

class SendPayload:
    def sendPayload(self, payload):
         connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
         channel = connection.channel()
         channel.queue_declare(queue='app4Message')
         #payload = self.encryptAES(payload)
         channel.basic_publish(exchange="", routing_key='app4Message', body=payload[0].encode('utf-8'))
         print("Message Sent")
         connection.close()
