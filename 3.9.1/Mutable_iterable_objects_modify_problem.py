# -*- coding: utf-8 -*-
# @Time    : 2020/4/20 14:33
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : Mutable_iterable_objects_modify_problem.py
# @Software: PyCharm

#可变可迭代对象修改问题
#Python中有浅拷贝和深拷贝
#浅拷贝只复制父对象(一级元素)，深拷贝复制内部子对象
#x和y都属于同一片内存空间，所以使用深拷贝，修改y会对x产生影响

# x = [1, 2, 3, 4, 5]
# y = x   #深拷贝
# y[0] = 4
# print(x)

# x = [1, 2, 3, 4, 5]
# z = x[:]  #浅拷贝，并不改变x内部的值
# z[0] = 4
# print(x)

x = [1, 2,[ 3, 4] ]
y = x[:]  #或者y = x.copy()
y[0], y[2][0]= 6, 6
print(x)#一级元素没有变化，而二级元素被修改了
#浅拷贝只复制了父对象（一级元素），而不复制内部子对象
#若想都复制，即都不改变，可用y = copy.deepcopy(x)



