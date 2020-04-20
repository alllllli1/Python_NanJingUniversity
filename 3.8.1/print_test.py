# -*- coding: utf-8 -*-
# @Time    : 2020/4/20 12:35
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : print_test.py
# @Software: PyCharm

#如何在输出数据中加入一个非空白分隔符？（若数据为12和345）
x,y=4,5
print(x,y,sep=',')

#如何换行输出所有数据（若数据为23和345）

print(x) #默认换行end='\n'
print(y)

#如何将循环输出的所有数据放在同一行输出？
for i in  range(1,5):
    print(i,end=' ')
print()

#列表解析
lst = input('Input:').split(',')
print(lst)
print([eval(item) for item in lst])
#字符串变为数值类型，利用eval函数即可