# -*- encoding: utf-8 -*-
'''
@File : 1.2.py
@Time : 2020/03/04 15:50:14
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#一个字典中，存放了10个学生的学号（key）和分数（value）；
# 请筛选输出，大于80分的同学（按照格式：学号：分数）；
dict={
    1:88,
    2:84,
    3:90,
    4:60,
    5:76,
    6:68,
    7:96,
    8:98,
    9:58,
    10:76
    }
print('分数大于80的同学如下：')
for k,v in dict.items():
    if v>80 :
        print('学号为:{:6} 分数为:{:6}'.format(k,v))