# -*- coding: utf-8 -*-
# @Time    : 2020/4/22 21:50
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : set.py
# @Software: PyCharm

#集合（set）是一个无序的不重复元素序列。
#可变集合set 和 不可变集合frozenset
#可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

#人事部门的一份工资信息表登记时由于工作人员的疏忽有部分姓名重复登记了，如何快速解决这个问题？
#set（）能自动去掉重复元素
names = ['Caifeifan','Maoyuwei','Caifeifan','Gongzhe']
namesset = set(names)
print(namesset)

#集合比较 in | not in
aSet = set('Caifeifan')
print('C' in aSet)  #属于
bSet = set('Maoyuwei')
print('M' not in bSet)  #不属于
print(aSet == bSet)  #是否相等
print(aSet < bSet)   #<表示包含右边包含左边  <= 表示包含或者相等
print(aSet > bSet)   #>表示左边包含右边  >= 表示包含或者相等
print(aSet & bSet)   #& 表示 交集
print(aSet | bSet)   #| 表示 并集
print(aSet - bSet)   #- 表示 差 属于aset不属于bset
print(aSet ^ bSet)   #^ 表示 不同时属于两个集合的元素
aSet -= set('aien')
print(aSet)                     #运算符可复合 &= |= -= ^=