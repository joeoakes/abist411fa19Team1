#Project: Project Diamond
#Purpose Details: Run app 4
#Course: IST 411
#Author: Team 1
#Date Developed: 11/29/2019
#Last Date Changed: 12/11/2019
#Rev: 0

from app4AES import app4AES
from app4Pyro import app4Pyro
from app4Rabbit import SendPayload

def main():
    app4Pyro.getURI()
    SendPayload.sendPayload()

if __name__ == '__main__':
    main()
