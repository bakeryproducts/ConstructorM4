from PyQt5 import QtCore, QtGui, QtWidgets
from UI.pys.move import Ui_Form

class move(QtWidgets.QWidget, Ui_Form):
    def __init__(self,x,y, parent=None):
        super(move, self).__init__(parent)
        self.setupUi(self)

        self.setGeometry(x, y, 100, 100)
        self.movestep = 0
        self.rotatestep = 0
        self.mx = 0
        self.my = 0
        self.mz = 0
        self.rx = 0
        self.ry = 0
        self.rz = 0
        self.orgcomps = []
        self.comps = []

        self.dsb_mx.valueChanged.connect(self.act_dsb_mx)
        self.dsb_my.valueChanged.connect(self.act_dsb_my)
        self.dsb_mz.valueChanged.connect(self.act_dsb_mz)
        self.dsb_rx.valueChanged.connect(self.act_dsb_rx)
        self.dsb_ry.valueChanged.connect(self.act_dsb_ry)
        self.dsb_rz.valueChanged.connect(self.act_dsb_rz)

        self.ln_movestep.textChanged.connect(self.act_ln_movestep)
        self.ln_rotatestep.textChanged.connect(self.act_ln_rotatestep)

        self.dsb_mx.setRange(-1e9, 1e9)
        self.dsb_my.setRange(-1e9, 1e9)
        self.dsb_mz.setRange(-1e9, 1e9)
        self.dsb_rx.setRange(-1e9, 1e9)
        self.dsb_ry.setRange(-1e9, 1e9)
        self.dsb_rz.setRange(-1e9, 1e9)

        self.dsb_mx.setValue(0)
        self.dsb_my.setValue(0)
        self.dsb_mz.setValue(0)
        self.dsb_rx.setValue(0)
        self.dsb_ry.setValue(0)
        self.dsb_rz.setValue(0)

        self.btn_done.clicked.connect(self.act_btn_done)
        # self.cmb_component.currentIndexChanged.connect(self.act_cmb_change)
        self.lst_comps.itemChanged.connect(self.act_lst_change)

        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)

    def act_btn_done(self):

        for icomp, orgcomp in zip(self.comps, self.orgcomps):
            comp = icomp.getcopy()
            catname = comp.categoryname
            # print(comp.geoobj.psMatrix,icomp.geoobj.psMatrix)

            self.mainwindow.delcomp(orgcomp)
            self.mainwindow.pushcomponent(comp, catname)
            self.mainwindow.glwidget.cleartmpobjs()

        self.mainwindow.glwidget.dropselection()
        self.mainwindow.glwidget.mode = "pick0"
        self.mainwindow.glwidget.cleartmpobjs()
        self.mainwindow.glwidget.addtoconsole('Moved.')
        self.mainwindow.glwidget.upmat()
        del (self.comps)
        del (self.orgcomps)

        self.close()

    def act_dsb_mx(self, value):
        for comp in self.comps:
            comp.geoobj.move((value - self.mx, 0, 0))

        self.mx = value
        self.mainwindow.glwidget.upmat()

    def act_dsb_my(self, value):
        for comp in self.comps:
            comp.geoobj.move((0, value - self.my, 0))
        self.my = value
        self.mainwindow.glwidget.upmat()

    def act_dsb_mz(self, value):
        for comp in self.comps:
            comp.geoobj.move((0, 0, value - self.mz))
        self.mz = value
        self.mainwindow.glwidget.upmat()

    def act_dsb_rx(self, value):
        for comp in self.comps:
            comp.geoobj.rotate((value - self.rx, 0, 0))
        self.rx = value
        self.mainwindow.glwidget.upmat()

    def act_dsb_ry(self, value):
        for comp in self.comps:
            comp.geoobj.rotate((0, value - self.ry, 0))
        self.ry = value
        self.mainwindow.glwidget.upmat()

    def act_dsb_rz(self, value):
        for comp in self.comps:
            comp.geoobj.rotate((0, 0, value - self.rz))
        self.rz = value
        self.mainwindow.glwidget.upmat()

    def act_ln_movestep(self, ev):
        self.movestep = int(ev)
        self.dsb_mx.setSingleStep(self.movestep)
        self.dsb_my.setSingleStep(self.movestep)
        self.dsb_mz.setSingleStep(self.movestep)

    def act_ln_rotatestep(self, ev):
        self.rotatestep = int(ev)
        self.dsb_rx.setSingleStep(self.rotatestep)
        self.dsb_ry.setSingleStep(self.rotatestep)
        self.dsb_rz.setSingleStep(self.rotatestep)

    def loadinit(self, mainw):
        self.mainwindow = mainw
        self.maincomponents = mainw.components
        self.mainwindow.glwidget.cleartmpobjs()
        for comp in self.maincomponents:
            item = QtWidgets.QListWidgetItem()
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
            item.setText(comp.getname())
            self.lst_comps.addItem(item)
            # self.orgcomp = self.mainwindow.components[self.cmb_component.currentIndex()]
            # self.comp = self.orgcomp.getcopy()
            # self.mainwindow.glwidget.addtmpobj(self.comp.geoobj)
            # self.mainwindow.glwidget.upmat()

    def act_lst_change(self, item):
        self.mainwindow.glwidget.cleartmpobjs()
        self.comps = []
        self.orgcomps = []
        self.lst_comps.blockSignals(True)

        for index in range(self.lst_comps.count()):
            if self.lst_comps.item(index).checkState() == QtCore.Qt.Checked:
                # inds.append(index)

                # if item.checkState() == QtCore.Qt.Checked:
                print('checked', index)
                c = self.maincomponents[index]
                cp = c.getcopy()
                self.orgcomps.append(c)
                self.comps.append(cp)
                self.mainwindow.glwidget.addtmpobj(cp.geoobj)

                # elif item.checkState() == QtCore.Qt.Unchecked:
                #     print('unchecked', index)
                #     self.orgcomps.remove(self.maincomponents[i])

        self.lst_comps.blockSignals(False)
        self.mainwindow.glwidget.addtoconsole('Selected ' + str(len(self.comps)) + ' components.')

        # self.orgcomps = self.maincomponents[i]
        # self.comp = self.orgcomp.getcopy()
        # self.mainwindow.glwidget.addtmpobj(self.comp.geoobj)
        self.mainwindow.glwidget.upmat()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_4:
            self.dsb_mx.stepDown()

        elif event.key() == QtCore.Qt.Key_6:
            self.dsb_mx.stepUp()

        elif event.key() == QtCore.Qt.Key_2:
            self.dsb_my.stepDown()

        elif event.key() == QtCore.Qt.Key_8:
            self.dsb_my.stepUp()

        elif event.key() == QtCore.Qt.Key_Minus:
            self.dsb_mz.stepDown()

        elif event.key() == QtCore.Qt.Key_Plus:
            self.dsb_mz.stepUp()

        elif event.key() == QtCore.Qt.Key_PageUp:
            self.dsb_rx.stepUp()
        elif event.key() == QtCore.Qt.Key_PageDown:
            self.dsb_rx.stepDown()
        elif event.key() == QtCore.Qt.Key_Home:
            self.dsb_ry.stepUp()
        elif event.key() == QtCore.Qt.Key_End:
            self.dsb_ry.stepDown()
        elif event.key() == QtCore.Qt.Key_Slash:
            self.dsb_rz.stepUp()
        elif event.key() == QtCore.Qt.Key_Asterisk:
            self.dsb_rz.stepDown()



        else:
            pass
            # self.proceed()

        event.accept()

    def closeEvent(self, QCloseEvent):
        # self.act_btn_cancel()
        self.mainwindow.glwidget.cleartmpobjs()
        self.close()
