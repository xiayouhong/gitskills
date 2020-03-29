# -*- encoding: utf-8 -*-
'''
@File : 4.2.py
@Time : 2020/03/26 13:35:02
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#  定义一个函数，判断一个输入的日期，是当年的第几周，周几？  将程序改写一下，能针
#  对我们学校的校历时间进行计算（校历第1周，2月17-2月23；校历第27周，8月17-8月23；）；
from datetime import datetime
def date(year,mon,day):
    list1=[31,29,31,30,31,30,31,31,30,31,30,31] #今年2月份为29天
    total=(year-2020)*365
    for i in range(2,mon):
        total+=list1[i-1]
    total-=16#减去二月份前16天
    total+=day
    a=total/7
    a=(int)(a)
    if total%7==0:
        print('第',a,'周---周日')
    else:
        print('第',a+1,'周---周',total%7)
    # week=datetime.strptime('{}{}{}'.format(year,mon,day),'%Y%m%d').weekday()
    # print('星期',week)
    #自带方法
x,y,z=map(int,input('请输入年 月 日').split())
date(x,y,z)