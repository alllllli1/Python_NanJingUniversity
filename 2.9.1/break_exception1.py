# -*- coding: utf-8 -*-
# @Time    : 2020/3/21 10:03
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : break_exception1.py
# @Software: PyCharm

aList = [1,2,3,4,5]
i = 0
while True:
    try:
        print(aList[i])
    except IndexError:
        print('index error')
        break
    else:
        i += 1

    #break在哪就从哪跳出循环