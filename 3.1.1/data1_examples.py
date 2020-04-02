# -*- coding: utf-8 -*-
# @Time    : 2020/3/21 11:25
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : data1_examples.py
# @Software: PyCharm

#统计date1有多少行数据
#思路：
    #先readlines（）读取多行数据
    #str(lens)表示行数
    #try_except 捕获异常

file_name = 'data1.txt'
try:
    with open(file_name) as f:
        data = f.readlines()
except FileNotFoundError:
    print(file_name + 'Does not exist')
lens = len(data)
print('date1.txt' + ' has ' + str(lens) + ' lines')

