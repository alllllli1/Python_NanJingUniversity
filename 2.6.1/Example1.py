# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 15:01
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : Example1.py
# @Software: PyCharm

def f1(a,b):
    if b == 1 :
        return a
    else:
        return a+f1(a,b-1)
print(f1(3,5))

#模拟加法实现乘法的过程
#3+3+3+3+3