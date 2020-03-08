# -*- encoding: utf-8 -*-
'''
@File : 1.py
@Time : 2020/03/04 15:26:15
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
# 元素输出和查找：  请输出0-50之间的奇数，偶数，质数；能同时被2和3整除的数；
for n in range(1,50):
    if n%2!=0:
        print('奇数{}'.format(n))
    if n%2==0:
        print('偶数{}'.format(n))
    for m in range(2,n):
        if(n%m==0):
            break
    else:
        print('质数{}'.format(n))
    if n%2==0 and n%3==0:
        print('能被2，3整除{}'.format(n))
