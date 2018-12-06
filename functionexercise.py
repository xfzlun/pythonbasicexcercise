# _*_ coding: utf-8 _*_
'''
#@Time  :2018-12-06;10:22 AM
@author: aLuren

#@FileName: functionexercise.py
#@Software: PyCharm
Copyright(C)2018 SZ-MB-QTC
'''

def showname(name):
    '''This function is to show your name'''
    print('i am %s' % name)  #%s % name是什么意思？
    return print('all done')   #return值如果不写，default是none
    print('anything wrong?')   #return后面的代码都不会被执行

showname('Laurence')

