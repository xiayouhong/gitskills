# -*- encoding: utf-8 -*-
'''
@File : 4.3.py
@Time : 2020/03/28 17:05:58
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#  从键盘输入5个同学的账号和密码,然后将他们的姓名,
# 账号和密码(密码需要加密)保存到一个文件中;
import hashlib
with open(r'homework4\access.txt','w',encoding='utf-8') as f:
    for i in range(5):
        x=input('输入姓名：')
        y=input('输入账号：')
        z=input('输入密码：')
        f.write(x+'  '+y+'  ')
        md5 = hashlib.md5(z.encode('utf-8'))
        f.write(md5.hexdigest()+'\n')