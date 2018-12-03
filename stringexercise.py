# _*_ coding: utf-8 _*_
'''
#@Time  :2018-12-02;14:03
@author: aLuren
#@FileName: stringexercise.py
#@Software: PyCharm
Copyright(C)2018 SZ-MB-QTC
字符串可以执行的操作：
1. 合并
2. 重复
3. 索引
4. 切片
5. 成员资格in/not in
6. 长度
7. 最大值
8. 最小值
'''

a = 'apple'
b = 'orange'
c = 'apple1234'
d = 'ABC123abc'
print(a+b)  #合并a & b
print(a * 2) #重复a字串2次
print(a[2])
print(b[-3])
print(a[1:4:2])
print('a' in a)
print('b' not in b)
print(len(a))
print(max(c))
print(max(d))

