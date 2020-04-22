# -*- coding: utf-8 -*-
# @Time    : 2020/4/22 22:07
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : variable_set_rules.py
# @Software: PyCharm

#函数内置方法--面向可变集合
aSet = set(['Caifeifan','Maoyuwei','Caifeifan','Gongzhe'])
bSet = set(['mmmmx','Maoyuwei','Caifeifan','Gongzhe'])
aSet.add('Hanhan')  #添加元素
print(aSet)
aSet.remove('Hanhan') #删除元素
print(aSet)
aSet.update('Pig') # 给集合添加元素
print(aSet)
aSet.intersection_update(bSet) # 返回集合的交集
print(aSet)
aSet.discard('Pig') #删除指定元素
print(aSet)
bSet.difference_update(aSet) #移除集合中的元素，该元素在指定的集合也存在
print(bSet)
aSet.symmetric_difference_update(bSet) 	#移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
print(aSet)
print(aSet.pop()) #	随机移除元素
print(bSet.clear()) # 移除集合中的所有元素