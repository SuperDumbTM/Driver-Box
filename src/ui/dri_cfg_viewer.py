# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dri_cfg_viewer.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DriverConfigViewer(object):
    def setupUi(self, DriverConfigViewer):
        DriverConfigViewer.setObjectName("DriverConfigViewer")
        DriverConfigViewer.resize(711, 350)
        DriverConfigViewer.setStyleSheet("font: 10pt \"Microsoft JhengHei\";")
        self.gridLayout = QtWidgets.QGridLayout(DriverConfigViewer)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lan_dri_btn = QtWidgets.QPushButton(DriverConfigViewer)
        self.lan_dri_btn.setObjectName("lan_dri_btn")
        self.verticalLayout.addWidget(self.lan_dri_btn)
        self.display_dri_btn = QtWidgets.QPushButton(DriverConfigViewer)
        self.display_dri_btn.setObjectName("display_dri_btn")
        self.verticalLayout.addWidget(self.display_dri_btn)
        self.misc_dri_btn = QtWidgets.QPushButton(DriverConfigViewer)
        self.misc_dri_btn.setObjectName("misc_dri_btn")
        self.verticalLayout.addWidget(self.misc_dri_btn)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.new_dri_btn = QtWidgets.QPushButton(DriverConfigViewer)
        self.new_dri_btn.setObjectName("new_dri_btn")
        self.horizontalLayout.addWidget(self.new_dri_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.dri_info_scrollarea = QtWidgets.QScrollArea(DriverConfigViewer)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.dri_info_scrollarea.setFont(font)
        self.dri_info_scrollarea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.dri_info_scrollarea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.dri_info_scrollarea.setWidgetResizable(True)
        self.dri_info_scrollarea.setObjectName("dri_info_scrollarea")
        self.dri_info_sa_contents = QtWidgets.QWidget()
        self.dri_info_sa_contents.setGeometry(QtCore.QRect(0, 0, 580, 330))
        self.dri_info_sa_contents.setObjectName("dri_info_sa_contents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dri_info_sa_contents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.dri_info_scrollarea.setWidget(self.dri_info_sa_contents)
        self.gridLayout.addWidget(self.dri_info_scrollarea, 0, 1, 1, 1)

        self.retranslateUi(DriverConfigViewer)
        QtCore.QMetaObject.connectSlotsByName(DriverConfigViewer)

    def retranslateUi(self, DriverConfigViewer):
        _translate = QtCore.QCoreApplication.translate
        DriverConfigViewer.setWindowTitle(_translate("DriverConfigViewer", "軀動程式設定"))
        self.lan_dri_btn.setText(_translate("DriverConfigViewer", "有線網絡介卡"))
        self.display_dri_btn.setText(_translate("DriverConfigViewer", "顯示卡"))
        self.misc_dri_btn.setText(_translate("DriverConfigViewer", "其他"))
        self.new_dri_btn.setText(_translate("DriverConfigViewer", "新增"))
