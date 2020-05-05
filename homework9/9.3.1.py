# -*- encoding: utf-8 -*-
'''
@File : 9.3.py
@Time : 2020/05/04 23:32:28
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
# 编写一个UDP的聊天程序，客户端和服务器端能互相聊天应答；
# 服务器
# import socket
# seversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# host='192.168.1.108'
# port=9999
# seversocket.bind((host,port))
# seversocket.listen(3)
# while True:
#     data,addr=seversocket.recvfrom(1024)
#     print('receive from%s:%s'%(str(addr),data.decode('utf-8')))
#     reply=input('输入聊天内容:')
#     seversocket.sendto(reply.encode('utf-8'),addr)
import socket
import time
print("服务端开启")
#创建套接字
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#设置IP和端口
#host = socket.gethostname()
host = '192.168.1.108'
port = 3333
#bind绑定该端口
mySocket.bind((host, port))
#监听
mySocket.listen(10)
while True:
    #接收客户端连接
    print("等待连接....")
    client, address = mySocket.accept()
    print("新连接")
    print("IP is %s" % address[0])
    print("port is %d\n" % address[1]) 
    while True:
        #发送消息
        msg = input("服务端发送:")
        client.send(msg.encode(encoding='utf-8'))
        print("发送完成")
        print (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))#格式化时间戳为标准格式
        if msg == "EOF":
            break
        if msg == "quit":
            client.close()
            mySocket.close()
            print("程序结束\n")
            exit()
        
        #读取消息
        msg = client.recv(1024)
        print("服务端接收:",msg.decode("utf-8"))#把接收到的数据进行解码
        print("读取完成")
        if msg == b"EOF":
            break
        if msg == b"quit":
            client.close()
            mySocket.close()
            print("程序结束\n")
            exit()
