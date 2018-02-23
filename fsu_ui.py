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
        self.fsudict={}

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(548, 469)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tbl_fsu = QtGui.QTableWidget(Form)
        self.tbl_fsu.setObjectName(_fromUtf8("tbl_fsu"))
        self.tbl_fsu.setColumnCount(1)
        self.tbl_fsu.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tbl_fsu.setHorizontalHeaderItem(0, item)
        self.tbl_fsu.horizontalHeader().setDefaultSectionSize(110)
        self.gridLayout.addWidget(self.tbl_fsu, 0, 0, 1, 1)
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
        self.btn_savelay = QtGui.QPushButton(Form)
        self.btn_savelay.setObjectName(_fromUtf8("btn_savelay"))
        self.verticalLayout.addWidget(self.btn_savelay)
        self.btn_clearlay = QtGui.QPushButton(Form)
        self.btn_clearlay.setObjectName(_fromUtf8("btn_clearlay"))
        self.verticalLayout.addWidget(self.btn_clearlay)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.btn_ok = QtGui.QPushButton(Form)
        self.btn_ok.setObjectName(_fromUtf8("btn_ok"))
        self.verticalLayout.addWidget(self.btn_ok)
        self.btn_cancel = QtGui.QPushButton(Form)
        self.btn_cancel.setObjectName(_fromUtf8("btn_cancel"))
        self.verticalLayout.addWidget(self.btn_cancel)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)



        self.rdb_typea.clicked.connect(self.act_rdbtypea)

        #self.tbl_fsu.itemChanged.connect(self.tblchange)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Functional scheme of vulnerability", None))
        item = self.tbl_fsu.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Component #1", None))
        self.rdb_typea.setText(_translate("Form", "Type A", None))
        self.rdb_typeb.setText(_translate("Form", "Type B", None))
        self.rdb_typec.setText(_translate("Form", "Type C", None))
        self.rdb_typecustom.setText(_translate("Form", "Custom ", None))
        self.btn_savelay.setText(_translate("Form", "Save layout", None))
        self.btn_clearlay.setText(_translate("Form", "Clear layout", None))
        self.btn_ok.setText(_translate("Form", "Ok", None))
        self.btn_cancel.setText(_translate("Form", "Cancel", None))

    def loadinit(self,mainw):
        self.mainwindow = mainw
        self.cs = self.mainwindow.components
        self.tblinit()

    def tblinit(self):
        l = len(self.cs)
        self.tbl_fsu.blockSignals(True)
        self.tbl_fsu.setColumnCount(l)
        for i in range(l):
            self.tblnewrow()
        self.tbl_fsu.blockSignals(False)

    def tblnewrow(self):
        rowPosition = self.tbl_fsu.rowCount()
        self.tbl_fsu.insertRow(rowPosition)

        for i,c in enumerate(self.cs):
            item = QtGui.QComboBox()
            item.blockSignals(True)

            item.row = rowPosition
            item.col = i

            item.currentIndexChanged.connect(lambda checked,item=item: self.tblchange(item))
            #retarded signal connection:
            #https://martinfitzpatrick.name/article/transmit-extra-data-with-signals-in-pyqt/

            item.addItem('None')
            for ii,ci in enumerate(self.cs):
                item.addItem(ci.getname())
                self.fsudict[str(rowPosition)+';'+str(i)+';'+str(ii)] = ci.getid()

            item.setCurrentIndex(0)
            if i>0:
                #pass
                item.setDisabled(True)
            self.tbl_fsu.setCellWidget(rowPosition, i, item)
            item.blockSignals(False)
            #print(item.col, item.row)

    def act_rdbtypea(self):
        setm = [[1,-1,0,0],[1,2,-1,0],[3,2,1,-1]]
        setm = np.array(setm)
        self.setfsu(setm)

    def setfsu(self,setm):
        m,n = setm.shape
        self.tbl_fsu.blockSignals(True)
        for i in range(m):
            for j in range(n):
                fend=False
                item = self.tbl_fsu.cellWidget(i,j)
                item.blockSignals(True)

                if setm[i,j]!=-1:
                    item.setCurrentIndex(setm[i,j])
                else:
                    fend=True
                if item.currentIndex()==0 and not fend:
                    item.setDisabled(True)
                else:
                    item.setDisabled(False)
                item.blockSignals(False)

        self.tbl_fsu.blockSignals(False)

    def tblchange(self,chitem):
        m,n = self.tbl_fsu.columnCount(),self.tbl_fsu.rowCount()
        ci,cj = chitem.col,chitem.row
        print(ci,cj)

        if chitem.currentIndex()==0:
            for i in range(m-ci-1):
                item = self.tbl_fsu.cellWidget(cj,ci+i+1)
                item.blockSignals(True)
                item.setCurrentIndex(0)
                item.setDisabled(True)
                item.blockSignals(False)
            if ci == 0:
                self.droptbl(cj+1)
        elif ci!=m-1:
            item = self.tbl_fsu.cellWidget(cj,ci+1)
            if item.currentIndex()==0:
                item.blockSignals(True)
                #item.setCurrentIndex(0)
                item.setDisabled(False)
                item.blockSignals(False)

    def droptbl(self,startrow):
        rows,cols  = self.tbl_fsu.rowCount(),self.tbl_fsu.columnCount()
        for row in range(rows):
            if row >= startrow:
                for col in range(cols):
                    item = self.tbl_fsu.cellWidget(row,col)
                    item.blockSignals(True)
                    item.setCurrentIndex(0)
                    if col>0:
                        item.setDisabled(True)
                    item.blockSignals(False)

    def tblclick(self,item):
        print(item)