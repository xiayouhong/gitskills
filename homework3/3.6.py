# -*- encoding: utf-8 -*-
'''
@File : 3.6.py
@Time : 2020/03/22 10:19:35
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#在2个文件中存放了英文计算机技术文章(可以选择2篇关于Python技术文件操
# 作处理技巧的2篇英文技术文章),
#  请读取文章内容,进行词频的统计;并分别输出统计结果到另外的文件存放;
# 比较这2篇文章的相似度(如果词频最高的前10个词,重复了5个,相似度就是50%;
## 重复了6个,相似度就是60% ,......);
import os
try:
    with open(r'homework3\article1.txt','r',encoding='utf-8') as f:
        list1=f.readlines()
    dict1={}
    for i in list1:
        list2=i.split()
        for j in list2:
            if j=='?' or j=='.' or j==',' or j=='!':
                continue
            elif  j in dict1.keys():
                dict1[j]+=1
            else:
                dict1[j]=1
    list3=sorted(dict1.items(),key=lambda x:x[1],reverse=True)

    with open(r'homework3\article2.txt','r',encoding='utf-8') as f:
        list1=f.readlines()
    dict2={}
    for i in list1:
        list2=i.split()
        for j in list2:
            if j=='?' or j=='.' or j==',' or j=='!':
                    continue
            elif  j in dict2.keys():
                dict2[j]+=1
            else:
                dict2[j]=1
    list4=sorted(dict2.items(),key=lambda x:x[1],reverse=True)
    n=0 
    for i in range(10):
        for j in range(10):
            if list3[i][0]==list4[j][0]:
                n+=1
                # print('C重复的单词及词频：',list3[i])
    if n!=0:
        print('重复率为{}0% '.format(n))      
    else:
        print('重复率为0')
except IOError:
    print('cannot open')
except Exception as ex:
  print('表达式为空')
finally:
    print('end')