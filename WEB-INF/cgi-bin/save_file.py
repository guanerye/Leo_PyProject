#!/usr/bin/python
# -*- coding: UTF-8 -*-

import cgi, os
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

filename = form['filename']

if filename.filename:
    fn = os.path.basename(filename.filename)
    open('/tmp/' + fn, 'wb').write(filename.filename)
    message = 'file "' + fn + '"upload OK'
else:
    message = 'file upload failed'

print """
Content-Type: text/html\n
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
   <p>%s</p>
</body>
</html>
""" %(message,)

