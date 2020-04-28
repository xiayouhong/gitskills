# -*- encoding: utf-8 -*-
'''
@File : 7.4.py
@Time : 2020/04/20 13:56:54
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
# 爬取这个网址上http://www.python3.vip/doc/prac/python/0001/，
# 所有的Python练习题题目和答案；保存到txt文件中（只保留文字）
import requests
from bs4 import BeautifulSoup
url='http://www.python3.vip/doc/prac/python/0001/'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'
}
r=requests.get(url,headers=headers).content.decode('utf-8')
soup=BeautifulSoup(r,'html.parser')
re_a=soup.find_all(id='content').find_all('a')
list = []
for i in re_a:
	list.append(i.attrs['href'])
print(list)