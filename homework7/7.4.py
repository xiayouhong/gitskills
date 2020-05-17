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
# 爬取这个网址上https://www.programcreek.com/python/，搜索request的范例代码；
# 保存到txt文件中（只保留文字）；
#     文本文件类似（注意是类似的效果，不是说一定要做的一模一样）的效果如下：
import requests
from bs4 import BeautifulSoup
url='https://www.programcreek.com/python/example/3765/requests.get'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'
}
def get_html(url,headers):
    try:
        r=requests.get(url,headers=headers,timeout=5).content.decode('utf-8')
    except Exception as e:
        print(e)
    finally:
        return r

def get_requests(html):
    soup=BeautifulSoup(html,'html.parser')
    re=soup.find_all('pre')
    return re


def save_in_txt(pres):
    with open(r'homework7/request.txt', 'w', encoding='utf-8') as f:
        i=1
        for pre in pres:
            f.write('example'+str(i)+'\n')
            i=i+1
            f.write(pre.string)
            f.write('\n')

if __name__ == '__main__':
    html = get_html(url,headers)
    pres = get_requests(html)
    save_in_txt(pres)