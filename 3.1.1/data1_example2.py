# -*- coding: utf-8 -*-
# @Time    : 2020/3/21 11:31
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : data1_example2.py
# @Software: PyCharm

#假如存在多个文件
    #首先定义countLines函数读取一个文件
    #然后定义一个列表
    #for循环遍历列表即可

def countLines(fname):
    try:
        with open(fname) as f:
            data = f.readlines()
    except FileNotFoundError:
        print(fname+ 'does not exist')
    lens = len(data)
    print(fname +' has ' + str(lens) + ' lines')

files = ['1.txt','2.txt','firstpro.txt','data1.txt']  #相对路径
for fname in files:
    countLines(fname)
