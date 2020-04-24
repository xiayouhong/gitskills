# -*- encoding: utf-8 -*-
'''
@File : 7.1.py
@Time : 2020/04/19 13:29:41
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#  给定一个文件，请用正则表达式，逐行匹配提取其中的URL链接信息，并保存到另外一个文件中；
#    提示，文件有1000行，注意控制每次读取的行数；
import os
import re
with open (r'homework7\webspiderUrl.txt','r',encoding='utf-8') as f:
    lines=f.readlines()
with open (r'homework7\copy.txt','w',encoding='utf-8') as f:
    for line in lines:
        objs=re.search(r'http://www.[\w]*.(cn|com|net)',line)
        if objs:
            print(objs.group())
            f.write(objs.group())
            f.write('\n')
            