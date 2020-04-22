# -*- coding: utf-8 -*-
# @Time    : 2020/4/22 22:07
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : all_set_rules.py
# @Software: PyCharm

#集合内置函数--面向可变集合和不可变集合
aSet = set(['Caifeifan','Maoyuwei','Caifeifan','Gongzhe'])
bSet = set(['mmmmx','Maoyuwei','Caifeifan','Gongzhe'])
print(aSet.issubset(bSet))    #	判断指定集合bSet是否为该方法参数集合aSet的子集。
print(aSet.issuperset(bSet))  # 判断该方法aSet的参数集合是否为指定集合bSet的子集
print(aSet.union(bSet))       # 返回两个集合的并集
print(aSet.intersection(bSet))# 返回集合的交集
print(aSet.difference(bSet))  # 返回多个集合的差集
print(aSet.symmetric_difference(bSet)) #	返回两个集合中不重复的元素集合。
cSet = aSet.copy()            #	拷贝一个集合
print(cSet)