# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 10:42
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : for_prime_number.py
# @Software: PyCharm

#用for循环来实现输出2~100之间的素数
from math import sqrt
for i in range(2,101):
    k = int(sqrt(i))
    flag = 1            #flag = 1 说明i是素数，在print处打印
    for j in range(2,k+1):
        if i%j == 0 :
            flag = 0    #flag = 0 说明i不是素数，这样下面就不会print打印
            break
    if(flag):
        print(i,end = ' ')