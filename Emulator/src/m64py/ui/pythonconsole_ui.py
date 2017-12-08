# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/m64py/ui/pythonconsole.ui'
#
# Created: Thu Dec  7 18:09:21 2017
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PythonConsole(object):
    def setupUi(self, PythonConsole):
        PythonConsole.setObjectName("PythonConsole")
        PythonConsole.resize(641, 521)
        self.verticalLayout = QtWidgets.QVBoxLayout(PythonConsole)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textDisplay = QtWidgets.QTextEdit(PythonConsole)
        self.textDisplay.setReadOnly(True)
        self.textDisplay.setAcceptRichText(False)
        self.textDisplay.setObjectName("textDisplay")
        self.verticalLayout.addWidget(self.textDisplay)
        spacerItem = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEntry = QtWidgets.QPlainTextEdit(PythonConsole)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEntry.sizePolicy().hasHeightForWidth())
        self.textEntry.setSizePolicy(sizePolicy)
        self.textEntry.setObjectName("textEntry")
        self.horizontalLayout.addWidget(self.textEntry)
        spacerItem1 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(PythonConsole)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(PythonConsole)
        self.pushButton.clicked.connect(PythonConsole.evaluate)
        QtCore.QMetaObject.connectSlotsByName(PythonConsole)

    def retranslateUi(self, PythonConsole):
        _translate = QtCore.QCoreApplication.translate
        PythonConsole.setWindowTitle(_translate("PythonConsole", "Python Console"))
        self.pushButton.setText(_translate("PythonConsole", "Enter"))
        self.pushButton.setShortcut(_translate("PythonConsole", "Alt+Return"))

