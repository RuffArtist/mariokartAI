# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/m64py/ui/choices.ui'
#
# Created: Thu Dec  7 18:09:21 2017
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChoicesDialog(object):
    def setupUi(self, ChoicesDialog):
        ChoicesDialog.setObjectName("ChoicesDialog")
        ChoicesDialog.setEnabled(True)
        ChoicesDialog.resize(274, 239)
        ChoicesDialog.setModal(True)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(ChoicesDialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupChoices = QtWidgets.QGroupBox(ChoicesDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupChoices.sizePolicy().hasHeightForWidth())
        self.groupChoices.setSizePolicy(sizePolicy)
        self.groupChoices.setAutoFillBackground(False)
        self.groupChoices.setStyleSheet("QGroupBox {\n"
"    border: 1px solid #7F7F7F;\n"
"    border-radius: 3px;\n"
"    margin-top: 1ex; \n"
" }\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left; \n"
"    padding: 0 2px;\n"
" }")
        self.groupChoices.setTitle("")
        self.groupChoices.setFlat(False)
        self.groupChoices.setCheckable(False)
        self.groupChoices.setObjectName("groupChoices")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupChoices)
        self.verticalLayout_2.setContentsMargins(9, -1, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelDesc = QtWidgets.QLabel(self.groupChoices)
        self.labelDesc.setObjectName("labelDesc")
        self.verticalLayout_2.addWidget(self.labelDesc)
        self.labelName = QtWidgets.QLabel(self.groupChoices)
        self.labelName.setText("")
        self.labelName.setObjectName("labelName")
        self.verticalLayout_2.addWidget(self.labelName)
        self.scrollArea = QtWidgets.QScrollArea(self.groupChoices)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 241, 129))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.verticalLayout_3.addWidget(self.groupChoices)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(228, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushOk = QtWidgets.QPushButton(ChoicesDialog)
        self.pushOk.setObjectName("pushOk")
        self.horizontalLayout.addWidget(self.pushOk)
        self.pushCancel = QtWidgets.QPushButton(ChoicesDialog)
        self.pushCancel.setObjectName("pushCancel")
        self.horizontalLayout.addWidget(self.pushCancel)
        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.retranslateUi(ChoicesDialog)
        self.pushCancel.clicked.connect(ChoicesDialog.close)
        self.pushOk.clicked.connect(ChoicesDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(ChoicesDialog)

    def retranslateUi(self, ChoicesDialog):
        _translate = QtCore.QCoreApplication.translate
        ChoicesDialog.setWindowTitle(_translate("ChoicesDialog", "Choices"))
        self.labelDesc.setText(_translate("ChoicesDialog", "Choose a value to be used for:"))
        self.pushOk.setText(_translate("ChoicesDialog", "&Ok"))
        self.pushCancel.setText(_translate("ChoicesDialog", "&Cancel"))

