# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 15:08
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : HelloWorld.py
# @Software: PyCharm

myString = "HelloWorld"
print(myString)
price = int(input('input the stock price of Apple :'))
print("苹果的价格是：" + str(price))



# 输出使用print函数
# print(变量)
# print(字符串)
# 输入采用的是input函数
# 但是input返回值时字符类型，要是想要其他字符串类型，就可以在前面加上int、eval等

#Python无法判断24是数值24还是字符2和4。
#因此在字符串中使用整数时，需要显式地指出希望将这个整数用作字符串。
#因此，可以调用str()

#续行在句子后面加上\即可
#意思不变，续行好看一点，小括号，中括号，三引号无需续行，自带跨行书写功能

#缩进是最重要的：
     # 相同的缩进表示同级别的语句块
     # 减少缩进表示语句块的退出
     # 增加缩进表示语句块的开始