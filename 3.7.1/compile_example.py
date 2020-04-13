
# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 21:00
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : compile_example.py
# @Software: PyCharm

import re
pattern = re.compile(r'([a-z]+) ([a-z]+)',re.I)  #re.I表示忽略大小写
m = pattern.match('Hello world Wide web')
print(m)
print(m.span())
print(m.group(0))
print(m.group(1))
print(m.group(2))

