# -*- encoding: utf-8 -*-
'''
@File : 1.3.py
@Time : 2020/03/04 15:57:55
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#定义2个列表，并初始化；  找出这2个列表中，相同的元素并输出；
list1=[2,'afa',8,'sgy','eye']
list2=[2,'st','eye']
for x in list1:
    if x in list2:
        print(x)