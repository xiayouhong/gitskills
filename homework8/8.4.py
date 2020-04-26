# -*- encoding: utf-8 -*-
'''
@File : 8.4.py
@Time : 2020/04/26 11:46:08
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#  多进程通讯：
#   编写一个简单的聊天程序；其中一个进程发送文字聊天消息（从键盘输入文字消息）； 
#    另外一个进程接收并打印消息；
from multiprocessing import Queue
from multiprocessing import Process
import os,time
def write(q,x):
    for i in x:
        if not q.full():
            print('进程{} 发送信息'.format(os.getpid()))
            q.put(i)
            time.sleep(1)
        else:
            print('聊天上限')
def read(q):
    while not q.empty():
        print('进程{} 接受信息'.format(os.getpid()))
        print(q.get(True))
        time.sleep(1)
if __name__=='__main__':
    q=Queue(6)
    list1=[]
    print('子进程中无法使用input')
    for i in range(int(input('聊天次数：'))):
        list1.append(input('输入聊天信息：'))
    r=Process(target=read,args=(q,))
    w=Process(target=write,args=(q,list1))
    w.start()
    r.start()
    w.join()
    r.join()