# -*- coding: utf-8 -*-
# @Time    : 2020/4/21 18:37
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : dictionary_rules.py
# @Software: PyCharm

#字典的基本操作
aInfo = {'Caifeifan':8888,'Maoyuwei':9999,'Gongzhe':8888,'Linjingcan':16666}
#键值查找
print(aInfo['Caifeifan'])
#更新
aInfo['Caifeifan']=9999
print(aInfo['Caifeifan'])
#添加
aInfo['Guochongye']=19999
aInfo['hanhan']=19999
print(aInfo)
#成员判断
print('Maofaf' in aInfo)
#删除字典成员
del aInfo['hanhan']
print(aInfo)

#字典的内建函数
#常用的内建函数有：dict(),len(),hash()
names=['Maoyuwei','Gongzhe','Lingjingcan','Guochongye','Caifeifan']
salaries=[42432,42342,42342,33543,6546,43141]
bInfo = dict(zip(names,salaries))
print(len(bInfo))
print(bInfo)
print(hash('Caifeifan')) #hash判断一个对象是否可哈希

#字典方法
#已知有员工姓名和工资信息表（Wangdachuil：3000，Niuyun'：2000，Linling：4500，"Tiangi：8000，如何单独输出员工姓名和工资金额？
print(bInfo.keys())  #输出所有键
print(bInfo.values()) #输出所有值
for k,v in bInfo.items():  #items()能把所有键和值组成元组返回
    print(k,v,sep=',')

#人事部门有两份人员和工资信息表，第一份是原有信息，第二份是公司中有工资更改人员和新进人员的信息，如何处理可以较快地获得完整的信息表？
bInfo.update(aInfo)  #update函数能同时更新并且添加新增元素到字典中
print(bInfo)

#字典的查找方法--dict.get()方法
print(bInfo.get('Caifeifan'))

#字典的删除方法--dict.clear（）
bInfo.clear()
print(bInfo)
