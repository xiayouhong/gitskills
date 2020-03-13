# -*- encoding: utf-8 -*-
'''
@File : 2.3.py
@Time : 2020/03/09 09:38:28
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import random
#编写一个函数, 传入一个数字列表, 输出列表中的奇数;
#  数字列表请用随机数函数生成;
def ji(mylist):
    print('输出奇数：')
    for i in mylist:
         if i%2!=0:
             print(i)
list1=[random.randint(1,99) for i in range(10)]
ji(list1)