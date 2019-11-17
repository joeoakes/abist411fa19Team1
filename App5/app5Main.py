#Project: Project Diamond
#Purpose Details: Gets logs from other Apps
#Course: IST 411
#Author: Team 1, Andy Liu
#Date Developed: 11/14/2019
#Last Date Changed:11/16/2019
#Rev: 0


import logging
import logging.config
import time
import socket
import requests

#creates a listener on port 9999
#t = logging.config.listen(9999)
#t.start()
logInfo = ''

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 9999))
serversocket.listen(5)

#creates new logger
logger = logging.getLogger('app 5')

#created handler to get logs
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
logger.addHandler(stream_handler)

#sets logging level and format of what is passed in like time and name of where its from
logging.basicConfig(level = logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

try:

    logging.info('Test')
    while True:
        (clientsocket, address) = serversocket.accept()
        logInfo = clientsocket.recv(1024).decode()
        if logInfo != '':
            logging.info(logInfo)
            logInfo = ''


except Exception as e:
    print(e)
    logging.config.stopListening()
#    t.join()
