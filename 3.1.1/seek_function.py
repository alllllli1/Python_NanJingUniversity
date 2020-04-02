# -*- coding: utf-8 -*-
# @Time    : 2020/3/21 11:13
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : seek_function.py
# @Software: PyCharm

#file_obj.seek(offset,whence=0)
   #在文件中移动文件指针，从whence(0表示文件头部，
   #1表示当前位置，2表示文件尾部)偏移offset个字节
   #whence参数可选，默认值为0

s = 'Tencent Technology Company Limited'
with open('1.txt','a+') as f:
    f.writelines('\n')
    f.writelines(s)
    f.seek(0,0)
    cNames = f.readlines()
print(cNames)

#标准文件
  #当程序启动后，以下三种标准文件有效
    #stdio 标准输入
    #stdout 标准输出
    #stderr 标准错误
  #print其实就是标准输出函数，属于sys系统模块一部分
  #import sys
  #sys.stdout.write('Hello')