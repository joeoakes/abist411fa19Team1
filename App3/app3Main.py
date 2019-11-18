# Project: Project Diamond App3
# Purpose Details: Secure file transfer with SFTP
# Course: IST 411 Fall 2019
# Author: Team 1, Erik Ellis, David Chen
# Date Developed: 11/04/19
# Last Date Changed: 11/15/19
# Rev: 0

import sys
from datetime import date
from app3Compress import CompressPayload
from app3SFTP import SFTPReceive
from app3Email import EmailPayload
from app3Pyro import App3Pyro

"""Run all of the other files and create timestamps"""
def main():
    try:
        timestamp = 1545730073
        startDtObject = date.fromtimestamp(timestamp)

        SFTPReceive().connectSFTP()
        # Payload is read from SFTP
        payload = open('payloadReceiveTeam1.py', 'rb')
        payload.close()

        print("Sending payload through email")
        email = EmailPayload(payload)
        email.sendEmail()

        print("Create and sending pyro object with payload")
        App3Pyro.pyroPayload(payload)

        print("Compressing payload")
        payloadComp = CompressPayload.compress(payload)

        endDtObject = datetime.fromtimestamp(timestamp)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
