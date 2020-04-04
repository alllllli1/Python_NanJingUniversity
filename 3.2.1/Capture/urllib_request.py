# -*- coding: utf-8 -*-
# @Time    : 2020/4/4 12:21
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : urllib_request.py
# @Software: PyCharm

import requests
import io
import sys
import urllib.request
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码
res=urllib.request.urlopen('http://www.baidu.com')
htmlBytes=res.read()
print(htmlBytes.decode('utf-8'))