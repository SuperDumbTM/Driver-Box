from PyQt5 import QtCore, QtGui, QtWidgets
from hw_info import HwInfo
from element_factory import ElementFactory
import pythoncom

class HwInfoWorker(QtCore.QThread):
    
    el = ElementFactory()
    _add = QtCore.pyqtSignal(object, str)
    _print = QtCore.pyqtSignal(str)
    
    def __init__(self, parent: QtCore.QObject = None) -> None:
        super().__init__(parent)
        # self.vbox = QtWidgets.QVBoxLayout()
        # self.vbox.setObjectName("hwInfoVBox")

        
    def run(self):
        pythoncom.CoInitialize()
        self.hwi = HwInfo()
        self._print.emit('載入硬件資訊中..')
        
        self._add.emit(self.el.createHwInfoTitle, "底版 MOTHERBOARD")
        for item in self.hwi.get_mb_descr():
            self._add.emit(self.el.createHwInfoText, item)
        self._add.emit(self.el.createHwInfoTitle, "中央處理器 CPU")
        for item in self.hwi.get_cpu_descr():
            self._add.emit(self.el.createHwInfoText, item)
        self._add.emit(self.el.createHwInfoTitle, "記憶體 RAM")
        for item in self.hwi.get_ram_descr():
            self._add.emit(self.el.createHwInfoText, item)
        self._add.emit(self.el.createHwInfoTitle, "顯示卡 GPU")
        for item in self.hwi.get_gpu_descr():
            self._add.emit(self.el.createHwInfoText, item)
        self._add.emit(self.el.createHwInfoTitle, "網絡介面卡 NIC")
        for item in self.hwi.get_nic_descr():
            self._add.emit(self.el.createHwInfoText, item)
        self._add.emit(self.el.createHwInfoTitle, "儲存裝置 STORAGE")
        for item in self.hwi.get_disk_descr():
            self._add.emit(self.el.createHwInfoText, item)

        self._print.emit('完成載入硬件資訊')
        # ret = []
        # ret.append(self.el.createHwInfoTitle("底版 MOTHERBOARD"))
        # for item in self.hwi.get_mb_descr():
        #     ret.append(self.el.createHwInfoText(item))
        # ret.append(self.el.createHwInfoTitle("中央處理器 CPU"))
        # for item in self.hwi.get_cpu_descr():
        #     ret.append(self.el.createHwInfoText(item))
        # ret.append(self.el.createHwInfoTitle("記憶體 RAM"))
        # for item in self.hwi.get_ram_descr():
        #     ret.append(self.el.createHwInfoText(item))
        # ret.append(self.el.createHwInfoTitle("顯示卡 GPU"))
        # for item in self.hwi.get_gpu_descr():
        #     ret.append(self.el.createHwInfoText(item))
        # ret.append(self.el.createHwInfoTitle("網絡介面卡 NIC"))
        # for item in self.hwi.get_nic_descr():
        #     ret.append(self.el.createHwInfoText(item))
        # ret.append(self.el.createHwInfoTitle("儲存裝置 STORAGE"))
        # for item in self.hwi.get_disk_descr():
        #     ret.append(self.el.createHwInfoText(item))
        
        # self.vbox.addWidget(self.el.createHwInfoTitle("底版 MOTHERBOARD"))
        # for item in self.hwi.get_mb_descr():
        #     self.vbox.addWidget(self.el.createHwInfoText(item))
        # self.vbox.addWidget(self.el.createHwInfoTitle("中央處理器 CPU"))
        # for item in self.hwi.get_cpu_descr():
        #     self.vbox.addWidget(self.el.createHwInfoText(item))
        # self.vbox.addWidget(self.el.createHwInfoTitle("記憶體 RAM"))
        # for item in self.hwi.get_ram_descr():
        #     self.vbox.addWidget(self.el.createHwInfoText(item))
        # self.vbox.addWidget(self.el.createHwInfoTitle("顯示卡 GPU"))
        # for item in self.hwi.get_gpu_descr():
        #     self.vbox.addWidget(self.el.createHwInfoText(item))
        # self.vbox.addWidget(self.el.createHwInfoTitle("網絡介面卡 NIC"))
        # for item in self.hwi.get_nic_descr():
        #     self.vbox.addWidget(self.el.createHwInfoText(item))
        # self.vbox.addWidget(self.el.createHwInfoTitle("儲存裝置 STORAGE"))
        # for item in self.hwi.get_disk_descr():
        #     self.vbox.addWidget(self.el.createHwInfoText(item))
        
        # self.trigger.emit(ret)