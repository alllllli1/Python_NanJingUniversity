# -*- coding: utf-8 -*-
# @Time    : 2020/4/4 23:06
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : example_NECCS.py
# @Software: PyCharm


import requests
from bs4 import BeautifulSoup
import re


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
    url = "https://gw.qfnu.edu.cn/info/1096/1637.htm"
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
        link = "https://gw.qfnu.edu.cn" + l
        ff = requests.get(link)
        print(link + "正在下载")
        try:
            f = open('C:\\Users\\wscffaa\\Desktop\\NECCS' + str(l), 'wb')
            f.write(ff.content)
            f.close()
        except Exception as e:
            print("失败")

# #导入requests和BeautifulSoup库
# import requests
# from bs4 import BeautifulSoup
#
# url = "https://gw.qfnu.edu.cn/info/1096/1637.htm"
# #获取所有网页信息
# response = requests.get(url)
# #利用.text方法提取响应的文本信息
# r=requests.get(url)
# html = r.text
# soup =BeautifulSoup(html,'html.parser')
# #解析出下载链接，find_all（）函数返回的是tag的列表
# files = soup.find_all('a',class_='href')
# #下载链接
# links = "https://gw.qfnu.edu.cn"+files
# ff = requests.get(links)
# f = open('C:\\Users\\wscffaa\\Desktop\\NECCS')
# f.write(ff.content)
# f.close()
