# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addcomp.ui'
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

class Ui_wid_addcomp(object):
    def setupUi(self, wid_addcomp):
        wid_addcomp.setObjectName(_fromUtf8("wid_addcomp"))
        wid_addcomp.resize(1100, 600)
        wid_addcomp.setMinimumSize(QtCore.QSize(800, 0))
        self.horizontalLayout = QtGui.QHBoxLayout(wid_addcomp)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tbl_facestable = QtGui.QTableWidget(wid_addcomp)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbl_facestable.sizePolicy().hasHeightForWidth())
        self.tbl_facestable.setSizePolicy(sizePolicy)
        self.tbl_facestable.setMinimumSize(QtCore.QSize(300, 0))
        self.tbl_facestable.setMaximumSize(QtCore.QSize(240, 16777215))
        self.tbl_facestable.setShowGrid(True)
        self.tbl_facestable.setObjectName(_fromUtf8("tbl_facestable"))
        self.tbl_facestable.setColumnCount(3)
        self.tbl_facestable.setRowCount(1)
        item = QtGui.QTableWidgetItem()
        self.tbl_facestable.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tbl_facestable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tbl_facestable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tbl_facestable.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tbl_facestable.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tbl_facestable.setItem(0, 1, item)
        self.tbl_facestable.horizontalHeader().setVisible(True)
        self.tbl_facestable.horizontalHeader().setCascadingSectionResizes(False)
        self.tbl_facestable.horizontalHeader().setDefaultSectionSize(80)
        self.tbl_facestable.horizontalHeader().setHighlightSections(True)
        self.tbl_facestable.horizontalHeader().setMinimumSectionSize(70)
        self.tbl_facestable.horizontalHeader().setSortIndicatorShown(False)
        self.tbl_facestable.horizontalHeader().setStretchLastSection(True)
        self.tbl_facestable.verticalHeader().setVisible(False)
        self.horizontalLayout.addWidget(self.tbl_facestable)
        self.lay_gl = QtGui.QVBoxLayout()
        self.lay_gl.setObjectName(_fromUtf8("lay_gl"))
        self.lbl_gl = QtGui.QLabel(wid_addcomp)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_gl.sizePolicy().hasHeightForWidth())
        self.lbl_gl.setSizePolicy(sizePolicy)
        self.lbl_gl.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_gl.setObjectName(_fromUtf8("lbl_gl"))
        self.lay_gl.addWidget(self.lbl_gl)
        self.glbox = QtGui.QWidget(wid_addcomp)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.glbox.sizePolicy().hasHeightForWidth())
        self.glbox.setSizePolicy(sizePolicy)
        self.glbox.setMinimumSize(QtCore.QSize(300, 300))
        self.glbox.setObjectName(_fromUtf8("glbox"))
        self.lay_gl.addWidget(self.glbox)
        self.horizontalLayout.addLayout(self.lay_gl)
        self.line_4 = QtGui.QFrame(wid_addcomp)
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.horizontalLayout.addWidget(self.line_4)
        self.rightBox = QtGui.QVBoxLayout()
        self.rightBox.setObjectName(_fromUtf8("rightBox"))
        self.lbl_name = QtGui.QLabel(wid_addcomp)
        self.lbl_name.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_name.setObjectName(_fromUtf8("lbl_name"))
        self.rightBox.addWidget(self.lbl_name)
        self.lay_name = QtGui.QHBoxLayout()
        self.lay_name.setObjectName(_fromUtf8("lay_name"))
        self.ln_name = QtGui.QLineEdit(wid_addcomp)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_name.sizePolicy().hasHeightForWidth())
        self.ln_name.setSizePolicy(sizePolicy)
        self.ln_name.setMaximumSize(QtCore.QSize(100, 16777215))
        self.ln_name.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ln_name.setObjectName(_fromUtf8("ln_name"))
        self.lay_name.addWidget(self.ln_name)
        self.btn_setname = QtGui.QPushButton(wid_addcomp)
        self.btn_setname.setObjectName(_fromUtf8("btn_setname"))
        self.lay_name.addWidget(self.btn_setname)
        self.rightBox.addLayout(self.lay_name)
        self.line = QtGui.QFrame(wid_addcomp)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.rightBox.addWidget(self.line)
        self.lbl_set = QtGui.QLabel(wid_addcomp)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_set.sizePolicy().hasHeightForWidth())
        self.lbl_set.setSizePolicy(sizePolicy)
        self.lbl_set.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_set.setObjectName(_fromUtf8("lbl_set"))
        self.rightBox.addWidget(self.lbl_set)
        self.lay_select = QtGui.QHBoxLayout()
        self.lay_select.setObjectName(_fromUtf8("lay_select"))
        self.btn_startselect = QtGui.QPushButton(wid_addcomp)
        self.btn_startselect.setObjectName(_fromUtf8("btn_startselect"))
        self.lay_select.addWidget(self.btn_startselect)
        self.btn_selectall = QtGui.QPushButton(wid_addcomp)
        self.btn_selectall.setObjectName(_fromUtf8("btn_selectall"))
        self.lay_select.addWidget(self.btn_selectall)
        self.rightBox.addLayout(self.lay_select)
        self.lay_material = QtGui.QHBoxLayout()
        self.lay_material.setObjectName(_fromUtf8("lay_material"))
        self.lbl_material = QtGui.QLabel(wid_addcomp)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_material.sizePolicy().hasHeightForWidth())
        self.lbl_material.setSizePolicy(sizePolicy)
        self.lbl_material.setObjectName(_fromUtf8("lbl_material"))
        self.lay_material.addWidget(self.lbl_material)
        self.cmb_material = QtGui.QComboBox(wid_addcomp)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmb_material.sizePolicy().hasHeightForWidth())
        self.cmb_material.setSizePolicy(sizePolicy)
        self.cmb_material.setMinimumSize(QtCore.QSize(130, 0))
        self.cmb_material.setObjectName(_fromUtf8("cmb_material"))
        self.lay_material.addWidget(self.cmb_material)
        self.rightBox.addLayout(self.lay_material)
        self.lay_thickness = QtGui.QHBoxLayout()
        self.lay_thickness.setObjectName(_fromUtf8("lay_thickness"))
        self.lbl_thickness = QtGui.QLabel(wid_addcomp)
        self.lbl_thickness.setObjectName(_fromUtf8("lbl_thickness"))
        self.lay_thickness.addWidget(self.lbl_thickness)
        self.ln_thickness = QtGui.QLineEdit(wid_addcomp)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_thickness.sizePolicy().hasHeightForWidth())
        self.ln_thickness.setSizePolicy(sizePolicy)
        self.ln_thickness.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_thickness.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ln_thickness.setObjectName(_fromUtf8("ln_thickness"))
        self.lay_thickness.addWidget(self.ln_thickness)
        self.rightBox.addLayout(self.lay_thickness)
        self.btn_set = QtGui.QPushButton(wid_addcomp)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_set.sizePolicy().hasHeightForWidth())
        self.btn_set.setSizePolicy(sizePolicy)
        self.btn_set.setObjectName(_fromUtf8("btn_set"))
        self.rightBox.addWidget(self.btn_set)
        self.line_2 = QtGui.QFrame(wid_addcomp)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.rightBox.addWidget(self.line_2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.rightBox.addItem(spacerItem)
        self.line_3 = QtGui.QFrame(wid_addcomp)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.rightBox.addWidget(self.line_3)
        self.lay_btns = QtGui.QHBoxLayout()
        self.lay_btns.setObjectName(_fromUtf8("lay_btns"))
        self.btn_ok = QtGui.QPushButton(wid_addcomp)
        self.btn_ok.setObjectName(_fromUtf8("btn_ok"))
        self.lay_btns.addWidget(self.btn_ok)
        self.btn_cancel = QtGui.QPushButton(wid_addcomp)
        self.btn_cancel.setObjectName(_fromUtf8("btn_cancel"))
        self.lay_btns.addWidget(self.btn_cancel)
        self.rightBox.addLayout(self.lay_btns)
        self.horizontalLayout.addLayout(self.rightBox)

        self.retranslateUi(wid_addcomp)
        QtCore.QMetaObject.connectSlotsByName(wid_addcomp)

    def retranslateUi(self, wid_addcomp):
        wid_addcomp.setWindowTitle(_translate("wid_addcomp", "New component", None))
        item = self.tbl_facestable.horizontalHeaderItem(0)
        item.setText(_translate("wid_addcomp", "Plane #", None))
        item = self.tbl_facestable.horizontalHeaderItem(1)
        item.setText(_translate("wid_addcomp", "Thickness", None))
        item = self.tbl_facestable.horizontalHeaderItem(2)
        item.setText(_translate("wid_addcomp", "Material", None))
        __sortingEnabled = self.tbl_facestable.isSortingEnabled()
        self.tbl_facestable.setSortingEnabled(False)
        self.tbl_facestable.setSortingEnabled(__sortingEnabled)
        self.lbl_gl.setText(_translate("wid_addcomp", "Component preview", None))
        self.lbl_name.setText(_translate("wid_addcomp", "Component name", None))
        self.ln_name.setText(_translate("wid_addcomp", "TESTNAME", None))
        self.btn_setname.setText(_translate("wid_addcomp", "Set Name", None))
        self.lbl_set.setText(_translate("wid_addcomp", "Set thickness and material", None))
        self.btn_startselect.setText(_translate("wid_addcomp", "Select planes", None))
        self.btn_selectall.setText(_translate("wid_addcomp", "Select All", None))
        self.lbl_material.setText(_translate("wid_addcomp", "Material:", None))
        self.lbl_thickness.setText(_translate("wid_addcomp", "Thickness, mm:", None))
        self.ln_thickness.setText(_translate("wid_addcomp", "0", None))
        self.btn_set.setText(_translate("wid_addcomp", "Apply", None))
        self.btn_ok.setText(_translate("wid_addcomp", "OK", None))
        self.btn_cancel.setText(_translate("wid_addcomp", "Cancel", None))

