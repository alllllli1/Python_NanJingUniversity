# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 9:59
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : for_example.py
# @Software: PyCharm

for i in range(3,11,2):
    print(i , end = ' ') #range()返回的是一个iterable_object(可迭代对象)

s = 'Python'
for c in s :
    print(c,end = ' ')

for i in range(len(s)):
    print(s[i],end = ' ')
