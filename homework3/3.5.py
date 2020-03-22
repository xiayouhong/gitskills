# -*- encoding: utf-8 -*-
'''
@File : 3.5.py
@Time : 2020/03/22 10:19:19
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#文件编程小项目
import os
try:
    s = (
        'How many roads must a man walk down\n'
        'Before they call him a man\n'
        'How many seas must a white dove sail\n'
        'Before she sleeps in the sand\n'
        'How many times must the cannon balls fly\n'
        'Before they‘re forever banned\n'
        'The answer, my friend, is blowing in the wind\n'
        'The answer is blowing in the wind'
    )
    os.chdir('homework3')
    with open('Blowing in the wind.txt','w') as f:
         f.write(s)
    with open('Blowing in the wind.txt','r') as f:
         line=f.readlines()
         line.insert(0,'Blowin in the wind\n')
         line.insert(1,'Bob Dylan\n')
         line.insert(len(line)+1,'\n1962 by Warner Bros lnc')
    with open('Blowing in the wind.txt','w') as f:
         f.write(''.join(line))
    with open('Blowing in the wind.txt','r') as f:
         line=f.readlines()
         for i in line:
              print(''.join(i))
except IOError:
    print('cannot open')
except Exception as ex:
  print('表达式为空')
finally:
    print('end')