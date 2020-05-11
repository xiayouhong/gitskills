# -*- coding: utf-8 -*-
# @Time    : 2020/5/11 19:55
# @Author  : xyh
from sqlalchemy import Column, String,Integer,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class messages(Base):
    __tablename__='messages'
    id=Column(Integer,primary_key=True)
    msg=Column(String(255))
    name=Column(String(30))
    time=Column(String(36))
    is_delete=Column(Integer)

engine = create_engine('mysql+mysqlconnector://root:1234a@localhost:3306/test')
DBSession = sessionmaker(bind=engine)
session = DBSession()
# 查
try:
    message = session.query(messages).all()
    print('type:',type(message))
    for i in message:
        print(i.id,i.msg,i.name,i.time,i.is_delete)
except Exception as e:
    print(e)
# finally:
    # session.close()
# 增
new_message =messages(id=5, msg='eat',name='Bob',time='2000-09-09 09:09;09',is_delete=1)
try:
    session.add(new_message) # 添加到session
    session.commit()  # 提交即保存到数据库
except Exception as e:
    print(e)
# finally:
#     session.close()
# 删
try:
    session.query(messages).filter_by(id=5).delete() # 添加到session
    session.commit()  # 提交即保存到数据库
except Exception as e:
    print(e)
# finally:
#     session.close()
# 改
try:
    session.query(messages).filter_by(name = 'l').update({'name':'x'}) # 添加到session
    session.commit()  # 提交即保存到数据库
except Exception as e:
    print(e)
finally:
    session.close()