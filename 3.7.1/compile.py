# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 16:43
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : compile.py
# @Software: PyCharm

#compile函数用于编译正则表达式，生成一个正则表达式pattern对象，供match和search’函数使用
# re.compile(pattern[,flags])
# pattern : 一个字符串形式的正则表达式
# flags 可选，表示匹配模式，比如忽略大小写，多行模式等，具体参数为：
# # re.I 忽略大小写
# # re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
# # re.M 多行模式
# # re.S 即为' . '并且包括换行符在内的任意字符（' . '不包括换行符）
# # re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
# # re.X 为了增加可读性，忽略空格和' # '后面的注释

import re
pattern = re.compile(r'\d+')  #用于匹配至少一个数字
m = pattern.match('one12three456',3,10) #从1开始查找，match函数只匹配字符串的开始
print(m)
n = pattern.search('one12three456')
print(n)