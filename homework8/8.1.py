# -*- encoding: utf-8 -*-
'''
@File : 8.1.py
@Time : 2020/04/24 22:13:24
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
# 1  有100个同学的分数：数据请用随机函数生成；
#  A  利用多线程程序（比如，5个线程，每个线程负责输出20条记录），快速输出这100个同学的信息；
#   B 利用线程池来实现；
import threading
import random 
import time
# A
def grade():
    x=threading.currentThread().name
    for i in range(20):
        print('%s的第%d个学生   成绩：%d'%(x,i+1,(random.randint(0,100))))
        time.sleep(1)

# if __name__=='__main__':
#     t1=threading.Thread(target=grade)
#     t2=threading.Thread(target=grade)
#     t3=threading.Thread(target=grade)
#     t4=threading.Thread(target=grade)
#     t5=threading.Thread(target=grade)

#     t1.start()
#     t2.start()
#     t3.start()
#     t4.start()
#     t5.start()
#B
from concurrent.futures import ThreadPoolExecutor
threadPool = ThreadPoolExecutor(max_workers=5, thread_name_prefix='grade')
for i in range(100):
    future=threadPool.submit(grade)
print(future.result())
# threadPool.shutdown(wait=True)