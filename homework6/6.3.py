# -*- encoding: utf-8 -*-
'''
@File : 6.3.py
@Time : 2020/04/12 08:39:26
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
# 定义一个字典类：dictclass。完成下面的功能：
# dict = dictclass({你需要操作的字典对象})
# 1 删除某个key
# del_dict(key)
# 2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"
# get_dict(key)
# 3 返回键组成的列表：返回类型;(list)
# get_key()
# 4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)
# update_dict({要合并的字典})
class dictclass1:
    dict1={}
    def __init__(self,d):
        self.dict1=d
    def del_dict(self,key):
        if key in self.dict1.keys():
            del self.dict1[key]
    def get_dict(self,key):
        if key in self.dict1.keys():
            return self.dict1[key]
        else:
            return 'not found'
    def get_key(self):
        return list(self.dict1.keys())
    def update_dict(self,d2):
        self.dict1.update(d2)
        return list(self.dict1.values())
d1={1:2,2:3,'a':2}
d2={'a':1,'b':6}
d=dictclass1(d1)
d.del_dict(1)
print(d.dict1)
print(d.get_dict(2))
print(d.get_dict(3))
print(d.get_key())
print(d.update_dict(d2))