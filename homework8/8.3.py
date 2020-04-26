# -*- encoding: utf-8 -*-
'''
@File : 8.3.py
@Time : 2020/04/25 21:42:04
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
# 3  多进程练习：
# 计算1～100000之间所有素数的个数， 要求如下:
# - 编写函数判断一个数字是否为素数，然后统计素数的个数；
# -对比1: 对比使用多进程和不使用多进程两种方法的统计速度。
# -对比2：对比开启4个多进程和开启10个多进程两种方法的速度。
import time
from multiprocessing import Process 
from multiprocessing import Pool
def isprime(x):
    if x==1:
        return 0
    for i in range(2,x):
        if x%i==0:
            return 0
    return 1
def pool(count):
    pool=Pool(count)
    num=0
    t_start=time.time()
    for i in range(1,100000):
        num+=pool.apply_async(isprime,(i,)).get()
    pool.close()
    pool.join()
    t_end=time.time()
    print('有%d个进程同时计算出%d个素数 花费%f'%(count,num,t_end-t_start))
if __name__=='__main__':
    pool(10000)
    # pool(4)
    # pool(1)