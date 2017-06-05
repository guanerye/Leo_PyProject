#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

db = MySQLdb.connect("172.30.140.15","root","leo1234","test")

cursor = db.cursor()

sql_sex = 'MAC'
sql = "DELETE FROM EMPLOYEE  WHERE FIRST_NAME = '%s'" % (sql_sex)

try:
    cursor.execute(sql)
    db.commit()

except:
    db.rollback()



db.close()



