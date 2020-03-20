# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 14:50
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : hanoi.py
# @Software: PyCharm

#汉诺塔游戏
#三个塔座A，B、C上各有一根针，通过B把64个盘子从A针移动到C针上
# 移动时必须遵循下列规则：
#（1）圆盘可以插入在A、B或C塔座的针上
#（2）每次只能移动一个圆盘
# (3）任何时刻都不能将一个较大的圆盘压在较小的圆盘之上

def hanoi(a,b,c,n):
    if n==1:
        print(a,'->',c)
    else:
        hanoi(a,c,b,n-1)
        print(a,'->',c)
        hanoi(b,a,c,n-1)

hanoi('a','b','c',4)