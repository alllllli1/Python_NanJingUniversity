# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 18:51
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : function.py
# @Software: PyCharm

#函数可以看成类似于数学中的函数，也是完成一个特定功能的一段代码
#比如绝对值函数abs(x)、类型函数type(x)、四舍五入函数round(x)
#Python有四类函数
  #第一类：内建函数、内嵌函数---可以直接使用
    #str()、type()等使用与所有标准类型
    #数值型内建函数；abs/bool/oct/round/int/float/chr/complex等
    #实用函数：dir/help/len/open/range/input等
  #第二类：标准库函数：Python标准支持的函数，只需要将模块导入
  #第三类：第三方库，需要先安装库，然后再导入模块，最后使用
  #第四类：用户激励函数--按照一定的语法规则，由用户自行定义

#模块--供非内建函数使用
  #一个完整的Python文件就是一个模块
    #文件：物理上的组织方式 math.py
    #模块: 逻辑上的组织方式 math
  #Python通常用"import 模块"的方式将现成模块中的函数，类等重用到其他代码块中
  #模块里面可以导入指定的模块属性，也就是把指定名称导入到当前作用域
  #from Module1 import ModuleElement

#包--一个有层次的文件目录结构
  #定义了一个由模块和子包组成的Python应用程序执行环境

#常用导入方式
  #from AAA.CCC.c1 import func1
  #fun1(123)

#库：一组具有相关功能的模块的集合
  #Python的一大特色就是具有强大的标准库、以及第三方库、以及自定义模块