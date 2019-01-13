#!/usr/bin/python3
#_*_coding: utf-8 _*_
'''
@uthor:Julylun
Copyright(c)2019 SZ_MB-QTC
FileName:pythontoexe.py
@DATE:2019-Jan-12;Sat
@TIME:14:01:09
Note: 这是python转Exe档案的练习
先安装pip,pipvenv
$sudo apt-get install python3-pip
$sudo apt-get install 
Note:貌似不能在Linux系统下安装pywin32
$sudo pip install PyInstaller #这个库无法用Anaconda 安装，只能用pip
 Error Message: Could not install packages due to an EnvironmentError: [Errno 13] Permission denied: '/home/julylun/anaconda3/lib/python3.7/site-packages/pefile.py'
Consider using the `--user` option or check the permissions.
检查后发现这个资料夹属于root权限，但是root中没有安装python3.7以及 pip3，所以，切换到root，安装pip3,再用pip3安装PyInstaller
$pip3 install PyQT5
'''
#使用 PyQT5做一个简单的GUI，创建一个窗体
import sys
from PyQt5.Qt import *

app = QApplication(sys.argv) #建立实例对象

#设定窗体大小
window = QWidget()
window.resize(500,500)
window.setWindowTitle('测试')

#显示窗体
window.show()
sys.exit(app.exec_())
#在窗体上添加一个标签
#标签
label = QLabel(window)
label.setText('测试显示')
label.move(250,100)

#定义两个槽函数，功能是修改标签上的内容
#槽函数1
def btn_Old():
    label.setText('测试显示')

#槽函数2
def btn_New():
    label.setText('点我干啥')

#在窗体上添加两个按钮，开链接槽函数
#按钮1
btn1 = QPushButton(window)
btn1.setText('恢复显示')
btn1.move(200,200)
btn1.clicked.connect(btn_Old) #信号与槽

#按钮2
btn1 = QPushButton(window)
btn1.setText('修改显示')
btn1.move(300,200)
btn1.clicked.connect(btn_New)#信号与槽

#显示窗体
window.show()
sys.exit(app.exec_())


'''
打开命令窗口，切换到放置这个档案文件的路径之下，假设是d:\demo\My_Python
输入命令：
$pyinstaller -F -w test.py
开始运行代码以后，在d:\demo\My_Python的目录下会有一个dist的资料夹，里面就有text.exe

PyInstaller部分参数含义：
-F:表示生成单个可执行文件
-w：表示去掉控制窗口，这个在GUI界面是非常好用，不过如果是命令程序就把这个选项删除
-i:表示可执行的文件

注意事项：
1. 有些代码调用的图片和窗口资源，是不会自动导入的，需要自己手动复制进去，否则exe文件在运行时命令窗口会报错找不到文件
'''