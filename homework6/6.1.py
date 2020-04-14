# -*- encoding: utf-8 -*-
'''
@File : 6.1.py
@Time : 2020/04/09 13:48:58
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
# 一、定义一个狗类,里面有一个 列表成员变量(列表的元素是字典), 
# 分别记录了 3种颜色的狗的颜色, 数量,和价格;
#     #    实现狗的买卖交易方法;  打印输出经过2-3次买卖方法后,剩下的各类狗的数量;
class dog:
    list1=[]
    def __init__(self,list2):
        self.list1=list2
    def sell(self,a,b):
        for i in self.list1:
            if i['颜色']==a:
                i['数量']-=b
    def buy(self,a,b):
         for i in self.list1:
            if i['颜色']==a:
                i['数量']+=b   
    def all(self):
        for i in self.list1:
            print(i)
list3=[
         {'颜色':'黑色','数量':10,'价格':600},
         {'颜色':'白色','数量':10,'价格':700},
         {'颜色':'黄色','数量':10,'价格':800},
      ]
dogs=dog(list3)
dogs.sell('黑色',2)
dogs.all()
print()
dogs.buy('白色',6)
dogs.all()