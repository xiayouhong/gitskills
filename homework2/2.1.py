# -*- encoding: utf-8 -*-
'''
@File : 2.1.py
@Time : 2020/03/09 09:08:51
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
# 写函数，判断用户传入的对象（字符串、列表、元组）长度,并返回给调用者。
def  length(x):
    return len(x)
list1=[1,3]
print(length(list1))
str='sgss'
print(length(str))
tuple1=(2,5)
print(length(tuple1))