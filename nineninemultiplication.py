# _*_ coding: utf-8 _*_
'''
@Time:2018-12-04;22:45
@author: aLuren
@FileName: nineninemultiplication.py
@SoftWare:PyCharm
COPYRIGHT(C)2018 SZ-MB-QTC
题目：循环的嵌套，案例99乘法表
'''

for row in range(1,10):
    for col in range(row,10):
        #print(row,'x',col,'=',row*col)
        print(row, 'x', col, '=', row * col,'  ',end='')  #end是什么意思？
        print('/n')
