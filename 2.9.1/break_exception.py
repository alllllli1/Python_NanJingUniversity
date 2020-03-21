# -*- coding: utf-8 -*-
# @Time    : 2020/3/21 10:01
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : break_exception.py
# @Software: PyCharm

while True:
    try:
        x=int(input('Enter the first number :'))
        y=int(input('Enter the second number : '))
        print(x/y)
    except Exception as err :
        print(err)
    else:
        break

    #无异常就执行else语句,break退出循环