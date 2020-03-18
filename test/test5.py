# -*- encoding: utf-8 -*-
'''
@File : test5.py
@Time : 2020/03/11 07:55:43
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#10个同学的成绩排序存放，每个学生一个元组
list1=[('a',2),('b',6),('c',8),('d',9),('e',4),
('f',12),('g',16),('h',18),('i',20),('j',11)]
list1.sort(key=lambda k: k[1])
for i in list1:
    print('name:{} score:{}'.format(i[0],i[1]))