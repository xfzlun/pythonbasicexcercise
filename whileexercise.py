# _*_ coding: utf-8 _*_
'''
@Time:2018-11-30;21:38
@author: aLuren
@FileName: whileexercise.py
@SoftWare:PyCharm
COPYRIGHT(C)2018 SZ-MB-QTC

8.2. The while statement
The while statement is used for repeated execution as long as an expression is true:

while_stmt ::=  "while" expression ":" suite
                ["else" ":" suite]
This repeatedly tests the expression and, if it is true, executes the first suite;
if the expression is false (which may be the first time it is tested) the suite of the else clause,
if present, is executed and the loop terminates.

A break statement executed in the first suite terminates the loop without executing the else clause’s suite.
A continue statement executed in the first suite skips the rest of the suite and goes back
to testing the expression.
'''
a = [11, 22, 33, 44 ]
i = 0
while i < len(a):
    print('第',i, '个元素为：', a[i])
    i += 1

