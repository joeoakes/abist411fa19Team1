#Project: Project Diamond
#Purpose Details: Gets logs from other Apps
#Course: IST 411
#Author: Team 1
#Date Developed: 11/14/2019
#Last Date Changed:11/16/2019
#Rev: 0


import logging

#creates new logger
logger = logging.getLogger(__name__)

#sets logging level and format of what is passed in like time and name of where its from
logging.basicConfig(level = logging.INFO, format='%(asctime)s:%(filename)s:%(levelname)s:%(message)s')

try:


except Exception as e:
    print(e)
