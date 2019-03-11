from PyQt5 import QtCore, QtGui, QtWidgets
from UI.pys.color import Ui_Form



class color(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(color, self).__init__(parent)
        self.setupUi(self)

        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        self.btn_clr.clicked.connect(self.act_btn_color)
        self.btn_reset.clicked.connect(self.act_btn_reset)

        self.sli_opacity.setMaximum(100)
        self.sli_opacity.setMinimum(0)
        self.sli_opacity.setValue(100)
        self.sli_opacity.setTickInterval(5)
        self.sli_opacity.valueChanged.connect(self.act_sli_opacity)

    def loadinit(self, mainw, comp):
        self.mainwindow = mainw
        self.comp = comp

    def act_btn_color(self):
        col = QtWidgets.QColorDialog.getColor()
        col = col.getRgbF()[:3]
        self.comp.setcol(col)
        self.mainwindow.glwidget.upmat()

    def act_btn_reset(self):
        self.comp.defcolset()
        self.comp.defopacityset()
        self.mainwindow.glwidget.upmat()

    def act_sli_opacity(self, value):
        if value == 60:
            value = 59
        self.comp.setopacity(value / 100)
        self.mainwindow.glwidget.upmat()
