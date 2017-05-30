#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Employee:
    empCount = 0

    def __init__(self,name,salary):
        self.sss = name
        self.eee = salary
        Employee.empCount += 1


    def displayCount(self):
        print self.empCount

    def displayEmployee(self):
        print self.sss, self.eee


em1 = Employee("leo",30)
em1.displayCount()
em2 = Employee("leo2",44)
em2.displayCount()
