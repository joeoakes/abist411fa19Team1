#Project: Project Diamond
#Purpose Details: Send with RabbitMQ
#Course: IST 411
#Author: Team 1
#Date Developed: 11/29/2019
#Last Date Changed: 12/11/2019
#Rev: 0

import pika, Pyro4, zlib, sys, datetime, socket
from Crypto.Cipher import AES
from app4AES import app4AES

class SendPayload:
    def sendPayload(self, payload):
         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         try:
             connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
             channel = connection.channel()
             channel.queue_declare(queue='app4Message')
             channel.basic_publish(exchange="", routing_key='app4Message', body=payload[0].encode('utf-8'))
             print("Message Sent")
             connection.close()

             #Logging success
             s.connect('localhost', 9999)
             s.send('App 4 successfully sent with Rabbit'.encode())
             s.close()
         except Exceptions as e:
             print(e)

             #Logging
             s.connect('localhost', 9999)
             s.send('App 4 failed to send with Rabbit'.encode())
