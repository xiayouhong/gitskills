# -*- encoding: utf-8 -*-
'''
@File : 4.6.py
@Time : 2020/03/28 19:12:11
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#  通过Python来实现显示给定文件夹下的所有文件和文件夹,以及时间，
#  如果是文件，显示大小; 输出格式效果如下:
#     名称         日期                   类型（文件夹或者 文件）       大小

# 效果如：
import os 
import time
def printf(path):
    files=os.listdir(path)
    print('{:16} {:30} {:16} {:16}'.format('名称','日期','类型','大小'))
    for file in files:
        size=os.path.getsize(file)
        time1=time.localtime(os.path.getctime(file))
        date='{}-{}-{} {}:{}:{}'.format(time1.tm_year,time1.tm_mon,time1.tm_mday,
        time1.tm_hour,time1.tm_min,time1.tm_sec)
        if os.path.isfile(file):
            print('{:16} {:30} {:16} {:16}字节'.format(file,date,'文件',size))
        else:
            print('{:16} {:30} {:16} {:16}字节'.format(file,date,'文件夹',size))
printf(r'G:\PythonProject\MyfirstProject\venv')