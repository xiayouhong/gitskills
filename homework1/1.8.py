# -*- encoding: utf-8 -*-
'''
@File : 1.8.py
@Time : 2020/03/04 17:11:30
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
dict1={'工号':1,'姓名':'A','年龄':30,'工资':1}
dict2={'工号':2,'姓名':'B','年龄':30,'工资':2}
dict3={'工号':3,'姓名':'C','年龄':30,'工资':3}
dict4={'工号':4,'姓名':'D','年龄':30,'工资':6}
dict5={'工号':5,'姓名':'E','年龄':30,'工资':5}
dict6={'工号':6,'姓名':'F','年龄':30,'工资':4}
dict7={'工号':7,'姓名':'G','年龄':30,'工资':7}
dict8={'工号':8,'姓名':'H','年龄':30,'工资':8}
dict9={'工号':9,'姓名':'I','年龄':30,'工资':9}
dict10={'工号':10,'姓名':'J','年龄':30,'工资':10}
list1=[dict1,dict2,dict3,dict4,dict5,dict6,dict7,dict8,dict9,dict10]
list2=sorted(list1,key=lambda k:k['工资'],reverse=True)
print(list1)
print(list2)