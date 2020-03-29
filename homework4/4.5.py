# -*- encoding: utf-8 -*-
'''
@File : 4.5.py
@Time : 2020/03/28 18:39:26
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
# 通过Python来模拟实现一个txt文件的拷贝过程;
with open(r'homework4\homework4.txt','r',encoding='utf-8') as f:
    lines=f.readlines()
with open(r'homework4\ctrlv.txt','w',encoding='utf-8') as f:
    f.writelines(lines)