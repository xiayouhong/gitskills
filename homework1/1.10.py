# -*- encoding: utf-8 -*-
'''
@File : 1.10.py
@Time : 2020/03/04 19:28:17
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
s='what is your name?my name is ok.hello,hi,nice to meet you.'
s=s.replace('?',' ')
s=s.replace('.',' ')
s=s.replace(',',' ')
s=s.replace('!',' ')
list1=s.split()
dict1={}
print(s)
for x in list1:
    if x in dict1.keys():
        dict1[x]+=1
    else:
        dict1[x]=1
print(dict1)
for k,v in dict1.items():
    print('{} 出现次数: {}'.format(k,v))