# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 11:05
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : Prime_number.py
# @Software: PyCharm

#输出1-100之间的素数
from math import sqrt
def isprime(x):
    if x == 1 :
        return False
    k = int(sqrt(x))
    for j in range(2,k+1):  #假如j不是素数就不返回False
        if x%j == 0:
            return False
    return True             #所有的素数会返回True
for i in range(2,101):
    if isprime(i):
        print(i,end=' ')