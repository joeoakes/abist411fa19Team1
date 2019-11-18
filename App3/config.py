# Project: Project Diamond
# Purpose Details: Secure File Transfer
# Course: IST 411 Fall 2019
# Author: Team 1
# Date Developed: 11/04/19
# Last Date Changed: 11/14/19
# Rev:

"""Configuration for SFTP client"""
import pysftp, sys
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
cinfo = {'cnopts': cnopts, 'host': 'oz-ist-linux-oakes', 'username': 'ftpuser', 'password': 'test1234', 'port': 100}

