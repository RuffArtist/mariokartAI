# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/m64py/ui/logview.ui'
#
# Created: Thu Dec  7 18:09:22 2017
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LogView(object):
    def setupUi(self, LogView):
        LogView.setObjectName("LogView")
        LogView.resize(641, 521)
        self.verticalLayout = QtWidgets.QVBoxLayout(LogView)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(LogView)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        spacerItem = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(438, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(LogView)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(LogView)
        self.pushButton.clicked.connect(LogView.hide)
        QtCore.QMetaObject.connectSlotsByName(LogView)

    def retranslateUi(self, LogView):
        _translate = QtCore.QCoreApplication.translate
        LogView.setWindowTitle(_translate("LogView", "Log Viewer"))
        self.pushButton.setText(_translate("LogView", "&Close"))

