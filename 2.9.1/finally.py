# -*- coding: utf-8 -*-
# @Time    : 2020/3/21 9:48
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : finally.py
# @Software: PyCharm

#finally子句： 无论异常发不发生，都会被执行
def finallyTest():
    try:
        x=int(input('Enter the first number :'))
        y=int(input('Enter the second number : '))
        print(x/y)
        return 1
    except Exception as err:
        print(err)
        return 0
    finally:
        print('It is a finally clause.')
result = finallyTest()
print(result)