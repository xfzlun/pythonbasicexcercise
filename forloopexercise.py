# _*_ coding: utf-8 _*_
'''
@Time:2018-11-30;22:38
@author: aLuren
@FileName: forloopexercise.py
@SoftWare:PyCharm
COPYRIGHT(C)2018 SZ-MB-QTC
'''
a = [11, 22, 33, 44 ]
for i in range(len(a)):
    print('第', i, '个元素为：', a[i])

for i in range(0, len(a), 2):
    print('第', i, '个元素为：', a[i])

for i in range(len(a)-1,-1,-1):  #len(a)是4,不存在，所以减1位，0:右边是开区间，所以取不到0 为什么开区间取不到0
    print('第', i, '个元素为：', a[i])
