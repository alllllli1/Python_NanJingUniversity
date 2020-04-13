# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 21:07
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : compile_findall_function.py
# @Software: PyCharm

#re,findall(string[, pos[,endpos]])
# string   待匹配的字符串。
# pos      可选参数，指定字符串的起始位置，默认为 0。
# endpos   可选参数，指定字符串的结束位置，默认为字符串的长度。

import re

pattern = re.compile(r'\d+')  #查找数字
result1 = pattern.findall('runnoob 124 google 234')
reuslt2 = pattern.findall('run88noobgoogle456',0,20)

print(result1)
print(reuslt2)

#re.finditer 在字符串中找到正则表达式所匹配的所有子串，并把他们作为一个迭代器返回
#re.finditer(pattern,string,flags=0)
# pattern	匹配的正则表达式
# string	要匹配的字符串。
# flags  	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。参见：正则表达式修饰符 - 可选标志

it = re.finditer(r"\d+","12a232fa3413")
for match in it:
    print(match.group())


#re.split 能够按照匹配的子串将字符串分割后返回列表，他的使用形式如下：
#re.split(pattern,string[,maxsplit=0.flags=0])
# pattern	匹配的正则表达式
# string	要匹配的字符串。
# maxsplit	分隔次数，maxsplit=1 分隔一次，默认为 0，不限制次数。
# flags	    标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。参见：正则表达式修饰符 - 可选标志
abc=re.split('\W+','runnov,python,google.')
print(abc)
