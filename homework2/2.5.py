# -*- encoding: utf-8 -*-
'''
@File : 2.5.py
@Time : 2020/03/09 09:55:59
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#写函数，检查传入字典的每一个value长度，
# 如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者;
def check(mydict):
    for k,v in mydict.items():
       if len(v)>2:
           mydict[k]=v[0:2] 
    return mydict
dict1={2:'3','sg':'afaf'}
print('原字典：')
print(dict1)
print('传入函数后：')
print(check(dict1))