# -*- encoding: utf-8 -*-
'''
@File : test2.py
@Time : 2020/02/24 10:04:57
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#元组
tuple1=(97,80,66,78,88)
tuple2=('a','b','sfa',25,78)
print(max(tuple1))
print(min(tuple1))
print(len(tuple2))
print(tuple1+tuple2)
list=['sgs',3,75,'sgsgr']
tuple3=tuple(list)
print(tuple3)

#字典
dict1={'学号':1,'姓名':'无名氏','班级':'幼儿园大班','年龄':6}
dict2={'john':'class1','amy':'class1','bob':'class2','mike':'class3','linda':'class3'}
print(dict2['john'])
print(dict1)
print(dict2['bob'])

dict2['lucy']='class4'
dict2['bob']='class4'
del dict2['amy']
print(dict2)
dict1.clear()
print(dict1)

#集合
a=set (('faf',2,'sefs'))
b={1,3,'tfs',2}
print(a-b)
print(a|b)
a.add('hello')
a.update(('2',5,6))
a.remove(2)
print(a)
print(a.union(b))
a.pop()
b.pop()
print(a)
print(b)
