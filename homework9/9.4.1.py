# -*- encoding: utf-8 -*-
'''
@File : 9.4.py
@Time : 2020/05/04 23:32:39
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
# 设计一款能实现多人聊天的系统：使用socket和多线程技术，编写全多人聊天室；
#   参考文档：https://blog.csdn.net/CxsGhost/article/details/103319864
import socket,datetime,os,threading
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
class sever:
    def __init__(self):
        self.seversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.address=(get_ip(),8888)
        self.users={}

    def start(self):
        try:
            self.seversocket.bind(self.address)
        except Exception as e:
            print(e)
        self.seversocket.listen(3)
        print('服务器已开启，等待连接')
        self.acceptcount()
    
    def acceptcount(self):
        while True:
            client,address=self.seversocket.accept()
            self.users[address]=client
            count=len(self.users)
            print('用户{}连接成功！现在共有{}位用户'.format(address, count))
            threading.Thread(target=self.receve, args=(client, address)).start()
            if len(self.users)==0:
                break
    def receve(self,sock,addr):
        while True:
            try:
                msg='{}用户{}发来消息：{}'.format(get_time(),addr,sock.recv(1024).decode('utf-8'))
                for i in self.users.values():
                    i.send(msg.encode('utf-8'))
            except ConnectionResetError:
                print("用户{}已经退出聊天！".format(addr))
                sock.close()
                self.users.pop(addr)
                break

    def close(self):
        self.seversocket.close()
        os._exit(0)

if __name__=='__main__':
    seve=sever()
    t=threading.Thread(target=seve.start)
    t.start()
    while True:
        cmd=input('是否关闭服务器：stop sever(yes or no)\n')
        if cmd == 'yes':
            seve.close()
            exit()
        else:
            print('重新输入')
