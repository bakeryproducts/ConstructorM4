import numpy as np
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

class Ui_wid_fsu(QtGui.QWidget):
    def __init__(self):
        super(Ui_wid_fsu, self).__init__()
        #self.mainwindow=0
        self.fedit=False
        self.setupUi(self)
        self.loads = []
        self.fsvdict={}
        self.fragdict={}
        self.revfragdict = {}

        self.fragm=[]
        self.fsvm=[]

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

        self.rdb_typea.clicked.connect(self.act_rdbtypea)

        self.btn_setfrag.clicked.connect(self.act_savefrag)
        self.btn_delfrag.clicked.connect(self.act_delfrag)
        self.btn_newfrag.clicked.connect(self.act_newfrag)
        self.btn_clearfsv.clicked.connect(self.test)

        self.lst_frag.itemSelectionChanged.connect(self.lstchangesel)

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

    def loadinit(self, mainw):
        self.mainwindow = mainw
        self.cs = self.mainwindow.components
        for i,c in enumerate(self.cs,start=1):
            self.fragdict[i] = c.getname()
        for i,c in enumerate(self.cs,start=1):
            self.revfragdict[c.getname()] = i
        self.frags = ['f1','f2']
        self.tblfsvinit()
        self.tblfraginit()

    def tblfsvinit(self):
        l = len(self.frags)
        self.tbl_fsv.blockSignals(True)
        self.tbl_fsv.setColumnCount(l)
        for i in range(l):
            self.tblfsvnewrow()
        self.tbl_fsv.blockSignals(False)

    def tblfraginit(self):
        l = len(self.cs)
        self.tbl_frag.blockSignals(True)
        self.tbl_frag.setColumnCount(l)
        for i in range(l):
            self.tblfragnewrow()
        self.tbl_frag.blockSignals(False)

    def tblfsvnewrow(self):
        rowPosition = self.tbl_fsv.rowCount()
        self.tbl_fsv.insertRow(rowPosition)

        for i, c in enumerate(self.cs):
            item = QtGui.QComboBox()
            item.blockSignals(True)
            item.row,item.col = rowPosition,i
            item.currentIndexChanged.connect(lambda checked, item=item: self.tblfsvchange(item))
            # retarded signal connection:
            # https://martinfitzpatrick.name/article/transmit-extra-data-with-signals-in-pyqt/
            item.addItem('None')
            for ii, fi in enumerate(self.frags):
                item.addItem(fi)
                #self.fsvdict[str(rowPosition) + ';' + str(i) + ';' + str(ii)] = ci.getid()

            item.setCurrentIndex(0)
            if i > 0:
                # pass
                item.setDisabled(True)
            self.tbl_fsv.setCellWidget(rowPosition, i, item)
            item.blockSignals(False)
            # print(item.col, item.row)

    def tblfragnewrow(self):
        rowPosition = self.tbl_frag.rowCount()
        self.tbl_frag.insertRow(rowPosition)

        for i, c in enumerate(self.cs):
            item = QtGui.QComboBox()
            item.blockSignals(True)

            item.row = rowPosition
            item.col = i

            item.currentIndexChanged.connect(lambda checked, item=item: self.tblfragchange(item))
            # retarded signal connection:
            # https://martinfitzpatrick.name/article/transmit-extra-data-with-signals-in-pyqt/

            item.addItem('None')
            for ii, ci in enumerate(self.cs):
                item.addItem(ci.getname())
                #self.fsvdict[str(rowPosition) + ';' + str(i) + ';' + str(ii)] = ci.getid()

            item.setCurrentIndex(0)
            if i > 0:
                # pass
                item.setDisabled(True)
            self.tbl_frag.setCellWidget(rowPosition, i, item)
            item.blockSignals(False)
            # print(item.col, item.row)

    def act_rdbtypea(self):
        setm = [[1, -1, 0, 0], [1, 2, -1, 0], [3, 2, 1, -1]]
        setm = np.array(setm)

        self.setfsv(setm)

    def setfsv(self, setm):
        m, n = setm.shape
        self.tbl_fsv.blockSignals(True)
        for i in range(m):
            for j in range(n):
                fend = False
                item = self.tbl_fsv.cellWidget(i, j)
                item.blockSignals(True)

                if setm[i, j] != -1:
                    item.setCurrentIndex(setm[i, j])
                else:
                    fend = True
                if item.currentIndex() == 0 and not fend:
                    item.setDisabled(True)
                else:
                    item.setDisabled(False)
                item.blockSignals(False)

        self.tbl_fsv.blockSignals(False)

    def setfrag(self, setm):
        m, n = setm.shape
        self.tbl_frag.blockSignals(True)
        for i in range(m):
            for j in range(n):
                fend = False
                item = self.tbl_frag.cellWidget(i, j)
                item.blockSignals(True)

                if setm[i, j] != -1:
                    item.setCurrentIndex(setm[i, j])
                else:
                    fend = True
                if item.currentIndex() == 0 and not fend:
                    item.setDisabled(True)
                else:
                    item.setDisabled(False)
                item.blockSignals(False)

        self.tbl_frag.blockSignals(False)

    def tblfsvchange(self, chitem):
        m, n = self.tbl_fsv.columnCount(), self.tbl_fsv.rowCount()
        ci, cj = chitem.col, chitem.row
        print(ci, cj)

        if chitem.currentIndex() == 0:
            for i in range(m - ci - 1):
                item = self.tbl_fsv.cellWidget(cj, ci + i + 1)
                item.blockSignals(True)
                item.setCurrentIndex(0)
                item.setDisabled(True)
                item.blockSignals(False)
            if ci == 0:
                self.dropfsvtbl(cj + 1)
        elif ci != m - 1:
            item = self.tbl_fsv.cellWidget(cj, ci + 1)
            if item.currentIndex() == 0:
                item.blockSignals(True)
                # item.setCurrentIndex(0)
                item.setDisabled(False)
                item.blockSignals(False)

    def tblfragchange(self, chitem):
        m, n = self.tbl_frag.columnCount(), self.tbl_frag.rowCount()
        ci, cj = chitem.col, chitem.row
        #print(ci, cj)

        if chitem.currentIndex() == 0:
            for i in range(m - ci - 1):
                item = self.tbl_frag.cellWidget(cj, ci + i + 1)
                item.blockSignals(True)
                item.setCurrentIndex(0)
                item.setDisabled(True)
                item.blockSignals(False)
            if ci == 0:
                self.dropfragtbl(cj + 1)
        elif ci != m - 1:
            item = self.tbl_frag.cellWidget(cj, ci + 1)
            if item.currentIndex() == 0:
                item.blockSignals(True)
                # item.setCurrentIndex(0)
                item.setDisabled(False)
                item.blockSignals(False)

    def dropfsvtbl(self, startrow):
        rows, cols = self.tbl_fsv.rowCount(), self.tbl_fsv.columnCount()
        for row in range(rows):
            if row >= startrow:
                for col in range(cols):
                    item = self.tbl_fsv.cellWidget(row, col)
                    item.blockSignals(True)
                    item.setCurrentIndex(0)
                    if col > 0:
                        item.setDisabled(True)
                    item.blockSignals(False)

    def dropfragtbl(self, startrow):
        rows, cols = self.tbl_frag.rowCount(), self.tbl_frag.columnCount()
        for row in range(rows):
            if row >= startrow:
                for col in range(cols):
                    item = self.tbl_frag.cellWidget(row, col)
                    item.blockSignals(True)
                    item.setCurrentIndex(0)
                    if col > 0:
                        item.setDisabled(True)
                    item.blockSignals(False)

    def act_newfrag(self):
        self.dropfragtbl(-1)
        self.ln_fragname.setText('Fragment')
        self.fragm=[]

    def act_savefrag(self):
        frag = self.ln_fragname.text()
        self.addlist(frag)
        self.frags.append(frag)
        self.fsvdict[frag] = self.getfragm()

    def act_delfrag(self):
        try:
            item = self.lst_frag.takeItem(self.lst_frag.currentRow())
            #row = self.lst_frag.currentRow()
            fragname = item.text()
            del(self.fsvdict[fragname])
            item = None

        except:
            pass

    def getfragm(self):
        m, n = self.tbl_frag.columnCount(),self.tbl_frag.rowCount()
        #self.tbl_frag.blockSignals(True)
        frag_and = []
        for i in range(m):
            frag_or = []
            for j in range(n):
                item = self.tbl_frag.cellWidget(i,j)
                ind = item.currentIndex()
                if ind:
                    compname = self.fragdict[ind]
                    frag_or.append(compname)
            if frag_or:
                frag_and.append(frag_or)
        return frag_and

    def addlist(self,name):
        if name not in self.fsvdict.keys():
            item = QtGui.QListWidgetItem(name)
            self.lst_frag.addItem(item)

    def lstchangesel(self):
        self.dropfragtbl(-1)
        frag = self.lst_frag.currentItem().text()
        setm = self.loadfrag(frag)
        print(setm)
        self.setfrag(setm)

    def loadfrag(self,frag):
        fragmatr = []
        fragscheme = self.fsvdict[frag]
        print(fragscheme)
        for j,frag_or in enumerate(fragscheme):
            n_and = []
            for i in range(len(self.fragdict.keys())):
                if i<len(frag_or):
                    n_and.append(self.revfragdict[frag_or[i]])
                else:
                    n_and.append(0)
            fragmatr.append(n_and)
        print(fragmatr)
        return np.array(fragmatr)

    def test(self):
        for k,v in self.fsvdict.items():
            print(k,': ',v)
        for k, v in self.revfragdict.items():
            print(k, ': ', v)