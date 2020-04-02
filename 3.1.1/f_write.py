# -*- coding: utf-8 -*-
# @Time    : 2020/3/21 10:52
# @Author  : wscffaa
# @Email   : 1294714904@qq.com
# @File    : f_write.py
# @Software: PyCharm

#file_obj.write(str)
  #将一个字符串写入文件
        # f = open('firstpro.txt','w')
        # f.write('真TM烦死了啊！！！')
        # f.close()
  #上面的写法不推荐，文件的读写适合使用with语句
  #因为with语句可以进行文件异常处理，更加简洁且有效
with open('firstpro.txt','w') as f:
    f.write('你就不知道我在想什么叭')
