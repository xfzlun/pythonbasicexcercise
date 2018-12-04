# _*_ coding: utf-8 _*_
'''
@Time:2018-12-03;23:11
@author: aLuren
@FileName: guessnumber.py
@SoftWare:PyCharm
COPYRIGHT(C)2018 SZ-MB-QTC
练习：猜数字游戏
1. 让计算机想一个从0-100的数，记为A
2. 通过input函数输入自己猜测的数字，直到猜对为止
3. 输入数字之后，计算机会给出反馈：再猜大一点或再猜小一点
'''

import random
A = random.randrange(0, 100)
print(A)
B = int(input('猜猜我现在想什么数字？'))
i = 0
while i < 5:
    if B < A:
        print('再猜大一点')
        B = int(input('猜猜我现在想什么数字？'))
        i += 1
    elif B > A:
        print('再猜小一点')
        B = int(input('猜猜我现在想什么数字？'))
        i += 1
    else:
        print('Good Job!!')
        i = 5
print('Bye')
'''

print(A)
for i in range(1, 3):
    if B < A:
        print('再猜大一点')
        B = int(input('猜猜我现在想什么数字？'))
    elif B > A:
        print('再猜小一点')
        B = int(input('猜猜我现在想什么数字？'))
    else:
        print("goo")
        i = 5
if B == A:
    print()
else:
    print('你输了，我想的数字是', A, '下次再来吧!')
'''
'''
man={'age':26,'handsome':'yes','income':'13','job':'programmer'}
if man['age']>30:
    print('年龄太大，不见')
elif man['handsome']=='no':
    print('长得不帅，不见')
elif int(man['income'])<=15:
    print('收入太低，不见')
elif man['job']=='programmer':
    print('程序员呀，还可以，见！')
else:
    print('不见不见不见')
'''
'''
为啥在for循环里，设置i=5不会跳出循环？
'''