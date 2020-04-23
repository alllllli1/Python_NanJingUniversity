
# -*- coding: utf-8 -*-
# @Time    : 2020/4/23 9:21
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : scipy.py
# @Software: PyCharm

#简单介绍SciPy

#scipy:基于Python、开源的、为数学科学和工程服务的软件生态系统
#scipy:numpy、sciPy library、Matplotlab、IPython、Sympy、pandas
#网址：https://scipy.org/
#SciPy中的数据结构
    #ndarray（N维数组）
    #Series（变长字典）
    #DataFrame（数据框）

#NumPy
   #https://numpy.org/
   #NumPy(Numerical Python) 是 Python 语言的一个扩展程序库，支持大量的维度数组与矩阵运算，此外也针对数组运算提供大量的数学函数库。
   #NumPy 是一个运行速度非常快的数学库，主要用于数组计算，包含：
        # 一个强大的N维数组对象 ndarray
        # 广播功能函数
        # 整合 C/C++/Fortran 代码的工具
        # 线性代数、傅里叶变换、随机数生成等功能

import numpy as np
aArray = np.ones((3,4))
print(aArray)

#SciPy核心库
   #Python中科学计算程序的核心包
   #有效计算numpy阵，让NumPy和SciPy协同工作
   #致力于科学计算中常见问题的各个工具箱，其不同子模块有不同的应用，如插值、积分、优化和图像处理等

# >>> from scipy import linalg
# >>> a = np.array([[1,2,3], [4,5,6], [7,8,9]])
# >>> linalg.det(a)
# 0.0
# >>> a = np.array([[0,2,3], [4,5,6], [7,8,9]])
# >>> linalg.det(a)
# 3.0

#Matplotlib
    # https://matplotlib.org/
    # 特征:
    # 基于NumPy
    # 二维绘图库，简单快速地生成曲线图、直方图和散点图等形式的图
    # 常用的pyplot是一个简单提供类似MATLAB接口的模块

#pandas
    #https://pandas.pydata.org/
    #基于SciPy和NumPy
    # 高效的Series和DataFrame数据结构
    # 强大的可扩展数据操作与分析的Python库
    # 高效处理大数据集的切片等功能
    # 提供优化库功能读写多种文件格式，如CSV，HDF5