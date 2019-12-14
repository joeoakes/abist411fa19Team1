#Project: Project Diamond
#Purpose Details: Encrypt AES
#Course: IST 411
#Author: Team 1
#Date Developed: 11/29/2019
#Last Date Changed: 12/11/2019
#Rev: 0

import Pyro4, zlib, sys, socket, datetime

class app4AES:
    def encryptAES(self, payload):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            pad = b' '
            obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')

            length = 16 - (len(payload)%16)
            payload += length*pad

            ciphertext = obj.encrypt(payload)

            # Log success
            s.connect('localhost', 9999)
            s.send('App 4 encrypted with AES'.encode())
            s.close

            return ciphertext
        except Exception as e:
            # Log failure
            s.connect('localhost', 9999)
            s.send('App 4 failed to encrypt'.encode())
            s.close()

            print(e)

