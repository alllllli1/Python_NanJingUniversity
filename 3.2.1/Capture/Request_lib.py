# -*- coding: utf-8 -*-
# @Time    : 2020/4/2 15:30
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : Request_lib.py
# @Software: PyCharm

#Requests库是更简单、方便和人性化的Python HTTP第三方库

#基本方法：
   #request.get()   请求获取指定URL位置的资源，对应HTTP协议的GET方法

#豆瓣爬虫协议网站： https://www.douban.com/robots.txt
#Requests官网：https://requests.readthedocs.io/en/master/

import requests
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码
url = 'http://money.cnn.com/data/dow30/'
r = requests.get(url)
# print(r.text)

url1 = 'https://movie.douban.com/subject/26861685/comments'
r1 = requests.get(url1)
print(r.status_code)
print(r.text)