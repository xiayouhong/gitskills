# -*- encoding: utf-8 -*-
'''
@File : 9.3.2.py
@Time : 2020/05/05 09:03:40
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
# 编写一个UDP的聊天程序，客户端和服务器端能互相聊天应答；
# 客户端
# import socket
# client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# dest_addr = ('192.168.1.108',9999)
# while True:
#     data=input('输入聊天内容：')
#     client.sendto(data.encode('utf-8'),dest_addr)
#     print('seversocket:',client.recv(1024).decode('utf-8'))
# client.close()
import socket
print("客户端开启")
#创建套接字
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#设置ip和端口
#host = socket.gethostname()
host = '192.168.1.108'
port = 3333
 
try:
    mySocket.connect((host, port)) ##连接到服务器
    print("连接到服务器")
except :                           ##连接不成功，运行最初的ip
    print ('连接不成功')
 
while 1:
    #接收消息
    msg = mySocket.recv(1024)  
    print("客户端接收：%s" % msg.decode("utf-8"))#把接收到的数据进行解码
    print("读取完成")	
    if msg == b"EOF":
        break
    if msg == b"quit":
        mySocket.close()
        print("程序结束\n")
        exit()
    
    #发送消息
    msg = input("客户端发送:")
    mySocket.send(msg.encode(encoding='utf-8'))
    print("发送完成")
    if msg == "EOF":
        break
    if msg == "quit":
        mySocket.close()
        print("程序结束\n")
        exit()       
print("程序结束\n")
