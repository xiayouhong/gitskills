# -*- encoding: utf-8 -*-
'''
@File : 4.4.py
@Time : 2020/03/28 17:29:53
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
# 模拟用户登录:
#      5个同学的姓名,账号和密码(加密后的),保存在一个文件上;  
#      系统提示,请输入登录同学姓名, 正确后,请输入账号,
#       正确后,提示请输入密码（输入明文）;  如果都正确,打印提示, 您登录成功(失败);
import hashlib
list1=[]
with open(r'homework4\access.txt','r',encoding='utf-8') as f:
    lines=f.readlines()
for line in lines:
    list2=line.split()
    list1.append(list2)
x=input('请输入姓名：')
for i in list1:
    if i[0]==x:
        y=input('请输入账号：')
        if i[1]==y:
            z=input('请输入密码：')
            md5=hashlib.md5(z.encode('utf-8'))
            if i[2]==md5.hexdigest():
                print('登录成功')
                exit(1)
            else:
                print('登录失败，密码错误')
                exit(1)
        else:
            print('账号错误')
            exit(1)
print('姓名错误')
