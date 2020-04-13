# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 16:25
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : replace.py
# @Software: PyCharm

# re.sub(pattern,repl,string,count=0,flags=0)
# pattern : 正则中的模式字符串。
# repl : 替换的字符串，也可为一个函数，可以进行加乘等运算
# string : 要被查找替换的原始字符串。
# count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
# flags : 编译时用的匹配模式，数字形式。

import re
phone = "191-2169-9850  #上海的电话"

num = re.sub(r'#.*$',"",phone)
print("去掉注释后的电话号码：",num)

num = re.sub(r'\D',"",phone)
print("去掉非数字内容后的电话号码：",num)

def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)
s = 'A23GGKG3534888GSAE'
print(re.sub(r'(?P<value>\d+)',double,s)) #\d	匹配任意数字，等价于 [0-9]。