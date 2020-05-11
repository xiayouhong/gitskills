# -*- coding: utf-8 -*-
# @Time    : 2020/5/11 12:32
# @Author  : xyh
# 设计一个留言本的表（ID，留言内容，留言人，留言时间，是否删除）（表名，和字段名自己设计成英文：注意，不要用中文，用中文的直接0分）；
#    使用PyMySQL 驱动模块，实现对这个表的增加，删除，修改，查询；数据库操作需要加入异常处理逻辑；
import pymysql
import datetime
conn = pymysql.connect(host='127.0.0.1', user='root', passwd="1234a", db='test')
# conn = pymysql.connect(host='localhost',user='root',passwd='1234a',db='test')
cur = conn.cursor()
t = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
sql = """insert into messages values (4,'study','miki','"""+t+"""',0)"""
# print(sql)
try:
    cur.execute(sql)
    conn.commit()
except Exception as e:
    print(e)
# finally:
#     conn.close()
sql = """delete from messages where id = 1"""
# print(sql)
try:
    cur.execute(sql)
    conn.commit()
except Exception as e:
    print(e)
# finally:
#     conn.close()
sql = """update messages set msg ='read' where name ='miki'"""
# print(sql)
try:
    cur.execute(sql)
    conn.commit()
except Exception as e:
    print(e)
# finally:
#     conn.close()
sql = """select * from messages where id = 2"""
try:
    cur.execute(sql)
    conn.commit()
    for r in cur:
        print(r)
except Exception as e:
    print(e)
finally:
    conn.close()