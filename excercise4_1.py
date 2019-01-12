# _*_ coding: utf-8 _*_
'''
#@Time  :2018-12-06;10:46 AM
@author: aLuren
@FileName: excercise4_1.py
@Software: PyCharm
Copyright(C)2018 SZ-MB-QTC

题目：写一个函数，计算n的阶乘
n! = n*(n-1)*(n-2)*....*2*1
'''


def finalresult(n):
    '''This function is to calculate and get value'''
    result = 1
    for i in range(1,n+1):
        result *= i
    return result
a = finalresult(int(input('计算n阶乘结果，请输入一个数')))
print(a)
