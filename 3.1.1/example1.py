# -*- coding: utf-8 -*-
# @Time    : 2020/3/21 11:06
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : example1.py
# @Software: PyCharm

#将1.txt文件中的字符串前加上序号1,2,3...后写到另一个文件2.txt中去

#思路：
   #readlines读取1.txt多行内容
   #使用for循环在前面添加序号，str(序号)转成字符串
   #使用writelines写入2.txt文件内

with open('1.txt') as f1:
    cNames = f1.readlines()
for i in range(0,len(cNames)):
    cNames[i] = str(i+1) + '.' + cNames[i]
with open('2.txt','w') as f2:
    f2.writelines(cNames)