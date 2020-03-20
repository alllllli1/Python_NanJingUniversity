# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 9:38
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : range.py
# @Software: PyCharm

#range()有三种语法表达形式：
     #range(start,end,step=1)  step是步长，这里为1
     #range(start,end)    默认step为1
     #range(end)    默认start为0，step=1
     #起始值start是包括在内的，但是终值是不包括在内的，步长不能为0

print(list(range(3,21,2)))
print(list(range(3,21)))
print(list(range(21)))

