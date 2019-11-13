# Project: Project Diamond App3
# Purpose Details: Secure file transfer with SFTP
# Course: IST 411 Fall 2019
# Author: Erik Ellis
# Date Developed: 11/04/19
# Last Date Changed:
# Rev: 0

import sys, datetime
from app3Compress import CompressPayload
from app3SFTP import SFTPReceive

"""Run all of the other files and create timestamps"""
def main():
    try:
       timestamp = 1545730073
       startDtObject = datetime.fromtimestamp(timestamp)

       SFTPReceive().connectSFTP()
       # Payload is read from SFTP
       payload = open('payloadReceiveTeam1.py', 'rb')
       payload.close()
       print("Compressing payload")
       payloadComp = CompressPayload.compress(payload)

       endDtObject = datetime.fromtimestamp(timestamp)
   except Exception as e:
      print(e) 
