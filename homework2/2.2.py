# -*- encoding: utf-8 -*-
'''
@File : 2.2.py
@Time : 2020/03/09 09:33:59
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#编写一个函数,接收n个数字，求这些参数数字的和;
def sum(*arg):
    s=0
    for i in arg:
        s+=i
    print('和为:',s)
sum(1,3,4)
        