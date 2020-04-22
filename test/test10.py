# -*- encoding: utf-8 -*-
'''
@File : test10.py
@Time : 2020/04/08 09:10:51
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
class dog:
    count=0
    name=''
    color=''
    def __init__(self,a,b):
        self.name=a
        self.color=b
        dog.count+=1
    def printf(self):
        print(self.name,self.color)
    @staticmethod
    def counter():
        return dog.count
a=dog('a','yellow')
print(a.printf())
print(dog.count)