# -*- coding: utf-8 -*-
# @Time    : 2020/4/21 21:02
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : cases_dictionary.py
# @Software: PyCharm

#字典相关使用小案例
#JSON格式
    #javaScirpt Object Notation, JS 对象标记
    #一种轻量级的数据交换格式
    #json格式采用key:value的方式记录数据

#dumps：将python中的 字典 转换为 字符串 .因为如果直接将dict类型的数据写入json文件中会发生报错，因此在将数据写入时需要用到该函数。
#loads: 将 字符串 转换为 字典
#dump: 将数据写入json文件中
#load:把文件打开，并把字符串变换为数据类型

import json
x = {"name":"Maoyuwei","sex":"girl","age":"twenty-three","habit":"eat","address":{"city":"Shanghai","university":"SHU"}}
y = x['address']['university']
z = json.dumps(x)  #  json.dumps()用于将dict类型的数据转成str
m = json.loads(z)  #    json.loads()用于将str类型的数据转成dict。
print(m)
print(z)
print(y)

#打开文件
with open("D:/WorkSpace/python/Python_NanJingUniversity/4.2.1/test.json") as load_f:
    load_dict = json.load(load_f)
    print(load_dict)
