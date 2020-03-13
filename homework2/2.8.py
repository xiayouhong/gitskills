# -*- encoding: utf-8 -*-
'''
@File : 2.8.py
@Time : 2020/03/09 13:24:36
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#请用Python定义一个函数，给定一个字符串，找出该字符串
# 中出现次数最多的那个字符，并打印出该字符及其出现的次数。
#例如，输入 aaaabbc，输出：a:4
def most(str):
    dict1={}
    for i in str:
        if i in dict1.keys():
            dict1[i]+=1
        else:
            dict1[i]=1
    a=max(dict1,key=dict1.get)
    print('输出：',a,dict1[a])
str='afaahgjyrhth'
print('输入：',str)
most(str)