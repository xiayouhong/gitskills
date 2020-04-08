# -*- encoding: utf-8 -*-
'''
@File : 5.3.py
@Time : 2020/04/08 09:52:46
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
def  check(func):
    def inner():
        x=input('输入账号')
        y=input('输入密码')
        if x=='1' and y=='1':
            func()
        else:
            print('账号或密码错误')
    return inner
@check
def abc():
    print(1)
abc()