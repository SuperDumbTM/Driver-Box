# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(768, 467)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setStyleSheet("font: 10pt \"Microsoft JhengHei\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.right_vbox = QtWidgets.QVBoxLayout()
        self.right_vbox.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.right_vbox.setContentsMargins(0, -1, 0, -1)
        self.right_vbox.setSpacing(6)
        self.right_vbox.setObjectName("right_vbox")
        self.hwinfo_group_box = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hwinfo_group_box.sizePolicy().hasHeightForWidth())
        self.hwinfo_group_box.setSizePolicy(sizePolicy)
        self.hwinfo_group_box.setMinimumSize(QtCore.QSize(335, 350))
        self.hwinfo_group_box.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.hwinfo_group_box.setObjectName("hwinfo_group_box")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.hwinfo_group_box)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.hwInfo_refresh_btn = QtWidgets.QPushButton(self.hwinfo_group_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hwInfo_refresh_btn.sizePolicy().hasHeightForWidth())
        self.hwInfo_refresh_btn.setSizePolicy(sizePolicy)
        self.hwInfo_refresh_btn.setObjectName("hwInfo_refresh_btn")
        self.horizontalLayout_3.addWidget(self.hwInfo_refresh_btn)
        self.dri_opt_reset_btn = QtWidgets.QPushButton(self.hwinfo_group_box)
        self.dri_opt_reset_btn.setObjectName("dri_opt_reset_btn")
        self.horizontalLayout_3.addWidget(self.dri_opt_reset_btn)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.hwinfo_scroll_area = QtWidgets.QScrollArea(self.hwinfo_group_box)
        self.hwinfo_scroll_area.setWidgetResizable(True)
        self.hwinfo_scroll_area.setObjectName("hwinfo_scroll_area")
        self.hwinfo_scroll_area_content = QtWidgets.QWidget()
        self.hwinfo_scroll_area_content.setGeometry(QtCore.QRect(0, 0, 325, 326))
        self.hwinfo_scroll_area_content.setObjectName("hwinfo_scroll_area_content")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.hwinfo_scroll_area_content)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.hwinfo_vbox = QtWidgets.QVBoxLayout()
        self.hwinfo_vbox.setObjectName("hwinfo_vbox")
        self.verticalLayout_12.addLayout(self.hwinfo_vbox)
        self.hwinfo_scroll_area.setWidget(self.hwinfo_scroll_area_content)
        self.gridLayout_3.addWidget(self.hwinfo_scroll_area, 3, 0, 1, 1)
        self.right_vbox.addWidget(self.hwinfo_group_box)
        self.horizontalLayout_4.addLayout(self.right_vbox)
        self.left_vbox = QtWidgets.QVBoxLayout()
        self.left_vbox.setContentsMargins(0, -1, -1, -1)
        self.left_vbox.setObjectName("left_vbox")
        self.ur_hbox = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ur_hbox.sizePolicy().hasHeightForWidth())
        self.ur_hbox.setSizePolicy(sizePolicy)
        self.ur_hbox.setAutoFillBackground(False)
        self.ur_hbox.setObjectName("ur_hbox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.ur_hbox)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dri_dropdown_vbox = QtWidgets.QVBoxLayout()
        self.dri_dropdown_vbox.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.dri_dropdown_vbox.setObjectName("dri_dropdown_vbox")
        self.lan_dri_group_box = QtWidgets.QGroupBox(self.ur_hbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lan_dri_group_box.sizePolicy().hasHeightForWidth())
        self.lan_dri_group_box.setSizePolicy(sizePolicy)
        self.lan_dri_group_box.setMinimumSize(QtCore.QSize(125, 0))
        self.lan_dri_group_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.lan_dri_group_box.setObjectName("lan_dri_group_box")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.lan_dri_group_box)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lan_driver_dropdown = QtWidgets.QComboBox(self.lan_dri_group_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lan_driver_dropdown.sizePolicy().hasHeightForWidth())
        self.lan_driver_dropdown.setSizePolicy(sizePolicy)
        self.lan_driver_dropdown.setMinimumSize(QtCore.QSize(0, 30))
        self.lan_driver_dropdown.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lan_driver_dropdown.setObjectName("lan_driver_dropdown")
        self.lan_driver_dropdown.addItem("")
        self.verticalLayout_6.addWidget(self.lan_driver_dropdown)
        self.dri_dropdown_vbox.addWidget(self.lan_dri_group_box)
        self.display_dri_group_box = QtWidgets.QGroupBox(self.ur_hbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.display_dri_group_box.sizePolicy().hasHeightForWidth())
        self.display_dri_group_box.setSizePolicy(sizePolicy)
        self.display_dri_group_box.setMinimumSize(QtCore.QSize(125, 0))
        self.display_dri_group_box.setMaximumSize(QtCore.QSize(250, 16777215))
        self.display_dri_group_box.setObjectName("display_dri_group_box")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.display_dri_group_box)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.display_dri_dropdown = QtWidgets.QComboBox(self.display_dri_group_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.display_dri_dropdown.sizePolicy().hasHeightForWidth())
        self.display_dri_dropdown.setSizePolicy(sizePolicy)
        self.display_dri_dropdown.setMinimumSize(QtCore.QSize(0, 30))
        self.display_dri_dropdown.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.display_dri_dropdown.setObjectName("display_dri_dropdown")
        self.display_dri_dropdown.addItem("")
        self.verticalLayout_7.addWidget(self.display_dri_dropdown)
        self.dri_dropdown_vbox.addWidget(self.display_dri_group_box)
        self.horizontalLayout.addLayout(self.dri_dropdown_vbox)
        self.dri_checkbox_vbox = QtWidgets.QVBoxLayout()
        self.dri_checkbox_vbox.setObjectName("dri_checkbox_vbox")
        self.misc_dri_group_box = QtWidgets.QGroupBox(self.ur_hbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.misc_dri_group_box.sizePolicy().hasHeightForWidth())
        self.misc_dri_group_box.setSizePolicy(sizePolicy)
        self.misc_dri_group_box.setMinimumSize(QtCore.QSize(125, 0))
        self.misc_dri_group_box.setMaximumSize(QtCore.QSize(16777215, 160))
        self.misc_dri_group_box.setObjectName("misc_dri_group_box")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.misc_dri_group_box)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.misc_dri_scroll_area = QtWidgets.QScrollArea(self.misc_dri_group_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.misc_dri_scroll_area.sizePolicy().hasHeightForWidth())
        self.misc_dri_scroll_area.setSizePolicy(sizePolicy)
        self.misc_dri_scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.misc_dri_scroll_area.setWidgetResizable(True)
        self.misc_dri_scroll_area.setObjectName("misc_dri_scroll_area")
        self.misc_dri_scroll_area_content = QtWidgets.QWidget()
        self.misc_dri_scroll_area_content.setGeometry(QtCore.QRect(0, 0, 159, 101))
        self.misc_dri_scroll_area_content.setObjectName("misc_dri_scroll_area_content")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.misc_dri_scroll_area_content)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.misc_dri_vbox = QtWidgets.QVBoxLayout()
        self.misc_dri_vbox.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.misc_dri_vbox.setObjectName("misc_dri_vbox")
        self.verticalLayout_3.addLayout(self.misc_dri_vbox)
        self.misc_dri_scroll_area.setWidget(self.misc_dri_scroll_area_content)
        self.verticalLayout_9.addWidget(self.misc_dri_scroll_area)
        self.dri_checkbox_vbox.addWidget(self.misc_dri_group_box)
        self.horizontalLayout.addLayout(self.dri_checkbox_vbox)
        self.left_vbox.addWidget(self.ur_hbox)
        self.lr_hbox = QtWidgets.QHBoxLayout()
        self.lr_hbox.setContentsMargins(8, -1, 8, -1)
        self.lr_hbox.setObjectName("lr_hbox")
        self.install_option_vboc = QtWidgets.QVBoxLayout()
        self.install_option_vboc.setObjectName("install_option_vboc")
        self.exec_options_gridbox = QtWidgets.QGridLayout()
        self.exec_options_gridbox.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.exec_options_gridbox.setContentsMargins(-1, -1, -1, 0)
        self.exec_options_gridbox.setObjectName("exec_options_gridbox")
        self.install_mode_options = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.install_mode_options.sizePolicy().hasHeightForWidth())
        self.install_mode_options.setSizePolicy(sizePolicy)
        self.install_mode_options.setObjectName("install_mode_options")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.install_mode_options)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.at_install_cb = QtWidgets.QCheckBox(self.install_mode_options)
        self.at_install_cb.setChecked(True)
        self.at_install_cb.setObjectName("at_install_cb")
        self.verticalLayout_2.addWidget(self.at_install_cb)
        self.async_install_cb = QtWidgets.QCheckBox(self.install_mode_options)
        self.async_install_cb.setChecked(True)
        self.async_install_cb.setObjectName("async_install_cb")
        self.verticalLayout_2.addWidget(self.async_install_cb)
        self.at_retry_cb = QtWidgets.QCheckBox(self.install_mode_options)
        self.at_retry_cb.setCheckable(True)
        self.at_retry_cb.setChecked(True)
        self.at_retry_cb.setAutoRepeat(False)
        self.at_retry_cb.setAutoExclusive(False)
        self.at_retry_cb.setObjectName("at_retry_cb")
        self.verticalLayout_2.addWidget(self.at_retry_cb)
        self.exec_options_gridbox.addWidget(self.install_mode_options, 0, 0, 1, 1)
        self.halt_options = QtWidgets.QWidget(self.centralwidget)
        self.halt_options.setObjectName("halt_options")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.halt_options)
        self.verticalLayout.setObjectName("verticalLayout")
        self.at_nothing_rb = QtWidgets.QRadioButton(self.halt_options)
        self.at_nothing_rb.setWhatsThis("")
        self.at_nothing_rb.setObjectName("at_nothing_rb")
        self.verticalLayout.addWidget(self.at_nothing_rb)
        self.at_halt_rb = QtWidgets.QRadioButton(self.halt_options)
        self.at_halt_rb.setChecked(False)
        self.at_halt_rb.setAutoExclusive(True)
        self.at_halt_rb.setObjectName("at_halt_rb")
        self.verticalLayout.addWidget(self.at_halt_rb)
        self.at_reboot_rb = QtWidgets.QRadioButton(self.halt_options)
        self.at_reboot_rb.setChecked(True)
        self.at_reboot_rb.setAutoExclusive(True)
        self.at_reboot_rb.setObjectName("at_reboot_rb")
        self.verticalLayout.addWidget(self.at_reboot_rb)
        self.exec_options_gridbox.addWidget(self.halt_options, 0, 1, 1, 1)
        self.install_option_vboc.addLayout(self.exec_options_gridbox)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.install_option_vboc.addWidget(self.line)
        self.additional_tasks = QtWidgets.QGridLayout()
        self.additional_tasks.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.additional_tasks.setContentsMargins(-1, -1, -1, 0)
        self.additional_tasks.setObjectName("additional_tasks")
        self.set_passwd_cb = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.set_passwd_cb.sizePolicy().hasHeightForWidth())
        self.set_passwd_cb.setSizePolicy(sizePolicy)
        self.set_passwd_cb.setChecked(False)
        self.set_passwd_cb.setObjectName("set_passwd_cb")
        self.additional_tasks.addWidget(self.set_passwd_cb, 1, 0, 1, 1)
        self.set_passwd_txt = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.set_passwd_txt.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.set_passwd_txt.sizePolicy().hasHeightForWidth())
        self.set_passwd_txt.setSizePolicy(sizePolicy)
        self.set_passwd_txt.setMaximumSize(QtCore.QSize(100, 24))
        self.set_passwd_txt.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.set_passwd_txt.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.set_passwd_txt.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.set_passwd_txt.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.set_passwd_txt.setPlainText("")
        self.set_passwd_txt.setObjectName("set_passwd_txt")
        self.additional_tasks.addWidget(self.set_passwd_txt, 1, 1, 1, 1)
        self.at_init_disks_cb = QtWidgets.QCheckBox(self.centralwidget)
        self.at_init_disks_cb.setEnabled(False)
        self.at_init_disks_cb.setObjectName("at_init_disks_cb")
        self.additional_tasks.addWidget(self.at_init_disks_cb, 0, 0, 1, 2)
        self.install_option_vboc.addLayout(self.additional_tasks)
        self.exec_actions = QtWidgets.QVBoxLayout()
        self.exec_actions.setContentsMargins(-1, -1, -1, 0)
        self.exec_actions.setObjectName("exec_actions")
        self.disk_mgt_btn = QtWidgets.QPushButton(self.centralwidget)
        self.disk_mgt_btn.setObjectName("disk_mgt_btn")
        self.exec_actions.addWidget(self.disk_mgt_btn)
        self.install_btn = QtWidgets.QPushButton(self.centralwidget)
        self.install_btn.setObjectName("install_btn")
        self.exec_actions.addWidget(self.install_btn)
        self.install_option_vboc.addLayout(self.exec_actions)
        self.lr_hbox.addLayout(self.install_option_vboc)
        self.prog_msg_group_box = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prog_msg_group_box.sizePolicy().hasHeightForWidth())
        self.prog_msg_group_box.setSizePolicy(sizePolicy)
        self.prog_msg_group_box.setMinimumSize(QtCore.QSize(185, 0))
        self.prog_msg_group_box.setStatusTip("")
        self.prog_msg_group_box.setObjectName("prog_msg_group_box")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.prog_msg_group_box)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.prog_msg_box = QtWidgets.QListWidget(self.prog_msg_group_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prog_msg_box.sizePolicy().hasHeightForWidth())
        self.prog_msg_box.setSizePolicy(sizePolicy)
        self.prog_msg_box.setFocusPolicy(QtCore.Qt.NoFocus)
        self.prog_msg_box.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.prog_msg_box.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.prog_msg_box.setProperty("showDropIndicator", False)
        self.prog_msg_box.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.prog_msg_box.setProperty("isWrapping", False)
        self.prog_msg_box.setWordWrap(True)
        self.prog_msg_box.setObjectName("prog_msg_box")
        self.verticalLayout_13.addWidget(self.prog_msg_box)
        self.lr_hbox.addWidget(self.prog_msg_group_box)
        self.left_vbox.addLayout(self.lr_hbox)
        self.horizontalLayout_4.addLayout(self.left_vbox)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 768, 24))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.edit_driver_action = QtWidgets.QAction(MainWindow)
        self.edit_driver_action.setObjectName("edit_driver_action")
        self.menu.addAction(self.edit_driver_action)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OneClick Drivers Installer"))
        self.hwinfo_group_box.setTitle(_translate("MainWindow", "電腦硬件配置"))
        self.hwInfo_refresh_btn.setStatusTip(_translate("MainWindow", "重新載入電腦硬件配置。"))
        self.hwInfo_refresh_btn.setText(_translate("MainWindow", "重新載入"))
        self.dri_opt_reset_btn.setText(_translate("MainWindow", "重置選擇"))
        self.ur_hbox.setStatusTip(_translate("MainWindow", "選擇需要安裝的軀動程式"))
        self.lan_dri_group_box.setTitle(_translate("MainWindow", "有線網絡介面卡"))
        self.lan_driver_dropdown.setItemText(0, _translate("MainWindow", "- 請選擇 -"))
        self.display_dri_group_box.setTitle(_translate("MainWindow", "顯示卡"))
        self.display_dri_dropdown.setItemText(0, _translate("MainWindow", "- 請選擇 -"))
        self.misc_dri_group_box.setTitle(_translate("MainWindow", "其他"))
        self.at_install_cb.setStatusTip(_translate("MainWindow", "自動安裝所有軀動。"))
        self.at_install_cb.setText(_translate("MainWindow", "自動安裝"))
        self.async_install_cb.setStatusTip(_translate("MainWindow", "同時安裝所有軀動，有機會導致安裝失敗。"))
        self.async_install_cb.setText(_translate("MainWindow", "同步安裝"))
        self.at_retry_cb.setStatusTip(_translate("MainWindow", "如有任何軀動程式以自動模式安裝失敗，將以手動模式重試。"))
        self.at_retry_cb.setText(_translate("MainWindow", "失敗重試"))
        self.at_nothing_rb.setStatusTip(_translate("MainWindow", "成功安裝所有軀動後不執行任何動作。"))
        self.at_nothing_rb.setText(_translate("MainWindow", "毋須關機"))
        self.at_halt_rb.setStatusTip(_translate("MainWindow", "成功安裝所有軀動後自動關機。"))
        self.at_halt_rb.setText(_translate("MainWindow", "自動關機"))
        self.at_reboot_rb.setStatusTip(_translate("MainWindow", "成功安裝所有軀動後自動重新開機。"))
        self.at_reboot_rb.setText(_translate("MainWindow", "自動重啟"))
        self.set_passwd_cb.setStatusTip(_translate("MainWindow", "為現時登入的帳戶更改密碼"))
        self.set_passwd_cb.setText(_translate("MainWindow", "設定密碼"))
        self.at_init_disks_cb.setText(_translate("MainWindow", "初始化儲存裝置"))
        self.disk_mgt_btn.setText(_translate("MainWindow", "開啟磁碟管理員"))
        self.install_btn.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.install_btn.setText(_translate("MainWindow", "執行"))
        self.prog_msg_group_box.setTitle(_translate("MainWindow", "Message"))
        self.menu.setTitle(_translate("MainWindow", "管理"))
        self.menu_2.setTitle(_translate("MainWindow", "幫助"))
        self.edit_driver_action.setText(_translate("MainWindow", "編輯軀動程式"))
