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

print "Content-type:text/html"
print
print "<html>"
print "<head>"
print "<meta charset=\"utf-8\">"
print "<title>菜鸟教程 CGI 测试实例</title>"
print "</head>"
print "<body>"
print "<h2> 选中的选项是：%s</h2>" % dropdown_value
print "</body>"
print "</html>"