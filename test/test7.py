# -*- encoding: utf-8 -*-
'''
@File : test7.py
@Time : 2020/03/20 07:55:03
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import os,sys
os.chdir('test')
print(os.getcwd())
def copy(path1,path2):
    if os.path.exists(path1):
        j=os.path.basename(path1)
        with open(path1,'r',encoding='utf-8') as f:
            lines=f.readlines()
        s=path2+r'\ '+j
        with open(s,'w',encoding='utf-8') as w:
            for line in lines:
                w.write(line)
    else:
        print('false')
copy(r'testsys1\sys1.txt','testsys2')