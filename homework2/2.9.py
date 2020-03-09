# -*- encoding: utf-8 -*-
'''
@File : 2.9.py
@Time : 2020/03/09 13:46:06
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#定义一个函数，函数接收一个数组，
# 并把数组里面的数据从小到大排序(冒泡排序,  也可以直接使用相关的函数);
def sort(a):
    n=len(a)
    for x in range(n-1):
        for y in range(n-1-x):
            if a[y]>a[y+1]:
                 a[y],a[y+1]=a[y+1],a[y]
    print(a)
    return a
a=[3,1,4,6,9,8]
sort(a)