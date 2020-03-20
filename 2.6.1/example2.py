# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 15:02
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : example2.py
# @Software: PyCharm

def f2(n):
    if n >= 2 :
        f2(n//2)
    print(n%2,end=' ')

f2(8)

#n%2是先求出来的最后打印，将十进制换成二进制
#8---> 1000