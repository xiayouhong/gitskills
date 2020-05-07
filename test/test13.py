# -*- encoding: utf-8 -*-
'''
@File : test13.py
@Time : 2020/05/06 09:22:22
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', passwd="1234a", db='test')
cur = conn.cursor()
# cur.execute("SELECT * FROM message")
# for r in cur:
#   print(r)
# 增
# sql="INSERT INTO message(ID,theme,name,time) VALUES (1,'study','amy','5:00');"
# print(sql)
# cur.execute(sql)
# 删
# sql="delete from message where id =1 "
# cur.execute(sql)
# 改
# sql="update message set time='6:00' where id=2"
# cur.execute(sql)
# 查
sql="select * from message where id =3"
cur.execute(sql)
for r in cur:
      print(r)
conn.commit()
cur.execute("SELECT * FROM message")
for r in cur:
  print(r)
cur.close()
conn.close()