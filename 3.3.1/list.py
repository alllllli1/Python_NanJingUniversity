# -*- coding: utf-8 -*-
# @Time    : 2020/4/4 21:49
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : list.py
# @Software: PyCharm

#常见的四类序列
  #字符串序列：  aStr = 'Hello World'      单引号表示
  #列表：       aList= [2,1,23,4,5]       中括号表示
  #元组：      aTuple= ('Sunday','happy') 元括号表示
  #由元组构成的列表：[('AXP','American Express Company','78.51'),
#                  ('BA','The Boeing Company','184.76'),
#                  ('CVX','Chevron Corporation','106.09')]

# 序列： 字符串、列表、元组

# 序列：访问模式--元素从0开始下表偏移量访问，从0到n-1 或者 从 -1 到 -N
#      一次可访问一个或多个元素(切片)

#序列相关操作：
    #1.标准类型运算符
      #值比较  < > <= >= == !=
      #对象身份比较  is |  is not
      #布尔运算  not and or
    #2.序列类型运算符
      #获取
      #重复
      #连接
      #判断
    #3.内建函数
      #序列类型转换内建函数  list()  str() tuple()
      #序列类型可用内建函数

#2,序列类型运算符例题
# 1、x in s 如果x是序列s的元素，返回Ture，否则返回False
# 2、x not in s 如果x是序列s的元素,返回False,否则返回Ture
# 3、s + t 连接两个序列s和t
# 4、s* n或n* s 将序列s复制n次
# 5、s[i] 索引，返回s中的第i个元素，i是序列的序号
# 6、s[i:j]或s[i:j:k]切片，返回序列s中第i到j以k为步长的元素子序列

#3.其他常用函数和方法
# 1、len(s) 返回序列s的长度
# 2、min(s) 返回序列s的最小元素，s中元素需要可比较
# 3、max(s) 返回序列s的最大元素，s中元素需要可比较
# 4、s.index(x)或s.index(x,i,j) 返回序列s从i开始到j位置中第一次出现元素x的位置
# 5、s.count(x) 返回序列s中出现x的总次数
# 6、zip() 将元素打包成一个元组
# 7、sorted() 讲序列里面的元素从小到大排列

# 函数                     含义
#
# list(iter)              把可迭代对象转换为列表
# str(obj)              把obj 对象转换成字符串(对象的字符串表示法)
# unicode(obj)    把对象转换成Unicode 字符串(使用默认编码)
# basestring()     抽象工厂函数,其作用仅仅是为str 和unicode 函数提供父类，所以不能被实例化，也不能被调用(详见第6.2 节)
# tuple(iter)          把一个可迭代对象转换成一个元组对象
#
#
#
# 序列类型可用的内建函数
#
# 函数名                                                 功能
# enumerate(iter)                            接受一个可迭代对象作为参数，返回一个enumerate 对象(同时也是一个迭代器),该对象生成由iter 每                                                          个enumerate(iter) a 接受一个可迭代对象作为参数，返回一个enumerate 对象(同时也是一个迭代器),                                                          该对象生成由iter 每个元素的index 值和item 值组成的元组(PEP 279)
# len(seq)                                         返回seq 的长度
# max(iter,key=None) or
# max(arg0,arg1...,key=None)        返回iter 或(arg0,arg1,...)中的最大值，如果指定了key,这个key 必须是一个可以传给sort()方法的,用于                                                          比较的回调函数.
# min(iter, key=None) or
# min(arg0, arg1.... key=None)        返回iter 里面的最小值;或者返回(arg0,arg2,...)里面素的index 值和item 值组成的元组(PEP 279)
#                                                          的最小值;如果指定了key,这个key 必须是一个可以传给sort()方法的,用于比较的回调函数.
#
# reversed(seq)                                  接受一个序列作为参数,返回一个以逆序访问的迭代器(PEP 322)
#
#
# sorted(iter,func=None,key=None,  接受一个可迭代对象作为参数，返回一个有序的列表;可选参数
#
# reverse=False)                                  func,key 和reverse 的含义跟list.sort()内建函数的参数含义一 样.
#                                                                                    
# sum(seq, init=0)                              返回seq 和可选参数init 的总和, 其效果等同于reduce(operator.add,seq,init)
# zip([it0, it1,... itN])                            返回一个列表，其第一个元素是it0,it1,...这些元素的第一个元素组成的一个元组，第二个...,类推.



month = ['January','February','March','April','May','June','July','Aguest','September','October','November','December']
print(month[1],'\n',month[-5],'\n',month[1:8],'\n',month[:6],'\n',month[::-1])
print('apple'*3)
print('pine'+'apple')
print('BA' in ('BA','The Boeing Company','122.64'))