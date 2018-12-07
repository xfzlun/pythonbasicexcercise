# _*_ coding: utf-8 _*_
'''
#@Time  :2018-12-07;16:36
@author: aLuren

#@FileName: globalandlocalvariables.py
#@Software: PyCharm
Copyright(C)2018 SZ-MB-QTC
范例：全域变量与局部变量
'''

num= 100 #属于全局变量
def func():
    num= 200  #属于func函数的局部变量

func()
print(func())
'''
这个会输出100，尽管2个变量名字相同，但是作用域做了区分
'''

num = 100
def func():
    num += 100

func()
print(num)
'''
这个会报错，num+=100 -》 num=num+100,Python可以引用全局变量，但是不能给全局变量赋值，给全局变量赋值要利用global函数
'''
num= 100
def func():
    global num #引用全局变量num
    num+= 100  #函数内的变量，如果前面没有加上global,就是属于局部变量，之后的print不能直接调用
func()
print(num)
'''

'''
