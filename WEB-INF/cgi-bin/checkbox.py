#!/usr/bin/python
# -*- coding: UTF-8 -*-

import cgi, cgitb

form = cgi.FieldStorage()

if form.getvalue('google'):
    google_flag = "YES"
else:
    google_flag = "NO"

if form.getvalue('leo'):
    leo_flag = "YES"
else:
    leo_flag = "NO"


print "Content-type:text/html"

print "<html>"
print "<head>"
print "    <meta charset=\"UTF-8\">"
print "    <title>leo Project</title>"
print "</head>"
print "<body>"
print "<h2>if check the leo : %s</h2>" % leo_flag
print "<h2>if check the Google : %s</h2>" % google_flag
print "</body>"
print "</html>"
