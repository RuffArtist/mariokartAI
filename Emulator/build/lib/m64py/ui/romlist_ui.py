# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/m64py/ui/romlist.ui'
#
# Created: Thu Dec  7 18:09:21 2017
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ROMList(object):
    def setupUi(self, ROMList):
        ROMList.setObjectName("ROMList")
        ROMList.resize(850, 657)
        ROMList.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(ROMList)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupROMList = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupROMList.sizePolicy().hasHeightForWidth())
        self.groupROMList.setSizePolicy(sizePolicy)
        self.groupROMList.setAutoFillBackground(False)
        self.groupROMList.setStyleSheet("QGroupBox {\n"
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
        self.groupROMList.setFlat(False)
        self.groupROMList.setCheckable(False)
        self.groupROMList.setObjectName("groupROMList")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupROMList)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter = QtWidgets.QSplitter(self.groupROMList)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.listWidget = QtWidgets.QListWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setObjectName("listWidget")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupTitle = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupTitle.setAutoFillBackground(False)
        self.groupTitle.setStyleSheet("QGroupBox {\n"
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
        self.groupTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.groupTitle.setFlat(False)
        self.groupTitle.setCheckable(False)
        self.groupTitle.setObjectName("groupTitle")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupTitle)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.titleView = ImageView(self.groupTitle)
        self.titleView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.titleView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.titleView.setBackgroundBrush(brush)
        self.titleView.setObjectName("titleView")
        self.verticalLayout_3.addWidget(self.titleView)
        self.verticalLayout.addWidget(self.groupTitle)
        self.groupSnapshot = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupSnapshot.setAutoFillBackground(False)
        self.groupSnapshot.setStyleSheet("QGroupBox {\n"
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
        self.groupSnapshot.setAlignment(QtCore.Qt.AlignCenter)
        self.groupSnapshot.setFlat(False)
        self.groupSnapshot.setCheckable(False)
        self.groupSnapshot.setObjectName("groupSnapshot")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.groupSnapshot)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.snapshotView = ImageView(self.groupSnapshot)
        self.snapshotView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.snapshotView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.snapshotView.setBackgroundBrush(brush)
        self.snapshotView.setObjectName("snapshotView")
        self.verticalLayout_10.addWidget(self.snapshotView)
        self.verticalLayout.addWidget(self.groupSnapshot)
        self.horizontalLayout.addWidget(self.splitter)
        self.verticalLayout_2.addWidget(self.groupROMList)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushRefresh = QtWidgets.QPushButton(self.centralwidget)
        self.pushRefresh.setEnabled(False)
        self.pushRefresh.setObjectName("pushRefresh")
        self.horizontalLayout_7.addWidget(self.pushRefresh)
        self.labelAvailable = QtWidgets.QLabel(self.centralwidget)
        self.labelAvailable.setText("")
        self.labelAvailable.setObjectName("labelAvailable")
        self.horizontalLayout_7.addWidget(self.labelAvailable)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_7.addWidget(self.progressBar)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_7)
        spacerItem = QtWidgets.QSpacerItem(118, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem1 = QtWidgets.QSpacerItem(488, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.pushCancel = QtWidgets.QPushButton(self.centralwidget)
        self.pushCancel.setAutoDefault(False)
        self.pushCancel.setObjectName("pushCancel")
        self.horizontalLayout_8.addWidget(self.pushCancel)
        self.pushOpen = QtWidgets.QPushButton(self.centralwidget)
        self.pushOpen.setEnabled(False)
        self.pushOpen.setDefault(True)
        self.pushOpen.setObjectName("pushOpen")
        self.horizontalLayout_8.addWidget(self.pushOpen)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        ROMList.setCentralWidget(self.centralwidget)

        self.retranslateUi(ROMList)
        self.pushCancel.clicked.connect(ROMList.close)
        QtCore.QMetaObject.connectSlotsByName(ROMList)

    def retranslateUi(self, ROMList):
        _translate = QtCore.QCoreApplication.translate
        ROMList.setWindowTitle(_translate("ROMList", "Load ROM Image"))
        self.groupROMList.setTitle(_translate("ROMList", "ROMs List"))
        self.listWidget.setSortingEnabled(True)
        self.groupTitle.setTitle(_translate("ROMList", "Title Screen"))
        self.groupSnapshot.setTitle(_translate("ROMList", "In Game Snapshot"))
        self.pushRefresh.setText(_translate("ROMList", "Refresh"))
        self.pushCancel.setText(_translate("ROMList", "&Cancel"))
        self.pushOpen.setText(_translate("ROMList", "&Open"))

from m64py.ui.imageview import ImageView
