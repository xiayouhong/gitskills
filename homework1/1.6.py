# -*- encoding: utf-8 -*-
'''
@File : 1.6.py
@Time : 2020/03/04 16:58:51
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
a=0
b=1
print(a,b)
while True:
    c=a+b
    if c<100:
         print(c)
         a=b
         b=c
    else:
        break