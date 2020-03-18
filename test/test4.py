# -*- encoding: utf-8 -*-
'''
@File : test4.py
@Time : 2020/03/06 08:14:20
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
# def sum(num,price):
#     return num*price
# x,y=map(int,input('输入数量及单价:').split())

# def printf(mylist):
#     print(mylist)
#     print('未改变前的地址：',id(mylist))
#     mylist.append('s')
#     print(mylist)
#     print('改变后的地址：',id(mylist))
# list1 = [2,3]
# print('list1的地址:',id(list1))
# printf(list1)
# print('传了参数后的list1的地址:',id(list1))
# print('list1的值:', list1 )

# list2=list(range(1,20))
# print(list2)
# res = filter(lambda x: x%2!=0, list2) #返回奇数
# print(list(res))

def arg(arg1,*arg2):
    print('第一个元素:',arg1)
    print('第二个元素:',arg2)
    list3=[arg1]+list(arg2)
    print('封装后的列表:',list3)
    dict1={}
    for i in range(len(list3)):
        dict1[i+1]=list3[i]
    print('封装后的元组:',dict1)
arg(2,3,5,6,'ad')

