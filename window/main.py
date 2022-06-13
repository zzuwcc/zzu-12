# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import window
from window import modify
from window import entryUser

import smtplib
from email.mime.text import MIMEText
from email.header import Header


class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(1031, 719)
        self.label = QtWidgets.QLabel(Main)
        self.label.setGeometry(QtCore.QRect(60, 20, 91, 81))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Main)
        self.label_2.setGeometry(QtCore.QRect(170, 20, 461, 81))
        self.label_2.setText("")
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Main)
        self.pushButton.setGeometry(QtCore.QRect(840, 20, 141, 81))
        self.pushButton.setStyleSheet("QPushButton{\n"
"       text-decoration:none;  \n"
"    background:#05B8CC;\n"
"    color:#f2f2f2;    \n"
"    font-size:20px;  \n"
"    font-family: 微软雅黑,宋体,Arial,Helvetica,Verdana,sans-serif;  \n"
"    font-weight:bold; \n"
"    border-radius:3px;\n"
"}\n"
"QPushButton::pressed{ background: #3C79F2; border-color: #11505C; font-weight: bold; font-family:Microsoft YaHei; }")
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoExclusive(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Main)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 130, 93, 61))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"       text-decoration:none;  \n"
"    background:#05B8CC;\n"
"    color:#f2f2f2;    \n"
"    font-size:20px;  \n"
"    font-family: 微软雅黑,宋体,Arial,Helvetica,Verdana,sans-serif;  \n"
"    font-weight:bold; \n"
"    border-radius:3px;\n"
"}\n"
"QPushButton::pressed{ background: #3C79F2; border-color: #11505C; font-weight: bold; font-family:Microsoft YaHei; }")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Main)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 220, 93, 61))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"       text-decoration:none;  \n"
"    background:#05B8CC;\n"
"    color:#f2f2f2;    \n"
"    font-size:20px;  \n"
"    font-family: 微软雅黑,宋体,Arial,Helvetica,Verdana,sans-serif;  \n"
"    font-weight:bold; \n"
"    border-radius:3px;\n"
"}\n"
"QPushButton::pressed{ background: #3C79F2; border-color: #11505C; font-weight: bold; font-family:Microsoft YaHei; }")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Main)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 310, 93, 51))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"       text-decoration:none;  \n"
"    background:#05B8CC;\n"
"    color:#f2f2f2;    \n"
"    font-size:20px;  \n"
"    font-family: 微软雅黑,宋体,Arial,Helvetica,Verdana,sans-serif;  \n"
"    font-weight:bold; \n"
"    border-radius:3px;\n"
"}\n"
"QPushButton::pressed{ background: #3C79F2; border-color: #11505C; font-weight: bold; font-family:Microsoft YaHei; }")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayoutWidget = QtWidgets.QWidget(Main)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(170, 130, 811, 551))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.verticalLayoutWidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.listWidget = QtWidgets.QListWidget(self.page)
        self.listWidget.setGeometry(QtCore.QRect(5, 1, 801, 541))
        self.listWidget.setObjectName("listWidget")
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.page_3)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 100, 771, 441))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.formLayoutWidget = QtWidgets.QWidget(self.page_3)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 0, 361, 91))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.pushButton_6 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_6.setGeometry(QtCore.QRect(680, 60, 93, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.page_2)
        self.textBrowser.setGeometry(QtCore.QRect(-5, 1, 811, 551))
        self.textBrowser.setObjectName("textBrowser")
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout.addWidget(self.stackedWidget)
        self.pushButton_5 = QtWidgets.QPushButton(Main)
        self.pushButton_5.setGeometry(QtCore.QRect(670, 20, 151, 81))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"       text-decoration:none;  \n"
"    background:#05B8CC;\n"
"    color:#f2f2f2;    \n"
"    font-size:20px;  \n"
"    font-family: 微软雅黑,宋体,Arial,Helvetica,Verdana,sans-serif;  \n"
"    font-weight:bold; \n"
"    border-radius:3px;\n"
"}\n"
"QPushButton::pressed{ background: #3C79F2; border-color: #11505C; font-weight: bold; font-family:Microsoft YaHei; }")
        self.pushButton_5.setObjectName("pushButton_5")

        face = QtGui.QPixmap("./personal/face.png")
        self.label.setPixmap(face)  # 显示图片需要把Qlabel上的文字去掉
        self.label_2.setText("当前用户: " + window.id)
        Main.setStyleSheet("background-color: white")
        Main.PB1 = self.PB1
        Main.pB2 = self.PB2
        Main.pB3 = self.PB3
        Main.pB4 = self.PB4
        Main.pB5 = self.PB5
        Main.pB6 = self.PB6


        self.retranslateUi(Main)
        self.stackedWidget.setCurrentIndex(0)
        self.pushButton_2.clicked.connect(Main.pB2)
        self.pushButton_3.clicked.connect(Main.pB3)
        self.pushButton_4.clicked.connect(Main.pB4)
        self.pushButton.clicked.connect(Main.PB1)
        self.pushButton_5.clicked.connect(Main.pB5)
        self.pushButton_6.clicked.connect(Main.pB6)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Form"))
        self.label.setText(_translate("Main", "TextLabel"))
        self.pushButton.setText(_translate("Main", "修改个人资料"))
        self.pushButton_2.setText(_translate("Main", "收件箱"))
        self.pushButton_3.setText(_translate("Main", "垃圾箱"))
        self.pushButton_4.setText(_translate("Main", "写邮件"))
        self.label_3.setText(_translate("Main", "收件人"))
        self.label_4.setText(_translate("Main", "发件昵称"))
        self.label_5.setText(_translate("Main", "邮件主题"))
        self.pushButton_6.setText(_translate("Main", "发送"))
        self.pushButton_5.setText(_translate("Main", "录入人脸信息"))

    # 修改个人信息槽函数
    def PB1(self):
        self.dialog = QtWidgets.QDialog()
        d_ui = modify.Ui_Dialog()
        d_ui.setupUi(self.dialog)
        self.dialog.father = self
        self.dialog.show()

    # 收件箱槽函数
    def PB2(self):
        self.stackedWidget.setCurrentIndex(0)
        # 加载前先删除上一次列出的数据
        count = self.listWidget.count()
        for i in range(count):
            item = self.listWidget.takeItem(0)
            self.listWidget.removeItemWidget(item)
        text = ["item1", "item2", "item3"]
        self.listWidget.addItems(text)

    # 垃圾箱槽函数
    def PB3(self):
        self.stackedWidget.setCurrentIndex(0)

    # 写邮件槽函数
    def PB4(self):
        self.stackedWidget.setCurrentIndex(1)

    # 录入人脸信息槽函数
    def PB5(self):
        self.dialog = QtWidgets.QDialog()
        d_ui = entryUser.Ui_Dialog()
        d_ui.setupUi(self.dialog)
        self.dialog.show()

    # 发送邮件的接口
    # window.id: 发送者邮箱
    # window.password: 发送者邮箱密码
    # self.lineEdit.text(): 接收者邮箱
    # self.lineEdit_2.text(): 发送者昵称
    # self.lineEdit_3.text(): 邮件主题
    # self.plainTextEdit.toPalinText(): 发送内容
    def PB6(self):
        pass

    # 爬取邮件的槽函数，并存放到 ./file/email/用户id 目录下
    # window.id: 发送者邮箱
    # window.password: 发送者邮箱密码
    def getEmail(self):
        pass

    # 垃圾邮件识别 path是待识别文件的路径 返回-1代表是垃圾邮件，返回1代表是正常邮件
    def judgeEmail(self, path):
        pass

    # 垃圾分类  path是爬取的邮件的路径，把垃圾邮件存放到 ./file/email/用户id/spamEmail 目录下，把非垃圾邮件存放到./file/email/用户id/normalEmail 目录下
    def classifyEmail(self, path):
        pass

    # 垃圾邮件移动到收件箱中  path是垃圾邮件的路径，即把垃圾邮件存放到 ./file/email/用户id/normalEmail 目录下
    def movEmail(self, path):
        pass
