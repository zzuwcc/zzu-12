# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modify.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import window.main
from core.database import *
from window.main import *

class Ui_Dialog(object):
    def __int__(self):
        self.father = None

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(823, 509)
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(180, 80, 531, 61))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.pushButton_2 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(370, 440, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(390, 160, 311, 251))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")

        self.Dialog = Dialog
        Dialog.pB = self.pb
        Dialog.pB2 = self.pb2
        information = getInformation()
        self.lineEdit_3.setText(information[2])

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.pB)
        self.pushButton_2.clicked.connect(Dialog.pB2)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "密码"))
        self.label_4.setText(_translate("Dialog", "头像"))
        self.pushButton_2.setText(_translate("Dialog", "选择"))
        self.pushButton.setText(_translate("Dialog", "确定"))

    def __init__(self):
        self.Dialog = None

    def pb(self):
        self.Dialog.close()

    def pb2(self):
        result = QtWidgets.QFileDialog.getOpenFileName()
        print(result[0])
        picture = QtGui.QPixmap(result[0])
        self.label_5.setPixmap(picture)
        dst = open('./personal/face.png', "wb")
        src = open(result[0], 'rb')
        dst.write(src.read())
        self.Dialog.father.label.setPixmap(picture)

