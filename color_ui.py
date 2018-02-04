# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'color.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_color(QtGui.QWidget):
    def __init__(self):
        super(Ui_color,self).__init__()
        self.setupUi(self)
        #self.mainwindow=0

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(320, 125)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lbl_clr = QtGui.QLabel(Form)
        self.lbl_clr.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_clr.setObjectName(_fromUtf8("lbl_clr"))
        self.verticalLayout.addWidget(self.lbl_clr)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btn_clr = QtGui.QPushButton(Form)
        self.btn_clr.setObjectName(_fromUtf8("btn_clr"))
        self.horizontalLayout.addWidget(self.btn_clr)
        self.btn_reset = QtGui.QPushButton(Form)
        self.btn_reset.setObjectName(_fromUtf8("btn_reset"))
        self.horizontalLayout.addWidget(self.btn_reset)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.lbl_opacity = QtGui.QLabel(Form)
        self.lbl_opacity.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_opacity.setObjectName(_fromUtf8("lbl_opacity"))
        self.verticalLayout.addWidget(self.lbl_opacity)
        self.sli_opacity = QtGui.QSlider(Form)
        self.sli_opacity.setOrientation(QtCore.Qt.Horizontal)
        self.sli_opacity.setTickPosition(QtGui.QSlider.NoTicks)
        self.sli_opacity.setObjectName(_fromUtf8("sli_opacity"))
        self.verticalLayout.addWidget(self.sli_opacity)

        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        self.btn_clr.clicked.connect(self.act_btn_color)
        self.btn_reset.clicked.connect(self.act_btn_reset)

        self.sli_opacity.setMaximum(100)
        self.sli_opacity.setMinimum(0)
        self.sli_opacity.setValue(100)
        self.sli_opacity.setTickInterval(5)
        self.sli_opacity.valueChanged.connect(self.act_sli_opacity)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Color", None))
        self.lbl_clr.setText(_translate("Form", "Select color ", None))
        self.btn_clr.setText(_translate("Form", "Choose...", None))
        self.btn_reset.setText(_translate("Form", "Reset", None))
        self.lbl_opacity.setText(_translate("Form", "Set Opacity", None))

    def loadinit(self,mainw,comp):
        self.mainwindow=mainw
        self.comp = comp

    def act_btn_color(self):
        col= QtGui.QColorDialog.getColor()
        col = col.getRgbF()[:3]
        self.comp.setcol(col)
        self.mainwindow.glwidget.upmat()

    def act_btn_reset(self):
        self.comp.defcolset()
        self.comp.defopacityset()
        self.mainwindow.glwidget.upmat()

    def act_sli_opacity(self,value):
        if value ==60:
            value=59
        self.comp.setopacity(value/100)
        self.mainwindow.glwidget.upmat()
