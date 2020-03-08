# -*- encoding: utf-8 -*-
'''
@File : 1.5.py
@Time : 2020/03/04 16:08:06
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
# 使用random模块，生成随机数，来初始化一个列表，元组；
#    使用了 random 模块的 randint() 函数来生成随机数，查询一下相关函数的用法；
import random
x=int(input('输入你想创建的列表元素个数:'))
list1=[random.randint(1,99) for i in range(x)]
tuple1=tuple(random.randint(1,99) for i in range(x))
print(tuple1)
print(list1)