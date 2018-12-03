# _*_ coding: utf-8 _*_
'''
#@Time  :2018-12-01;21:15
@author: aLuren

#@FileName: numberexercise.py
#@Software: PyCharm
Copyright(C)2018 SZ-MB-QTC
题目：某一直角三角形，直角边为7和12，求这一直角三角形的斜边，以及以这条斜边为直径的圆面积
'''

from math import *
a = 7
b = 12
d = sqrt(pow(a, 2)+pow(b, 2))
print(d)  #d=直角三角形的斜边

c = pi * pow((d/2), 2)
print(c)  #c=圆面积

#为什么import math不能用？一定要用from math import *

