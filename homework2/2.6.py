# -*- encoding: utf-8 -*-
'''
@File : 2.6.py
@Time : 2020/03/09 12:44:05
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#定义一个函数, 打印输出n以内的斐波那契数列;
def printf(n):
    print('输出%d以内的斐波那契数列：'%n)
    a=0
    b=1
    print(a,b)
    c=a+b
    while c<=n:
        print(c)
        a=b
        b=c
        c=a+b
printf(20)