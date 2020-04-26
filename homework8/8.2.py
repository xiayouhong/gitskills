# -*- encoding: utf-8 -*-
'''
@File : 8.2.py
@Time : 2020/04/24 23:21:37
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
# 给定一组数据网址数据，请判断这些网址是否可以访问； 用多线程的方式来实现；
#    请查资料，Python的 requests库，如何判断一个网址可以访问；
# 提示 ：使用requests模块
#    def getHtmlText(url):
#     try:        # 网络连接有风险，异常处理很重要
#         r = requests.get(url,timeout=30)    # 查一下这个方法的使用
#         r.raise_for_status()       # 如果状态不是200，引发HTTPError异常
#         r.encoding = r.apparent_encoding
#         return r.text
#     except:
#          return "产生异常"
#   数据文件（1000个网址）：
import threading
from concurrent.futures import ThreadPoolExecutor
import requests
with open (r'homework8\url_data.txt','r') as f:
    lines=f.readlines()
def gethtml(url):
    try:
        r=requests.get(url,timeout=5)
        code = r.status_code
        if code == 200:
            print ('%s:%s网站访问正常'%(threading.currentThread().name,url))
        else:
            print  ("%s:error:%s"%(threading.currentThread().name,url))
    except:
        print("%s:error:%s"%(threading.currentThread().name,url))
threadpool=ThreadPoolExecutor(max_workers=3,thread_name_prefix='html')
for i in lines:
    f=threadpool.submit(gethtml,i.strip())
print(f.result())
threadpool.shutdown(wait=True)


