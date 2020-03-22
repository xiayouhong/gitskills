# -*- encoding: utf-8 -*-
'''
@File : 3.2.py
@Time : 2020/03/22 09:50:20
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
# 写一个程序，从input.txt中读取之前输入的数据，存入列表中，再加上行号打印显示；格式如下
#第一行： xxxx
#第二行： xxxx
try:
    with open(r'homework3\input.txt','r',encoding='utf-8') as f:
        i=1
        for line in f.readlines():
            print('第{}行: {}'.format(i,line))
            i+=1
except IOError:
    print('cannot open ')
finally:
    print('end')