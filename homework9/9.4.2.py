# -*- encoding: utf-8 -*-
'''
@File : 9.4.2.py
@Time : 2020/05/05 10:44:50
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#多线程客户端
import socket
import threading
import os
def get_ip():
    """用来搞到IP"""
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    return ip

def get_time():
    """得到发送时间"""
    now = datetime.datetime.now()
    send_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return send_time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = (get_ip(), 8888)
s.connect(addr)
def recv_msg():  #
    print("连接成功！现在可以接收消息！\n")
    while True:
        try:  # 测试发现，当服务器率先关闭时，这边也会报ConnectionResetError
            response = s.recv(1024)
            print(response.decode('utf-8'))
        except ConnectionResetError:
            print("服务器关闭，聊天已结束！")
            s.close()
            break
    os._exit(0)


def send_msg():
    print("连接成功！现在可以发送消息！\n")
    print("输入消息按回车来发送")
    print("输入esc来退出聊天")
    while True:
        msg = input()
        if msg == "esc":
            print("你退出了聊天")
            s.close()
            break
        s.send(msg.encode('utf-8'))
    os._exit(0)
if __name__=='__main__':
    threads = [threading.Thread(target=recv_msg), threading.Thread(target=send_msg)]
    for t in threads:
        t.start()
