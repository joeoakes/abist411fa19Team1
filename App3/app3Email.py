# Project: Project Diamond
# Purpose Details: To email team members the payload received from app2
# Course: IST 411
# Author: Team 1
# Date Developed: 11/10/2019
# Last Date Changed:
# Rev:

''' Import smtplib for the actual sending function '''
import smtplib

''' Import the email modules we'll need '''
from email.mime.text import MIMEText

''' Email payloads to specified email addresses '''
class EmailPayload:
    ''' Setup the email components Subject, From, To '''
    def __init__(self, payload):
        self.fromAddress = 'dkc5318@psu.edu'
        self.toAddresses = []
        self.subject = 'app3 Received Payload'
        self.msg = MIMEText(repr(payload))

    ''' Setup email header '''
    def emailHeader(self):
        try:
            self.msg['Subject'] = self.subject
            self.msg['From'] = self.fromAddress
            self.msg['To'] = ', '.join(self.toAddresses)

        except Exception as e:
            print("Error %s" % e.args[0])

            # Log statement here

    ''' Add emails to list for delivery '''
    def deliveryEmails(self):
        try:
            self.toAddresses.append('dkc5318@psu.edu')
            self.toAddresses.append('eae5206@psu.edu')
            self.toAddresses.append('akl5294@psu.edu')
            self.toAddresses.append('axa70@psu.edu')
            self.toAddresses.append('yxd75@psu.edu')
            self.toAddresses.append('tlb5767@psu.edu')

            # Log statement here

        except Exception as e:
            print("Error %s" % e.args[0])

            # Log statement here


    ''' Send the message via the SMTP server '''
    def sendEmail(self):
        try:
            s = smtplib.SMTP_SSL('authsmtp.psu.edu', 465)
            self.deliveryEmails()
            self.emailHeader()
            #for email in self.toAddresses:
            s.sendmail(self.fromAddress, self.toAddresses, self.msg.as_string())

                # Log statement here

            return True
        except Exception as e:
            print("Error %s" % e.args[0])

            # Log statement here

            return False
        finally:
            s.quit()

