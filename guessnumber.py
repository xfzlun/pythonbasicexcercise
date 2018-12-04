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
'''
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

for i in range(1, 5):
        if B < A:
            print('再猜大一点')
            B = int(input('猜猜我现在想什么数字？'))
        elif B > A:
            print('再猜小一点')
            B = int(input('猜猜我现在想什么数字？'))
        else:
            print("Well Done!")
            break

#如何在连续猜错5次以后，加入一句再见?





