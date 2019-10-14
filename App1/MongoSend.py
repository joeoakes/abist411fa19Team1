#Project: Project Diamond
#Purpose Details: Retrieve a JSON payload from the internet and send it to App2 using TLS. It will also retrieve an encrypted payload from App4 and save the JSON payload to a text file.
#Course: IST 411
#Author: Team 1
#Date Developed: 10/13/2019
#Last Date Changed:10/13/2019
#Rev: 0

#this class contains a method to send a set of text to a database

import sys, config


class MongoSend:

	def __init__(self):
		self.date = ""
	        self.text = ""

	# method to send to database
	def dbSend(date, text):
        	client = MongoClient('localhost', 27017)
        	db = client.Team1
        	collection = db.logs
        	post_id = collection.insert_one({"Date": date, "Action": text})
        	print(text)

