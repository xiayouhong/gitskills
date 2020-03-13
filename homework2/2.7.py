# -*- encoding: utf-8 -*-
'''
@File : 2.7.py
@Time : 2020/03/09 13:18:38
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
# 随机生成20个学生的成绩; 判断这20个学生成绩的等级; 用函数来实现;  
    # A---成绩>=90;  
    # B-->成绩在 [80,90)
    # C-->成绩在 [70,80)
    # D-->成绩<70
import random
def grade(x):
    if x>=90:
        return 'A'
    elif x<90 and x>=80:
        return 'B'
    elif x<80 and x>=70:
        return 'C'
    else:
        return 'D'
list1=[random.randint(0,101) for i in range(20)]
for i in list1:
    print('成绩为{:6} 等级为{:>6}'.format(i,grade(i)))