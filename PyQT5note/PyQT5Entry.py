
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
'''
#导入必要的模块，这些窗口的基本控件位于 PyQt5.QtWidgets模块中
import sys
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
#每个PyQt5应用程序都需要创建一个application对象
#sys.argv是从命令行传入的参数列表
#Python脚本可以从shell中运行，这是一种控制脚本启动的方式.

widget = QtWidgets.QWidget()
widget.resize(250,150)
widget.setWindowTitle('测试Test')
widget.show()
sys.exit(app.exec_())
