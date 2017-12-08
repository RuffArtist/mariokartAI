# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/m64py/ui/settings.ui'
#
# Created: Thu Dec  7 18:09:21 2017
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(508, 392)
        self.gridLayout = QtWidgets.QGridLayout(Settings)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(368, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.closeButton = QtWidgets.QPushButton(Settings)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout_2.addWidget(self.closeButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(Settings)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupLibrary = QtWidgets.QGroupBox(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupLibrary.sizePolicy().hasHeightForWidth())
        self.groupLibrary.setSizePolicy(sizePolicy)
        self.groupLibrary.setAutoFillBackground(False)
        self.groupLibrary.setStyleSheet("QGroupBox {\n"
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
        self.groupLibrary.setFlat(False)
        self.groupLibrary.setCheckable(False)
        self.groupLibrary.setObjectName("groupLibrary")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupLibrary)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pathLibrary = QtWidgets.QLineEdit(self.groupLibrary)
        self.pathLibrary.setObjectName("pathLibrary")
        self.horizontalLayout.addWidget(self.pathLibrary)
        self.browseLibrary = QtWidgets.QPushButton(self.groupLibrary)
        self.browseLibrary.setObjectName("browseLibrary")
        self.horizontalLayout.addWidget(self.browseLibrary)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.gridLayout_2.addWidget(self.groupLibrary, 0, 0, 1, 1)
        self.groupPlugins = QtWidgets.QGroupBox(self.tab_1)
        self.groupPlugins.setAutoFillBackground(False)
        self.groupPlugins.setStyleSheet("QGroupBox {\n"
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
        self.groupPlugins.setFlat(False)
        self.groupPlugins.setCheckable(False)
        self.groupPlugins.setObjectName("groupPlugins")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupPlugins)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pathPlugins = QtWidgets.QLineEdit(self.groupPlugins)
        self.pathPlugins.setObjectName("pathPlugins")
        self.horizontalLayout_7.addWidget(self.pathPlugins)
        self.browsePlugins = QtWidgets.QPushButton(self.groupPlugins)
        self.browsePlugins.setObjectName("browsePlugins")
        self.horizontalLayout_7.addWidget(self.browsePlugins)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.gridLayout_2.addWidget(self.groupPlugins, 1, 0, 1, 1)
        self.groupData = QtWidgets.QGroupBox(self.tab_1)
        self.groupData.setAutoFillBackground(False)
        self.groupData.setStyleSheet("QGroupBox {\n"
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
        self.groupData.setFlat(False)
        self.groupData.setCheckable(False)
        self.groupData.setObjectName("groupData")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupData)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pathData = QtWidgets.QLineEdit(self.groupData)
        self.pathData.setObjectName("pathData")
        self.horizontalLayout_3.addWidget(self.pathData)
        self.browseData = QtWidgets.QPushButton(self.groupData)
        self.browseData.setObjectName("browseData")
        self.horizontalLayout_3.addWidget(self.browseData)
        self.verticalLayout_8.addLayout(self.horizontalLayout_3)
        self.gridLayout_2.addWidget(self.groupData, 2, 0, 1, 1)
        self.groupROM = QtWidgets.QGroupBox(self.tab_1)
        self.groupROM.setAutoFillBackground(False)
        self.groupROM.setStyleSheet("QGroupBox {\n"
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
        self.groupROM.setFlat(False)
        self.groupROM.setCheckable(False)
        self.groupROM.setObjectName("groupROM")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupROM)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pathROM = QtWidgets.QLineEdit(self.groupROM)
        self.pathROM.setObjectName("pathROM")
        self.horizontalLayout_4.addWidget(self.pathROM)
        self.browseROM = QtWidgets.QPushButton(self.groupROM)
        self.browseROM.setObjectName("browseROM")
        self.horizontalLayout_4.addWidget(self.browseROM)
        self.verticalLayout_9.addLayout(self.horizontalLayout_4)
        self.gridLayout_2.addWidget(self.groupROM, 3, 0, 1, 1)
        self.groupScripts = QtWidgets.QGroupBox(self.tab_1)
        self.groupScripts.setAutoFillBackground(False)
        self.groupScripts.setStyleSheet("QGroupBox {\n"
"  border: 1px solid #7F7F7F;\n"
"  border-radius: 3px;\n"
"  margin-top: 1ex; \n"
" }\n"
"\n"
"QGroupBox::title {\n"
"  subcontrol-origin: margin;\n"
"  subcontrol-position: top left; \n"
"  padding: 0 2px;\n"
" }")
        self.groupScripts.setFlat(False)
        self.groupScripts.setCheckable(False)
        self.groupScripts.setObjectName("groupScripts")
        self.verticalLayout_9_2 = QtWidgets.QVBoxLayout(self.groupScripts)
        self.verticalLayout_9_2.setObjectName("verticalLayout_9_2")
        self.horizontalLayout_4_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4_2.setObjectName("horizontalLayout_4_2")
        self.pathScripts = QtWidgets.QLineEdit(self.groupScripts)
        self.pathScripts.setObjectName("pathScripts")
        self.horizontalLayout_4_2.addWidget(self.pathScripts)
        self.browseScripts = QtWidgets.QPushButton(self.groupScripts)
        self.browseScripts.setObjectName("browseScripts")
        self.horizontalLayout_4_2.addWidget(self.browseScripts)
        self.verticalLayout_9_2.addLayout(self.horizontalLayout_4_2)
        self.gridLayout_2.addWidget(self.groupScripts, 4, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.groupEmuMode = QtWidgets.QGroupBox(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupEmuMode.sizePolicy().hasHeightForWidth())
        self.groupEmuMode.setSizePolicy(sizePolicy)
        self.groupEmuMode.setAutoFillBackground(False)
        self.groupEmuMode.setStyleSheet("QGroupBox {\n"
"    border: 1px solid #7F7F7F;\n"
"    border-radius: 3px;\n"
"    margin-top: 1ex;\n"
" }\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left; \n"
"    padding: 0 2px;\n"
" }")
        self.groupEmuMode.setFlat(False)
        self.groupEmuMode.setCheckable(False)
        self.groupEmuMode.setObjectName("groupEmuMode")
        self.gridLayout_7.addWidget(self.groupEmuMode, 0, 0, 1, 1)
        self.groupEmuMode_2 = QtWidgets.QGroupBox(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupEmuMode_2.sizePolicy().hasHeightForWidth())
        self.groupEmuMode_2.setSizePolicy(sizePolicy)
        self.groupEmuMode_2.setAutoFillBackground(False)
        self.groupEmuMode_2.setStyleSheet("QGroupBox {\n"
"    border: 1px solid #7F7F7F;\n"
"    border-radius: 3px;\n"
"    margin-top: 1ex;\n"
" }\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left; \n"
"    padding: 0 2px;\n"
" }")
        self.groupEmuMode_2.setFlat(False)
        self.groupEmuMode_2.setCheckable(False)
        self.groupEmuMode_2.setObjectName("groupEmuMode_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupEmuMode_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.checkNoCompiledJump = QtWidgets.QCheckBox(self.groupEmuMode_2)
        self.checkNoCompiledJump.setObjectName("checkNoCompiledJump")
        self.gridLayout_4.addWidget(self.checkNoCompiledJump, 0, 0, 1, 2)
        self.checkDisableExtraMem = QtWidgets.QCheckBox(self.groupEmuMode_2)
        self.checkDisableExtraMem.setObjectName("checkDisableExtraMem")
        self.gridLayout_4.addWidget(self.checkDisableExtraMem, 1, 0, 1, 2)
        self.checkDelaySI = QtWidgets.QCheckBox(self.groupEmuMode_2)
        self.checkDelaySI.setObjectName("checkDelaySI")
        self.gridLayout_4.addWidget(self.checkDelaySI, 2, 0, 1, 1)
        self.comboCountPerOp = QtWidgets.QComboBox(self.groupEmuMode_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboCountPerOp.sizePolicy().hasHeightForWidth())
        self.comboCountPerOp.setSizePolicy(sizePolicy)
        self.comboCountPerOp.setMinimumContentsLength(0)
        self.comboCountPerOp.setObjectName("comboCountPerOp")
        self.comboCountPerOp.addItem("")
        self.comboCountPerOp.addItem("")
        self.comboCountPerOp.addItem("")
        self.comboCountPerOp.addItem("")
        self.comboCountPerOp.addItem("")
        self.gridLayout_4.addWidget(self.comboCountPerOp, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupEmuMode_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 3, 1, 1, 1)
        self.gridLayout_7.addWidget(self.groupEmuMode_2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.groupGraphics = QtWidgets.QGroupBox(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupGraphics.sizePolicy().hasHeightForWidth())
        self.groupGraphics.setSizePolicy(sizePolicy)
        self.groupGraphics.setAutoFillBackground(False)
        self.groupGraphics.setStyleSheet("QGroupBox {\n"
"    border: 1px solid #7F7F7F;\n"
"    border-radius: 3px;\n"
"    margin-top: 1ex;\n"
" }\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left; \n"
"    padding: 0 2px;\n"
" }")
        self.groupGraphics.setFlat(False)
        self.groupGraphics.setCheckable(False)
        self.groupGraphics.setObjectName("groupGraphics")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupGraphics)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.checkOSD = QtWidgets.QCheckBox(self.groupGraphics)
        self.checkOSD.setChecked(True)
        self.checkOSD.setObjectName("checkOSD")
        self.gridLayout_5.addWidget(self.checkOSD, 0, 0, 1, 1)
        self.checkDisableScreenSaver = QtWidgets.QCheckBox(self.groupGraphics)
        self.checkDisableScreenSaver.setObjectName("checkDisableScreenSaver")
        self.gridLayout_5.addWidget(self.checkDisableScreenSaver, 1, 0, 1, 1)
        self.checkEnableVidExt = QtWidgets.QCheckBox(self.groupGraphics)
        self.checkEnableVidExt.setChecked(False)
        self.checkEnableVidExt.setObjectName("checkEnableVidExt")
        self.gridLayout_5.addWidget(self.checkEnableVidExt, 2, 0, 1, 1)
        self.checkKeepAspect = QtWidgets.QCheckBox(self.groupGraphics)
        self.checkKeepAspect.setObjectName("checkKeepAspect")
        self.gridLayout_5.addWidget(self.checkKeepAspect, 3, 0, 1, 1)
        self.gridLayout_8.addWidget(self.groupGraphics, 0, 0, 1, 1)
        self.groupResolution = QtWidgets.QGroupBox(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupResolution.sizePolicy().hasHeightForWidth())
        self.groupResolution.setSizePolicy(sizePolicy)
        self.groupResolution.setAutoFillBackground(False)
        self.groupResolution.setStyleSheet("QGroupBox {\n"
"    border: 1px solid #7F7F7F;\n"
"    border-radius: 3px;\n"
"    margin-top: 1ex;\n"
" }\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left; \n"
"    padding: 0 2px;\n"
" }")
        self.groupResolution.setFlat(False)
        self.groupResolution.setCheckable(False)
        self.groupResolution.setObjectName("groupResolution")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupResolution)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.comboResolution = QtWidgets.QComboBox(self.groupResolution)
        self.comboResolution.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboResolution.sizePolicy().hasHeightForWidth())
        self.comboResolution.setSizePolicy(sizePolicy)
        self.comboResolution.setMinimumContentsLength(7)
        self.comboResolution.setObjectName("comboResolution")
        self.gridLayout_6.addWidget(self.comboResolution, 3, 0, 1, 1)
        self.checkFullscreen = QtWidgets.QCheckBox(self.groupResolution)
        self.checkFullscreen.setChecked(False)
        self.checkFullscreen.setObjectName("checkFullscreen")
        self.gridLayout_6.addWidget(self.checkFullscreen, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(361, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem1, 3, 1, 1, 1)
        self.checkVsync = QtWidgets.QCheckBox(self.groupResolution)
        self.checkVsync.setObjectName("checkVsync")
        self.gridLayout_6.addWidget(self.checkVsync, 1, 0, 1, 1)
        self.gridLayout_8.addWidget(self.groupResolution, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.groupVideo = QtWidgets.QGroupBox(self.tab_3)
        self.groupVideo.setAutoFillBackground(False)
        self.groupVideo.setStyleSheet("QGroupBox {\n"
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
        self.groupVideo.setFlat(False)
        self.groupVideo.setCheckable(False)
        self.groupVideo.setObjectName("groupVideo")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupVideo)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.groupVideo)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/plugins_video.png"))
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.comboVideo = QtWidgets.QComboBox(self.groupVideo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboVideo.sizePolicy().hasHeightForWidth())
        self.comboVideo.setSizePolicy(sizePolicy)
        self.comboVideo.setObjectName("comboVideo")
        self.horizontalLayout_5.addWidget(self.comboVideo)
        self.pushButtonVideo = QtWidgets.QPushButton(self.groupVideo)
        self.pushButtonVideo.setEnabled(False)
        self.pushButtonVideo.setObjectName("pushButtonVideo")
        self.horizontalLayout_5.addWidget(self.pushButtonVideo)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.gridLayout_9.addWidget(self.groupVideo, 0, 0, 1, 1)
        self.groupAudio = QtWidgets.QGroupBox(self.tab_3)
        self.groupAudio.setAutoFillBackground(False)
        self.groupAudio.setStyleSheet("QGroupBox {\n"
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
        self.groupAudio.setFlat(False)
        self.groupAudio.setCheckable(False)
        self.groupAudio.setObjectName("groupAudio")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupAudio)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.groupAudio)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/icons/plugins_audio.png"))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.comboAudio = QtWidgets.QComboBox(self.groupAudio)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboAudio.sizePolicy().hasHeightForWidth())
        self.comboAudio.setSizePolicy(sizePolicy)
        self.comboAudio.setObjectName("comboAudio")
        self.horizontalLayout_6.addWidget(self.comboAudio)
        self.pushButtonAudio = QtWidgets.QPushButton(self.groupAudio)
        self.pushButtonAudio.setEnabled(False)
        self.pushButtonAudio.setObjectName("pushButtonAudio")
        self.horizontalLayout_6.addWidget(self.pushButtonAudio)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.gridLayout_9.addWidget(self.groupAudio, 1, 0, 1, 1)
        self.groupInput = QtWidgets.QGroupBox(self.tab_3)
        self.groupInput.setAutoFillBackground(False)
        self.groupInput.setStyleSheet("QGroupBox {\n"
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
        self.groupInput.setFlat(False)
        self.groupInput.setCheckable(False)
        self.groupInput.setObjectName("groupInput")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupInput)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_3 = QtWidgets.QLabel(self.groupInput)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/icons/plugins_input.png"))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_8.addWidget(self.label_3)
        self.comboInput = QtWidgets.QComboBox(self.groupInput)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboInput.sizePolicy().hasHeightForWidth())
        self.comboInput.setSizePolicy(sizePolicy)
        self.comboInput.setObjectName("comboInput")
        self.horizontalLayout_8.addWidget(self.comboInput)
        self.pushButtonInput = QtWidgets.QPushButton(self.groupInput)
        self.pushButtonInput.setEnabled(False)
        self.pushButtonInput.setObjectName("pushButtonInput")
        self.horizontalLayout_8.addWidget(self.pushButtonInput)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.gridLayout_9.addWidget(self.groupInput, 2, 0, 1, 1)
        self.groupRSP = QtWidgets.QGroupBox(self.tab_3)
        self.groupRSP.setAutoFillBackground(False)
        self.groupRSP.setStyleSheet("QGroupBox {\n"
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
        self.groupRSP.setFlat(False)
        self.groupRSP.setCheckable(False)
        self.groupRSP.setObjectName("groupRSP")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupRSP)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_4 = QtWidgets.QLabel(self.groupRSP)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/icons/plugins_rsp.png"))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_9.addWidget(self.label_4)
        self.comboRSP = QtWidgets.QComboBox(self.groupRSP)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboRSP.sizePolicy().hasHeightForWidth())
        self.comboRSP.setSizePolicy(sizePolicy)
        self.comboRSP.setObjectName("comboRSP")
        self.horizontalLayout_9.addWidget(self.comboRSP)
        self.pushButtonRSP = QtWidgets.QPushButton(self.groupRSP)
        self.pushButtonRSP.setEnabled(False)
        self.pushButtonRSP.setObjectName("pushButtonRSP")
        self.horizontalLayout_9.addWidget(self.pushButtonRSP)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.gridLayout_9.addWidget(self.groupRSP, 3, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Settings)
        self.tabWidget.setCurrentIndex(2)
        self.closeButton.clicked.connect(Settings.close)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "Settings"))
        self.closeButton.setText(_translate("Settings", "&Close"))
        self.groupLibrary.setTitle(_translate("Settings", "Library file"))
        self.browseLibrary.setText(_translate("Settings", "Browse"))
        self.groupPlugins.setTitle(_translate("Settings", "Plugins directory"))
        self.browsePlugins.setText(_translate("Settings", "Browse"))
        self.groupData.setTitle(_translate("Settings", "Data directory"))
        self.browseData.setText(_translate("Settings", "Browse"))
        self.groupROM.setTitle(_translate("Settings", "ROMs directory"))
        self.browseROM.setText(_translate("Settings", "Browse"))
        self.groupScripts.setTitle(_translate("Settings", "Scripts directory"))
        self.browseScripts.setText(_translate("Settings", "Browse"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("Settings", "Paths"))
        self.groupEmuMode.setTitle(_translate("Settings", "CPU Core"))
        self.groupEmuMode_2.setTitle(_translate("Settings", "Compatibility"))
        self.checkNoCompiledJump.setText(_translate("Settings", "No Compiled Jump"))
        self.checkDisableExtraMem.setText(_translate("Settings", "Disable Extra Memory"))
        self.checkDelaySI.setText(_translate("Settings", "Delay SI"))
        self.comboCountPerOp.setItemText(0, _translate("Settings", "0"))
        self.comboCountPerOp.setItemText(1, _translate("Settings", "1"))
        self.comboCountPerOp.setItemText(2, _translate("Settings", "2"))
        self.comboCountPerOp.setItemText(3, _translate("Settings", "3"))
        self.comboCountPerOp.setItemText(4, _translate("Settings", "4"))
        self.label_5.setText(_translate("Settings", "cycles per emulated instruction"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Settings", "Emulator"))
        self.groupGraphics.setTitle(_translate("Settings", "Graphics"))
        self.checkOSD.setText(_translate("Settings", "On Screen Display"))
        self.checkDisableScreenSaver.setToolTip(_translate("Settings", "Disables ScreenSaver when emulator is running"))
        self.checkDisableScreenSaver.setText(_translate("Settings", "Disable ScreenSaver"))
        self.checkEnableVidExt.setToolTip(_translate("Settings", "Enable embedding of OpenGL window."))
        self.checkEnableVidExt.setText(_translate("Settings", "Enable Video Extension"))
        self.checkKeepAspect.setToolTip(_translate("Settings", "Maintain aspect-ratio on resizing"))
        self.checkKeepAspect.setText(_translate("Settings", "Keep Aspect Ratio"))
        self.groupResolution.setTitle(_translate("Settings", "Video"))
        self.comboResolution.setToolTip(_translate("Settings", "Used only when video extension is disabled"))
        self.checkFullscreen.setToolTip(_translate("Settings", "Fullscreen, used only when video extension is disabled"))
        self.checkFullscreen.setText(_translate("Settings", "Fullscreen"))
        self.checkVsync.setText(_translate("Settings", "Vertical Sync"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Settings", "Graphics"))
        self.groupVideo.setTitle(_translate("Settings", "Video"))
        self.pushButtonVideo.setText(_translate("Settings", "Configure"))
        self.groupAudio.setTitle(_translate("Settings", "Audio"))
        self.pushButtonAudio.setText(_translate("Settings", "Configure"))
        self.groupInput.setTitle(_translate("Settings", "Input"))
        self.pushButtonInput.setText(_translate("Settings", "Configure"))
        self.groupRSP.setTitle(_translate("Settings", "Rsp"))
        self.pushButtonRSP.setText(_translate("Settings", "Configure"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Settings", "Plugins"))

from . import icons_rc
