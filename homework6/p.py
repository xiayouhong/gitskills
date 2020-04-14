# -*- encoding: utf-8 -*-
'''
@File : 6.5.py
@Time : 2020/04/12 09:35:39
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
class people:
    attack=10
    live=100
    n=0
    name=''
    def __init__(self,name):
        self.name=name
    def get_attack(self):
        if self.live!=0 and self.attack>=2:
            self.attack=self.attack-2
            return self.attack
        else:
            self.attack=0
            return 0
    def get_live(self):
        if self.live<=0:
            print('people： {}  die'.format(self.name))
            self.live=0
            return 0
        else:
            return self.live
    def get_attacked(self):
        return self.n