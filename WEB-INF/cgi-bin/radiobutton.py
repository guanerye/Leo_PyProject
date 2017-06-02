#!/usr/bin/python
# -*- coding: UTF-8 -*-

import cgi, cgitb

form = cgi.FieldStorage()

if form.getvalue('site'):
    site = form.getvalue('site')
else:
    site = "It's empty!!"

print "Content-type:text/html"
print
print "<html>"
print "<head>"
print "<meta charset=\"utf-8\>"
print "<title>Leo Project CGI TEST</title>"
print "</head>"
print "<body>"
print "<h2>selected is : %s</h2>" %site
print "</body>"
print "</html>"