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
# 给定一段英文文本，统计每个单词出现的次数；打印输出，按照词频从高到低输出：
#    提示：可以用字典来统计：key 是单词，value 是单词出现次数；
#     先创建一个字典，然后遍历刚刚取出的单词列表，接着做一个判断： 
#     如果字典中 key 已经出现了这个单词，那么它对应的 value ，
#     也就是出现次数就 +1；
#      如果这个单词没出现过，就直接 插入这个单词及 value 为 1 到 字典中；


# s='what is your name?my name is ok.hello,hi,nice to meet you.'
# s=s.replace('?',' ')
# s=s.replace('.',' ')
# s=s.replace(',',' ')
# s=s.replace('!',' ')
# list1=s.split()
# dict1={}
# print(s)
# for x in list1:
#     if x in dict1.keys():
#         dict1[x]+=1
#     else:
#         dict1[x]=1
# print(dict1)
# for k,v in dict1.items():
#     print('{} 出现次数: {}'.format(k,v))

s='what is your name?my name is ok.hello,hi,nice to meet you.'
s=s.replace('?',' ')
s=s.replace('.',' ')
s=s.replace(',',' ')
s=s.replace('!',' ')
#方法1：
# result={word:s.split().count(word) for word in set(s.split())}
# for k,v in result.items():
#     print('{:10} 出现次数: {:10}'.format(k,v))

#方法3：
from collections import Counter
counts=Counter(s.split())
for k,v in counts.items():
    print('{:10} 出现次数: {:10}'.format(k,v))