# -*- encoding: utf-8 -*-
'''
@File : 4.1.py
@Time : 2020/03/26 12:46:08
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
# 1 定义一个10个元素的列表，通过列表自带的函数，实现元素在尾部插入和头部插入并记录程序
# 运行的时间；用deque来实现，同样记录程序所耗费的时间；输出这2个时间的差值；
#  提示：列表原生的函数实现头部插入数据：list.insert(0, v)；list.append（2）)
from collections import deque
import datetime
list1=[]
a=datetime.datetime.now()
for i in range(5):
    list1.insert(0,i)
    list1.append(i)
b=datetime.datetime.now()
print(a,b)
print((b-a).seconds)
t1=(b-a).seconds
q=deque([])
c=datetime.datetime.now()
for i in range(5):
    q.append(i)
    q.appendleft(i)
d=datetime.datetime.now()
print(c,d)
print((d-c).seconds)
t2=(d-c).seconds
print(t2-t1)