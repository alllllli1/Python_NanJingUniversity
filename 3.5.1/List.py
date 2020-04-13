# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 9:00
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : List.py
# @Software: PyCharm

#序列：python中最基本的数据结构。序列中的每个元素都会分配一个数字--它的位置or索引，从0开始递加
#基本操作：索引、切片、加、乘、检查成员
#列表：最常用的Python数据类型，通过逗号分隔不同数据并使用方括号括起来即可。
list1 = ['Google','MaoYuWei','CaiFeifan',1997,1998]
list2 = [1,2,3,4,5]
list3 = ["a","b","c","d"]

#访问列表中的值
print("list1的第一个序列：",list1[0])
print("list2[0:5]:",list2[0:5])

#更新列表，通过append()方法来添加列表项--列表末尾
list1[0] = 'Python'
list1.append(2020)
print(list1)

#删除列表元素 --del语句
del list1[5]
print(list1)

#Python列表脚本操作符
# Python 表达式	                                 结果	             描述
# len([1, 2, 3])	                              3	                 长度
# [1, 2, 3] + [4, 5, 6]	                  [1, 2, 3, 4, 5, 6]	     组合
# ['Hi!'] * 4	                   ['Hi!', 'Hi!', 'Hi!', 'Hi!']      重复
# 3 in [1, 2, 3]	                            True	           元素是否存在于列表中
# for x in [1, 2, 3]: print(x, end=" ")      	1 2 3	             迭代

#Python列表截取与拼接
L=['Google', 'Runoob', 'Taobao']
# Python表达式	    结果	                描述
# L[2]	         'Taobao'	         读取第三个元素
# L[-2]	         'Runoob'	         从右侧开始读取倒数第二个元素: count from the right
# L[1:]	    ['Runoob', 'Taobao']	 输出从第二个元素开始后的所有元素
L += list1
print(L)

#嵌套列表
M = [L,list1,list2,list3]
print(M[0])
print(M[1])

#Python列表函数和方法
print(len(M))  #列表元素个数
print(max(list2))  #返回列表元素最大值，只支持数字
print(min(list2))  #返回列表元素最小值
#list(seq)  将元组转换为列表

list2.append(6)  #列表末尾添加新的对象
list2.extend(list1)  #在列表末尾扩展另外一个列表中的元素
print(list2.count(0))   #统计某个元素在列表中出现的次数
print(list2)
print(list2.index(3))  #找出某个值的第一个匹配项的值
list2.insert(0,2020)  #在列表中某个位置插入一个值
print(list2)
list2.pop(0)  #移除index=0处的值
print(list2)
list2.reverse()  #反向列表中的元素
print(list2)
list4=list2.copy() #列表复制
print(list4)
list4.clear()  #清空列表
print(list4)
#list2.sort(key=None,reverse=False) #对原列表进行排序
