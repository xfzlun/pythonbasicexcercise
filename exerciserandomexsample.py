# _*_ coding: utf-8 _*_
'''
#@Time  :2018-12-01;21:40
@author: aLuren

#@FileName: exerciserandomexsample.py
#@Software: PyCharm
Copyright(C)2018 SZ-MB-QTC
主旨：random函数的使用
'''
import random
x = random.random()
a = random.seed(x)  #seed的用法？？
h = random.randrange(0, 100, 3)
print(a)
print(x)
print(h)

'''
seed
shuffle
这两个函数还要查一下用法，比较模糊
如果要使用import random, 则要加上模块名的限定，但是如果使用from random import *, 则不用加上模块名的限定
'''




