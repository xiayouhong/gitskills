# -*- encoding: utf-8 -*-
'''
@File : 5.1.py
@Time : 2020/04/07 23:07:50
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import time
def times(func):
    def inner():
        time1=time.time()
        func()
        time2=time.time()
        print(time2-time1)
    return inner
@times
def func():
    j=0
    for i in range(10):
        j+=i
        time.sleep(1)
    print(j)
func()