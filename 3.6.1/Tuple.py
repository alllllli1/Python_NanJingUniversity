# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 9:38
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : Tuple.py
# @Software: PyCharm

#元组：和列表list类似，不同之处在于元组的元素不能修改
#元组使用小括号表示，用逗号隔开即可

tup0 = (2020)   #不加逗号，类型为整型
print(type(tup0))
tup1 = (2020,)  #加逗号，类型为元组Tuple
print(type(tup1))

#元组和字符串类似，下表索引从0开始，可以进行截取和组合等
tup2 = ('MaoYuWei','CaiFeiFan','Python',1997,1998)
tup3 = (1,2,3,4,5,6,7)
print(tup2[0])
print(tup3[0:])

#元组内元素无法修改，但是可以进行连接组合
tup4 = tup2 + tup3
print(tup4)

#元组内的元素无法删除，只能通过del语句删除整个元组
del tup4
#     print(tup4)
# NameError: name 'tup4' is not defined

#元组运算符与字符串一样，有+ * in len 迭代等
print(len(tup3))
print(tup3 * 2 + tup2 * 2)
print(1 in tup3)
for x in tup3:     #迭代
    print(x,)

#元组不可变性：元组所指向的内存中的内容不可变

#Python元组截取与拼接
L=['Google', 'Runoob', 'Taobao']
# Python表达式	    结果	                描述
# L[2]	         'Taobao'	         读取第三个元素
# L[-2]	         'Runoob'	         从右侧开始读取倒数第二个元素: count from the right
# L[1:]	    ['Runoob', 'Taobao']	 输出从第二个元素开始后的所有元素

tup5 = tuple(L)   #将列表转化为元组
print(type(tup5))