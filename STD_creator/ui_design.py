# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'STD_creator/UI_template.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(253, 266)
        MainWindow.setMinimumSize(QtCore.QSize(253, 266))
        MainWindow.setMaximumSize(QtCore.QSize(253, 266))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(253, 252))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 251, 241))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.InLcdNumber = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InLcdNumber.sizePolicy().hasHeightForWidth())
        self.InLcdNumber.setSizePolicy(sizePolicy)
        self.InLcdNumber.setObjectName("InLcdNumber")
        self.horizontalLayout.addWidget(self.InLcdNumber)
        self.InFolderButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InFolderButton.sizePolicy().hasHeightForWidth())
        self.InFolderButton.setSizePolicy(sizePolicy)
        self.InFolderButton.setObjectName("InFolderButton")
        self.horizontalLayout.addWidget(self.InFolderButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.OutLcdNumber = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OutLcdNumber.sizePolicy().hasHeightForWidth())
        self.OutLcdNumber.setSizePolicy(sizePolicy)
        self.OutLcdNumber.setObjectName("OutLcdNumber")
        self.horizontalLayout_2.addWidget(self.OutLcdNumber)
        self.OutFolderButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OutFolderButton.sizePolicy().hasHeightForWidth())
        self.OutFolderButton.setSizePolicy(sizePolicy)
        self.OutFolderButton.setObjectName("OutFolderButton")
        self.horizontalLayout_2.addWidget(self.OutFolderButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.ScrpLcdNumber = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ScrpLcdNumber.sizePolicy().hasHeightForWidth())
        self.ScrpLcdNumber.setSizePolicy(sizePolicy)
        self.ScrpLcdNumber.setObjectName("ScrpLcdNumber")
        self.horizontalLayout_4.addWidget(self.ScrpLcdNumber)
        self.ScriptButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ScriptButton.sizePolicy().hasHeightForWidth())
        self.ScriptButton.setSizePolicy(sizePolicy)
        self.ScriptButton.setObjectName("ScriptButton")
        self.horizontalLayout_4.addWidget(self.ScriptButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.StaffingIndicator = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StaffingIndicator.sizePolicy().hasHeightForWidth())
        self.StaffingIndicator.setSizePolicy(sizePolicy)
        self.StaffingIndicator.setAlignment(QtCore.Qt.AlignCenter)
        self.StaffingIndicator.setObjectName("StaffingIndicator")
        self.horizontalLayout_6.addWidget(self.StaffingIndicator)
        self.StaffingButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StaffingButton.sizePolicy().hasHeightForWidth())
        self.StaffingButton.setSizePolicy(sizePolicy)
        self.StaffingButton.setObjectName("StaffingButton")
        self.horizontalLayout_6.addWidget(self.StaffingButton)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.TemplateIndicator = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TemplateIndicator.sizePolicy().hasHeightForWidth())
        self.TemplateIndicator.setSizePolicy(sizePolicy)
        self.TemplateIndicator.setAlignment(QtCore.Qt.AlignCenter)
        self.TemplateIndicator.setObjectName("TemplateIndicator")
        self.horizontalLayout_3.addWidget(self.TemplateIndicator)
        self.TemplateButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TemplateButton.sizePolicy().hasHeightForWidth())
        self.TemplateButton.setSizePolicy(sizePolicy)
        self.TemplateButton.setObjectName("TemplateButton")
        self.horizontalLayout_3.addWidget(self.TemplateButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.progressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_5.addWidget(self.progressBar)
        self.CompillButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CompillButton.sizePolicy().hasHeightForWidth())
        self.CompillButton.setSizePolicy(sizePolicy)
        self.CompillButton.setObjectName("CompillButton")
        self.horizontalLayout_5.addWidget(self.CompillButton)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Компилятор дерева в ССЗ"))
        self.InFolderButton.setText(_translate("MainWindow", "Папка входа"))
        self.OutFolderButton.setText(_translate("MainWindow", "Папка выхода"))
        self.ScriptButton.setText(_translate("MainWindow", "Список шифров"))
        self.StaffingIndicator.setText(_translate("MainWindow", "Отсутсвует"))
        self.StaffingButton.setText(_translate("MainWindow", "Штатное"))
        self.TemplateIndicator.setText(_translate("MainWindow", "Отсутсвует"))
        self.TemplateButton.setText(_translate("MainWindow", "Шаблон"))
        self.CompillButton.setText(_translate("MainWindow", "Компилировать"))
