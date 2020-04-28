# -*- encoding: utf-8 -*-
'''
@File : 7.3.py
@Time : 2020/04/20 19:46:43
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
# 给定一个网址（包含了优质的英语学习音频文件）
# ，http://www.listeningexpress.com/studioclassroom/ad/；  
# 请大家写一个爬虫，将里面的英语节目MP3，都下载下来；
#      这些音频文件 在网页的html文件内容都是以mp3结尾的
import requests,os,re,wget
from urllib.parse import quote 
#获取网页的html，与requests包一样的功能
def getHtml(url):
    hd={'User-Agent':'Mozilla/5.0'}
    r=requests.get(url,timeout=5,headers=hd)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    html=r.text
    return html

#获取音频对应的src属性代码
def getmp3Url(html):  
    #通过re-compile-findall二连函数操作来获取图片src属性对应的代码
    src =r'sc-ad [\w\s-]*.mp3'     # 正则表达式匹配规则
    imgre = re.compile(src)     # re.compile()，可以把正则表达式编译成一个正则表达式对象
    mp3list1 = re.findall(imgre, html)    # 读取html中包含imgre（正则表达式）的数据,imglist是包含了所有src元素的数组
    mp3list2=[]
    for i in mp3list1:
        j=i[6:]
        k=quote(j)
        mp3list2.append(k)
    return  mp3list2

#下载
def downloadmp3(list,url,path):
    #判断给定的路径是否存在,不存在则创建
    if not os.path.exists(path):
        os.mkdir(path)
    os.chdir(path)
    for i in list:
        file_name = wget.download(url,i)
        print('downloading: ',file_name)

if __name__=='__main__':
    url="http://www.listeningexpress.com/studioclassroom/ad/"  # 指定目标网址
    path=r"G:\PythonProject\MyfirstProject\venv\homework7\mp3file"   # 设定目标路径,前面的r表示后面的字符串不转义
    html = getHtml(url)
    mp3urls=getmp3Url(html)
    downloadmp3(mp3urls,url,path)
    print('download success!')
