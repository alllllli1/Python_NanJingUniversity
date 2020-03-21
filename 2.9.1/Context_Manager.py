# -*- coding: utf-8 -*-
# @Time    : 2020/3/21 10:05
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : Context_Manager.py
# @Software: PyCharm

#用文件来输出异常
# try:
#     f = open('date.txt')
#     for line in f:
#         print(line,end=' ')
# except IOError:
#     print('cannot open the file !')
# finally:
#     f.close()

#with语句定义和控制代码块执行前的准备动作及执行后的收尾动作

with open('date.txt') as f:
    for line in f:
        print(line,end=' ')