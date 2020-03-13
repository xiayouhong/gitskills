# -*- encoding: utf-8 -*-
'''
@File : 2.4.py
@Time : 2020/03/09 09:45:03
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#写函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果;
# def count(str):
#     i1=i2=i3=i4=0
#     for i in str:
#         if i.isalpha():
#             i1+=1
#         elif i.isdigit():
#             i2+=1
#         # elif i==' ':
#         elif i.isspace():  
#             i3+=1
#         else:
#             i4+=1
#     s='{}个字母，{}个数字，{}个空格，{}个其他字符'.format(i1,i2,i3,i4)
#     return s
# str1='affa245qzgss  /'
# print(count(str1))

def count(str):
    i1=i2=i3=i4=0
    for i in str:
        if i.isalpha():
            i1+=1
        elif i.isdigit():
            i2+=1
        # elif i==' ':
        elif i.isspace():  
            i3+=1
        else:
            i4+=1
    return i1,i2,i3,i4
str1='affa245qzgss  /'
x=count(str1)
print('{}个字母，{}个数字，{}个空格，{}个其他字符'.format(x[0],x[1],x[2],x[3]))

