# -*- coding: utf-8 -*-
# @Time    : 2020/4/4 13:38
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : Example_KuGou.py
# @Software: PyCharm

#shift+table 反向缩进


#导入requests和BeautifulSoup库
import requests
from bs4 import BeautifulSoup

url = "https://www.kugou.com/yy/rank/home/1-8888.html?from=rank"
#获取所有网页信息
response = requests.get(url)
#利用.text方法提取响应的文本信息
r=requests.get(url)
html = r.text
soup =BeautifulSoup(html,'html.parser')
#解析出歌名，find_all（）函数返回的是tag的列表
names = soup.find_all('a',class_='pc_temp_songname')
# 打印names
print(names)
for name in names:
    #利用split方法把歌手和曲目分隔返回成列表形式赋值给item
    item = name.get_text().split('-')
    #q巧妙利用数组格式化依次输出曲名和歌手
    print("曲名:{}  歌手:{} ".format(item[1],item[0]))