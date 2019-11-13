# Project: Project Diamond
# Purpose Details: Compress the payload for app3 Team1
# Course: IST 411 Fall 2019
# Author: Erik Ellis
# Date Developed: 11/10/19
# Last Date Changed:
# Rev:

import zlib, json, sys
#from mongo import MongoDB

class CompressPayload:

    def compress(payload):
        try:
            data = payload.read()
            payload.close()

            print("Compressing Payload")
            # Compress the byte array file contents and create checksum
            payloadComp = zlib.compress(data)
            chcecksum = zlib.crc32(data)
            return payloadComp
        except Exception as e:
            print(e)
