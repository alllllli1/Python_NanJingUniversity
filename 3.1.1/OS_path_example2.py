# -*- coding: utf-8 -*-
# @Time    : 2020/3/21 11:38
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : OS_path_example2.py
# @Software: PyCharm

import os
def countLines(fname):
    try:
        with open(fname) as f:
            data = f.readlines()
    except FileNotFoundError:
        print(fname + ' does not exist ! ')
    lens = len(data)
    print(fname.split('\\')[1] + ' has ' + str(lens) + ' Lines')

path = 'D://WorkSpace//python//Python_NanJingUniversity//3.1.1'
for fname in os.listdir(path):
    if fname.endswith('.txt'):
        file_path = os.path.join(path,fname)
        countLines(file_path)