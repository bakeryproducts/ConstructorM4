# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fsu.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(654, 500)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lst_frag = QtGui.QListWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lst_frag.sizePolicy().hasHeightForWidth())
        self.lst_frag.setSizePolicy(sizePolicy)
        self.lst_frag.setMaximumSize(QtCore.QSize(120, 16777215))
        self.lst_frag.setObjectName(_fromUtf8("lst_frag"))
        self.gridLayout.addWidget(self.lst_frag, 1, 1, 1, 1)
        self.tbl_fsv = QtGui.QTableWidget(Form)
        self.tbl_fsv.setObjectName(_fromUtf8("tbl_fsv"))
        self.tbl_fsv.setColumnCount(0)
        self.tbl_fsv.setRowCount(0)
        self.gridLayout.addWidget(self.tbl_fsv, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.ln_fragname = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_fragname.sizePolicy().hasHeightForWidth())
        self.ln_fragname.setSizePolicy(sizePolicy)
        self.ln_fragname.setObjectName(_fromUtf8("ln_fragname"))
        self.horizontalLayout_2.addWidget(self.ln_fragname)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.tbl_frag = QtGui.QTableWidget(Form)
        self.tbl_frag.setObjectName(_fromUtf8("tbl_frag"))
        self.tbl_frag.setColumnCount(0)
        self.tbl_frag.setRowCount(0)
        self.tbl_frag.horizontalHeader().setDefaultSectionSize(110)
        self.verticalLayout_2.addWidget(self.tbl_frag)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.rdb_typea = QtGui.QRadioButton(Form)
        self.rdb_typea.setObjectName(_fromUtf8("rdb_typea"))
        self.verticalLayout.addWidget(self.rdb_typea)
        self.rdb_typeb = QtGui.QRadioButton(Form)
        self.rdb_typeb.setObjectName(_fromUtf8("rdb_typeb"))
        self.verticalLayout.addWidget(self.rdb_typeb)
        self.rdb_typec = QtGui.QRadioButton(Form)
        self.rdb_typec.setObjectName(_fromUtf8("rdb_typec"))
        self.verticalLayout.addWidget(self.rdb_typec)
        self.rdb_typecustom = QtGui.QRadioButton(Form)
        self.rdb_typecustom.setObjectName(_fromUtf8("rdb_typecustom"))
        self.verticalLayout.addWidget(self.rdb_typecustom)
        self.btn_savefsv = QtGui.QPushButton(Form)
        self.btn_savefsv.setObjectName(_fromUtf8("btn_savefsv"))
        self.verticalLayout.addWidget(self.btn_savefsv)
        self.btn_loadfsv = QtGui.QPushButton(Form)
        self.btn_loadfsv.setObjectName(_fromUtf8("btn_loadfsv"))
        self.verticalLayout.addWidget(self.btn_loadfsv)
        self.btn_clearfsv = QtGui.QPushButton(Form)
        self.btn_clearfsv.setObjectName(_fromUtf8("btn_clearfsv"))
        self.verticalLayout.addWidget(self.btn_clearfsv)
        self.btn_newfrag = QtGui.QPushButton(Form)
        self.btn_newfrag.setObjectName(_fromUtf8("btn_newfrag"))
        self.verticalLayout.addWidget(self.btn_newfrag)
        self.btn_setfrag = QtGui.QPushButton(Form)
        self.btn_setfrag.setObjectName(_fromUtf8("btn_setfrag"))
        self.verticalLayout.addWidget(self.btn_setfrag)
        self.btn_delfrag = QtGui.QPushButton(Form)
        self.btn_delfrag.setObjectName(_fromUtf8("btn_delfrag"))
        self.verticalLayout.addWidget(self.btn_delfrag)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.btn_ok = QtGui.QPushButton(Form)
        self.btn_ok.setObjectName(_fromUtf8("btn_ok"))
        self.verticalLayout.addWidget(self.btn_ok)
        self.btn_cancel = QtGui.QPushButton(Form)
        self.btn_cancel.setObjectName(_fromUtf8("btn_cancel"))
        self.verticalLayout.addWidget(self.btn_cancel)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Functional scheme of vulnerability", None))
        self.label_2.setText(_translate("Form", "Model scheme", None))
        self.label_3.setText(_translate("Form", "Fragments list", None))
        self.label.setText(_translate("Form", "Fragment scheme", None))
        self.ln_fragname.setText(_translate("Form", "Fragment", None))
        self.rdb_typea.setText(_translate("Form", "Type A", None))
        self.rdb_typeb.setText(_translate("Form", "Type B", None))
        self.rdb_typec.setText(_translate("Form", "Type C", None))
        self.rdb_typecustom.setText(_translate("Form", "Custom ", None))
        self.btn_savefsv.setText(_translate("Form", "Save FSV", None))
        self.btn_loadfsv.setText(_translate("Form", "Load FSV", None))
        self.btn_clearfsv.setText(_translate("Form", "Clear FSV", None))
        self.btn_newfrag.setText(_translate("Form", "New fragment", None))
        self.btn_setfrag.setText(_translate("Form", "Set fragment", None))
        self.btn_delfrag.setText(_translate("Form", "Del fragment", None))
        self.btn_ok.setText(_translate("Form", "Ok", None))
        self.btn_cancel.setText(_translate("Form", "Cancel", None))

