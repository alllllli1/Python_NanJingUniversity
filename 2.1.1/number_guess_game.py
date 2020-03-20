# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 9:29
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : number_guess_game.py
# @Software: PyCharm

from random import randint

x = randint(0,300)
digit = int(input('Please input a number between 0~300:'))
if digit == x:
    print('Bingo!')
elif digit > x :
    print('Too large,please try again!')
else:
    print('Too small,Please try again.')

        # X if E else Y
        #t = 1 if x>=0 else 0
        #只要x>=0t=1，否则t=0