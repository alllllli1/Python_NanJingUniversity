# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 15:06
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : scope_of_variable.py
# @Software: PyCharm

#变量作用域
    #全局变量 global_str
    #局部变量 local_str

#全局变量和局部变量用同一个名字
  #遵循规则：
      #内层屏蔽外层

#global语句强调全局变量

def f(x):
    global a
    print(a)
    a = 5
    print(a + x)

a = 3
f(8)
print(a)