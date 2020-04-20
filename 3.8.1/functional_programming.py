# -*- coding: utf-8 -*-
# @Time    : 2020/4/20 12:57
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : functional_programming.py
# @Software: PyCharm

#参考教程：https://www.cnblogs.com/sddai/p/10105401.html
#函数式编程;3个基本函数+一个算子
#基本函数：map(),reduce(),filter()
#基本算子（operator）：lambda

#lambda 实现函数创建的功能
# func1 = lambda : <expression()>  创建午餐函数func1
# 调用func1的时候，虽然不需要传入参数，但是必须要带有括号()，否则返回的只是函数的定义，而非函数执行的结果。
# func2 = lambda x : <expression(x)> 创建需要传入1个参数的函数func2
# func3 = lambda x,y : <expression(x,y)> 创建需要传入2个参数的函数func3
addition = lambda a, b: a + b
print(addition(3, 4))

#map(function,iterable)
#map(函数名，可迭代对象--列表、元素等)
#功能：将第二个参数iterable中的每一个元素分别传给第一个函数，依次执行函数得到结构。
val = [1, 2, 3, 4, 5, 6]
print(list(map(lambda x: x * 2, val)))

#map(func, iterable1, iterable2)
#在传入多个可迭代对象的情况下，map()会依次从所有可迭代对象中依次取一个元素，组成一个元组列表，然后将元组依次传给func；
#若可迭代对象的长度不一致，则会以None进行补上。
a= list(eval(input('Input：')))
b= list(eval(input('Input：')))
plus = lambda x,y : x+y
print(list(map(plus,a,b)))

#reduce(func, iterable[, initializer])
#功能是对可迭代对象（iterable）中的元素从左到右进行累计运算，
#最终得到一个数值。第三个参数initializer是初始数值，可以空置，
#空置为None时就从可迭代对象（iterable）的第二个元素开始，并将第一个元素作为之前的结果。
from functools import reduce  #python3中reduce被移入functools中，所以需要导入
plus = lambda x,y : x+y
print(reduce(plus,[1,2,3,4,5],10))

#filter(func, iterable)
#将第二个参数（iterable）中的每一个元素分别传给第一个参数（func），依次执行函数得到结果；
#差异在于，filter()会判断每次执行结果的bool值，并只将bool值为False的筛选出来，组成一个新的列表并进行返回。
model2 = lambda x : x%2
print(list(filter(model2,[1,2,3,4,6,6,7,74,345])))
