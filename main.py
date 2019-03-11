
from PyQt5 import QtCore, QtGui, QtWidgets

from UI.pys.cnst import Ui_MainWindow
from new_comp import new_comp
from move import move
from dir_shoot import dir_shoot
from orb_shoot import orb_shoot
from color import color

from GL.glwidget import *
import pickle


class mainProgram(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(mainProgram, self).__init__(parent)
        self.wsizew, self.wsizeh = 1200, 600
        self.wox, self.woy = 100, 100
        self.setGeometry(100, 100, 100, 100)

        self.setupUi(self)

        self.components = []
        self.activecompid = 0
        self.fexit = False

        self.horizontalLayout.addWidget(self.glbox)
        self.glwidget = GLWidget()
        mainLayout = QtWidgets.QHBoxLayout()
        mainLayout.addWidget(self.glwidget)
        self.glbox.setLayout(mainLayout)

        self.glwidget.mode = "pick0"
        # self.disablelay(True)
        self.disablebtn(True)

        self.actionNew.triggered.connect(self.act_btn_new)
        self.actionfOpen.triggered.connect(self.act_btn_open)

        self.actionSavecomp.triggered.connect(self.act_btn_savecomp)
        self.actionOpencomp.triggered.connect(self.act_btn_opencomp)
        self.actionBasecomp.triggered.connect(self.act_btn_add_basecomp)
        self.actionDeletecomp.triggered.connect(self.act_btn_delete)

        self.actionEdit.triggered.connect(self.act_btn_edit)
        self.actionFree_roaming.triggered.connect(self.act_btn_move)
        self.actionDirectional_shooting.triggered.connect(self.act_btn_dir_shoot)
        self.actionOrbital_shooting.triggered.connect(self.act_btn_orb_shoot)

        self.tre_manager.itemChanged.connect(self.act_tre_check)
        self.tre_manager.setHeaderLabels(["Target", "col1"])
        self.tre_manager.itemSelectionChanged.connect(self.act_tre_test)
        self.tre_manager.itemClicked.connect(self.act_tre_test)
        self.tre_manager.hideColumn(1)

        self.actionFront.triggered.connect(self.act_btn_front)
        self.actionBack.triggered.connect(self.act_btn_back)
        self.actionTop.triggered.connect(self.act_btn_top)
        self.actionBottom.triggered.connect(self.act_btn_bottom)
        self.actionLeft.triggered.connect(self.act_btn_left)
        self.actionRight.triggered.connect(self.act_btn_right)

        self.actionArmor_th.triggered.connect(self.act_btn_armor)
        self.actionColor.triggered.connect(self.act_btn_color)

        self.actionfClose.triggered.connect(self.close)

    def act_btn_new(self):
        for comp in reversed(self.components):
            self.delcomp(comp)
        self.glwidget.objects.clear()
        #db = DB('MATERIALS\\GOST.xml')
        #mat = db.getdefmat()
        #self.materials = {db.exportmat(mat)}
        self.glwidget.addtoconsole('New model.')

    def act_btn_open(self):

        filedialog = QtWidgets.QFileDialog(self)
        file,_ = filedialog.getOpenFileName(self, "Load Model", "SAVES\MODELS\MODEL.svm", filter="svm (*.svm *.)")
        # file = "SAVES\MODELS\\abraplus.svm"
        print(file)
        if file:
            for comp in reversed(self.components):
                self.delcomp(comp)
            # file = 'RESULTS\SAVECOMP.sav'
            tempcomps = self.loadobj(file)
            # GEOOBJ._arids = tids
            for comp in tempcomps:
                comp.setid()
                tc = comp.getcopy()
                catname = tc.categoryname
                self.pushcomponent(tc, catname)

                for mat in comp.matarr:
                    if mat not in self.materials:
                        self.materials.add(mat)
            self.glwidget.upmat()

    def act_btn_add_basecomp(self):
        filedialog = QtWidgets.QFileDialog(self)
        filepath, _ = filedialog.getOpenFileName(self, "Open STL geometry", "CNST/GEO/dz.stl", filter="stl (*.stl *.)")
        # filepath = "C:\\Users\\User\Documents\GitHub\ConstructorM4\CNST\GEO\\cube100.stl"
        if filepath:
            # self.act_btn_add(filepath)
            self.addwind = new_comp()
            self.addwind.show()
            self.addwind.newwobj(filepath, self)

    def act_btn_savecomp(self):
        comp = self.activecomp
        filedialog = QtWidgets.QFileDialog(self)
        file,_ = filedialog.getSaveFileName(self, "Save Component As", "./SAVES/COMPONENTS/" + comp.getname() + ".svc",
                                          filter="svc (*.svc *.)")
        if file:
            # file = 'RESULTS\SAVECOMP.sav'
            print(comp,file)
            self.saveobj(comp, file)
            #comp.save(file)
            self.glwidget.addtoconsole('Component saved as: ' + file)

    def act_btn_opencomp(self):
        filedialog = QtWidgets.QFileDialog(self)
        file,_ = filedialog.getOpenFileName(self, "Load Component", "./SAVES/COMPONENTS/", filter="svc (*.svc *.)")
        if file:
            tempcomp = self.loadobj(file)
            tempcomp.setid()
            comp = tempcomp.getcopy()
            catname = comp.categoryname
            self.pushcomponent(comp, catname)
            self.glwidget.upmat()

    def act_btn_saveas(self):
        filedialog = QtWidgets.QFileDialog(self)
        file, _ = filedialog.getSaveFileName(self, "Save Model As", "SAVES/MODELS/MODEL.svm", filter="svm (*.svm *.)")
        if file:
            # file = 'RESULTS\SAVECOMP.sav'
            self.saveobj(self.components, file)
            self.glwidget.addtoconsole('Model saved as: ' + file)

    def act_btn_edit(self):
        category = self.activecomp.categoryname
        if category == 'Main components':
            self.addwind = new_comp()
            self.addwind.show()
            self.addwind.newwobj(self.activecomp, self, edt=True)
        else:
            pass

    def act_btn_move(self):
        self.movewind = move(self.wox + self.frameGeometry().width() - 294, self.woy + 20)
        self.movewind.loadinit(self)
        self.movewind.show()

    def act_btn_dir_shoot(self):
        self.statswind = dir_shoot()
        self.statswind.show()
        self.statswind.loadinit(self)

    def act_btn_orb_shoot(self):
        self.statsshowwind = orb_shoot()
        self.statsshowwind.show()
        self.statsshowwind.loadinit(self)

    def act_tre_check(self, item, column):
        # checkboxes in tree
        tid = item.text(1)
        if tid:
            changecomp = [self.getcompbygeoid(int(tid))]
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
            activeid = int(activetree.text(1))

            if activeid == -1:
                self.activecomp = None
                self.disablebtn(True)
            else:
                self.activecomp = self.getcompbygeoid(activeid)
                self.disablebtn(False)

    def pushcomponent(self, comp, categoryname):
        comp.categoryname = categoryname
        self.components.append(comp)
        self.treenewentry(comp)
        self.glwidget.addobj(comp.getgeo())
        self.activecomp = comp

    def treenewentry(self, comp):
        name = comp.getname()
        # cat = comp.categoryname
        cat = comp.comptype
        category = self.setcategory(cat)
        child = QtWidgets.QTreeWidgetItem(category, [name, str(comp.getid())])
        child.setCheckState(0, QtCore.Qt.Checked)
        child.setFlags(child.flags())
        self.tre_manager.clearSelection()
        self.activecomp = None
        self.disablebtn(True)

    def setcategory(self, cat):
        catitem = self.tre_manager.findItems(cat, QtCore.Qt.MatchFixedString)
        if not catitem:
            parent = QtWidgets.QTreeWidgetItem(self.tre_manager, [cat, '-1'])
            parent.setFlags(parent.flags() | QtCore.Qt.ItemIsTristate | QtCore.Qt.ItemIsUserCheckable)
            parent.setCheckState(0, QtCore.Qt.Checked)
            return parent
        else:
            return catitem[0]

    def disablebtn(self, bool):
        self.actionEdit.setDisabled(bool)
        self.actionDeletecomp.setDisabled(bool)
        self.actionSavecomp.setDisabled(bool)
        self.actionColor.setDisabled(bool)
        self.actionArmor_th.setDisabled(bool)

    def delcomp(self, comp):
        # cat = comp.categoryname
        cat = comp.comptype
        parent = self.tre_manager.findItems(cat, QtCore.Qt.MatchFixedString, 0)[0]
        child = \
            self.tre_manager.findItems(str(comp.getid()), QtCore.Qt.MatchFixedString | QtCore.Qt.MatchRecursive, 1)[
                0]
        child.setCheckState(0, QtCore.Qt.Checked)
        parent.removeChild(child)
        if parent.childCount() == 0:
            (parent.parent() or self.tre_manager.invisibleRootItem()).removeChild(parent)

        self.glwidget.objects.remove(comp.getgeo())
        self.components.remove(comp)
        self.glwidget.upmat()
        del (comp)
        # comp.geoobj.bufdrop()

    def act_btn_delete(self):
        answer = QtWidgets.QMessageBox.question(
            self,
            'Delete component',
            'Are you sure?',
            QtWidgets.QMessageBox.Yes,
            QtWidgets.QMessageBox.No)
        if answer == QtWidgets.QMessageBox.Yes:
            self.delcomp(self.activecomp)
            self.activecomp = None
            self.disablebtn(True)
            self.glwidget.addtoconsole('Component removed.')

    def getcompbygeoid(self, id):
        for comp in self.components:
            if comp.getid() == id:
                return comp

    def saveobj(self, obj, file):
        obj = obj.getcopy()
        obj.geoobj.bufdrop()
        with open(file, 'wb') as output:
            pickle.dump(obj, output, -1)

    def loadobj(self, file):
        with open(file, 'rb') as input:
            obj = pickle.load(input)
            obj.geoobj.bufinit()
            return obj

    def act_btn_front(self):
        self.glwidget.act_btn_front()
        self.glwidget.upmat()

    def act_btn_right(self):
        self.glwidget.act_btn_right()
        self.glwidget.upmat()

    def act_btn_left(self):
        self.glwidget.act_btn_left()
        self.glwidget.upmat()

    def act_btn_top(self):
        self.glwidget.act_btn_top()
        self.glwidget.upmat()

    def act_btn_bottom(self):
        self.glwidget.act_btn_bottom()
        self.glwidget.upmat()

    def act_btn_back(self):
        self.glwidget.act_btn_back()
        self.glwidget.upmat()

    def act_btn_armor(self):
        if self.actionArmor_th.isChecked():
            self.armor_color()
        else:
            self.activecomp.geoobj.ffc = False
            self.glwidget.upmat()

    def armor_color(self):
        from colour import Color
        blue = Color("blue")
        comp = self.activecomp#self.components[0]
        ths = comp.thickarr[:]
        uniths = set(ths)
        n = len(uniths)
        colors = list(blue.range_to(Color("red"), n))
        cdict={}
        for th,col in zip(sorted(uniths),colors):
            cdict[th] = [255*c for c in col.rgb]
        newcols=[]
        for th in ths:
            newcols.append(cdict[th])
        newcols = np.array([newcols[j] for j, face in enumerate(comp.geoobj.faces) for i in range(len(face))], dtype=np.ubyte)
        comp.geoobj.cbinit(newcols)
        comp.geoobj.ffc = True
        self.glwidget.upmat()

    def act_btn_color(self):
        self.colorwnd = color()
        self.colorwnd.loadinit(self, self.activecomp)
        self.colorwnd.show()

    def closeEvent(self, event):
        self.glwidget.objects = []
        self.glwidget.upmat()
        for comp in self.components:
            del (comp.geoobj)

if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    nextGui = mainProgram()
    nextGui.show()
    sys.exit(app.exec_())