import CNST.clELEM
import CNST.clTARGETMAIN
from GL.glwidget import *
from PyQt5 import QtCore, QtGui, QtWidgets
from UI.pys.addcomp import Ui_wid_addcomp


#from CNST.remesh import remeshing
#import sys

import re


class new_comp(QtWidgets.QWidget, Ui_wid_addcomp):
    def __init__(self, parent=None):
        super(new_comp, self).__init__(parent)
        self.setupUi(self)

        self.fedit = False
        self.fmouseclick = False
        self.category = "Main components"
        self.thickness = 13

        self.glwidget = GLWidget()
        mainLayout = QtWidgets.QHBoxLayout()
        mainLayout.addWidget(self.glwidget)
        self.glbox.setLayout(mainLayout)
        self.glwidget.mode = "pick0"

        self.btn_ok.clicked.connect(self.act_btn_ok)
        self.btn_cancel.clicked.connect(self.close)
        self.btn_startselect.clicked.connect(self.act_btn_startselect)
        self.btn_set.clicked.connect(self.act_btn_set)
        self.btn_startselect.setCheckable(True)
        self.btn_selectall.setCheckable(True)
        self.btn_selectall.clicked.connect(self.act_btn_selectall)

        #self.btn_remesh.clicked.connect(self.act_btn_remesh)
        self.btn_scale.clicked.connect(self.act_btn_scale)

        self.tbl_facestable.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        # self.tbl_facestable.clicked.connect(self.act_tblclicked)
        self.tbl_facestable.itemSelectionChanged.connect(self.act_tblselchanged)
        self.tbl_facestable.itemChanged.connect(self.act_tblchanged)

        self.glwidget.ObjSelected.connect(self.select)


    def select(self, arg):
        plane = arg[1]
        self.fmouseclick = True
        self.tbl_facestable.selectRow(plane - 1)
        self.fmouseclick = False

    def act_btn_startselect(self):
        self.glwidget.dropselection()
        self.btn_selectall.setChecked(False)
        self.glwidget.mode = "pickmany"
        self.glwidget.setFocus()
        self.glwidget.addtoconsole('Hold Control for mouseover selection.')
        self.glwidget.addtoconsole('Picking mode: Multiple faces.')
        self.btn_set.setEnabled(True)
        self.glwidget.upmat()

    def act_btn_selectall(self):
        self.glwidget.dropselection()
        self.btn_startselect.setChecked(False)
        self.glwidget.mode = "pickwhole"
        self.glwidget.addtoconsole('Picking mode: Object.')
        self.btn_set.setEnabled(True)
        self.glwidget.upmat()

    def act_btn_set(self):

        thickness = int(self.ln_thickness.text())
        materialname = self.cmb_material.currentText()
        # for mat in self.materials:
        #     if materialname == mat.getname():
        #         material = mat

        self.ln_thickness.setText("0")

        for objid, planeid in self.glwidget.selection:
            self.comp.setthick(planeid - 1, thickness)
            # self.comp.setmat(planeid - 1, material)
            self.editrow(planeid-1, str(thickness), str(materialname))

        self.glwidget.mode = "pick0"
        self.glwidget.addtoconsole('Picking mode: None.')
        self.glwidget.addtoconsole('Parameters applied.')
        self.glwidget.dropselection()
        self.btn_startselect.setChecked(False)
        self.btn_selectall.setChecked(False)
        self.btn_set.setEnabled(False)

    def act_btn_ok(self):
        self.glwidget.doneCurrent()
        self.mainwindow.glwidget.makeCurrent()
        self.comp.comptype = self.ln_cat.text()
        if self.fedit:
            self.mainwindow.delcomp(self.orgcomp)
            del(self.orgcomp)
        self.comp.setname(self.ln_name.text())
        self.mainwindow.pushcomponent(self.comp.getcopy(), self.category)
        self.glwidget.objects=[]
        self.glwidget.upmat()
        del (self.comp)
        self.close()

    def act_tblclicked(self, row):
        self.glwidget.dropselection()
        self.glwidget.setselection((self.glwidget.objects[0].getid(), 1 + row.row()))

    def act_tblselchanged(self):
        if not self.fmouseclick:
            itemid = 1 + self.tbl_facestable.selectedItems()[0].row()
            self.glwidget.dropselection()
            self.glwidget.setselection((self.glwidget.objects[0].getid(), itemid))

    def act_tblchanged(self, item):
        row = item.row()
        value = item.text()
        column = item.column()
        if column == 0:
            self.comp.setfacename(value, row)
        elif column == 1:
            self.comp.thickarr[row] = int(value)
        elif column == 2:
            pass
            # self.comp.matarr[row] = value

    def newrow(self, rowname, rowvalue, rowmat):
        rowPosition = self.tbl_facestable.rowCount()
        self.tbl_facestable.insertRow(rowPosition)
        item1 = QtWidgets.QTableWidgetItem(rowname)
        item1.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)

        item2 = QtWidgets.QTableWidgetItem(rowvalue)
        item2.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)

        item3 = QtWidgets.QTableWidgetItem(rowmat)
        item3.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item3.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        self.tbl_facestable.setItem(rowPosition, 0, item1)
        self.tbl_facestable.setItem(rowPosition, 1, item2)
        self.tbl_facestable.setItem(rowPosition, 2, item3)

    def editrow(self, rowPosition, rowValue, rowMat):
        item1 = QtWidgets.QTableWidgetItem(rowValue)
        item1.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)

        item2 = QtWidgets.QTableWidgetItem(rowMat)
        item2.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item2.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        self.tbl_facestable.setItem(rowPosition, 1, item1)
        self.tbl_facestable.setItem(rowPosition, 2, item2)

    def newwobj(self, path, mainw, edt=False):
        self.mainwindow = mainw

        if not edt:
            name = re.split('\*|/', path)
            name = re.sub('\.', '', name[-1])

            geos = techs.georedo(path, 10)
            geoobj = clGEOOBJ.GEOOBJ(geos, name)
            self.comp = CNST.clTARGETMAIN.TARGETMAIN(geoobj)
            #self.comp.defmatinit(list(self.mainwindow.materials)[0])
            self.glwidget.addtoconsole('New component: ' + name)

        else:
            self.fedit = True
            self.orgcomp = path
            self.comp = path.getcopy()
            self.ln_cat.setText(self.comp.comptype)
            name = self.comp.getname()
            self.glwidget.addtoconsole('Edit component: ' + name)

        #name = name.split('/')[-1]
        self.ln_name.setText(name)
        self.lbl_gl.setText("Component preview: " + name)
        self.btn_set.setEnabled(False)
        self.glinit()
        self.tabinit()
        self.cmbinit()

        # TODO IMHERE
        #self.act_btn_ok()

    def glinit(self):
        self.glwidget.objects.clear()
        self.glwidget.addobj(self.comp.getgeo())
        self.glwidget.upmat()

    def cmbinit(self):
        self.materials = []
        args = ['DEF_MAT']
        # for mat in self.mainwindow.materials:
        #     self.materials.append(mat)
        #     args.append(mat.getname())

        self.cmb_material.addItems(args)

        # def closeEvent(self, QCloseEvent):
        #     self.act_btn_cancel()

    def tabinit(self):
        for facen, facet in zip(self.comp.facesnames, self.comp.thickarr):
            self.newrow(facen, str(facet), 'DEF_MAT')

    # def act_btn_remesh(self):
    #     self.glwidget.addtoconsole('Remeshing...')
    #     g = self.comp.geoobj
    #     geos = remeshing(list(g.points), list(g.faces))
    #     geoobj = clGEOOBJ.GEOOBJ(geos, self.comp.geoobj.getname())
    #     self.comp = CNST.clTARGETMAIN.TARGETMAIN(geoobj)
    #     self.comp.defmatinit(list(self.mainwindow.materials)[0])
    #     self.tbl_facestable.setRowCount(0)
    #     self.glwidget.addtoconsole('Remeshing is complete.')
    #     self.glinit()
    #     self.tabinit()

    def act_btn_scale(self):
        scale = float(self.ln_scale.text())
        ps = self.comp.geoobj.points[:]
        ps = [np.array([p[0] * scale, p[1] * scale, p[2] * scale]) for p in ps]
        self.comp.geoobj.points = ps
        self.glwidget.addtoconsole('Applied scale: ' + str(scale) + '.')
        # self.glwidget.objects=[]
        # self.glwidget.addobj(self.comp.geoobj)
        self.comp.geoobj.updatenpoints()
        self.glinit()

