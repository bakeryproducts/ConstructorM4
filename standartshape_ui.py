import sys
from glwidget import *
import CNST.clELEM
import CNST.clDZ
import CNST.FC.boxmaker
import CNST.geoimport
import CNST.clSHAPE
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


class Ui_wid_addshape(QtGui.QWidget):
    def __init__(self):
        super(Ui_wid_addshape, self).__init__()
        # self.mainwindow=0
        self.setupUi(self)
        # self.shapedict = {'box': self.crbox, 'cyl': self.crcyl,
        #                   'con': self.crcon, 'pri': self.crpri,
        #                   'sph': self.crsph}
        self.fshape = 'box'
        self.category = 'Shape'

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(900, 400)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.rdb_cube = QtGui.QRadioButton(Form)
        self.rdb_cube.setObjectName(_fromUtf8("rdb_cube"))
        self.verticalLayout.addWidget(self.rdb_cube)
        self.rdb_cyl = QtGui.QRadioButton(Form)
        self.rdb_cyl.setObjectName(_fromUtf8("rdb_cyl"))
        self.verticalLayout.addWidget(self.rdb_cyl)
        self.rdb_cone = QtGui.QRadioButton(Form)
        self.rdb_cone.setObjectName(_fromUtf8("rdb_cone"))
        self.verticalLayout.addWidget(self.rdb_cone)
        self.rdb_prism = QtGui.QRadioButton(Form)
        self.rdb_prism.setObjectName(_fromUtf8("rdb_prism"))
        self.verticalLayout.addWidget(self.rdb_prism)
        self.rdb_sph = QtGui.QRadioButton(Form)
        self.rdb_sph.setObjectName(_fromUtf8("rdb_sph"))
        self.verticalLayout.addWidget(self.rdb_sph)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.glbox = QtGui.QWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.glbox.sizePolicy().hasHeightForWidth())
        self.glbox.setSizePolicy(sizePolicy)
        self.glbox.setObjectName(_fromUtf8("glbox"))
        self.horizontalLayout.addWidget(self.glbox)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_4.addWidget(self.label_6)
        self.ln_name = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_name.sizePolicy().hasHeightForWidth())
        self.ln_name.setSizePolicy(sizePolicy)
        self.ln_name.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_name.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_name.setObjectName(_fromUtf8("ln_name"))
        self.horizontalLayout_4.addWidget(self.ln_name)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_5.addWidget(self.label_5)
        self.ln_cat = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_cat.sizePolicy().hasHeightForWidth())
        self.ln_cat.setSizePolicy(sizePolicy)
        self.ln_cat.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_cat.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_cat.setObjectName(_fromUtf8("ln_cat"))
        self.horizontalLayout_5.addWidget(self.ln_cat)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.label = QtGui.QLabel(Form)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.tbl_params = QtGui.QTableWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbl_params.sizePolicy().hasHeightForWidth())
        self.tbl_params.setSizePolicy(sizePolicy)
        self.tbl_params.setMaximumSize(QtCore.QSize(240, 16777215))
        self.tbl_params.setObjectName(_fromUtf8("tbl_params"))
        self.tbl_params.setColumnCount(2)
        self.tbl_params.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        self.tbl_params.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        self.tbl_params.setHorizontalHeaderItem(1, item)
        self.verticalLayout_2.addWidget(self.tbl_params)
        self.line = QtGui.QFrame(Form)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_2.addWidget(self.line)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.ln_remesh = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_remesh.sizePolicy().hasHeightForWidth())
        self.ln_remesh.setSizePolicy(sizePolicy)
        self.ln_remesh.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_remesh.setObjectName(_fromUtf8("ln_remesh"))
        self.horizontalLayout_2.addWidget(self.ln_remesh)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.btn_remesh = QtGui.QPushButton(Form)
        self.btn_remesh.setObjectName(_fromUtf8("btn_remesh"))
        self.verticalLayout_2.addWidget(self.btn_remesh)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.btn_ok = QtGui.QPushButton(Form)
        self.btn_ok.setObjectName(_fromUtf8("btn_ok"))
        self.horizontalLayout_3.addWidget(self.btn_ok)
        self.btn_cancel = QtGui.QPushButton(Form)
        self.btn_cancel.setObjectName(_fromUtf8("btn_cancel"))
        self.horizontalLayout_3.addWidget(self.btn_cancel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.glwidget = GLWidget()
        mainLayout = QtGui.QHBoxLayout()
        mainLayout.addWidget(self.glwidget)
        self.glbox.setLayout(mainLayout)
        # self.glwidget.mode = "pick0"

        self.rdb_cube.clicked.connect(self.act_rdb_box)
        self.rdb_cyl.clicked.connect(self.act_rdb_cyl)
        self.rdb_cone.clicked.connect(self.act_rdb_con)
        self.rdb_prism.clicked.connect(self.act_rdb_pri)
        self.rdb_sph.clicked.connect(self.act_rdb_sph)

        # self.btn_remesh.clicked.connect(self.act_btn_remesh)
        self.btn_ok.clicked.connect(self.act_btn_ok)
        self.btn_cancel.clicked.connect(self.close)

        self.tbl_params.setSelectionBehavior(QtGui.QTableView.SelectRows)
        self.tbl_params.itemChanged.connect(self.tbl_change)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Shape generator", None))
        self.label_4.setText(_translate("Form", "Standart shapes:", None))
        self.rdb_cube.setText(_translate("Form", "Cube", None))
        self.rdb_cyl.setText(_translate("Form", "Cylinder", None))
        self.rdb_cone.setText(_translate("Form", "Cone", None))
        self.rdb_prism.setText(_translate("Form", "Prism", None))
        self.rdb_sph.setText(_translate("Form", "Sphere", None))
        self.label_6.setText(_translate("Form", "Component name:", None))
        self.ln_name.setText(_translate("Form", "Part", None))
        self.label_5.setText(_translate("Form", "Category name:", None))
        self.ln_cat.setText(_translate("Form", "Standart", None))
        self.label.setText(_translate("Form", "Shape: ", None))
        item = self.tbl_params.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Parameter", None))
        item = self.tbl_params.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Value", None))
        self.label_2.setText(_translate("Form", "Remeshing", None))
        self.label_3.setText(_translate("Form", "Max offset distance:", None))
        self.ln_remesh.setText(_translate("Form", "0.01", None))
        self.btn_remesh.setText(_translate("Form", "Apply remeshing", None))
        self.btn_ok.setText(_translate("Form", "OK", None))
        self.btn_cancel.setText(_translate("Form", "CANCEL", None))

    def act_btn_ok(self):
        self.glwidget.doneCurrent()
        self.mainwindow.glwidget.makeCurrent()
        comptype = self.ln_cat.text()
        self.comp.comptype = comptype
        self.comp.setname(self.ln_name.text())
        self.mainwindow.pushcomponent(self.comp.getcopy(), self.category)
        self.glwidget.objects = []
        self.glwidget.upmat()
        del (self.comp)
        self.close()

    def newrow(self, rowname, rowvalue):
        rowPosition = self.tbl_params.rowCount()
        self.tbl_params.insertRow(rowPosition)
        item1 = QtGui.QTableWidgetItem(rowname)
        item1.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item1.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        item2 = QtGui.QTableWidgetItem(rowvalue)
        item2.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)

        self.tbl_params.setItem(rowPosition, 0, item1)
        self.tbl_params.setItem(rowPosition, 1, item2)

    def editrow(self, rowPosition, rowValue, rowMat, rowcat):
        item1 = QtGui.QTableWidgetItem(rowValue)
        item1.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)

        item2 = QtGui.QTableWidgetItem(rowMat)
        item2.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item2.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        item3 = QtGui.QTableWidgetItem(rowcat)
        item3.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item3.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        self.tbl_facestable.setItem(rowPosition, 1, item1)
        self.tbl_facestable.setItem(rowPosition, 2, item2)
        self.tbl_facestable.setItem(rowPosition, 3, item3)

    def loadinit(self, mainw):
        self.mainwindow = mainw
        # self.recreate()

    def act_rdb_box(self):
        self.tbl_params.blockSignals(True)
        self.tbl_params.setRowCount(0)
        self.newrow('W', '100')
        self.newrow('H', '100')
        self.newrow('D', '100')
        self.fshape = 'box'
        self.tbl_params.blockSignals(False)
        self.crbox()

    def act_rdb_cyl(self):
        self.tbl_params.blockSignals(True)
        self.tbl_params.setRowCount(0)
        self.newrow('R', '100')
        self.newrow('H', '200')
        self.fshape = 'cyl'
        self.tbl_params.blockSignals(False)
        self.crcyl()

    def act_rdb_con(self):
        self.tbl_params.blockSignals(True)
        self.tbl_params.setRowCount(0)
        self.newrow('R1', '50')
        self.newrow('R2', '100')
        self.newrow('H', '200')
        self.fshape = 'con'
        self.tbl_params.blockSignals(False)
        self.crcon()

    def act_rdb_pri(self):
        self.tbl_params.blockSignals(True)
        self.tbl_params.setRowCount(0)
        self.newrow('P1', '0,0,0')
        self.newrow('P2', '100,0,0')
        self.newrow('P3', '0,100,0')
        self.newrow('H', '200')
        self.fshape = 'pri'
        self.tbl_params.blockSignals(False)
        self.crpri()

    def act_rdb_sph(self):
        self.tbl_params.blockSignals(True)
        self.tbl_params.setRowCount(0)
        self.newrow('R', '100')
        self.fshape = 'sph'
        self.tbl_params.blockSignals(False)
        self.crsph()

    def tbl_change(self):
        shapedict = {'box': self.crbox, 'cyl': self.crcyl,
                     'con': self.crcon, 'pri': self.crpri,
                     'sph': self.crsph}
        shapefunc = shapedict[self.fshape]
        shapefunc()

    def crbox(self):
        name = 'Box'
        pdict = self.loadparams()
        w, d, h = pdict['W'], pdict['D'], pdict['H']
        pie = CNST.FC.boxmaker.Box(w, d, h)
        print(w, d, h)
        geos = pie.getgeo()
        geoobj = clGEOOBJ.GEOOBJ(geos, name)
        # self.comp = CNST.clSHAPE.SHAPE(geoobj)
        self.comp = CNST.clDZ.DZ(geoobj, 1, 1, 1, 1)
        self.glinit()

    def crcyl(self):
        name = 'Cylinder'
        pdict = self.loadparams()
        r, h = pdict['R'], pdict['H']
        pie = CNST.FC.boxmaker.Cylinder(r, h)
        # pie = CNST.FC.boxmaker.Cylinder(10, 10)
        geos = pie.getgeo()
        geoobj = clGEOOBJ.GEOOBJ(geos, name)
        self.comp = CNST.clSHAPE.SHAPE(geoobj)
        self.glinit()

    def crcon(self):
        name = 'Cone'
        pdict = self.loadparams()
        r1, r2, h = pdict['R1'], pdict['R2'], pdict['H']
        pie = CNST.FC.boxmaker.Cone(r1, r2, h)
        geos = pie.getgeo()
        geoobj = clGEOOBJ.GEOOBJ(geos, name)
        self.comp = CNST.clSHAPE.SHAPE(geoobj)
        self.glinit()

    def crpri(self):
        name = 'Prism'
        pdict = self.loadparams()
        p1, p2, p3, h = pdict['P1'], pdict['P2'], pdict['P3'], pdict['H']
        pie = CNST.FC.boxmaker.Prism(p1, p2, p3, h)
        geos = pie.getgeo()
        geoobj = clGEOOBJ.GEOOBJ(geos, name)
        self.comp = CNST.clSHAPE.SHAPE(geoobj)
        self.glinit()

    def crsph(self):
        name = 'Sphere'
        pdict = self.loadparams()
        r = pdict['R']
        pie = CNST.FC.boxmaker.Sphere(r)
        geos = pie.getgeo()
        geoobj = clGEOOBJ.GEOOBJ(geos, name)
        self.comp = CNST.clSHAPE.SHAPE(geoobj)
        self.glinit()

    def glinit(self):
        self.glwidget.dropselection()
        self.glwidget.cleartmpobjs()
        self.glwidget.objects.clear()
        self.glwidget.addobj(self.comp.getgeo())
        self.glwidget.upmat()

    def tabinit(self):
        self.btn_set.setEnabled(False)
        for facen, facet, facem in zip(self.comp.facesnames, self.comp.thickarr, self.comp.matarr):
            self.newrow(facen, str(facet), facem.getname(), facem.getcategory())

    def loadparams(self):
        pdict = {}
        for row in range(self.tbl_params.rowCount()):
            k = self.tbl_params.item(row, 0).text()
            vsst = self.tbl_params.item(row, 1).text().split(',')
            v = [float(vst) for vst in vsst]
            if len(v) == 1:
                v = v[0]
            pdict[k] = v
        return pdict

