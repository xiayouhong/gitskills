# -*- encoding: utf-8 -*-
'''
@File : 7.2.py
@Time : 2020/04/19 14:53:54
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#  给定100个企业网站首页链接地址（用1中给出的URL地址）；请爬取每个页面上，企业介绍的链接地址；
#     说明，满足企业介绍网址的条件是， 标题包含：企业介绍，关于我们，企业发展，发展历史，企业概况等关键字的URL地址；
#     提示：要用到requests库，BeautifulSoup库
from bs4 import BeautifulSoup
import requests,re
def geturl(line):
    with open (r'homework7\copy.txt','r',encoding='utf-8') as f:
        for i in range(100):
            line.append(f.readline().strip())
    return line
hd={'User-Agent':'Mozilla/5.0'}
def gethtml(url):
    try:
        adaptlist=['企业介绍','关于我们','企业发展','发展历史','企业概况','公司简介']
        r=requests.get(url,timeout=5,headers=hd)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        txt=r.text
        soup=BeautifulSoup(txt,'html.parser')
        list1=soup.select('a')
        for i in list1:
            if i.string in adaptlist:
                html=i['href']
                if re.match('^http/',html):
                    print(html)
                    break
                else:
                    print(url+'/'+html)
                    break#已经有了adaptlist中的一个 打印并退出
    except Exception as result:
        print('错误类型：',result)
if __name__=='__main__':
    line=[]
    line=geturl(line)
    for i in line:
        gethtml(i)