
#!/usr/bin/python3
#_*_coding: utf-8 _*_
'''
@uthor:Julylun
Copyright(c)2019 SZ_MB-QTC
FileName:PyQT5Entry.py
@DATE:2019-Jan-13;Sun
@TIME:15:43:23
PyQT5 Tutorial
在Terminal中安装PyQT5
$pip/pip3 install PyQT5
以下整份代码会在屏幕上生成一个小窗体
'''
#导入必要的模块，这些窗口的基本控件位于 PyQt5.QtWidgets模块中
import sys
from PyQt5 import QtWidgets

if __name__ == '__main__':
#如果是直接调用，就执行if__name__ == '__main__':后面的语句，如果是模块调用，就不执行后面的语句
    app = QtWidgets.QApplication(sys.argv)
#每个PyQt5应用程序都需要创建一个application对象
#sys.argv是从命令行传入的参数列表
#Python脚本可以从shell中运行，这是一种控制脚本启动的方式.

    widget = QtWidgets.QWidget()
#控件QWidget是PyQT5中所有UI对象的基类，这里调用了QWidget的默认构造函数，默认构造器没有parent函数，没有parent的控件称为窗体(window)
#默认的构造函数显示该控件不继承任何父类，在PyQt5中，没有父类的控件被定义为窗口
#换成白话文，这个命令搭配下面show跟sys.exit就能产生一个基本的窗口

    widget.resize(250,150)
#调整控件，也就是窗口大小，这边设置成 宽250px 和 高150px
    widget.move(300,300)
#move()方法是移动控件到屏幕上的一个位置，这里设定的坐标是x=300,y=300
    widget.setWindowTitle('测试Test')
#为这个窗口设定标题，标题会显示在标题栏中
    widget.show()
#show表示在场景中显示控件，所有控件首先在内存被创建，然后显示在屏幕上
    sys.exit(app.exec_())
#进入应用程序的主循环，事件处理从这点开始，主循环从窗口系统接收事件，并分派给应用程序窗口的部件。当结束主循环时，如果我们用调用exit()方法，主控件将直接被销毁
#sys.exit()方法为了确保干净的退出，环境将告知应用程序如何结束
#exec_()方法后缀下划线是因为exec是Python的关键字。因此，用exec_()代替.
#如果没这句，窗口就会显示一下就不见了.