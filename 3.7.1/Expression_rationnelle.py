# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 15:37
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : Expression_rationnelle.py
# @Software: PyCharm

# 正则表达式：用来检查一个字符串是否与某种模式匹配

#  re.match(pattern,string,flags)  #(匹配的正则表达式，要匹配的字符串，标志位--用于控制正则表达式的匹配方法，如区分大小写，多行匹配等)
#  匹配成功re.match就返回一个匹配的对象，否则返回None
#  group(num)和groups()能匹配对象函数来获取匹配表达式
#  group(num=0) 匹配的整个表达式的字符串，group()可以一次输入多个组号，将返回一个包含那些组对应值的元组
#  groups() 返回一个包含所有小组字符串的元组，从1到所含的小组号

import re
line = "CaiFeiFan is smarter than MaoYuWei"
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
matchObj = re.match(r'(.*) is (.*?) .*',line,re.M|re.I)
if matchObj:
    print("matchObj.group():",matchObj.group())
    print("matchObj.group(1):", matchObj.group(1))
    print("matchObj.group(2):", matchObj.group(2))
else:
    print("No match!")

#  re.search(pattern,string,flags=0) （匹配的正则表达式，要匹配的字符串，标志位--用于控制正则表达式的匹配方法，如区分大小写，多行匹配等）
#  匹配成功re.search就返回一个匹配的对象，否则返回Nonev
searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)

if searchObj:
    print("searchObj.group() : ", searchObj.group())
    print("searchObj.group(1) : ", searchObj.group(1))
    print("searchObj.group(2) : ", searchObj.group(2))
else:
    print("Nothing found!!")




