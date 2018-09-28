# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(342, 248)
        self.centralwidget = QtWidgets.QWidget(login)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 40, 191, 21))
        self.label.setObjectName("label")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(82, 90, 181, 33))
        self.password.setObjectName("password")
        self.ok = QtWidgets.QPushButton(self.centralwidget)
        self.ok.setGeometry(QtCore.QRect(120, 160, 101, 31))
        self.ok.setObjectName("ok")
        #login.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(login)
        self.statusbar.setObjectName("statusbar")
        #login.setStatusBar(self.statusbar)

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "LOGIN WINDOW"))
        self.label.setText(_translate("login", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">ENTER PASSWORD</span></p></body></html>"))
        self.ok.setText(_translate("login", "OK"))

