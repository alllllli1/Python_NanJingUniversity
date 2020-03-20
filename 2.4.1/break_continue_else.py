# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 10:32
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : break_continue_else.py
# @Software: PyCharm

# break作用：终止当前循环，转而执行循环之后的语句

#输出2-100之间的素数:2~根号x 只要没有可以整除的数，x就是素数
from math import sqrt
j = 2
while j <= 100 :
    i = 2
    k = sqrt(j)
    while i <= k :
        if j%i == 0 : break
        i = i + 1
    if i > k :
        print(j, end=' ')
    j += 1
