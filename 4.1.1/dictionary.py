# -*- coding: utf-8 -*-
# @Time    : 2020/4/21 13:39
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : dictionary.py
# @Software: PyCharm

#什么是字典--一种映射类型，key-value对
#某公司人事部门让技术部门用Python构建一个简易的员工信息表包含员工的姓名和工资信息。根据信息表查询员工牛云的工资。
names = ['Wangdachui','Niuyun','Linling','Tianqi']
salaries = [3000,2000,4500,8000]
print(salaries[names.index('Niuyun')])

#插入知识点：元组、集合、字典、列表 格式区别
     #元组：包含零个或多个任意类型元素，且不可变。用（）定义
     #列表：包含零个或多个任意类型元素，可进行增删改操作，用[]定义
     #字典：每个元素拥有与之对应的不同的键，通过键值来访问，元素的顺序无关紧要，可变
     #集合：像只有键的字典一样，无需关注该元素是否存在，就用集合。

#创建字典
#法一 集合
aInfo = {'Wangdachui':3000,'Niuyun':2000,'Liulin':4500,'Tianqi':8000}
#法二 列表里面元素都是元组
info = [('Wangdachui',3000),('Niuyun',2000),('Linling',4500),('Tianqi',8000)]
bInfo = dict(info)
#法三 元组里面元素都是列表
cInfo = dict([['Wangdachui',3000],['Niuyun',2000],['Liuling',4500],['Tianqi',8000]])
#法四 一个元组，里面用的=来连接表示
dInfo = dict(wangdachui = 3000,Niuyun = 2000, Liuling = 4500, Tianqi = 8000)
print(aInfo,bInfo,cInfo,dInfo,sep='\n')

#创建员工信息表时如何将所有员工的工资默认值设置为3000？
aDict = {}.fromkeys(('Wangdachui','Niuyun','Liuling','Tianqi'),3000)
print(aDict)

#已知有姓名列表和工资列表，如何生成字典类型的员工信息表？
#zip()函数在Python2和Python3中的用法不同，Python3需要先用list函数将zip里面的内容转换后才能输出列表
print(list(zip(names,salaries)))

#对于几个公司的财经数据，如何构造公司代码和股票价格的字典？
#序列索引迭代思路，i是每个元素的索引
pList = [('AXP','American Express company','78.51'),('BA','The Boeing Company','184.76'),('CAT','Caterpillar Inc','96.39')]
aList = []
bList = []
for i in range(3):
    aStr = pList[i][0]
    bStr = pList[i][2]
    aList.append(aStr)
    bList.append(bStr)
Adict = dict(zip(aList,bList))
print(Adict)
#序列索引迭代思路：直接从序列本身去寻找item
Bdict = {}
for item in pList:
    Bdict[item[0]]=item[2]
print(Bdict)
