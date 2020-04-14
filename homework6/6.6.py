# -*- encoding: utf-8 -*-
'''
@File : 6.6.py
@Time : 2020/04/12 09:40:01
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#  用面向对象,实现一个学生Python成绩管理系统;
#       学生的信息存储在文件中;学生信息的字段有(班级,学号,姓名, Python成绩)
#       实现对学生信息及成绩的增,删,改,查方法;
class manage(object):
    stulist=[]
    def save(self):
        with open(r'homework6\stu.txt','w',encoding='utf-8') as f:
            for i in self.stulist:
                f.write(' '.join(str(j) for j in i))
                f.write('\n')
    def get(self):
        self.stulist=[]
        with open(r'homework6\stu.txt','r',encoding='utf-8') as f:
            lines=f.readlines()
        for line in lines:
            self.stulist.append(line.strip().split())
    def __init__(self,l):
        self.stulist=l
        self.save()
    def add(self):
        name=input('输入姓名：')
        clas=input('输入班级：')
        no=input('输入学号：') 
        grade=input('输入Python成绩：')
        self.get() 
        self.stulist.append([clas,no,name,grade])
        self.save()
    def delete(self):
        name=input('输入姓名：')
        clas=input('输入班级：')
        no=input('输入学号：') 
        self.get()
        a=0
        for i in self.stulist:
            if i[0]==no and i[1]==clas and i[2]==name:
                self.stulist.remove(i)
                a=1
        if a==0:
            print('查无此人')
        else:
            print('删除成功')
            self.save()
    def find(self):
        name=input('输入姓名：')
        clas=input('输入班级：')
        no=input('输入学号：') 
        self.get()
        a=0
        for i in self.stulist:
            if i[0]==no or i[1]==clas or i[2]==name:
                print('姓名：{} 学号：{} 班级：{} 成绩：{}'.format(i[2],i[0],i[1],i[3]))
                a=1
        if a==0:
            print('查无此人')
        else:
            self.save()
    def update(self):
        name=input('输入姓名：')
        clas=input('输入班级：')
        no=input('输入学号：') 
        self.get()
        a=0
        for i in self.stulist:
            if i[0]==no and i[1]==clas and i[2]==name:
                x=input('输入修改的分数：')
                i[3]=x
                a=1
        if a==0:
            print('查无此人')
        else:
            self.save()
    def printf(self):
        self.get()
        for i in self.stulist:
            print(i)
l=[[1,'class2','lihua',99],[2,'class3','wang',98]]
m=manage(l)
m.printf()
print('增')
m.add()
m.printf()
print('删')
m.delete()
m.printf()
print('查')
m.find()
m.printf()
print('改')
m.update()
m.printf()
        