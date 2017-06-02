#!/usr/bin/python
# -*- coding: UTF-8 -*-

import cgi, os
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

fileitem = form['filename']

if fileitem.filename:
    fn = os.path.basename(fileitem.filename)
    open('/tmp/' + fn, 'wb').write(fileitem.file.read())
    message = 'file "' + fn + '"is uploaded ok'
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

