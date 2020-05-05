# -*- encoding: utf-8 -*-
'''
@File : 9.2.py
@Time : 2020/05/03 23:31:50
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
# 编写一个接收数据的网络程序，由“网络调试工具”发送数据，你的程序接收数据并打印输出；
from socket import *
def main():
       # 绑定端口信息
    udp_socket=socket(AF_INET,SOCK_DGRAM)
    
    local_addr=('',9999)

    udp_socket.bind(local_addr)
   # 接收数据
    recv_data = udp_socket.recvfrom(1024)  # 1024表示本次接收的最大字节数
   # 打印显示接收到的数据
    print(recv_data)


   # 关闭套接字
    udp_socket.close()

if __name__ == "__main__":
    main()