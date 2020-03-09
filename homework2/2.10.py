# -*- encoding: utf-8 -*-
'''
@File : 2.10.py
@Time : 2020/03/09 13:46:34
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#编写一个函数cacluate, 可以实现2个数的运算(加,减 乘,除)
def cacluate(x,y,z):
    if z=='+':
        return x+y
    elif z=='-':
        return x-y
    elif z=='*':
        return x*y
    elif z=='/':
        return x/y
    else:
        return -1
print(cacluate(1,4,'+'))