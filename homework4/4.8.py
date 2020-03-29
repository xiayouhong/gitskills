# -*- encoding: utf-8 -*-
'''
@File : 4.8.py
@Time : 2020/03/29 09:26:50
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
# 1） 生成一个大文件ip.txt,要求1200行，每行随机为172.25.254.1---172.25.254.254之间的ip地址;
# 2） 读取ip.txt文件统计这个文件中ip出现频率排前10的ip
import os
import random
ip = ['172.25.254.' + str(i) for i in range(1,255)]
with open(r'homework4\ip.txt','w') as f:
    for i in range(1200):
        # f.write('172.25.254.'+str(random.randint(1,254))+'\n')
        f.write(''.join(random.sample(ip,1))+ '\n')
dict1={}
with open (r'ip.txt','r') as f:
    lines=f.readlines()
for line in lines:
    line=line.strip()
    if line in dict1.keys():
        dict1[line]+=1
    else:
        dict1[line]=1
list1=sorted(dict1.items(),key=lambda x: x[1],reverse=True)[:10]
print('出现频率前10')
print('{:16} {:10}'.format('ip','出现次数'))
for i in list1:
    print('{:16} {:10}'.format(i[0],i[1]))

  