import sys
import gc
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

class Ui_crearray(QtGui.QWidget):
    def __init__(self,x,y):
        super(Ui_crearray, self).__init__()
        self.setGeometry(x,y,100,100)

        #self.mainwindow=0
        self.selcomp = 0
        self.maincomponents=[]
        self.basec=0
        self.basepoint=0
        self.nx,self.ny,self.dx,self.dy,self.ang = 0,0,0,0,0

        self.setupUi(self)

    def setupUi(self, crearray):
        crearray.setObjectName(_fromUtf8("crearray"))
        crearray.resize(294, 275)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(crearray.sizePolicy().hasHeightForWidth())
        crearray.setSizePolicy(sizePolicy)
        crearray.setFocusPolicy(QtCore.Qt.TabFocus)
        self.verticalLayout = QtGui.QVBoxLayout(crearray)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lay_compselect = QtGui.QHBoxLayout()
        self.lay_compselect.setObjectName(_fromUtf8("lay_compselect"))
        self.lbl_compselect = QtGui.QLabel(crearray)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_compselect.sizePolicy().hasHeightForWidth())
        self.lbl_compselect.setSizePolicy(sizePolicy)
        self.lbl_compselect.setObjectName(_fromUtf8("lbl_compselect"))
        self.lay_compselect.addWidget(self.lbl_compselect)
        self.cmb_compselect = QtGui.QComboBox(crearray)
        self.cmb_compselect.setObjectName(_fromUtf8("cmb_compselect"))
        self.cmb_compselect.addItem(_fromUtf8(""))
        self.lay_compselect.addWidget(self.cmb_compselect)
        self.verticalLayout.addLayout(self.lay_compselect)
        self.lay_selplane = QtGui.QHBoxLayout()
        self.lay_selplane.setObjectName(_fromUtf8("lay_selplane"))
        self.lbl_selplane = QtGui.QLabel(crearray)
        self.lbl_selplane.setObjectName(_fromUtf8("lbl_selplane"))
        self.lay_selplane.addWidget(self.lbl_selplane)
        self.btn_selplane = QtGui.QPushButton(crearray)
        self.btn_selplane.setObjectName(_fromUtf8("btn_selplane"))
        self.lay_selplane.addWidget(self.btn_selplane)
        self.verticalLayout.addLayout(self.lay_selplane)
        self.lay_nfirst = QtGui.QHBoxLayout()
        self.lay_nfirst.setObjectName(_fromUtf8("lay_nfirst"))
        self.lbl_nfirst = QtGui.QLabel(crearray)
        self.lbl_nfirst.setObjectName(_fromUtf8("lbl_nfirst"))
        self.lay_nfirst.addWidget(self.lbl_nfirst)
        self.ln_nfirst = QtGui.QLineEdit(crearray)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_nfirst.sizePolicy().hasHeightForWidth())
        self.ln_nfirst.setSizePolicy(sizePolicy)
        self.ln_nfirst.setMaximumSize(QtCore.QSize(50, 16777215))
        self.ln_nfirst.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_nfirst.setObjectName(_fromUtf8("ln_nfirst"))
        self.lay_nfirst.addWidget(self.ln_nfirst)
        self.verticalLayout.addLayout(self.lay_nfirst)
        self.lay_nsecond = QtGui.QHBoxLayout()
        self.lay_nsecond.setObjectName(_fromUtf8("lay_nsecond"))
        self.lbl_nsecond = QtGui.QLabel(crearray)
        self.lbl_nsecond.setObjectName(_fromUtf8("lbl_nsecond"))
        self.lay_nsecond.addWidget(self.lbl_nsecond)
        self.ln_nsecond = QtGui.QLineEdit(crearray)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_nsecond.sizePolicy().hasHeightForWidth())
        self.ln_nsecond.setSizePolicy(sizePolicy)
        self.ln_nsecond.setMaximumSize(QtCore.QSize(50, 16777215))
        self.ln_nsecond.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_nsecond.setObjectName(_fromUtf8("ln_nsecond"))
        self.lay_nsecond.addWidget(self.ln_nsecond)
        self.verticalLayout.addLayout(self.lay_nsecond)
        self.lay_stepfirst = QtGui.QHBoxLayout()
        self.lay_stepfirst.setObjectName(_fromUtf8("lay_stepfirst"))
        self.lbl_stelfirst = QtGui.QLabel(crearray)
        self.lbl_stelfirst.setObjectName(_fromUtf8("lbl_stelfirst"))
        self.lay_stepfirst.addWidget(self.lbl_stelfirst)
        self.ln_stepfirst = QtGui.QLineEdit(crearray)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_stepfirst.sizePolicy().hasHeightForWidth())
        self.ln_stepfirst.setSizePolicy(sizePolicy)
        self.ln_stepfirst.setMaximumSize(QtCore.QSize(50, 16777215))
        self.ln_stepfirst.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_stepfirst.setObjectName(_fromUtf8("ln_stepfirst"))
        self.lay_stepfirst.addWidget(self.ln_stepfirst)
        self.verticalLayout.addLayout(self.lay_stepfirst)
        self.lay_stepsecond = QtGui.QHBoxLayout()
        self.lay_stepsecond.setObjectName(_fromUtf8("lay_stepsecond"))
        self.lbl_stepsecond = QtGui.QLabel(crearray)
        self.lbl_stepsecond.setObjectName(_fromUtf8("lbl_stepsecond"))
        self.lay_stepsecond.addWidget(self.lbl_stepsecond)
        self.ln_stepsecond = QtGui.QLineEdit(crearray)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_stepsecond.sizePolicy().hasHeightForWidth())
        self.ln_stepsecond.setSizePolicy(sizePolicy)
        self.ln_stepsecond.setMaximumSize(QtCore.QSize(50, 16777215))
        self.ln_stepsecond.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_stepsecond.setObjectName(_fromUtf8("ln_stepsecond"))
        self.lay_stepsecond.addWidget(self.ln_stepsecond)
        self.verticalLayout.addLayout(self.lay_stepsecond)
        self.lay_angle = QtGui.QHBoxLayout()
        self.lay_angle.setObjectName(_fromUtf8("lay_angle"))
        self.lbl_angle = QtGui.QLabel(crearray)
        self.lbl_angle.setObjectName(_fromUtf8("lbl_angle"))
        self.lay_angle.addWidget(self.lbl_angle)
        self.ln_angle = QtGui.QLineEdit(crearray)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_angle.sizePolicy().hasHeightForWidth())
        self.ln_angle.setSizePolicy(sizePolicy)
        self.ln_angle.setMaximumSize(QtCore.QSize(50, 16777215))
        self.ln_angle.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_angle.setObjectName(_fromUtf8("ln_angle"))
        self.lay_angle.addWidget(self.ln_angle)
        self.verticalLayout.addLayout(self.lay_angle)
        self.lay_changes = QtGui.QHBoxLayout()
        self.lay_changes.setObjectName(_fromUtf8("horizontalLayout"))
        self.btn_changes = QtGui.QPushButton(crearray)
        self.btn_changes.setObjectName(_fromUtf8("pushButton"))
        self.lay_changes.addWidget(self.btn_changes)
        self.btn_save = QtGui.QPushButton(crearray)
        self.btn_save.setObjectName(_fromUtf8("btn_save"))
        self.lay_changes.addWidget(self.btn_save)
        self.verticalLayout.addLayout(self.lay_changes)

        self.btn_selplane.setCheckable(True)

        self.btn_selplane.clicked.connect(self.act_btn_selplane)
        self.btn_save.clicked.connect(self.act_btn_save)
        self.btn_changes.clicked.connect(self.act_btn_changes)
        self.cmb_compselect.currentIndexChanged.connect(self.act_cmb_change)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        self.retranslateUi(crearray)
        QtCore.QMetaObject.connectSlotsByName(crearray)

    def retranslateUi(self, crearray):
        crearray.setWindowTitle(_translate("crearray", "Component Array Maker", None))
        self.lbl_compselect.setText(_translate("crearray", "Component for copying", None))
        self.cmb_compselect.setItemText(0, _translate("crearray", "Choose component", None))
        self.lbl_selplane.setText(_translate("crearray", "Selet base plane ", None))
        self.btn_selplane.setText(_translate("crearray", "Select", None))
        self.lbl_nfirst.setText(_translate("crearray", "Number of elements,first direction", None))
        self.ln_nfirst.setText(_translate("crearray", "2", None))
        self.lbl_nsecond.setText(_translate("crearray", "Number of elements,second direction", None))
        self.ln_nsecond.setText(_translate("crearray", "2", None))
        self.lbl_stelfirst.setText(_translate("crearray", "Step in first direction", None))
        self.ln_stepfirst.setText(_translate("crearray", "250", None))
        self.lbl_stepsecond.setText(_translate("crearray", "Step in second direction", None))
        self.ln_stepsecond.setText(_translate("crearray", "250", None))
        self.lbl_angle.setText(_translate("crearray", "Basis rotation angle", None))
        self.ln_angle.setText(_translate("crearray", "0", None))
        self.btn_changes.setText(_translate("crearray", "View changes", None))
        self.btn_save.setText(_translate("crearray", "Save array", None))

    def act_btn_selplane(self):
        self.mainwindow.glwidget.dropselection()
        self.mainwindow.glwidget.mode = "pickone"

    def select(self,args):
        self.basec = args[0]
        self.basepoint = args[1]
        #print(self.basec,self.basepoint)

    def act_btn_changes(self):
        self.nx = int(self.ln_nfirst.text())
        self.ny = int(self.ln_nsecond.text())
        self.dx = int(self.ln_stepfirst.text())
        self.dy = int(self.ln_stepsecond.text())
        self.ang = int(self.ln_angle.text())
        tempcomponents = self.makearray((self.nx,self.ny,self.dx,self.dy),self.ang)
        self.mainwindow.glwidget.cleartmpobjs()
        for tcomp in tempcomponents[1:]:
            self.mainwindow.glwidget.addtmpobj(tcomp.getgeo())

        self.arraycomponents = tempcomponents[1:]
        self.mainwindow.glwidget.upmat()
        self.mainwindow.glwidget.dropselection()
        self.mainwindow.glwidget.mode = "pick0"
        self.btn_selplane.setChecked(False)

    def act_btn_save(self):
        self.mainwindow.glwidget.cleartmpobjs()
        for comp in reversed(self.arraycomponents):
            tcomp = comp.getcopy()
            tcat = comp.categoryname
            self.mainwindow.pushcomponent(tcomp, tcat)

        del(self.arraycomponents)
        self.mainwindow.glwidget.dropsphs()
        self.close()

    def act_btn_cancel(self):
        self.mainwindow.glwidget.cleartmpobjs()
        self.mainwindow.glwidget.dropsphs()
        self.close()

    def closeEvent(self, QCloseEvent):
        self.act_btn_cancel()

    def loadinit(self,mainw):
        self.mainwindow = mainw
        self.maincomponents = mainw.components
        self.cmb_compselect.addItems(list(mainw.treeids.keys()))

        self.mainwindow.glwidget.ObjSelected.connect(self.select)

    def act_cmb_change(self,i):
        self.selcomp = self.maincomponents[i-1]
        self.movec = self.selcomp.getid()
        #print(self.cmb_compselect.currentText())

    def makearray(self, grid, angbasis=0):
        baseid = self.mainwindow.glwidget.getobjbyid(self.basec[0])
        baseplane = self.basec[1]
        baseobj = self.mainwindow.glwidget.objects[baseid]
        normalbase = baseobj.getnormaltoface(baseplane) * (-1)

        offset = (0,0,0)
        nx, ny, dx, dy = grid
        tcomps = []
        for j in range(ny):
            for i in range(nx):
                tmpcomp = self.selcomp.getcopy()
                toffset = offset[0] + i * dx, offset[1], offset[2]
                toffset = toffset[0], toffset[1] + j * dy, toffset[2]
                tmpcomp.geoobj.makearrayitem(toffset,angbasis,normalbase)
                tcomps.append(tmpcomp)
        return tcomps