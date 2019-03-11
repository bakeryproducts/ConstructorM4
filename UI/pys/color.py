# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'color.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(320, 125)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_clr = QtWidgets.QLabel(Form)
        self.lbl_clr.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_clr.setObjectName("lbl_clr")
        self.verticalLayout.addWidget(self.lbl_clr)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_clr = QtWidgets.QPushButton(Form)
        self.btn_clr.setObjectName("btn_clr")
        self.horizontalLayout.addWidget(self.btn_clr)
        self.btn_reset = QtWidgets.QPushButton(Form)
        self.btn_reset.setObjectName("btn_reset")
        self.horizontalLayout.addWidget(self.btn_reset)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.lbl_opacity = QtWidgets.QLabel(Form)
        self.lbl_opacity.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_opacity.setObjectName("lbl_opacity")
        self.verticalLayout.addWidget(self.lbl_opacity)
        self.sli_opacity = QtWidgets.QSlider(Form)
        self.sli_opacity.setOrientation(QtCore.Qt.Horizontal)
        self.sli_opacity.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.sli_opacity.setObjectName("sli_opacity")
        self.verticalLayout.addWidget(self.sli_opacity)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Color"))
        self.lbl_clr.setText(_translate("Form", "Select color "))
        self.btn_clr.setText(_translate("Form", "Choose..."))
        self.btn_reset.setText(_translate("Form", "Reset"))
        self.lbl_opacity.setText(_translate("Form", "Set Opacity"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
