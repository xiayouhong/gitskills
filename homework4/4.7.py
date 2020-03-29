# -*- encoding: utf-8 -*-
'''
@File : 4.7.py
@Time : 2020/03/29 09:19:07
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
# 使用python代码统计一个文件夹中所有文件的总大小
import os
x=input('输入文件夹路径：')
print(os.path.getsize(x),'KB')