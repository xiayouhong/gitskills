# -*- encoding: utf-8 -*-
'''
@File : 3.1.py
@Time : 2020/03/22 09:06:55
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#写一个程序，读取键盘输入的任意行文字信息，当输入空行时结束输入，
# 将读入的字符串存于列表;然后将列表里面的内容写入到文件input.txt中；
list1=[]
while True:
    s=input('输入：')
    if s!=' ':
        list1.append(s)
    else:
        break
try:
    with open(r'homework3\input.txt','w',encoding='utf-8') as f:
        for i in list1:
            f.write(i)
except IOError:
        print('cannot open')
