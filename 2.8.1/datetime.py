# -*- coding: utf-8 -*-
# @Time    : 2020/3/21 8:48
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : datetime.py
# @Software: PyCharm

import datetime
from datetime import date
print(date.today())  #打印今天日期

from datetime import time
print(time(20,23,30))  #time(时，分，秒)

from datetime import datetime
dt = datetime.now()
print(dt)
print(dt.strftime('%a,%b %d %Y %H:%M'))   #%a简化的星期

dt1 = datetime(2020,6,6,9,11)  #各地时区有区别
print(dt1)
ts = dt1.timestamp()   #转换为时间戳，全世界计算机上时间戳统一
print(ts)
print(datetime.fromtimestamp(ts))  #将时间戳转换为当地时间