# -*- coding: utf-8 -*-
# @Time    : 2020/3/21 10:59
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : f_read.py
# @Software: PyCharm

#file_obj.read(size)
   #从文件中至多读出size字节数据，返回一个字符串
#file_obj.read()
   #读文件知道文件结束，返回一个字符串

#同样使用with语句
with open('firstpro.txt') as f:
    p1 = f.read(5)  #读取前五个
    p2 = f.read()   #读取剩余的字符
print(p1,p2)        #读完后会自动关闭文件，所以不需要f.close()来关闭文件

#file_obj.readlines()    读取多行数据
#file_obj.readline()     读取单行数据
#file_obj.writelines()   写入多行数据

#读取多行数据
with open('firstpro.txt') as f:
    cNames = f.readlines()
print(cNames)


