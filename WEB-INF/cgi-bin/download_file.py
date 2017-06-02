#!/usr/bin/python
# -*- coding: UTF-8 -*-

print "Content-Disposition: attachment; filename=\"foo.txt\""
print

fo = open("foo.txt","rb")

str = fo.read()
print str

fo.close()
