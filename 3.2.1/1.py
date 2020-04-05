# -*- coding: utf-8 -*-
# @Time    : 2020/4/4 23:49
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : 1.py
# @Software: PyCharm

# https://physionet.org/physiobank/database/hbedb/BDS00001.dat

import requests
from bs4 import BeautifulSoup
import re
import os
import urllib


def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"


def getBat(html):
    reg = r'href=".*.bat"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    return imglist


if __name__ == "__main__":
    lst = []
    url = "https://physionet.org/physiobank/database/hbedb/"
    text = getHTMLText(url)
    soup = BeautifulSoup(text, "html.parser")
    files = soup.find_all('a')
    for i in files:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r'BDS.*.hea', href)[0])
        except:
            continue
    for l in lst:
        link = "https://physionet.org/physiobank/database/hbedb/" + l
        ff = requests.get(link)
        print(link + "正在下载")
        try:
            f = open('C:\\Users\\wscffaa\\Desktop\\NECCS' + str(l), 'wb')
            f.write(ff.content)
            f.close()
        except Exception as e:
            print("失败")