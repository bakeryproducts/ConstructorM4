from MATERIALS.clMATERIAL import MATERIAL
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


class Ui_newmathetero(QtGui.QWidget):
    def __init__(self):
        super(Ui_newmathetero, self).__init__()
        # self.mainwindow=0
        self.category = "HETERO"
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(528, 259)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tbl_mats = QtGui.QTableWidget(Form)
        self.tbl_mats.setMinimumSize(QtCore.QSize(310, 0))
        self.tbl_mats.setMaximumSize(QtCore.QSize(9999, 16777215))
        self.tbl_mats.setObjectName(_fromUtf8("tbl_mats"))
        self.tbl_mats.setColumnCount(2)
        self.tbl_mats.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        self.tbl_mats.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        self.tbl_mats.setHorizontalHeaderItem(1, item)
        self.tbl_mats.horizontalHeader().setDefaultSectionSize(150)
        self.horizontalLayout.addWidget(self.tbl_mats)
        self.lay_right = QtGui.QVBoxLayout()
        self.lay_right.setObjectName(_fromUtf8("lay_right"))
        self.lay_name = QtGui.QHBoxLayout()
        self.lay_name.setObjectName(_fromUtf8("lay_name"))
        self.lbl_name = QtGui.QLabel(Form)
        self.lbl_name.setObjectName(_fromUtf8("lbl_name"))
        self.lay_name.addWidget(self.lbl_name)
        self.ln_name = QtGui.QLineEdit(Form)
        self.ln_name.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_name.setObjectName(_fromUtf8("ln_name"))
        self.lay_name.addWidget(self.ln_name)
        self.lay_right.addLayout(self.lay_name)
        self.line_2 = QtGui.QFrame(Form)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.lay_right.addWidget(self.line_2)
        self.lbl_add = QtGui.QLabel(Form)
        self.lbl_add.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_add.setObjectName(_fromUtf8("lbl_add"))
        self.lay_right.addWidget(self.lbl_add)
        self.lay_matsel = QtGui.QHBoxLayout()
        self.lay_matsel.setObjectName(_fromUtf8("lay_matsel"))
        self.lbl_matsel = QtGui.QLabel(Form)
        self.lbl_matsel.setObjectName(_fromUtf8("lbl_matsel"))
        self.lay_matsel.addWidget(self.lbl_matsel)
        self.cmb_matsel = QtGui.QComboBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmb_matsel.sizePolicy().hasHeightForWidth())
        self.cmb_matsel.setSizePolicy(sizePolicy)
        self.cmb_matsel.setMinimumSize(QtCore.QSize(120, 0))
        self.cmb_matsel.setObjectName(_fromUtf8("cmb_matsel"))
        self.lay_matsel.addWidget(self.cmb_matsel)
        self.lay_right.addLayout(self.lay_matsel)
        self.lay_thick = QtGui.QHBoxLayout()
        self.lay_thick.setObjectName(_fromUtf8("lay_thick"))
        self.lbl_thick = QtGui.QLabel(Form)
        self.lbl_thick.setObjectName(_fromUtf8("lbl_thick"))
        self.lay_thick.addWidget(self.lbl_thick)
        self.ln_thick = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_thick.sizePolicy().hasHeightForWidth())
        self.ln_thick.setSizePolicy(sizePolicy)
        self.ln_thick.setMaximumSize(QtCore.QSize(120, 16777215))
        self.ln_thick.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_thick.setObjectName(_fromUtf8("ln_thick"))
        self.lay_thick.addWidget(self.ln_thick)
        self.lay_right.addLayout(self.lay_thick)
        self.btn_add = QtGui.QPushButton(Form)
        self.btn_add.setObjectName(_fromUtf8("btn_add"))
        self.lay_right.addWidget(self.btn_add)
        self.line = QtGui.QFrame(Form)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.lay_right.addWidget(self.line)
        self.btn_delete = QtGui.QPushButton(Form)
        self.btn_delete.setObjectName(_fromUtf8("btn_delete"))
        self.lay_right.addWidget(self.btn_delete)
        self.btn_save = QtGui.QPushButton(Form)
        self.btn_save.setObjectName(_fromUtf8("btn_save"))
        self.lay_right.addWidget(self.btn_save)
        self.btn_cancel = QtGui.QPushButton(Form)
        self.btn_cancel.setObjectName(_fromUtf8("btn_cancel"))
        self.lay_right.addWidget(self.btn_cancel)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.lay_right.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.lay_right)

        self.btn_add.clicked.connect(self.act_btn_addlayer)
        self.btn_save.clicked.connect(self.act_btn_save)
        self.btn_delete.clicked.connect(self.act_btn_delete)
        self.btn_cancel.clicked.connect(self.act_btn_cancel)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "New material", None))
        item = self.tbl_mats.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Material", None))
        item = self.tbl_mats.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Thickness", None))
        self.lbl_name.setText(_translate("Form", "Material name:", None))
        self.ln_name.setText(_translate("Form", "NewMaterial", None))
        self.lbl_add.setText(_translate("Form", "Add new layer", None))
        self.lbl_matsel.setText(_translate("Form", "Material:", None))
        self.lbl_thick.setText(_translate("Form", "Thickness:", None))
        self.ln_thick.setText(_translate("Form", "0", None))
        self.btn_add.setText(_translate("Form", "Add", None))
        self.btn_delete.setText(_translate("Form", "Delete selected", None))
        self.btn_save.setText(_translate("Form", "Save", None))
        self.btn_cancel.setText(_translate("Form", "Cancel", None))

    def loadinit(self, mainw):
        self.mainwindow = mainw
        self.cmbinit()

    def cmbinit(self):
        self.materials = []
        args = []
        for mat in self.mainwindow.materials:
            if mat.category != self.category:
                self.materials.append(mat)
                args.append(mat.getname())

        self.cmb_matsel.addItems(args)

    def act_btn_addlayer(self):
        mat = self.cmb_matsel.currentText()
        thick = self.ln_thick.text()
        self.newrow(mat, thick)

    def act_btn_cancel(self):
        self.close()

    def act_btn_save(self):
        matname = self.ln_name.text()
        hetmat = MATERIAL(self.category, matname)
        for row in range(self.tbl_mats.rowCount()):
            matname, thick = self.tbl_mats.cellWidget(row, 0), self.tbl_mats.item(row, 1)
            hetmat.addprop(matname.currentText(), thick.text())

        self.mainwindow.materials.append(hetmat)

    def act_btn_delete(self):
        ind = self.tbl_mats.currentRow()
        self.tbl_mats.removeRow(ind)

    def newrow(self, rowname, rowvalue):
        rowPosition = self.tbl_mats.rowCount()
        self.tbl_mats.insertRow(rowPosition)
        item1 = QtGui.QComboBox()
        tmpind = 0
        for ind, t in enumerate(self.materials):
            if t.getname() == rowname:
                tmpind = ind
            item1.addItem(t.getname())
        item1.setCurrentIndex(tmpind)

        item2 = QtGui.QTableWidgetItem(rowvalue)
        item2.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)

        self.tbl_mats.setCellWidget(rowPosition, 0, item1)
        self.tbl_mats.setItem(rowPosition, 1, item2)

    def editrow(self, rowPosition, rowValue):
        # item1 = QtGui.QTableWidgetItem(rowValue)
        # item1.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item2 = QtGui.QTableWidgetItem(rowValue)
        item2.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        # item2.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        # self.tbl_mats.setItem(rowPosition, 0, item1)
        self.tbl_mats.setItem(rowPosition, 1, item2)
