#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 引入 CGI 处理模块
import cgi, cgitb

form = cgi.FieldStorage()

if form.getvalue('dropdown'):
    if form.getvalue('dropdown')=="leo":
        dropdown_value = 'leo1111'
    else:
        dropdown_value = 'Google111'

else:
    dropdown_value = 'nothing'

print """
Content-type:text/html"

<html>
<head>
<meta charset=\"utf-8\">
<title>菜鸟教程 CGI 测试实例</title>
</head>
<body>
<h2> 选中的选项是：%s</h2>""" % dropdown_value
"""
</body>
</html>
"""