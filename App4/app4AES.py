#Project: Project Diamond
#Purpose Details: Encrypt AES
#Course: IST 411
#Author: Team 1
#Date Developed: 11/29/2019
#Last Date Changed: 12/11/2019
#Rev: 0

import Pyro4, zlib, sys

class app4AES:
    def encryptAES(self, payload):
        try:
            pad = b' '
            obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')

            #plaintext = message.encode('utf-8')
            #print(plaintext)
            length = 16 - (len(payload)%16)
            #print(length)
            payload += length*pad

            ciphertext = obj.encrypt(payload)
            self.logger.addLog('Node4','Node4 encrypted with AES')
            return ciphertext
        except Exception as e:
            print(e)

