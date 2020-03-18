# -*- encoding: utf-8 -*-
'''
@File : 输入输出.py
@Time : 2020/03/02 19:59:52
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#x=input()
#xtuple=x.split()
#print(xtuple)
#print(tuple(xtuple))

#h,p=map(float,input("输入购买的苹果的重量(斤)和单价(元):").split())
#print("共花费：%f"%(h*p))

# name=input()
# grade=input()
# info='name:'+name+' grade:'+grade+''
# print(info)
# info='name: %s grade: %d'%(name,int(grade))
# print(info)
# info='name: {name_} grade: {grade_}'.format(name_=name,grade_=grade)
# print(info)
# info='name" {0} grade: {1}'.format(name,grade)
# print(info)

# xlist=list(range(10))
# print(xlist)
# for a in xlist:
#     if a%2==0:
#        print(a)
# print()

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')