#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QLabel
from PyQt5 import QtCore
 
 
"""
Lily PyQt5 tutorial
In this example, we show a dialog.
Author: Lily Yu
Website: https://blog.csdn.net/yl_best/article/category/8312614
Last edited: November 2018
"""
 
 
class Example(QDialog):
 
    def __init__(self):
        super().__init__()
 
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle('Dialog')
        self.resize(400, 300)   # set dialog size to 400*300
        self.lb = QLabel("Code style - Hello PyQt5 Dialog!",self)        # add a label to this dialog
        self.lb.setGeometry(QtCore.QRect(70, 40, 201, 51))   # set label position and size
        self.show()
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())