# -*- encoding: utf-8 -*-
'''
@File : 1.py
@Time : 2020/03/04 15:26:15
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#元素输出和查找：  请输出0-50之间的奇数，偶数，质数；能同时被2和3整除的数；
# for n in range(1,50):
#     if n%2!=0:
#         print('{:<6}是奇数'.format(n))
#     if n%2==0:
#         print('{:<6}是偶数'.format(n))
#     for m in range(2,n):
#         if(n%m==0):
#             break
#     else:
#         print('{:<6}是质数'.format(n))
#     if n%2==0 and n%3==0:
#         print('{:<6}能同时被2和3整除'.format(n))

#输出格式2：
print('奇数如下：')
for n in range(1,50):
    if n%2!=0:
       print(n)
print('偶数如下：')
for n in range(1,50):
    if n%2==0:
        print(n)
print('质数如下：')
for n in range(1,50):
    for m in range(2,n):
        if(n%m==0):
            break
    else:
        print(n)
print('能同时被2和3整除的数如下：')
for n in range(1,50):
    if n%2==0 and n%3==0:
        print(n)