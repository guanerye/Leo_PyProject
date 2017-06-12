#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'leo@shabi.com'
receivers = ['lisongnan7@hotmail.com']

charset = 'UTF-8'

message = MIMEText('Python test email contents','plain', charset)
message['From'] =Header("leo email",charset)
message['To'] = Header("Hello",charset)

subject = "Python email test"
message['Subject'] = Header(subject,charset)

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender,receivers,message.as_string())
    print "email send succeed"
except smtplib.SMTPException:
    print "Error: can not send the email"
