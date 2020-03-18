# -*- encoding: utf-8 -*-
'''
@File : test6.py
@Time : 2020/03/18 07:55:10
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import os
# pwd = os.path.abspath('.')
# print(pwd)
# print( os.path.basename(pwd) )   # 返回文件名
# print( os.path.dirname(pwd) )    # 返回目录路径
# print( os.path.split(pwd) )      # 分割文件名与路径
# print( os.path.join('test','test6.py') )  # 将目录和文件名合成一个路径


# f=open(r'G:\PythonProject\MyfirstProject\venv\iotest.txt','w')
# f.write('af')
# f.close()
# f=open(r'homework2\homework2.txt')
# f.close()
# with open(r'test\iotest2.txt','r') as f:
#    print(f.read())

# with open(r'iotest.txt','r',encoding='utf-8') as f:
#     for line in f.readlines():
#        print(line.strip()) 

#读取文件内容输出
# 排序后存入另一个文件 包括中文字符的编码设置
# with open(r'iotest.txt','r',encoding='utf-8') as f:
#     list1=[]
#     for line in f.readlines():
#        list2=[]
#        print(line.strip()) 
#        list2=line.strip().split()
#        list1.append(list2)
# list3=[]
# for i in range(1,len(list1)):
#     list3.append(list1[i])
# print('未排序 ',list3)
# list3.sort(key=lambda x: (int)(x[2]))
# print('排序后 ',list3)
# with open(r'iotest2.txt','w',encoding='utf-8') as f:
#     for i in range(1):
#         f.write(' '.join(str(j) for j in list1[i]))
#         f.write('\n')
#     for i in range(len(list3)):
#         f.write(' '.join(str(j) for j in list3[i]))
#         f.write('\n')

#存入5个学生信息后并读取输出
import pickle
dict1={
    1:[1,'小明',20],
    2:[2,'小红',20],
    3:[3,'小军',20],
    4:[4,'小君',20],
    5:[5,'小康',20],
}
f=open(r'iotest1.txt','wb')
pickle.dump(dict1,f,0)
f.close()
f=open(r'iotest1.txt','rb')
data=pickle.load(f)
print(data)
