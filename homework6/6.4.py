# -*- encoding: utf-8 -*-
'''
@File : 6.4.py
@Time : 2020/04/12 09:17:50
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
# 封装一个学生类，有姓名，有年龄，有性别，有英语成绩，数学成绩，语文成绩，
#       封装方法，求单个学生的总分，平均分，以及打印学生的信息。
class student:
    name=''
    age=0
    sex=''
    egrade=mgraade=cgrade=0
    def __init__(self,name,age,sex,egrade,mgraade,cgrade):
        self.name=name
        self.age=age
        self.sex=sex
        self.egrade=egrade
        self.mgraade=mgraade
        self.cgrade=cgrade
    def allgrade(self):
        return self.egrade+self.mgraade+self.cgrade
    def average(self):
        return self.allgrade()/3
    def printf(self):
        print(' {} {} {} 英语：{}数学：{}语文：{}'.format(self.name,self.age,self.sex,self.egrade,
        self.mgraade,self.cgrade))
s=student('mike',20,'boy',100,100,100)
print(s.allgrade())
print(s.average())
s.printf()
