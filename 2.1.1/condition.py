# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 19:48
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : condition.py
# @Software: PyCharm

        #if expression:
            #expr_ture_suite
        #else:
            #expr_false_suite

        #expression:
          #条件表达式：
                #成员运算符
                #比较运算符
                #逻辑运算符
         #expr_true_suite:
            #expression条件为true时执行的代码块
            #代码块必须缩进(通常为四个空格)
         #expr_false_suite:
               #expression条件为false时执行的代码
               #代码块必须缩进
               #else语句不缩进

sd1 = int(input("The first side:"))
sd2 = int(input("The second side: "))
if(sd1 == sd2):
    print("The square's area is",sd1*sd2)
else:
    print("the rectangle's area is",sd1*sd2)

        #if expression:
            #expr_true_suite
        #elif expression2:
            #expr2_true_suite
        #elif expressionn:
            #exprn_true_suite
        #else:
            #none_of_the_above_suite

k = int(input('input the index of shape:'))
if k == 1:
    print('circle')
elif k == 2:
    print('oval')
elif k == 3:
    print('rectangle')
elif k == 4:
    print('triangle')
else:
    print('you input the invalid number')

    #条件嵌套：同等缩进为同一条件结构

