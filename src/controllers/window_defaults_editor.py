import os
from PyQt5 import QtCore, QtGui, QtWidgets

import definitions
from enums.halt_option import HaltOption
from install.intall_option import InstallOption
from ui.defaults_editor import Ui_DefaultsEditor


class InstallOptionEditorWindow(Ui_DefaultsEditor, QtWidgets.QDialog):

    qsig_save = QtCore.pyqtSignal(InstallOption)

    def __init__(self, config: InstallOption, parent: QtWidgets.QWidget = None) -> None:
        super().__init__(parent=parent)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(
            os.path.join(definitions.DIR_PIC, "setting.ico")))

        for option in HaltOption:
            self.halt_option_dropdown.addItem(option.value, option)

        self.config = config
        self.fill_data(config)
        # ---------- events ----------
        self.action_btns.accepted.connect(self.save)
        self.action_btns.rejected.connect(self.close)

    def fill_data(self, config: InstallOption):
        self.at_install_cb.setChecked(config.auto_install)
        self.async_install_cb.setChecked(config.async_install)
        self.at_retry_cb.setChecked(config.retry_on_fail)
        self.halt_option_dropdown.setCurrentIndex(
            self.halt_option_dropdown.findData(config.halt_option))
        self.set_passwd_cb.setChecked(config.is_set_passwd)
        self.set_passwd_txt.setText(config.passwd)

    def save(self):
        self.config.auto_install = self.at_install_cb.isChecked()
        self.config.async_install = self.async_install_cb.isChecked()
        self.config.retry_on_fail = self.at_retry_cb.isChecked()
        self.config.halt_option = self.halt_option_dropdown.currentData()
        self.config.is_set_passwd = self.set_passwd_cb.isChecked()
        self.config.passwd = self.set_passwd_txt.text()
        self.config.persist()

        self.qsig_save.emit(self.config)
