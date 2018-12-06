# _*_ coding: utf-8 _*_
'''
@Time  :2018-12-06;5:34 PM
@author: aLuren
@FileName: parametersample.py
@Software: PyCharm
Copyright(C)2018 SZ-MB-QTC
Topic:这是参数类型的案例研究
'''

def word(name,greeting=[]):
    greeting.append('hello')
    print(greeting,name +'!')

word('jack')  #执行后，greeting的默认值变成‘hello’
word('rose',['hi']) #执行后，实参'hi'暂时替代了默认值greeting的‘hello’，到程序第二行再加入一个'hello'
word('mary')
'''最后一行函数调用执行后，greeting因为没有新的实参赋值，所以在原本的默认值一个‘hello'的基础上再加入一个'hello'，变成我们看到的这个结果'''
word('mary',['haha'])
word('mary')
