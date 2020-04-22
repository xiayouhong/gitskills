# -*- encoding: utf-8 -*-
'''
@File : test8.py
@Time : 2020/04/01 08:31:39
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
# def a(x,y):
#     return x+y
# def b(x,y):
#     return x-y
# def c(x,y):
#     return x*y
# def d(x,y):
#     return x/y
# def calculate(a,b,c,d,x,y):
#     z=input('输入想做的运算+ - * /,分别用a b c d代替输入')
#     if x==a:
#        return a(x,y)
#     if x==b:
#        return b(x,y)
#     if x==c:
#        return c(x,y)
#     if x==d:
#        return d(x,y)
# print(calculate(a,b,c,d,1,2))
a=1.0
for i in range(10):
    a=a*0.9
b=a/0.9
c=1-b-a
print(c)
d=4*c*(1-c)*(1-c)*(1-c)+2*6*c*c*(1-c)*(1-c)+3*4*c*c*c*(1-c)+4*c*c*c*c
print(d)