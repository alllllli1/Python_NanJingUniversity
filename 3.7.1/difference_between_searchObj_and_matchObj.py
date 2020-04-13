# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 16:11
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : difference_between_searchObj_and_matchObj.py
# @Software: PyCharm

#re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None
#re.search匹配整个字符串，直到找到一个匹配项为止
import re

line = "Cats are smarter than dogs"

matchObj = re.match(r'dogs',line,re.M|re.I)
if matchObj != None:
    print("match --> matchObj.group():",matchObj.group())
elif matchObj == None:
    searchObj = re.search(r'dogs',line,re.M|re.I)
    print("search --> searchObj.group():",searchObj.group())
else:
    print("No match!!")

