# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'navigation.ui'
#
# Created: Mon Nov 21 14:06:34 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 440)
        self.cwidget = QtGui.QWidget(MainWindow)
        self.cwidget.setObjectName("cwidget")
        self.gridLayout_2 = QtGui.QGridLayout(self.cwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.vertLayout = QtGui.QVBoxLayout()
        self.vertLayout.setObjectName("vertLayout")
        self.label = QtGui.QLabel(self.cwidget)
        self.label.setMaximumSize(QtCore.QSize(15888321, 20))
        self.label.setObjectName("label")
        self.vertLayout.addWidget(self.label)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtGui.QLabel(self.cwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.startinp = QtGui.QLineEdit(self.cwidget)
        self.startinp.setObjectName("startinp")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.startinp)
        self.label_3 = QtGui.QLabel(self.cwidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.zielin = QtGui.QLineEdit(self.cwidget)
        self.zielin.setObjectName("zielin")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.zielin)
        self.vertLayout.addLayout(self.formLayout)
        self.gridLayout_2.addLayout(self.vertLayout, 0, 0, 1, 1)
        self.vertLayout2 = QtGui.QVBoxLayout()
        self.vertLayout2.setObjectName("vertLayout2")
        self.ausgabe = QtGui.QTextBrowser(self.cwidget)
        self.ausgabe.setMaximumSize(QtCore.QSize(16777215, 300))
        self.ausgabe.setObjectName("ausgabe")
        self.vertLayout2.addWidget(self.ausgabe)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.closebutt = QtGui.QPushButton(self.cwidget)
        self.closebutt.setObjectName("closebutt")
        self.gridLayout.addWidget(self.closebutt, 0, 2, 1, 1)
        self.submitbutt = QtGui.QPushButton(self.cwidget)
        self.submitbutt.setMinimumSize(QtCore.QSize(600, 28))
        self.submitbutt.setMaximumSize(QtCore.QSize(150, 16777215))
        self.submitbutt.setObjectName("submitbutt")
        self.gridLayout.addWidget(self.submitbutt, 0, 0, 1, 1)
        self.button_reset = QtGui.QPushButton(self.cwidget)
        self.button_reset.setObjectName("button_reset")
        self.gridLayout.addWidget(self.button_reset, 0, 1, 1, 1)
        self.vertLayout2.addLayout(self.gridLayout)
        self.gridLayout_2.addLayout(self.vertLayout2, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.cwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statbar = QtGui.QStatusBar(MainWindow)
        self.statbar.setObjectName("statbar")
        MainWindow.setStatusBar(self.statbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.closebutt, QtCore.SIGNAL("clicked()"), MainWindow.close)
        QtCore.QObject.connect(self.button_reset, QtCore.SIGNAL("clicked()"), self.ausgabe.clear)
        QtCore.QObject.connect(self.button_reset, QtCore.SIGNAL("clicked()"), self.zielin.clear)
        QtCore.QObject.connect(self.button_reset, QtCore.SIGNAL("clicked()"), self.startinp.clear)
        QtCore.QObject.connect(self.button_reset, QtCore.SIGNAL("clicked()"), self.statbar.clearMessage)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "GOOGLE NAVIGATION", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "START:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "ZIEL:", None, QtGui.QApplication.UnicodeUTF8))
        self.closebutt.setText(QtGui.QApplication.translate("MainWindow", "Beenden", None, QtGui.QApplication.UnicodeUTF8))
        self.submitbutt.setText(QtGui.QApplication.translate("MainWindow", "Anzeigen", None, QtGui.QApplication.UnicodeUTF8))
        self.button_reset.setText(QtGui.QApplication.translate("MainWindow", "Neustart", None, QtGui.QApplication.UnicodeUTF8))

