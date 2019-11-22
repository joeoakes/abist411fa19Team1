# Project: Project Diamond App 2
# Purpose: Implement App 2 to receive secure payload using TLS
# Course: IST 411-001
# Author: Team 1, Teresa Barker and Asraa Alkurdi
# Date Developed: October 9, 2019
# Last Date Revised: November 13, 2019
# Rev: 9

import hmac, socket, ssl, pysftp, hashlib, sys
from mongo import MongoDB
from app2 import App2

def main():
    try:
        App2().tls_connection()
        App2().hash_payload_hmac()
        App2().send_payload_sftp()
    except Exception as e:
        print(e)


if __name__=='__main__':
    main()
