# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_start(object):
    def setupUi(self, start):
        start.setObjectName("start")
        start.resize(400, 300)
        self.label = QtWidgets.QLabel(start)
        self.label.setGeometry(QtCore.QRect(60, 70, 341, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(start)
        self.label_2.setGeometry(QtCore.QRect(150, 130, 99, 21))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(start)
        self.pushButton.setGeometry(QtCore.QRect(150, 170, 71, 41))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(start)
        self.label_3.setGeometry(QtCore.QRect(250, 240, 99, 21))
        self.label_3.setObjectName("label_3")
        self.enfp = QtWidgets.QLabel(start)
        self.enfp.setGeometry(QtCore.QRect(30, 130, 100, 110))
        self.enfp.setText("")
        self.enfp.setObjectName("enfp")
        self.enfp.setPixmap(QtGui.QPixmap(r"enfp.jpg"))
        self.enfp.setScaledContents(True)
        self.label_5 = QtWidgets.QLabel(start)
        self.label_5.setGeometry(QtCore.QRect(250, 130, 99, 75))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_5.setPixmap(QtGui.QPixmap(r"nie.jpg"))
        self.label_5.setScaledContents(True)

        self.retranslateUi(start)
        self.pushButton.clicked.connect(start.click_start) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(start)

    def retranslateUi(self, start):
        _translate = QtCore.QCoreApplication.translate
        start.setWindowTitle(_translate("start", "开始！"))
        self.label.setText(_translate("start", "让我们开始一场有趣的冒险吧~"))
        self.label_2.setText(_translate("start", "3…2…1"))
        self.pushButton.setText(_translate("start", "开始！"))
        self.label_3.setText(_translate("start", "by 冰冰酱"))