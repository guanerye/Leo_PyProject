#!/usr/bin/python
# -*- coding: UTF-8 -*-

print "Content-Disposition: attachment; filename=\"foo2.txt\""
print

fo = open("/usr/local/apache-tomcat8/webapps/Leo_PyProject/WEB-INF/cgi-bin/foo2.txt","rb")

str = fo.read()
print str

fo.close()
