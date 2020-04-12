# -*- coding: utf-8 -*-
# @Time    : 2020/4/12 16:40
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : Character_String.py
# @Software: PyCharm

#字符串是Python中最常用的数据类型
#通常通过单引号或者双引号来创建字符串
#我们只需要给变量分配一个值即可创建字符串

var1 = 'hello world'
var2 = "Python Runnob"
print(var1)
print(var2)

#Python访问字符串中的值
#Python访问子字符串，可以使用方括号来截取字符串

print("var1[0]: ",var1[0])
print("var2[1:5]",var2[1:5])
print("var2[3:8]",var2[3:8])

#Python字符串连接
#我们可以通过字符串进行截取并与其它字符串进行连接

#Python转义字符Escape Character --ESC
print("输出：",var1[0:5] + " " + var2[0:6])
print(var1[0:5]+"\n"+var2[0:6])

#Python字符串运算符
print((var2[0:6]+" ")*2 + "\n" + (var1[0:5]+" ")*3)
print((var2[0:6]+" ")*2 + r'\n ' + (var1[0:5]+" ")*3)  #加个r表示只代表普通字符串
print("H" in var1)
print("P" not in var2)

#Python字符串格式化
#基本用法：将一个值插入到一个由字符串格式符%s的自复仇那种
print("%s is my lover forever and she is %d kg now !"% ('MaoYuWei',54))
print("%s is my lover forever and she is %o kg now !"% ('MaoYuWei',44)) #8进制数转换为10进制数
print("%s is my lover forever and she is %X kg now !"% ('MaoYuWei',84))  #十六进制数转换为10进制数
print("%s is my lover forever and she is %e kg now !"% ('MaoYuWei',54.0232))

#Python三引号
#三引号可以将复杂的字符串进行赋值，三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符
#语法表示：一对连续的单引号或者双引号
#主要作用：三引号让程序员从引号和特殊字符串的泥潭里面解脱出来，自始至终保持一小块字符串的格式是所谓的WYSIWYG（所见即所得）格式的。
hi ='''i 
love you'''
print(hi)

#Unicode 字符串
#Python 中定义一个 Unicode 字符串和定义一个普通字符串一样简单：
w = u'HelloWorld!'
w1 = u'Hello\u0020World!'  #被替换的 \u0020 标识表示在给定位置插入编码值为 0x0020 的 Unicode 字符（空格符）
print(w+w1)

#Python的字符串内建函数

print(var1.count("o"))     #统计出现次数
print(var1.capitalize())  #首字母大写
print(var1.center(10))    #返回指定宽度的字符串
print(var1.encode(encoding='UTF-8',errors='stict'))