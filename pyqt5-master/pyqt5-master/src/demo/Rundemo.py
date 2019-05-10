# -*- coding：utf-8 -*-
# time ：2019/4/21 14:44
# author: 毛利

import sys
import demo
from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = demo.Ui_MainWindow()
    # 向主窗口上添加控件
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())