# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyAPRS-ISpass_ui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(737, 345)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(200, 20, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 130, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 130, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 80, 231, 41))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 200, 441, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(510, 200, 101, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 737, 38))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyAPRS-ISpass(APRS-IS PASSCODE计算程序 )"))
        self.label.setText(_translate("MainWindow", "请输入呼号："))
        self.label_2.setText(_translate("MainWindow", "APRS-IS密码："))
        self.pushButton.setText(_translate("MainWindow", "计算密码"))
        self.label_3.setText(_translate("MainWindow", "APRS-IS PASSCODE计算程序 by:BH5HIQ"))
        self.label_4.setText(_translate("MainWindow", "2018-5-5"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))

