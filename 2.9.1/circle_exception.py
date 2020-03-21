# -*- coding: utf-8 -*-
# @Time    : 2020/3/21 9:54
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : circle_exception.py
# @Software: PyCharm

while True:
    try:
        x=int(input('Enter the first number :'))
        y=int(input('Enter the second number : '))
        print(x/y)
        break
    except ValueError:
        print('Please input a digit!')
    except ZeroDivisionError:
        print('The second number connot be zero')

#通过while循环实现不断检测异常的功能

