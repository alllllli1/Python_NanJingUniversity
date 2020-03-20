# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 11:01
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : selfdefining_function.py
# @Software: PyCharm

#自定义函数的格式：
   #def function_name([arguments]):
       #"optional documentation string"  写注释
       #function_suite

#自定义函数的调用：
   #函数名加上函数运算符，一对小括号
      #括号之间是所有可选的参数
      #即使没有参数，也不能省略括号
#比如 addMe2Me（5）

#默认参数：
    #函数的参数可以有一个默认值，如果提供有默认值
    #在函数定义中，默认参数以赋值语句的形式提供

def f(x=True):
    '''whether x is a correct word or not'''
    if x:
        print('x is a correct word')
    print('OK')

f()
f(False)

#默认参数的值可以改变
#默认参数一般需要放置在参数列表的最后

def g(x,y = True):
    '''x and y both correct words or not'''
    if y:
        print(x,'and y both correct')
    print(x,'is OK')

g(68,False)

#关键字参数是让调用者通过使用参数名区分参数，允许改变参数列表中的参数顺序

#传递函数：函数可以像参数一样传递给另外一个函数

def addMe2Me(x):
    return x+x
def self(f,y):
    print(f(y))
self(addMe2Me,2.2)