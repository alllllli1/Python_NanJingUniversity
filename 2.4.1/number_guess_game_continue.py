# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 10:51
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : number_guess_game_continue.py
# @Software: PyCharm

#程序随机产生一个0~300间的整数玩家竞猜，
# 允许玩家自己控制游戏次数，如果猜中系统给出提示并退出程序，
# 如果猜错给出"太大了"或“太小了"的提示，如果不想继续玩可以退出。

from random import randint
x = randint(0,300)
go = 'y'
while go == 'y':
    digit = int(input('Please input a number between 0~300:'))
    if digit == x :
        print('Bingo!')
    elif digit > x :
        print('Too large ! Please try again !')
    else:
        print('Too small ! please try again ! ')
    print('Input y if you want to continue.')
    go = input()
    print(go)
else:
    print('goodBye')

#循环中的else：
    #如果循环代码从break处终止，跳出循环
    #正常结束循环，则执行else中代码
