# -*- encoding: utf-8 -*-
'''
@File : 1.4.py
@Time : 2020/03/04 16:01:13
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
# 判断用户输入的年份是否为闰年
m=int(input('输入要判断的年份:'))
if m%4==0 and m%100!=0:
    print('{}是闰年'.format(m))