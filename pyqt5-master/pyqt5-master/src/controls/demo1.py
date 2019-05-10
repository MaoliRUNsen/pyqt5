# -*- coding：utf-8 -*-
# time ：2019/5/9 21:57
# author: 毛利

import sys
from PyQt5.QtWidgets import QDesktopWidget,QMainWindow,QApplication

class Center(QMainWindow):
    def __init__(self):
        super(Center,self).__init__()
        self.setWindowTitle("让窗口居中")
        self.resize(1000,800)

    def center(self):
        # 获取屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口坐标系
        size = self.geometry()
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 2
        self.move(newLeft, newTop)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Center()
    main.show()

    sys.exit(app.exec_())
