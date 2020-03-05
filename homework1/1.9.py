# -*- encoding: utf-8 -*-
'''
@File : 1.9.py
@Time : 2020/03/04 19:02:44
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import random
x=2
n=int(input('输入最多猜的次数:'))
y=int(input('输入你猜的数字1-98:'))
i=0
while x!=y:
    if y>x:
        print('比y小')
    else:
        print('比y大')
    i+=1
    if n>i:
        y=int(input('输入你猜的数字1-98:'))
    else:
        print('失败')
        break
else:
    print('猜对了！是{}'.format(y))      
