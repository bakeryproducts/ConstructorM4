# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'materials.ui'
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
        Form.resize(836, 762)
        Form.setMinimumSize(QtCore.QSize(650, 0))
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lay_target1 = QtGui.QHBoxLayout()
        self.lay_target1.setObjectName(_fromUtf8("lay_target1"))
        self.tre_target = QtGui.QTreeWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tre_target.sizePolicy().hasHeightForWidth())
        self.tre_target.setSizePolicy(sizePolicy)
        self.tre_target.setMaximumSize(QtCore.QSize(9999, 180))
        self.tre_target.setObjectName(_fromUtf8("tre_target"))
        self.lay_target1.addWidget(self.tre_target)
        self.tbl_target = QtGui.QTableWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbl_target.sizePolicy().hasHeightForWidth())
        self.tbl_target.setSizePolicy(sizePolicy)
        self.tbl_target.setMinimumSize(QtCore.QSize(420, 0))
        self.tbl_target.setMaximumSize(QtCore.QSize(16777215, 180))
        self.tbl_target.setObjectName(_fromUtf8("tbl_target"))
        self.tbl_target.setColumnCount(2)
        self.tbl_target.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tbl_target.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tbl_target.setHorizontalHeaderItem(1, item)
        self.tbl_target.horizontalHeader().setDefaultSectionSize(188)
        self.lay_target1.addWidget(self.tbl_target)
        self.verticalLayout.addLayout(self.lay_target1)
        self.lay_buttons = QtGui.QHBoxLayout()
        self.lay_buttons.setObjectName(_fromUtf8("lay_buttons"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.lay_buttons.addItem(spacerItem)
        self.btn_load = QtGui.QPushButton(Form)
        self.btn_load.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btn_load.setObjectName(_fromUtf8("btn_load"))
        self.lay_buttons.addWidget(self.btn_load)
        self.btn_del = QtGui.QPushButton(Form)
        self.btn_del.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btn_del.setObjectName(_fromUtf8("btn_del"))
        self.lay_buttons.addWidget(self.btn_del)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lay_buttons.addWidget(self.pushButton)
        self.btn_save = QtGui.QPushButton(Form)
        self.btn_save.setObjectName(_fromUtf8("btn_save"))
        self.lay_buttons.addWidget(self.btn_save)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.lay_buttons.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.lay_buttons)
        self.tab_db = QtGui.QTabWidget(Form)
        self.tab_db.setObjectName(_fromUtf8("tab_db"))
        self.lay_tab1 = QtGui.QWidget()
        self.lay_tab1.setObjectName(_fromUtf8("lay_tab1"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.lay_tab1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tre_tab1 = QtGui.QTreeWidget(self.lay_tab1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tre_tab1.sizePolicy().hasHeightForWidth())
        self.tre_tab1.setSizePolicy(sizePolicy)
        self.tre_tab1.setMaximumSize(QtCore.QSize(9999, 16777215))
        self.tre_tab1.setObjectName(_fromUtf8("tre_tab1"))
        self.tre_tab1.headerItem().setText(0, _fromUtf8("1"))
        self.horizontalLayout.addWidget(self.tre_tab1)
        self.tbl_tab1 = QtGui.QTableWidget(self.lay_tab1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbl_tab1.sizePolicy().hasHeightForWidth())
        self.tbl_tab1.setSizePolicy(sizePolicy)
        self.tbl_tab1.setMinimumSize(QtCore.QSize(405, 0))
        self.tbl_tab1.setObjectName(_fromUtf8("tbl_tab1"))
        self.tbl_tab1.setColumnCount(2)
        self.tbl_tab1.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tbl_tab1.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tbl_tab1.setHorizontalHeaderItem(1, item)
        self.tbl_tab1.horizontalHeader().setDefaultSectionSize(190)
        self.tbl_tab1.horizontalHeader().setMinimumSectionSize(41)
        self.horizontalLayout.addWidget(self.tbl_tab1)
        self.tab_db.addTab(self.lay_tab1, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tab_db.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tab_db)

        self.retranslateUi(Form)
        self.tab_db.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Manage materials", None))
        self.tre_target.headerItem().setText(0, _translate("Form", "Target", None))
        item = self.tbl_target.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Property", None))
        item = self.tbl_target.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Value", None))
        self.btn_load.setText(_translate("Form", "UP", None))
        self.btn_del.setText(_translate("Form", "DOWN", None))
        self.pushButton.setText(_translate("Form", "Set Property", None))
        self.btn_save.setText(_translate("Form", "Save", None))
        item = self.tbl_tab1.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Property", None))
        item = self.tbl_tab1.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Value", None))
        self.tab_db.setTabText(self.tab_db.indexOf(self.lay_tab1), _translate("Form", "Tab 1", None))
        self.tab_db.setTabText(self.tab_db.indexOf(self.tab_2), _translate("Form", "Tab 2", None))

