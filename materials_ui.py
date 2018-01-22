from PyQt4 import QtCore, QtGui
import MATERIALS.clMATERIAL as MATERIAL
import MATERIALS.db as matdb
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

class Ui_materials(QtGui.QWidget):
    def __init__(self):
        super(Ui_materials, self).__init__()
        # self.mainwindow = 0
        self.db = matdb.DB('MATERIALS\\GOST.xml')

        self.objects=[]
        self.curritemdb = 0
        self.categoriesbd = []
        self.curritempr = 0
        self.materialsnamespr=[]
        self.categoriespr = []

        self.setupUi(self)
        self.loadtree()

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
        # self.tab_2 = QtGui.QWidget()
        # self.tab_2.setObjectName(_fromUtf8("tab_2"))
        # self.tab_db.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tab_db)


        self.tre_tab1.itemSelectionChanged.connect(self.act_tre_tab)
        self.tre_target.itemSelectionChanged.connect(self.act_tre_tar)

        self.btn_load.clicked.connect(self.act_btn_load)
        self.btn_del.clicked.connect(self.act_btn_del)
        self.btn_save.clicked.connect(self.act_btn_save)
        self.pushButton.clicked.connect(self.act_btn_changes)
        self.tbl_target.itemChanged.connect(self.act_tbltargetchanged)


        self.newtab()
        self.pushButton.setEnabled(False)
        self.retranslateUi(Form)
        self.tab_db.setCurrentIndex(0)

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

    def act_btn_del(self):
        root = self.tre_target.invisibleRootItem()
        for item in self.tre_target.selectedItems():
            if item not in self.categoriespr:
                par = item.parent()
                materialname = item.text(0)
                self.materialsnamespr.remove(materialname)
                for obj in self.objects:
                    if materialname == obj.getname():
                        self.objects.remove(obj)

                (item.parent() or root).removeChild(item)
                if par.childCount() == 0:
                    self.categoriespr.remove(par)
                    (par.parent() or root).removeChild(par)

    def act_btn_save(self):
        # print(self.objects)
        # print(self.materialspr)
        # print(self.categoriespr)
        self.mainwindow.materials = self.objects  # [:]
        self.close()

    def act_tre_tar(self):
        try:
            getselected = self.tre_target.selectedItems()
            activeitem = getselected[0]
            activet = activeitem.text(0)
            if activeitem not in self.categoriespr:
                self.curritempr = activeitem
                self.droptablepr()
                self.loadtablepr(activet)
            else:
                self.droptablepr()
                self.curritempr = 0
        except Exception as e:
            pass  # print('errs', e)

    def act_tre_tab(self):
        getselected = self.tre_tab1.selectedItems()
        activeitem = getselected[0]
        activet = activeitem.text(0)
        if activet not in self.categoriesbd:
            self.curritemdb = activeitem
            self.droptablebd()
            self.loadtablebd(activet)
        else:
            self.curritemdb = 0
            self.droptablebd()

    def act_btn_load(self):
        if self.curritemdb:
            mat = self.curritemdb.text(0)
            matobj = self.db.exportmat(mat)
            categorypr = matobj.getcategory()

            parent = self.tre_target.findItems(categorypr, QtCore.Qt.MatchFixedString)
            if not parent:
                parent = QtGui.QTreeWidgetItem(self.tre_target)
                parent.setText(0, matobj.getcategory())
                self.categoriespr.append(parent)
            else:
                parent = parent[0]

            mat = matobj.getname()
            if mat not in self.materialsnamespr:
                child = QtGui.QTreeWidgetItem(parent)
                child.setText(0, mat)
                child.setFlags(child.flags())
                self.materialsnamespr.append(mat)
                self.objects.append(matobj)
                self.curritemdb = 0

    def act_btn_changes(self):
        matname = self.curritempr.text(0)
        for mat in self.objects:
            if mat.getname() == matname:
                for row in range(self.tbl_target.rowCount()):
                    prop, value = self.tbl_target.item(row, 0), self.tbl_target.item(row, 1)
                    mat.addprop(prop.text(), value.text())
        self.pushButton.setEnabled(False)

    def act_tbltargetchanged(self, item):
        self.pushButton.setEnabled(True)

    def droptablepr(self):
        self.tbl_target.setRowCount(0)

    def loadtablepr(self, matitem):
        for mat in self.objects:
            if mat.getname() == matitem:
                props = mat.getprops()
                break
        for k, v in props.items():
            self.newrow(self.tbl_target, k, v)

    def droptablebd(self):
        self.tbl_tab1.setRowCount(0)

    def loadtablebd(self, matitem):
        props = self.db.getmat(matitem)
        for prop in props:
            self.newrow(self.tbl_tab1, *prop)

    def newrow(self, table, rowname, rowvalue):
        rowPosition = table.rowCount()
        table.insertRow(rowPosition)
        item1 = QtGui.QTableWidgetItem(rowname)
        item1.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        item2 = QtGui.QTableWidgetItem(rowvalue)

        table.setItem(rowPosition, 0, item1)
        table.setItem(rowPosition, 1, item2)

    def loadtree(self):
        self.tre_tab1.headerItem().setText(0, _fromUtf8("GOST"))
        self.categoriesbd = self.db.getcats()

        cats = []
        parent = 0
        for cat in self.categoriesbd:
            mats = self.db.getcatmat(cat)
            if not mats:
                parent = QtGui.QTreeWidgetItem(self.tre_tab1)
                parent.setText(0, cat)
                for scat in cats:
                    smats = self.db.getcatmat(scat)
                    if smats:
                        sparent = QtGui.QTreeWidgetItem(parent)
                        sparent.setText(0, scat)
                        for smat in smats:
                            child = QtGui.QTreeWidgetItem(sparent)
                            child.setText(0, smat)
                            child.setFlags(child.flags())

                cats = []
            else:
                cats.append(cat)


                # for cat in self.categoriesbd:
                #     parent = QtGui.QTreeWidgetItem(self.tre_tab1)
                #     parent.setText(0, cat)
                #     mats = self.db.getcatmat(cat)
                #     for mat in mats:
                #         child = QtGui.QTreeWidgetItem(parent)
                #         child.setText(0, mat)
                #         child.setFlags(child.flags())

    def loadinit(self, mainw):
        self.mainwindow = mainw
        for mat in mainw.materials:
            categorypr = mat.getcategory()
            parent = self.tre_target.findItems(categorypr, QtCore.Qt.MatchFixedString)
            if not parent:
                parent = QtGui.QTreeWidgetItem(self.tre_target)
                parent.setText(0, mat.getcategory())
                self.categoriespr.append(parent)
            else:
                parent = parent[0]

            matname = mat.getname()
            if matname not in self.materialsnamespr:
                child = QtGui.QTreeWidgetItem(parent)
                child.setText(0, matname)
                child.setFlags(child.flags())
                self.materialsnamespr.append(matname)
                self.objects.append(mat)

    def newtab(self):
        self.lay_tab2 = QtGui.QWidget()
        self.lay_tab2.setObjectName(_fromUtf8("lay_tab2"))
        self.horizontalLayout2 = QtGui.QHBoxLayout(self.lay_tab2)
        self.horizontalLayout2.setObjectName(_fromUtf8("horizontalLayout2"))
        self.tre_tab2 = QtGui.QTreeWidget(self.lay_tab2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tre_tab2.sizePolicy().hasHeightForWidth())
        self.tre_tab2.setSizePolicy(sizePolicy)
        self.tre_tab2.setMaximumSize(QtCore.QSize(9999, 16777215))
        self.tre_tab2.setObjectName(_fromUtf8("tre_tab2"))
        self.tre_tab2.headerItem().setText(0, _fromUtf8("1"))
        self.horizontalLayout2.addWidget(self.tre_tab2)
        self.tbl_tab2 = QtGui.QTableWidget(self.lay_tab2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbl_tab2.sizePolicy().hasHeightForWidth())
        self.tbl_tab2.setSizePolicy(sizePolicy)
        self.tbl_tab2.setMinimumSize(QtCore.QSize(405, 0))
        self.tbl_tab2.setObjectName(_fromUtf8("tbl_tab2"))
        self.tbl_tab2.setColumnCount(2)
        self.tbl_tab2.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tbl_tab2.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tbl_tab2.setHorizontalHeaderItem(1, item)
        self.tbl_tab2.horizontalHeader().setDefaultSectionSize(190)
        self.tbl_tab2.horizontalHeader().setMinimumSectionSize(41)
        self.horizontalLayout2.addWidget(self.tbl_tab2)
        self.tab_db.addTab(self.lay_tab2, _fromUtf8(""))

        item = self.tbl_tab2.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Property", None))
        item = self.tbl_tab2.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Value", None))
        self.tab_db.setTabText(self.tab_db.indexOf(self.lay_tab2), _translate("Form", "Tab 2", None))
