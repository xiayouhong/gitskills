# -*- encoding: utf-8 -*-
'''
@File : 3.3.py
@Time : 2020/03/22 09:58:27
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#编写一个程序，读取文件中保存的10个
# 学生成绩名单信息(学号,姓名, Python课程分数); 然后按照分数从高到低进行排序输出
try:
    with open(r'homework3\grade.txt','r',encoding='utf-8') as f:
        list1=[]
        for i in f.readlines():
            list2=i.strip().split()
            list1.append(list2)
    list1.sort(key=lambda x:(int)(x[2]),reverse=True)
    for i in list1:
        print(i)
except IOError:
    print('cannot open')
except IndexError:
    print('list index out of range')
