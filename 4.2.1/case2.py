# -*- coding: utf-8 -*-
# @Time    : 2020/4/22 21:06
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : case2.py
# @Software: PyCharm

#搜索引擎关键词查询
import requests
kw = {'q':'python dict'}
r = requests.get('http://cn.bing.com/search',params=kw)
print(r.url)
print(r.text)
