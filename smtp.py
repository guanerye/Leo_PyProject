#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'leo@shabi.com'
receivers = ['lisongnan7@hotmail.com']

charset = 'ISO-2022-JP'

message = MIMEText('Python test email contents','plain', charset)
message['From'] =Header("leo email",'utf-8')
message['To'] = Header("Hello",'utf-8')

subject = "Python email test"
message['Subject'] = Header(subject,'utf-8')

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender,receivers,message.as_string())
    print "email send succeed"
except smtplib.SMTPException:
    print "Error: can not send the email"
