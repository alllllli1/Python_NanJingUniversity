# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 18:14
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : operation.py
# @Software: PyCharm

#算数运算符的优先级： 乘方** 、 正负号 +—、 乘除 */ 、 整除 // 、 取余 %、 加减 +-

#数值的比较： 按值比大小
#字符串你的比较：按ASCII码值比大小

3<4<7  #same as 3<4 and 4 < 7

4>3==3 # 4 > 3 and 3 == 3

#逻辑运算符优先级：not、and、or

#原始字符串操作符(r/R):用于一些不希望转义字符起作用的地方
f=open(r'c:\python\test.py','W')
f=open('C:\\python\\test.py','W')  #两个等价的

#算数运算符、位运算符、比较运算符、逻辑运算符
#优先级逐渐递减

#3<<5 = 3*2^5 = 96
#1<<1 = 1*2^1 = 2
#4>>1 = 4 / 2^1 = 2
#16 >> 2 = 16 / 2^2 = 4