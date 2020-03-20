# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 10:06
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : number_guess_game.py
# @Software: PyCharm

from random import randint

x = randint(0,300)
for count in range(5):  #猜5次数字
    digit = int(input('Please input a number between 0~300:'))
    if digit == x:
        print('Bingo!')
    elif digit > x :
        print('Too large,please try again!')
    else:
        print('Too small,Please try again.')