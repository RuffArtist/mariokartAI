# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/m64py/ui/archive.ui'
#
# Created: Thu Dec  7 18:09:22 2017
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ArchiveDialog(object):
    def setupUi(self, ArchiveDialog):
        ArchiveDialog.setObjectName("ArchiveDialog")
        ArchiveDialog.resize(274, 224)
        ArchiveDialog.setModal(False)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(ArchiveDialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.fileChoices = QtWidgets.QGroupBox(ArchiveDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileChoices.sizePolicy().hasHeightForWidth())
        self.fileChoices.setSizePolicy(sizePolicy)
        self.fileChoices.setAutoFillBackground(False)
        self.fileChoices.setStyleSheet("QGroupBox {\n"
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
        self.fileChoices.setTitle("")
        self.fileChoices.setFlat(False)
        self.fileChoices.setCheckable(False)
        self.fileChoices.setObjectName("fileChoices")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.fileChoices)
        self.verticalLayout_2.setContentsMargins(9, -1, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.fileChoices)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.scrollArea = QtWidgets.QScrollArea(self.fileChoices)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 232, 120))
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
        self.verticalLayout_3.addWidget(self.fileChoices)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(228, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushOk = QtWidgets.QPushButton(ArchiveDialog)
        self.pushOk.setObjectName("pushOk")
        self.horizontalLayout.addWidget(self.pushOk)
        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.retranslateUi(ArchiveDialog)
        self.listWidget.setCurrentRow(-1)
        self.pushOk.clicked.connect(ArchiveDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(ArchiveDialog)

    def retranslateUi(self, ArchiveDialog):
        _translate = QtCore.QCoreApplication.translate
        ArchiveDialog.setWindowTitle(_translate("ArchiveDialog", "Archive"))
        self.label.setText(_translate("ArchiveDialog", "Choose a file from archive:"))
        self.pushOk.setText(_translate("ArchiveDialog", "&Ok"))

