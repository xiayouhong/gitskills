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
import random
x=int(input('输入你想创建的列表元素个数:'))
list1=[random.randint(1,99) for i in range(x)]
tuple1=tuple(random.randint(1,99) for i in range(x))
print(tuple1)
print(list1)
 
 
