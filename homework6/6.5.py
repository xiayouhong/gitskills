# -*- encoding: utf-8 -*-
'''
@File : 6.5.py
@Time : 2020/04/12 16:55:30
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#   请写一个小游戏，人狗大站;  规则:
#     1   2个角色，人和狗，游戏开始后，生成2个人，3条狗，
#     人狗互相交替对战(注意,人只能打狗,  狗也只会咬人); 
#         人的打击力为10;  初始化血为100;    狗的攻击力为 15; 初始化血为80;
#     2  人被狗咬了会掉血，狗被人打了也掉血，狗和人的攻击力，
#     具备的功能都不一样。血为0的话,表示死亡,退出游戏;
#         人和狗的攻击力,都会因为被咬, 或者被打而降低(人被咬一次,打击力降低2; 
#          狗被打一次,攻击力降低3);
#     3   对战规则: 
#      A  随机决定,谁先开始攻击; 
#      B  一方攻击完毕后, 另外一方再开始攻击;  攻击的目标是随机的
#      (比如, 人要打狗了, 随机找一条血不为0的狗攻击);
#      C  每次攻击, 双方只能安排一个人,或者一条狗进行攻击;
# 提示：注意组织代码的方式；狗类用一个单独的py文件； 人用一个单独的py文件；
#  在写一个fight模块（也用类来组织；
# 在这个模块中，导入人和狗模块中编写好的方法）
import random
from d import dog
from p import people
class fight:
    p1=people('p1')
    p2=people('p2')
    d1=dog('d1')
    d2=dog('d2')
    d3=dog('d3')
    men=[p1,p2]
    dogs=[d1,d2,d3]
    def victory(self):
        for i in self.men:
            if i.live==0:
                self.men.remove(i)
        for i in self.dogs:
            if i.live==0:
                self.dogs.remove(i)   
        if len(self.men)==0:
            print('狗胜利')
            return 0
        elif len(self.dogs)==0:
            print('人胜利')
            return 0
        else:
            a=0
            for i in self.dogs:
                if i.attack!=0:
                    a=1
                    break
            for i in self.men:
                if i.attack!=0:
                    a=1
                    break
            if a==0:
                print('平局') #所有人和狗的攻击力都为0时平局
            return a
    def selectp(self):
        a=random.randint(0,len(self.men)-1)
        return self.men[a]
    def selectd(self):
        a=random.randint(0,len(self.dogs)-1)
        return self.dogs[a]
    def fights(self):
        a=random.randint(0,1)
        if a==0:
            print('人先攻击')
            while self.victory()==1:
                x=self.selectp()
                y=self.selectd()
                print('{}攻击{}，{}失血{}'.format(x.name,y.name,y.name,x.attack))
                y.live-=x.attack
                y.n+=1
                y.get_attack()
                print('{}被攻击{}次 攻击力降为为{}'.format(y.name,y.n,y.attack))
                y.get_live()
                if self.victory()==1:
                    x=self.selectp()
                    y=self.selectd()
                    print('{}攻击{}，{}失血{}'.format(y.name,x.name,x.name,y.attack))
                    x.live-=y.attack
                    x.n+=1
                    x.get_attack()
                    print('{}被攻击{}次 攻击力降为为{}'.format(x.name,x.n,x.attack))
                    x.get_live()
                else:
                    break
        else:
            print('狗先攻击')
            while self.victory()==1:
                y=self.selectp()
                x=self.selectd()
                print('{}攻击{}，{}失血{}'.format(x.name,y.name,y.name,x.attack))
                y.live-=x.attack
                y.n+=1
                y.get_attack()
                print('{}被攻击{}次 攻击力降为为{}'.format(y.name,y.n,y.attack))
                y.get_live()
                if self.victory()==1:
                    y=self.selectp()
                    x=self.selectd()
                    print('{}攻击{}，{}失血{}'.format(y.name,x.name,x.name,y.attack))
                    x.live-=y.attack
                    x.n+=1
                    x.get_attack()
                    print('{}被攻击{}次 攻击力降为为{}'.format(x.name,x.n,x.attack))
                    x.get_live()
                else:
                    break
f=fight()
f.fights()