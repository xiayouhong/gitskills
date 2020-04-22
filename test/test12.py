# -*- encoding: utf-8 -*-
'''
@File : test12.py
@Time : 2020/04/15 09:07:01
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
# 题目1：匹配出163的邮箱地址，且@符号之前有4到20位，例如hello@163.com
import re
x=input('输入邮箱：')
ret=re.match(r'^[\w]{4,20}@163.com$',x)
if ret:
    print('邮箱为：%s 正确' % x)
else:
    print('邮箱为：%s 错误' % x)