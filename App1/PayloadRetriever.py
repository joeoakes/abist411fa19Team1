# Project: Project Diamond
# Purpose Details: Retrieve a JSON payload from the internet
# Course: IST 411
# Author: Team 1
# Date Developed: 10/9/2019
# Last Date Changed:
# Rev:


import sys, urllib.request, json, config


class PayloadRetriever:
    # Default constructor declaring URL and PARAM going to be used
    def __init__(self):
        self.url = config.URL
        self.param = config.PARAM

    # Gets JSON payload using URL and PARAM
    def readAndDecodeJSON(self):
        try:
            with urllib.request.urlopen(self.url + self.param) as payload:
                jsonPayload = payload.read().decode('utf-8')
                
                # Log to App5 Success

                return jsonPayload


        except Exception as e:
            print("error: %s" % e)

            # Log to App5 Failure
