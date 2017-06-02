#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 引入 CGI 处理模块
import cgi, cgitb

form = cgi.FieldStorage()

if form.getvalue('textcontent'):
    text_content = form.getvalue('textcontent')
else:
    text_content = 'there is no contents'

print "Content-type:text/html"
print
print "<html>"
print "<head>"
print "<meta charset=\"utf-8\">"
print "<title>菜鸟教程 CGI 测试实例</title>"
print "</head>"
print "<body>"
print "<h2> 输入的内容是：%s</h2>" % text_content
print "</body>"
print "</html>"