# -*- encoding: utf-8 -*-
'''
@File : 6.2.py
@Time : 2020/04/10 21:44:28
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
# 定义一个学生Student类。有下面的类属性：
# 1 姓名 name
# 2 年龄 age
# 3 成绩 score（语文，数学，英语) [每课成绩的类型为整数]
# 类方法：
# 1 获取学生的姓名：get_name() 返回类型:str
# 2 获取学生的年龄：get_age() 返回类型:int
# 3 返回3门科目中最高的分数。get_course() 返回类型:int
class student:
    name=''
    age=0
    score={'语文':0,'数学':0,'英语':0}

    def __init__(self,a,b,c):
        self.name=a
        self.age=b
        self.score=c
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_course(self):
        return max(self.score.values())
s1=student('a',1,{'语文':110,'数学':110,'英语':120})
print(s1.get_course())
s2=student('b',1,{'语文':120,'数学':120,'英语':130})
print(s2.get_name())
print(s2.get_course())
print(s1.get_age())