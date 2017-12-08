# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/m64py/ui/cheat.ui'
#
# Created: Thu Dec  7 18:09:21 2017
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CheatDialog(object):
    def setupUi(self, CheatDialog):
        CheatDialog.setObjectName("CheatDialog")
        CheatDialog.resize(350, 382)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(CheatDialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupCheats = QtWidgets.QGroupBox(CheatDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupCheats.sizePolicy().hasHeightForWidth())
        self.groupCheats.setSizePolicy(sizePolicy)
        self.groupCheats.setMinimumSize(QtCore.QSize(0, 0))
        self.groupCheats.setAutoFillBackground(False)
        self.groupCheats.setStyleSheet("QGroupBox {\n"
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
        self.groupCheats.setFlat(False)
        self.groupCheats.setCheckable(False)
        self.groupCheats.setObjectName("groupCheats")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupCheats)
        self.verticalLayout.setObjectName("verticalLayout")
        self.treeWidget = QtWidgets.QTreeWidget(self.groupCheats)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.treeWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.treeWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.treeWidget.header().setVisible(False)
        self.verticalLayout.addWidget(self.treeWidget)
        self.verticalLayout_3.addWidget(self.groupCheats)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(208, 18, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushUnmarkAll = QtWidgets.QPushButton(CheatDialog)
        self.pushUnmarkAll.setObjectName("pushUnmarkAll")
        self.horizontalLayout_2.addWidget(self.pushUnmarkAll)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.groupNotes = QtWidgets.QGroupBox(CheatDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupNotes.sizePolicy().hasHeightForWidth())
        self.groupNotes.setSizePolicy(sizePolicy)
        self.groupNotes.setMinimumSize(QtCore.QSize(0, 75))
        self.groupNotes.setAutoFillBackground(False)
        self.groupNotes.setStyleSheet("QGroupBox {\n"
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
        self.groupNotes.setFlat(False)
        self.groupNotes.setCheckable(False)
        self.groupNotes.setObjectName("groupNotes")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupNotes)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.groupNotes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy)
        self.scrollArea_2.setStyleSheet("background: #FFF;")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 308, 44))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_2.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.labelDesc = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelDesc.sizePolicy().hasHeightForWidth())
        self.labelDesc.setSizePolicy(sizePolicy)
        self.labelDesc.setText("")
        self.labelDesc.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelDesc.setWordWrap(True)
        self.labelDesc.setObjectName("labelDesc")
        self.verticalLayout_4.addWidget(self.labelDesc)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.addWidget(self.scrollArea_2)
        self.verticalLayout_3.addWidget(self.groupNotes)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(228, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushClose = QtWidgets.QPushButton(CheatDialog)
        self.pushClose.setObjectName("pushClose")
        self.horizontalLayout.addWidget(self.pushClose)
        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.retranslateUi(CheatDialog)
        self.pushClose.clicked.connect(CheatDialog.hide)
        QtCore.QMetaObject.connectSlotsByName(CheatDialog)

    def retranslateUi(self, CheatDialog):
        _translate = QtCore.QCoreApplication.translate
        CheatDialog.setWindowTitle(_translate("CheatDialog", "Cheats"))
        self.groupCheats.setTitle(_translate("CheatDialog", "Cheats"))
        self.pushUnmarkAll.setText(_translate("CheatDialog", "Unmark All"))
        self.groupNotes.setTitle(_translate("CheatDialog", "Notes"))
        self.pushClose.setText(_translate("CheatDialog", "&Close"))

