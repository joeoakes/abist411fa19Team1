# Project: Project Diamond
# Purpose Details: Reciever Rabbit from App4
# Course: IST 411 Section 001
# Author: Team 1
# Date Developed: 12/13/2019
# Last Date Changed:
# Rev:

import pika, time 
from datetime import date
class RabbitReciever:
    def getMessage(startTime):
        try:
            print("Connecting to localhost")
            connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
            channel = connection.channel()
            channel.queue_declare(queue='app4Message')
            #callback function that will receive the message
            def callback(ch,method,properties,body):
                print(" [x] Received %r" % body)
                print(str(time.time() - startTime) + " seconds")
            channel.basic_consume('app4Message',callback,auto_ack=True)
            print(' [*] Waiting for messages. To exit press CTRL+C')
            channel.start_consuming()

        except Exception as e:
            print(e)
