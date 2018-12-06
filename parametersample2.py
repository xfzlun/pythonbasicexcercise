# _*_ coding: utf-8 _*_
'''
@Time  :2018-12-06;5:44 PM
@author: aLuren
@FileName: parametersample2.py
@Software: PyCharm
Copyright(C)2018 SZ-MB-QTC
题目：可变参数案例
'''
'''
def word(name,*greeting,**name1):
    print(greeting, name + '!', name1)
word('jack','hi','Nice to meet you')

#演示可变参数没有默认值
'''
'''
def word1(name,*greeting=('hi'),**name1={'n'= 2}):
    print(greeting, name + '!', name1)
word('jack','hi','Nice to meet you')
'''

#演示有默认值的参数，排序位置是如何的？默认参数是在元祖与列表前面

def word1(name='rose', *greeting,**name1):
    print(greeting, name + '!', name1)
word1('jack','hi','Nice to meet you')

#演示位置参数一定会比可变参数先拿到实参的是使用权，如同下面的’hi'
def word2(name='rose', greet='wo', *greeting,**name1):
    print(greeting, name + '!', name1)
word2('jack','hi','Nice to meet you','haha')

#演示python中，字典传参的样式，必须要按照字典的定义形式，键 = 值 的形式来传递参数
def word2(name='rose', greet='wo', *greeting,**name1):
    print(greeting, name + '!', name1)
word2('jack','hi','Nice to meet you','haha',Name='fiona')
