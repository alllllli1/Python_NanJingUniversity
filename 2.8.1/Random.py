# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 19:54
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : Random.py
# @Software: PyCharm

import random

a = [1,2,3,4,5]

print(random.choice(a))  #从序列a中抽取一个随机值

print(random.randint(1,100)) #随机生成一个1~100的一个值

print(random.randrange(0,10,2))
#random.randrange ([start,] stop [,step])
#randrange() 方法返回指定递增基数集合中的一个随机数，基数默认值为1。

print(random.random())   #随机生成[0,1.0)之间的一个浮点数

print(random.uniform(5,10)) #随机生成[5,10)之间的一个浮点数

print(random.sample(range(100),10)) #随机从[0,100）内抽取10个数

nums = [1001,1003,1002,1004,1005]
random.shuffle(nums)
print(nums)  #将序列nums打乱，生成随机新序列


