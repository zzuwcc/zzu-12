# !/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from window import register
from window import main

# 主程序入口
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = register.Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    # w = QMainWindow()
    # w_ui = main.Ui_Main()
    # w_ui.setupUi(w)
    # w.show()
    sys.exit(app.exec())
