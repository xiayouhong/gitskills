# -*- encoding: utf-8 -*-
'''
@File : 3.4.py
@Time : 2020/03/22 10:16:58
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#题目要求：
#  在当前目录新建目录img, 里面包含10个文件, 10个文件名各不相同(X4G5.png)
#  将当前img目录所有以.png结尾的后缀名改为.jpg.
import os
try:
    os.chdir('homework3')
    #os.rmdir('img')
    os.mkdir('img')
    print(os.getcwd())
    os.chdir('img')
    print(os.getcwd())
    for i in range(1,11):
      #  os.rmdir('a{}.png'.format(i))
         os.mkdir('a{}.png'.format(i))
    filenames=os.listdir(os.getcwd())
    for i in filenames:
         j=os.path.splitext(i)
         if j[1]=='.png':
             newname=j[0]+'.jpg'
             os.rename(i,newname)
except SyntaxError:
     print(' ')