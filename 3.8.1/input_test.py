# -*- coding: utf-8 -*-
# @Time    : 2020/4/19 16:10
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : test1.py
# @Software: PyCharm

#如何输入获得两个字符串，比如输入abc def 或 abc，def
x,y = input('Input_str:').split()  #split是分隔符，默认空格，也可以用逗号
print("x:",x,end='\n')
print("y:",y)

#如何输入获得两个整数？若输入34,567
a,b = eval(input("input_integer:"))
print("a:",a,end='\n')
print("b:",b)

#如何输入后获得一个元素均为数值型的列表？
#比如输入12,3,4,567或[12,3,4,567]
lst = list(eval(input("input:")))
print(lst)

lst2 = eval(input("Input_list:"))
print(lst2)

# eval()函数又称为评估函数，作用是去掉参数中最外层引号并执行剩余语句。
# 划重点：只去掉最外层引号
# eval()的参数形式为字符串或字符串变量
# 在程序中可以将字符串形式的输入值转化为数字进行计算。