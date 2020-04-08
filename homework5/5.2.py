# -*- encoding: utf-8 -*-
'''
@File : 5.2.py
@Time : 2020/04/07 23:26:58
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import datetime,os
def record(func):
    def inner():
        t=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(func,t)
        func()
        try:
            with open(r'homework5\record.txt','w',encoding='utf-8') as f:
                s='{}{} \n'.format(func,t)
                f.write(s)
        except IOError:
            print('error')
    return inner

@record
def a():
    j=0
    for i in range(10):
        j+=i
    print('try one',j)
a()


