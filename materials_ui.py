from PyQt4 import QtCore, QtGui
import MATERIALS.clMATERIAL as MATERIAL
import MATERIALS.db as matdb

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

class Ui_materials(QtGui.QWidget):
    def __init__(self):
        super(Ui_materials, self).__init__()
        #self.mainwindow = 0
        self.db = matdb.DB('MATERIALS\\GOST.xml')

        self.setupUi(self)
        self.loadtree()

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(749, 461)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lay_target0 = QtGui.QHBoxLayout()
        self.lay_target0.setObjectName(_fromUtf8("lay_target0"))
        self.lbl_target0mat = QtGui.QLabel(Form)
        self.lbl_target0mat.setMaximumSize(QtCore.QSize(180, 16777215))
        self.lbl_target0mat.setObjectName(_fromUtf8("lbl_target0mat"))
        self.lay_target0.addWidget(self.lbl_target0mat)
        self.lbl_target0prop = QtGui.QLabel(Form)
        self.lbl_target0prop.setObjectName(_fromUtf8("lbl_target0prop"))
        self.lay_target0.addWidget(self.lbl_target0prop)
        self.verticalLayout.addLayout(self.lay_target0)
        self.lay_target1 = QtGui.QHBoxLayout()
        self.lay_target1.setObjectName(_fromUtf8("lay_target1"))
        self.tre_target = QtGui.QTreeWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tre_target.sizePolicy().hasHeightForWidth())
        self.tre_target.setSizePolicy(sizePolicy)
        self.tre_target.setMaximumSize(QtCore.QSize(180, 180))
        self.tre_target.setObjectName(_fromUtf8("tre_target"))
        self.tre_target.headerItem().setText(0, _fromUtf8("1"))
        self.lay_target1.addWidget(self.tre_target)
        self.tbl_target = QtGui.QTableWidget(Form)
        self.tbl_target.setMaximumSize(QtCore.QSize(16777215, 180))
        self.tbl_target.setObjectName(_fromUtf8("tbl_target"))
        self.tbl_target.setColumnCount(0)
        self.tbl_target.setRowCount(0)
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
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.lay_buttons.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.lay_buttons)
        self.tab_db = QtGui.QTabWidget(Form)
        self.tab_db.setObjectName(_fromUtf8("tab_db"))
        self.lay_tab1 = QtGui.QWidget()
        self.lay_tab1.setObjectName(_fromUtf8("lay_tab1"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.lay_tab1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.lay_tab1db1_2 = QtGui.QHBoxLayout()
        self.lay_tab1db1_2.setObjectName(_fromUtf8("lay_tab1db1_2"))
        self.lbl_db1mat = QtGui.QLabel(self.lay_tab1)
        self.lbl_db1mat.setMaximumSize(QtCore.QSize(190, 16777215))
        self.lbl_db1mat.setObjectName(_fromUtf8("lbl_db1mat"))
        self.lay_tab1db1_2.addWidget(self.lbl_db1mat)
        self.lbl_db1prop = QtGui.QLabel(self.lay_tab1)
        self.lbl_db1prop.setObjectName(_fromUtf8("lbl_db1prop"))
        self.lay_tab1db1_2.addWidget(self.lbl_db1prop)
        self.verticalLayout_2.addLayout(self.lay_tab1db1_2)
        self.lay_tab1db1 = QtGui.QHBoxLayout()
        self.lay_tab1db1.setObjectName(_fromUtf8("lay_tab1db1"))
        self.tre_tab1 = QtGui.QTreeWidget(self.lay_tab1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tre_tab1.sizePolicy().hasHeightForWidth())
        self.tre_tab1.setSizePolicy(sizePolicy)
        self.tre_tab1.setMaximumSize(QtCore.QSize(180, 16777215))
        self.tre_tab1.setObjectName(_fromUtf8("tre_tab1"))
        self.tre_tab1.headerItem().setText(0, _fromUtf8("1"))
        self.lay_tab1db1.addWidget(self.tre_tab1)
        self.tbl_tab1 = QtGui.QTableWidget(self.lay_tab1)
        self.tbl_tab1.setObjectName(_fromUtf8("tbl_tab1"))
        self.tbl_tab1.setColumnCount(0)
        self.tbl_tab1.setRowCount(0)
        self.lay_tab1db1.addWidget(self.tbl_tab1)
        self.verticalLayout_2.addLayout(self.lay_tab1db1)
        self.tab_db.addTab(self.lay_tab1, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tab_db.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tab_db)

        self.tre_tab1.itemSelectionChanged.connect(self.act_tre_tab)

        self.retranslateUi(Form)
        self.tab_db.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Manage materials", None))
        self.lbl_target0mat.setText(_translate("Form", "Target materials", None))
        self.lbl_target0prop.setText(_translate("Form", "Material properties", None))
        self.btn_load.setText(_translate("Form", "UP", None))
        self.btn_del.setText(_translate("Form", "DOWN", None))
        self.lbl_db1mat.setText(_translate("Form", "Database materials", None))
        self.lbl_db1prop.setText(_translate("Form", "Material properties", None))
        self.tab_db.setTabText(self.tab_db.indexOf(self.lay_tab1), _translate("Form", "Tab 1", None))
        self.tab_db.setTabText(self.tab_db.indexOf(self.tab_2), _translate("Form", "Tab 2", None))

    def act_tre_tab(self):
        getselected = self.tre_tab1.selectedItems()
        activeitem = getselected[0]
        activet = activeitem.text(0)
        if activet not in self.categories:
            self.loadtable(activet)

    def loadtable(self,matitem):
        props = self.db.getmat(matitem)
        for prop in props:
            self.newrow(*prop)


    def newrow(self, rowname, rowvalue):
        rowPosition = self.tbl_tab1.rowCount()
        self.tbl_tab1.insertRow(rowPosition)
        item1 = QtGui.QTableWidgetItem(rowname)
        item1.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)

        item2 = QtGui.QTableWidgetItem(rowvalue)
        item2.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)

        self.tbl_tab1.setItem(rowPosition, 0, item1)
        self.tbl_tab1.setItem(rowPosition, 1, item2)

    def loadtree(self):
        self.tre_tab1.headerItem().setText(0, _fromUtf8("GOST"))
        self.categories = self.db.getcats()

        for cat in self.categories:
            parent = QtGui.QTreeWidgetItem(self.tre_tab1)
            parent.setText(0, cat)
            #parent.setFlags(parent.flags() | QtCore.Qt.ItemIsTristate | QtCore.Qt.ItemIsUserCheckable)
            #parent.setCheckState(0, QtCore.Qt.Checked)
            mats = self.db.getcatmat(cat)
            for mat in mats:
                child = QtGui.QTreeWidgetItem(parent)
                child.setText(0, mat)
                #child.setCheckState(0, QtCore.Qt.Checked)
                child.setFlags(child.flags())

    def loadinit(self,mainw):
        self.mainwindow = mainw