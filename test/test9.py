# -*- encoding: utf-8 -*-
'''
@File : test9.py
@Time : 2020/04/03 08:36:25
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
# def createCounter():
#     i=1
#     def count():
#         print(i)
#         i+=1
#     return count
# counterA = createCounter()
# print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
# counterB = createCounter()
# if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
#     print('测试通过!')
# else:
#     print('测试失败!')
def date(add):
    def inner(*args):
        print(add,':周五')
        r=add(*args)
        return r
    return inner
@date
def add(x,y):
    print(x+y)
    return x+y 
a=add(1,2)
print(a)