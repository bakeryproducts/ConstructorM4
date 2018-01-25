# TODO cleanup input for characters
# TODO carefully separate inputs
# TODO all input lines uses int()!
# TODO colors can be obtained from materials db!
# TODO lock input fields at addomp material
# TODO adding custom materials;
# TODO selecting feature works dumb : geoobject.showplane
# TODO decide whta to do with materials databases
# TODO local axis on constrain


import sys
from glwidget import *
import pickle
from CNST.clGEOOBJ import GEOOBJ
from addcomp_ui import Ui_wid_addcomp
from crearray_ui import Ui_crearray
from materials_ui import Ui_materials
from creconstrained_ui import Ui_creconstrained

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.wsizew,self.wsizeh=1200,600
        self.wox,self.woy=100,100
        self.setGeometry(100,100,100,100)

        self.setupUi(self)

        self.parents = []
        self.parentsitems=[]
        self.components = []
        self.treeids = {}
        self.activecompid = 0
        self.idcounter = 1
        self.materials=[]
        self.fexit=False

    self.horizontalLayout.addWidget(self.glbox)
    self.glwidget = GLWidget()
    mainLayout = QtGui.QHBoxLayout()
    mainLayout.addWidget(self.glwidget)
    self.glbox.setLayout(mainLayout)

    self.tre_manager.itemChanged.connect(self.act_tre_check)
    self.btn_setrot.clicked.connect(self.act_btn_rotation)
    self.btn_setpos.clicked.connect(self.act_btn_position)

    self.tre_manager.setHeaderLabel("Target")
    self.actionActive_Armor.triggered.connect(self.act_btn_add_aa)
    self.actionHelp.triggered.connect(self.act_btn_help)
    self.actionArrays.triggered.connect(self.act_btn_arrays)
    self.action_Constrain.triggered.connect(self.act_btn_constrain)
    self.actionManage.triggered.connect(self.act_btn_materials)
    self.actionEdit.triggered.connect(self.act_btn_edit)
    self.actionDelete.triggered.connect(self.act_btn_delete)
    self.actionClose.triggered.connect(self.act_btn_export)
    self.actionImport.triggered.connect(self.act_btn_saveas)
    self.actionLoad.triggered.connect(self.act_btn_load)

    self.tre_manager.itemSelectionChanged.connect(self.act_tre_test)
    self.tre_manager.itemClicked.connect(self.act_tre_test)

    self.glwidget.mode = "pick0"
    self.disablelay(True)
    self.disablebtn(True)




    def act_btn_add_aa(self):
        filedialog = QtGui.QFileDialog(self)
        filepath = filedialog.getOpenFileName(self, "Open STL geometry", "CNST\GEO\dz.stl", filter="stl (*.stl *.)")
        # filepath = "C:\\Users\\User\Documents\GitHub\ConstructorM4\CNST\GEO\\dz.stl"
        if filepath:
            self.act_btn_add(filepath)

    def act_btn_add(self, path):
        self.addwind = Ui_wid_addcomp()
        self.addwind.show()
        self.addwind.newwobj(path, self)


    def act_btn_delete(self):
        answer = QtGui.QMessageBox.question(
            self,
            'Delete component',
            'Are you sure?',
            QtGui.QMessageBox.Yes,
            QtGui.QMessageBox.No)
        if answer == QtGui.QMessageBox.Yes:
            self.delcomp(self.activecomp)
            self.activecomp = None
            self.disablebtn(True)


    def act_btn_help(self):
        self.act_btn_add_aa()
        self.act_btn_add_aa()
        self.test()


    def act_btn_arrays(self):
        self.arrayswind = Ui_crearray(self.wox + self.frameGeometry().width() - 294, self.woy + 20)
        self.arrayswind.loadinit(self)
        self.arrayswind.show()


    def act_btn_constrain(self):
        self.constrainwind = Ui_creconstrained(self.wox + self.frameGeometry().width() - 294, self.woy + 20)
        self.constrainwind.loadinit(self)
        self.constrainwind.show()


    def act_btn_materials(self):
        self.materialswind = Ui_materials()
        self.materialswind.loadinit(self)
        self.materialswind.show()


    def act_btn_edit(self):
        category = self.activecomp.categoryname  # .text(0)
        if category == 'Main components':
            self.addwind = Ui_wid_addcomp()
            self.addwind.show()
            self.addwind.newwobj(self.activecomp, self)
        else:
            pass


    def trywrite(self, text, file):
        try:
            file.write(text)
        except UnicodeEncodeError:
            file.write(text.encode('cp1251').decode('latin1'))


    def act_btn_export(self):
        filedialog = QtGui.QFileDialog(self)
        path = filedialog.getSaveFileName(self, "Save Model As", "RESULTS\EXPORT.trg", filter="trg (*.trg *.)")
        if path:
            # path = 'C:/Users/User/Desktop/OOEF2017/InGEOBDS/TARGET.trg'
            # path = "RESULTS/NEW.TRG"
            intro = ':Цель агрегатная Target\n'
            # br = ':броня '
            # poi = ':точки\n'
            # fac = ':грани 0\n'
            outro = ':end'

            with open(path, 'w') as f:
                self.trywrite(intro, f)
                for i, comp in enumerate(self.components, start=1):
                    comp.export(f, i)
                self.trywrite(outro, f)


    def saveobj(self, obj, file):
        with open(file, 'wb') as output:
            pickle.dump(obj, output, -1)


    def loadobj(self, file):
        with open(file, 'rb') as input:
            return pickle.load(input)


    def act_btn_saveas(self):
        filedialog = QtGui.QFileDialog(self)
        file = filedialog.getSaveFileName(self, "Save Model As", "SAVES\SAVECOMP.sav", filter="sav (*.sav *.)")
        if file:
            # file = 'RESULTS\SAVECOMP.sav'
            self.saveobj([self.components, GEOOBJ._arids], file)


    def act_btn_load(self):
        filedialog = QtGui.QFileDialog(self)
        file = filedialog.getOpenFileName(self, "Load Model", "SAVES\SAVECOMP.sav", filter="sav (*.sav *.)")
        if file:
            for comp in reversed(self.components):
                self.delcomp(comp)
            # file = 'RESULTS\SAVECOMP.sav'
            tempcomps, tids = self.loadobj(file)
            GEOOBJ._arids = tids
            for comp in tempcomps:
                catname = comp.categoryname  # .text(0)
                self.pushcomponent(comp.getcopy(), catname)
                for mat in comp.matarr:
                    if mat not in self.materials:
                        self.materials.append(mat)
            self.glwidget.upmat()


    def act_btn_rotation(self):
        text = self.ln_rot.text()
        x, y, z = [int(el) for el in text.split(',')]
        ang = (x, y, z)
        self.activecomp.geoobj.setrotate(ang)
        self.glwidget.upmat()
        print(x, y, z)


    def act_btn_position(self):
        text = self.ln_pos.text()
        x, y, z = [int(el) for el in text.split(',')]
        pos = (x, y, z)
        self.activecomp.geoobj.setcoord(pos)
        self.glwidget.upmat()
        print(x, y, z)


    def act_tre_check(self, item, column):
        # checkboxes in tree
        changecomp = self.findcomp(item.text(0))
        self.tre_manager.blockSignals(True)
        if item.checkState(0) == QtCore.Qt.Checked:
            self.glwidget.delinvisible(changecomp)
        elif item.checkState(0) == QtCore.Qt.Unchecked:
            self.glwidget.addinvisible(changecomp)
        self.tre_manager.blockSignals(False)


    def act_tre_test(self):
        # one click selection in tree
        getselected = self.tre_manager.selectedItems()
        if getselected:
            activetree = getselected[0]
            activecategory = activetree.text(0)

            if activecategory in self.parents:
                self.disablelay(True)
                self.clearlines()
                self.activecomp = None  # self.getcompbycat(activecategory)
                self.disablebtn(True)

            else:
                self.disablelay(False)
                self.activecomp = self.findcomp(getselected[0].text(0))[0]
                self.disablebtn(False)


    def pushcomponent(self, comp, categoryname):
        # comp.category = self.setcategory(categoryname)
        comp.categoryname = categoryname
        self.components.append(comp)
        self.treenewentry(comp)
        self.glwidget.addobj(comp.getgeo())
        self.activecomp = comp  # [comp]


    def treenewentry(self, comp):
        name = comp.getname()
        name = str(self.idcounter) + ".  " + name
        # category = comp.category
        category = self.setcategory(comp.categoryname)
        child = QtGui.QTreeWidgetItem(category)
        child.setText(0, name)
        child.setCheckState(0, QtCore.Qt.Checked)
        child.setFlags(child.flags())
        self.treeids[name] = comp  # self.idcounter
        self.idcounter += 1
        self.tre_manager.clearSelection()
        self.activecomp = None
        self.disablebtn(True)


        # go from widget item in tree to real representing object id


    def findcomp(self, treewiditemtext):
        self.tre_manager.blockSignals(True)
        key = treewiditemtext
        try:
            res = [self.treeids[key]]
        except:
            # print(self.getcompbycat(key))
            res = self.getcompbycat(key)
        self.tre_manager.blockSignals(False)
        return res


        # set new type in tree


    def setcategory(self, cat):
        catitem = self.tre_manager.findItems(cat, QtCore.Qt.MatchFixedString)
        if not catitem:
            parent = QtGui.QTreeWidgetItem(self.tre_manager)
            parent.setText(0, cat)
            parent.setFlags(parent.flags() | QtCore.Qt.ItemIsTristate | QtCore.Qt.ItemIsUserCheckable)
            parent.setCheckState(0, QtCore.Qt.Checked)
            self.parents.append(cat)
            self.parentsitems.append(parent)
            return parent
        else:
            return catitem[0]


    def getcompbycat(self, cat):
        ids = []
        for comp in self.components:
            if comp.categoryname == cat:  # .text(0) == cat:
                ids.append(comp.getid())
        return ids


    def clearlines(self):
        self.ln_pos.setText("0,0,0")
        self.ln_rot.setText("0,0,0")


    def disablelay(self, bool):
        layers = self.lay_pos, self.lay_rot
        try:
            for lay in layers:
                for i in reversed(range(lay.count())):
                    lay.itemAt(i).widget().setDisabled(bool)
        except Exception as e:
            print(e)

            # adding components with parent heads from child windows


    def disablebtn(self, bool):
        self.actionEdit.setDisabled(bool)
        self.actionDelete.setDisabled(bool)


    def delcomp(self, comp):
        # print(self.components)
        # print(comp)
        self.components.remove(comp)
        self.glwidget.objects.remove(comp.getgeo())

        parent = self.tre_manager.findItems(comp.categoryname, QtCore.Qt.MatchFixedString)[0]

        for childind in range(parent.childCount()):
            if self.treeids[parent.child(childind).text(0)] is comp:
                del (self.treeids[parent.child(childind).text(0)])
                parent.removeChild(parent.child(childind))
                break
        if parent.childCount() == 0:
            (parent.parent() or self.tre_manager.invisibleRootItem()).removeChild(parent)


    def test(self):
        pass


    def getcompbygeoid(self, id):
        for comp in self.components:
            if comp.getid() == id:
                return comp


    def closeEvent(self, event):
        answer = QtGui.QMessageBox.question(
            self,
            'QUIT',
            'Are you sure?',
            QtGui.QMessageBox.Yes,
            QtGui.QMessageBox.No)
        if answer == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec_())
#########################

import sys
from glwidget import *
import CNST.clELEM
import CNST.clTARGETMAIN


class Ui_wid_addcomp(QtGui.QWidget):
    def __init__(self):
        super(Ui_wid_addcomp, self).__init__()
        #self.mainwindow=0
        self.setupUi(self)
        self.fmouseclick = False
        self.category = "Main components"
        self.thickness = 13

    self.glwidget = GLWidget()
    mainLayout = QtGui.QHBoxLayout()
    mainLayout.addWidget(self.glwidget)
    self.glbox.setLayout(mainLayout)
    self.glwidget.mode = "pick0"

    self.btn_setname.clicked.connect(self.act_btn_setname)
    self.btn_ok.clicked.connect(self.act_btn_ok)
    self.btn_cancel.clicked.connect(self.close)
    self.btn_startselect.clicked.connect(self.act_btn_startselect)
    self.btn_set.clicked.connect(self.act_btn_set)
    self.btn_startselect.setCheckable(True)
    self.btn_selectall.setCheckable(True)
    self.btn_selectall.clicked.connect(self.act_btn_selectall)
    self.tbl_facestable.setSelectionBehavior(QtGui.QTableView.SelectRows)
    # self.tbl_facestable.clicked.connect(self.act_tblclicked)
    self.tbl_facestable.itemSelectionChanged.connect(self.act_tblselchanged)
    self.tbl_facestable.itemChanged.connect(self.act_tblchanged)

    self.glwidget.ObjSelected.connect(self.select)

    def select(self,arg):
        plane = arg[1]
        self.fmouseclick=True
        self.tbl_facestable.selectRow(plane-1)
        self.fmouseclick = False

    def act_btn_startselect(self):
        self.glwidget.dropselection()
        self.btn_selectall.setChecked(False)
        self.glwidget.mode = "pickmany"
        self.btn_set.setEnabled(True)

    def act_btn_selectall(self):
        self.glwidget.dropselection()
        self.btn_startselect.setChecked(False)
        self.glwidget.mode = "pickwhole"
        self.btn_set.setEnabled(True)

    def act_btn_set(self):

        thickness = int(self.ln_thickness.text())
        material = self.cmb_material.currentText()

        self.ln_thickness.setText("0")

        for objid, planeid in self.glwidget.selection:
            self.comp.setthick(planeid-1, thickness)
            self.editrow(planeid - 1, str(thickness),str(material))

        self.glwidget.mode = "pick0"
        self.glwidget.dropselection()
        self.btn_startselect.setChecked(False)
        self.btn_selectall.setChecked(False)
        self.btn_set.setEnabled(False)

    def act_btn_ok(self):
        self.glwidget.doneCurrent()
        self.mainwindow.glwidget.makeCurrent()
        self.mainwindow.pushcomponent(self.comp.getcopy(), self.category)
        self.glwidget.objects.clear()
        self.comp.export()
        self.close()

    def act_btn_setname(self):
        name = self.ln_name.text()
        self.comp.setname(name)
        self.lbl_gl.setText("Component preview: " + name)

    def act_tblclicked(self,row):
        self.glwidget.dropselection()
        self.glwidget.setselection((self.glwidget.objects[0].getid(),1+row.row()))

    def act_tblselchanged(self):
        if not self.fmouseclick:
            itemid = 1+self.tbl_facestable.selectedItems()[0].row()
            self.glwidget.dropselection()
            self.glwidget.setselection((self.glwidget.objects[0].getid(), itemid))

    def act_tblchanged(self,item):
        row = item.row()
        value = item.text()
        column = item.column()
        if column == 0:
            self.comp.setfacename(value,row)
        elif column == 1:
            self.comp.thickarr[row] = value
        elif column == 2:
            pass
            #self.comp.matarr[row] = value

    def newrow(self, rowname, rowvalue,rowmat):
        rowPosition = self.tbl_facestable.rowCount()
        self.tbl_facestable.insertRow(rowPosition)
        item1 = QtGui.QTableWidgetItem(rowname)
        item1.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)

        item2 = QtGui.QTableWidgetItem(rowvalue)
        item2.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)

        item3 = QtGui.QTableWidgetItem(rowmat)
        item3.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)

        #item1.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        self.tbl_facestable.setItem(rowPosition, 0, item1)
        self.tbl_facestable.setItem(rowPosition, 1, item2)
        self.tbl_facestable.setItem(rowPosition, 2, item3)

    def editrow(self, rowPosition, rowValue,rowMat):
        item1 = QtGui.QTableWidgetItem(rowValue)
        item1.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)

        item2 = QtGui.QTableWidgetItem(rowMat)
        item2.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)

        self.tbl_facestable.setItem(rowPosition, 1, item1)
        self.tbl_facestable.setItem(rowPosition, 2, item2)

    def newwobj(self, path, mainw):
        self.mainwindow = mainw

        geos = techs.georedo(path, 100)
        name = path.split("/")[-1]
        geoobj = clGEOOBJ.GEOOBJ(geos, name)
        self.comp = CNST.clTARGETMAIN.TARGETMAIN(geoobj)

        matnames=[]
        for mat in self.mainwindow.materials:
            matnames.append(mat.getname())
        if self.comp.defmat.getname() not in matnames:
            self.mainwindow.materials.append(self.comp.defmat)

        self.glwidget.addobj(self.comp.getgeo())
        self.ln_name.setText(name)
        self.lbl_gl.setText("Component preview: " + name)
        self.btn_set.setEnabled(False)

        self.cmbinit()

        for facename in self.comp.facesnames:
            self.newrow(facename, str(self.comp.defthick),self.comp.defmat.getname())

        # TODO IMHERE
        #self.act_btn_ok()

    def cmbinit(self):

        args = []
        for mat in self.mainwindow.materials:
            args.append(mat.getname())
        self.cmb_material.addItems(args)


#########################

class Ui_crearray(QtGui.QWidget):
    def __init__(self):
        super(Ui_crearray, self).__init__()
        self.setupUi(self)
        self.selcomp = 0
        self.nx,self.ny,self.dx,self.dy,self.ang = 0,0,0,0,0

    self.btn_save.clicked.connect(self.act_btn_save)
    self.cmb_compselect.currentIndexChanged.connect(self.act_cmb_change)

    def act_btn_save(self):
        self.mainwindow.const
        #self.close()

    def loadinit(self,mainw):
        self.mainwindow = mainw
        self.components = mainw.components
        self.cmb_compselect.addItems(list(mainw.treeids.keys()))
        self.nx = self.ln_nfirst.text()
        self.ny = self.ln_nsecond.text()
        self.dx = self.ln_stepfirst.text()
        self.dy = self.ln_stepsecond.text()
        self.ang = self.ln_
    def act_cmb_change(self,i):
        self.selcomp = self.components[i-1]
        print(self.cmb_compselect.currentText())

#########################

class Ui_creconstrained(QtGui.QWidget):
    def __init__(self):
        super(Ui_creconstrained, self).__init__()
        #self.mainwindow=0

        self.fbase,self.fmove = False,False
        self.setupUi(self)

    self.btn_basepick.clicked.connect(self.act_btn_basepick)
    self.btn_movepick.clicked.connect(self.act_btn_movepick)
    self.btn_btnsshow.clicked.connect(self.act_btn_btnsshow)
    self.btn_btnssave.clicked.connect(self.act_btn_btnssave)
    self.btn_btnscancel.clicked.connect(self.act_btn_btnscancel)

    def loadinit(self,mainw):
        self.mainwindow = mainw
        self.mainwindow.glwidget.ObjSelected.connect(self.select)

    def select(self,arg):
        if self.fbase:
            self.ln_basecomp = arg[0][0]
            self.ln_baseplane = arg[0][1]
        elif self.fmove:
            self.ln_movecomp = arg[0][0]
            self.ln_moveplane = arg[0][1]

    def act_btn_basepick(self):
        self.mainwindow.glwidget.dropselection()
        self.mainwindow.glwidget.setmode("pickone")
        self.fbase=True
        self.fmove=False

    def act_btn_movepick(self):
        self.mainwindow.glwidget.dropselection()
        self.mainwindow.glwidget.setmode("pickone")
        self.fbase = False
        self.fmove = True

    def act_btn_btnsshow(self):
        pass

    def act_btn_btnssave(self):
        pass

    def act_btn_btnscancel(self):
        self.mainwindow.glwidget.dropselection()
        self.mainwindow.glwidget.setmode("pick0")
        self.close()


#########################

from PyQt4 import QtCore, QtGui
import MATERIALS.clMATERIAL as MATERIAL
import MATERIALS.db as matdb


class Ui_materials(QtGui.QWidget):
    def __init__(self):
        super(Ui_materials, self).__init__()
        #self.mainwindow = 0
        self.db = matdb.DB('MATERIALS\\GOST.xml')

        self.setupUi(self)
        self.loadtree()

    self.tre_tab1.itemSelectionChanged.connect(self.act_tre_tab)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Manage materials", None))
        self.lbl_target0mat.setText(_translate("Form", "Target materials", None))
        self.lbl_target0prop.setText(_translate("Form", "Material properties", None))
        self.tre_target.headerItem().setText(0, _translate("Form", "Target", None))
        item = self.tbl_target.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Property", None))
        item = self.tbl_target.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Value", None))
        self.btn_load.setText(_translate("Form", "UP", None))
        self.btn_del.setText(_translate("Form", "DOWN", None))
        self.lbl_db1mat.setText(_translate("Form", "Database materials", None))
        self.lbl_db1prop.setText(_translate("Form", "Material properties", None))
        item = self.tbl_tab1.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Property", None))
        item = self.tbl_tab1.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Value", None))
        self.tab_db.setTabText(self.tab_db.indexOf(self.lay_tab1), _translate("Form", "Tab 1", None))
        self.tab_db.setTabText(self.tab_db.indexOf(self.tab_2), _translate("Form", "Tab 2", None))

    def act_tre_tab(self):
        getselected = self.tre_tab1.selectedItems()
        activeitem = getselected[0]
        activet = activeitem.text(0)
        if activet not in self.categories:
            self.droptable()
            self.loadtable(activet)

    def droptable(self):
        self.tbl_tab1.setRowCount(0)

    def loadtable(self, matitem):
        props = self.db.getmat(matitem)
        for prop in props:
            self.newrow(*prop)

    def newrow(self, rowname, rowvalue):
        rowPosition = self.tbl_tab1.rowCount()
        self.tbl_tab1.insertRow(rowPosition)
        item1 = QtGui.QTableWidgetItem(rowname)
        # item1.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)

        item2 = QtGui.QTableWidgetItem(rowvalue)
        # item2.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)

        self.tbl_tab1.setItem(rowPosition, 0, item1)
        self.tbl_tab1.setItem(rowPosition, 1, item2)

    def loadtree(self):
        self.tre_tab1.headerItem().setText(0, _fromUtf8("GOST"))
        self.categories = self.db.getcats()

        for cat in self.categories:
            parent = QtGui.QTreeWidgetItem(self.tre_tab1)
            parent.setText(0, cat)
            # parent.setFlags(parent.flags() | QtCore.Qt.ItemIsTristate | QtCore.Qt.ItemIsUserCheckable)
            # parent.setCheckState(0, QtCore.Qt.Checked)
            mats = self.db.getcatmat(cat)
            for mat in mats:
                child = QtGui.QTreeWidgetItem(parent)
                child.setText(0, mat)
                # child.setCheckState(0, QtCore.Qt.Checked)
                child.setFlags(child.flags())

    def loadinit(self, mainw):
        self.mainwindow = mainw