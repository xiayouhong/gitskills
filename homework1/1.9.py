# -*- encoding: utf-8 -*-
'''
@File : 1.9.py
@Time : 2020/03/04 19:02:44
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
# 设计一个猜数字 游戏；最多只能猜测N次，
# 在N次之内猜不出，就退出程序，提示猜测失败；
import random
x=random.randint(1,99)
n=int(input('输入最多猜的次数:'))
y=int(input('输入你猜的数字1-98:'))
i=0
while x!=y:
    i+=1
    if y>x:
        print('答案错误，正确答案比y小')
    else:
        print('答案错误，正确答案比y大')
    if n>i:
        y=int(input('输入你猜的数字1-98:'))
    else:
        print('失败，游戏结束')
        break
else:
    print('恭喜你猜对了！是{}'.format(y))      
