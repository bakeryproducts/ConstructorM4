import sys
from glwidget import *
import pickle
from CNST.clGEOOBJ import GEOOBJ
from MATERIALS.db import DB
from addcomp_ui import Ui_wid_addcomp
from crearray_ui import Ui_crearray
from materials_ui import Ui_materials
from creconstrained_ui import Ui_creconstrained
from newmathetero_ui import Ui_newmathetero
from adddz_ui import Ui_wid_adddz

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


class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.wsizew, self.wsizeh = 1200, 600
        self.wox, self.woy = 100, 100
        self.setGeometry(100, 100, 100, 100)

        self.setupUi(self)
        self.components = []
        self.activecompid = 0

        db = DB('MATERIALS\\GOST.xml')
        mat = db.getdefmat()
        #self.materials = [db.exportmat(mat)]
        self.materials = set([db.exportmat(mat)])

        self.fexit = False

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1200, 600)
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tre_manager = QtGui.QTreeWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tre_manager.sizePolicy().hasHeightForWidth())
        self.tre_manager.setSizePolicy(sizePolicy)
        self.tre_manager.setMaximumSize(QtCore.QSize(200, 16777215))
        self.tre_manager.setFrameShape(QtGui.QFrame.Box)
        self.tre_manager.setObjectName(_fromUtf8("tre_manager"))
        #self.tre_manager.headerItem().setText(0, _fromUtf8("1"))
        self.horizontalLayout.addWidget(self.tre_manager)
        self.glbox = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.glbox.sizePolicy().hasHeightForWidth())
        self.glbox.setSizePolicy(sizePolicy)
        self.glbox.setMinimumSize(QtCore.QSize(200, 0))
        self.glbox.setObjectName(_fromUtf8("glbox"))
        self.horizontalLayout.addWidget(self.glbox)

        self.horizontalLayout.addWidget(self.glbox)
        self.glwidget = GLWidget()
        mainLayout = QtGui.QHBoxLayout()
        mainLayout.addWidget(self.glwidget)
        self.glbox.setLayout(mainLayout)

        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.horizontalLayout.addWidget(self.line_3)
        self.lay_right = QtGui.QVBoxLayout()
        self.lay_right.setObjectName(_fromUtf8("lay_right"))
        self.lbl_pos = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_pos.sizePolicy().hasHeightForWidth())
        self.lbl_pos.setSizePolicy(sizePolicy)
        self.lbl_pos.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_pos.setObjectName(_fromUtf8("lbl_pos"))
        self.lay_right.addWidget(self.lbl_pos)
        self.lay_pos = QtGui.QHBoxLayout()
        self.lay_pos.setObjectName(_fromUtf8("lay_pos"))
        self.ln_pos = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_pos.sizePolicy().hasHeightForWidth())
        self.ln_pos.setSizePolicy(sizePolicy)
        self.ln_pos.setMaximumSize(QtCore.QSize(100, 16777215))
        self.ln_pos.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_pos.setObjectName(_fromUtf8("ln_pos"))
        self.lay_pos.addWidget(self.ln_pos)
        self.btn_setpos = QtGui.QPushButton(self.centralwidget)
        self.btn_setpos.setObjectName(_fromUtf8("btn_setpos"))
        self.lay_pos.addWidget(self.btn_setpos)
        self.lay_right.addLayout(self.lay_pos)
        self.lbl_rot = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_rot.sizePolicy().hasHeightForWidth())
        self.lbl_rot.setSizePolicy(sizePolicy)
        self.lbl_rot.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_rot.setObjectName(_fromUtf8("lbl_rot"))
        self.lay_right.addWidget(self.lbl_rot)
        self.lay_rot = QtGui.QHBoxLayout()
        self.lay_rot.setObjectName(_fromUtf8("lay_rot"))
        self.ln_rot = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_rot.sizePolicy().hasHeightForWidth())
        self.ln_rot.setSizePolicy(sizePolicy)
        self.ln_rot.setMaximumSize(QtCore.QSize(100, 16777215))
        self.ln_rot.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_rot.setObjectName(_fromUtf8("ln_rot"))
        self.lay_rot.addWidget(self.ln_rot)
        self.btn_setrot = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_setrot.sizePolicy().hasHeightForWidth())
        self.btn_setrot.setSizePolicy(sizePolicy)
        self.btn_setrot.setObjectName(_fromUtf8("btn_setrot"))
        self.lay_rot.addWidget(self.btn_setrot)
        self.lay_right.addLayout(self.lay_rot)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.lay_right.addWidget(self.line_2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.lay_right.addItem(spacerItem)
        self.lay_okc = QtGui.QHBoxLayout()
        self.lay_okc.setObjectName(_fromUtf8("lay_okc"))
        self.btn_okc = QtGui.QDialogButtonBox(self.centralwidget)
        self.btn_okc.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_okc.sizePolicy().hasHeightForWidth())
        self.btn_okc.setSizePolicy(sizePolicy)
        self.btn_okc.setStandardButtons(QtGui.QDialogButtonBox.Cancel | QtGui.QDialogButtonBox.Ok)
        self.btn_okc.setObjectName(_fromUtf8("btn_okc"))
        self.lay_okc.addWidget(self.btn_okc, QtCore.Qt.AlignRight)
        self.lay_right.addLayout(self.lay_okc)
        self.horizontalLayout.addLayout(self.lay_right)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 740, 34))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuViews = QtGui.QMenu(self.menuView)
        self.menuViews.setObjectName(_fromUtf8("menuViews"))
        self.menuVisual_Style = QtGui.QMenu(self.menuView)
        self.menuVisual_Style.setObjectName(_fromUtf8("menuVisual_Style"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        self.menuComponents = QtGui.QMenu(self.menubar)
        self.menuComponents.setGeometry(QtCore.QRect(783, 177, 192, 166))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuComponents.sizePolicy().hasHeightForWidth())
        self.menuComponents.setSizePolicy(sizePolicy)
        self.menuComponents.setMinimumSize(QtCore.QSize(150, 0))
        self.menuComponents.setObjectName(_fromUtf8("menuComponents"))
        self.menuAddcomp = QtGui.QMenu(self.menuComponents)
        self.menuAddcomp.setGeometry(QtCore.QRect(970, 180, 292, 166))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuAddcomp.sizePolicy().hasHeightForWidth())
        self.menuAddcomp.setSizePolicy(sizePolicy)
        self.menuAddcomp.setMinimumSize(QtCore.QSize(0, 0))
        self.menuAddcomp.setObjectName(_fromUtf8("menuAddcomp"))
        self.menuModify = QtGui.QMenu(self.menubar)
        self.menuModify.setObjectName(_fromUtf8("menuModify"))
        self.menuMa_terials = QtGui.QMenu(self.menubar)
        self.menuMa_terials.setObjectName(_fromUtf8("menuMa_terials"))
        self.menuCurrent = QtGui.QMenu(self.menuMa_terials)
        self.menuCurrent.setObjectName(_fromUtf8("menuCurrent"))
        self.menuNewmaterial = QtGui.QMenu(self.menuMa_terials)
        self.menuNewmaterial.setObjectName(_fromUtf8("menuNewmaterial"))
        MainWindow.setMenuBar(self.menubar)
        self.actionfSaveas = QtGui.QAction(MainWindow)
        self.actionfSaveas.setObjectName(_fromUtf8("actionfSaveas"))
        self.actionfExport = QtGui.QAction(MainWindow)
        self.actionfExport.setObjectName(_fromUtf8("actionfExport"))
        self.actionFront = QtGui.QAction(MainWindow)
        self.actionFront.setObjectName(_fromUtf8("actionFront"))
        self.actionBack = QtGui.QAction(MainWindow)
        self.actionBack.setObjectName(_fromUtf8("actionBack"))
        self.actionLeft = QtGui.QAction(MainWindow)
        self.actionLeft.setObjectName(_fromUtf8("actionLeft"))
        self.actionRight = QtGui.QAction(MainWindow)
        self.actionRight.setObjectName(_fromUtf8("actionRight"))
        self.actionTop = QtGui.QAction(MainWindow)
        self.actionTop.setObjectName(_fromUtf8("actionTop"))
        self.actionBottom = QtGui.QAction(MainWindow)
        self.actionBottom.setObjectName(_fromUtf8("actionBottom"))
        self.actionSolid = QtGui.QAction(MainWindow)
        self.actionSolid.setObjectName(_fromUtf8("actionSolid"))
        self.actionWireframe = QtGui.QAction(MainWindow)
        self.actionWireframe.setObjectName(_fromUtf8("actionWireframe"))
        self.actionLighting = QtGui.QAction(MainWindow)
        self.actionLighting.setCheckable(True)
        self.actionLighting.setObjectName(_fromUtf8("actionLighting"))
        self.actionBasecomp = QtGui.QAction(MainWindow)
        self.actionBasecomp.setObjectName(_fromUtf8("actionBasecomp"))
        self.actionArrays = QtGui.QAction(MainWindow)
        self.actionArrays.setObjectName(_fromUtf8("actionArrays"))
        self.actionHelp = QtGui.QAction(MainWindow)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.actionERA = QtGui.QAction(MainWindow)
        self.actionERA.setObjectName(_fromUtf8("actionERA"))
        self.action_Constrain = QtGui.QAction(MainWindow)
        self.action_Constrain.setObjectName(_fromUtf8("action_Constrain"))
        self.actionManage = QtGui.QAction(MainWindow)
        self.actionManage.setObjectName(_fromUtf8("actionManage"))
        self.actionfOpen = QtGui.QAction(MainWindow)
        self.actionfOpen.setObjectName(_fromUtf8("actionfOpen"))
        self.actionfClose = QtGui.QAction(MainWindow)
        self.actionfClose.setObjectName(_fromUtf8("actionfClose"))
        self.actionEdit = QtGui.QAction(MainWindow)
        self.actionEdit.setObjectName(_fromUtf8("actionEdit"))
        self.actionDeletecomp = QtGui.QAction(MainWindow)
        self.actionDeletecomp.setObjectName(_fromUtf8("actionDeletecomp"))
        self.actionOpen_2 = QtGui.QAction(MainWindow)
        self.actionOpen_2.setObjectName(_fromUtf8("actionOpen_2"))
        self.actionOpencomp = QtGui.QAction(MainWindow)
        self.actionOpencomp.setObjectName(_fromUtf8("actionOpencomp"))
        self.actionSavecomp = QtGui.QAction(MainWindow)
        self.actionSavecomp.setObjectName(_fromUtf8("actionSavecomp"))
        self.actionSave_2 = QtGui.QAction(MainWindow)
        self.actionSave_2.setObjectName(_fromUtf8("actionSave_2"))
        self.actionLoad = QtGui.QAction(MainWindow)
        self.actionLoad.setObjectName(_fromUtf8("actionLoad"))
        self.actionSavematdb = QtGui.QAction(MainWindow)
        self.actionSavematdb.setObjectName(_fromUtf8("actionSavematdb"))
        self.actionLoadmatdb = QtGui.QAction(MainWindow)
        self.actionLoadmatdb.setObjectName(_fromUtf8("actionLoadmatdb"))
        self.actionHomo = QtGui.QAction(MainWindow)
        self.actionHomo.setObjectName(_fromUtf8("actionHomo"))
        self.actionHetero = QtGui.QAction(MainWindow)
        self.actionHetero.setObjectName(_fromUtf8("actionHetero"))
        self.menuFile.addAction(self.actionfOpen)
        self.menuFile.addAction(self.actionfSaveas)
        self.menuFile.addAction(self.actionfExport)
        self.menuFile.addAction(self.actionfClose)
        self.menuViews.addAction(self.actionFront)
        self.menuViews.addAction(self.actionBack)
        self.menuViews.addAction(self.actionLeft)
        self.menuViews.addAction(self.actionRight)
        self.menuViews.addAction(self.actionTop)
        self.menuViews.addAction(self.actionBottom)
        self.menuVisual_Style.addAction(self.actionSolid)
        self.menuVisual_Style.addAction(self.actionWireframe)
        self.menuView.addAction(self.menuViews.menuAction())
        self.menuView.addAction(self.menuVisual_Style.menuAction())
        self.menuView.addAction(self.actionLighting)
        self.menuAbout.addAction(self.actionHelp)
        self.menuAddcomp.addAction(self.actionOpencomp)
        self.menuAddcomp.addAction(self.actionBasecomp)
        self.menuAddcomp.addAction(self.actionERA)
        self.menuComponents.addAction(self.menuAddcomp.menuAction())
        self.menuComponents.addAction(self.actionDeletecomp)
        self.menuComponents.addAction(self.actionSavecomp)
        self.menuModify.addAction(self.actionEdit)
        self.menuModify.addAction(self.action_Constrain)
        self.menuModify.addAction(self.actionArrays)
        self.menuCurrent.addAction(self.actionSavematdb)
        self.menuCurrent.addAction(self.actionLoadmatdb)
        self.menuNewmaterial.addAction(self.actionHomo)
        self.menuNewmaterial.addAction(self.actionHetero)
        self.menuMa_terials.addAction(self.actionManage)
        self.menuMa_terials.addAction(self.menuNewmaterial.menuAction())
        self.menuMa_terials.addAction(self.menuCurrent.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuComponents.menuAction())
        self.menubar.addAction(self.menuModify.menuAction())
        self.menubar.addAction(self.menuMa_terials.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.tre_manager.itemChanged.connect(self.act_tre_check)
        self.tre_manager.setHeaderLabels(["Target","col1"])
        self.tre_manager.itemSelectionChanged.connect(self.act_tre_test)
        self.tre_manager.itemClicked.connect(self.act_tre_test)
        self.tre_manager.hideColumn(1)


        self.btn_setrot.clicked.connect(self.act_btn_rotation)
        self.btn_setpos.clicked.connect(self.act_btn_position)

        self.actionfExport.triggered.connect(self.act_btn_export)
        self.actionfSaveas.triggered.connect(self.act_btn_saveas)
        self.actionfOpen.triggered.connect(self.act_btn_open)
        self.actionfClose.triggered.connect(self.close)

        self.actionBasecomp.triggered.connect(self.act_btn_add_basecomp)
        self.actionERA.triggered.connect(self.act_btn_add_era)
        self.actionSavecomp.triggered.connect(self.act_btn_savecomp)
        self.actionOpencomp.triggered.connect(self.act_btn_opencomp)
        self.actionDeletecomp.triggered.connect(self.act_btn_delete)

        self.actionEdit.triggered.connect(self.act_btn_edit)
        self.actionArrays.triggered.connect(self.act_btn_arrays)
        self.action_Constrain.triggered.connect(self.act_btn_constrain)

        self.actionManage.triggered.connect(self.act_btn_materials)
        self.actionSavematdb.triggered.connect(self.act_btn_savemat)
        self.actionLoadmatdb.triggered.connect(self.act_btn_loadmat)

        self.actionHetero.triggered.connect(self.act_btn_newmathetero)
        self.actionHelp.triggered.connect(self.act_btn_help)
        self.actionLighting.triggered.connect(self.test)

        self.actionWireframe.triggered.connect(self.act_btn_edges)

        self.glwidget.mode = "pick0"
        self.disablelay(True)
        self.disablebtn(True)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Constructor", None))
        self.lbl_pos.setText(_translate("MainWindow", "Component position (X,Y,Z)", None))
        self.ln_pos.setText(_translate("MainWindow", "0,0,0", None))
        self.btn_setpos.setText(_translate("MainWindow", "Set position", None))
        self.lbl_rot.setText(_translate("MainWindow", "Component Rotation angles ", None))
        self.ln_rot.setText(_translate("MainWindow", "0,0,0", None))
        self.btn_setrot.setText(_translate("MainWindow", "Set rotation", None))
        self.menuFile.setTitle(_translate("MainWindow", "&File", None))
        self.menuView.setTitle(_translate("MainWindow", "&View", None))
        self.menuViews.setTitle(_translate("MainWindow", "Views", None))
        self.menuVisual_Style.setTitle(_translate("MainWindow", "Visual Style", None))
        self.menuAbout.setTitle(_translate("MainWindow", "Ab&out", None))
        self.menuComponents.setTitle(_translate("MainWindow", "&Components", None))
        self.menuAddcomp.setTitle(_translate("MainWindow", "&Add", None))
        self.menuModify.setTitle(_translate("MainWindow", "&Modify", None))
        self.menuMa_terials.setTitle(_translate("MainWindow", "Ma&terials", None))
        self.menuCurrent.setTitle(_translate("MainWindow", "Current", None))
        self.menuNewmaterial.setTitle(_translate("MainWindow", "New material", None))
        self.actionfSaveas.setText(_translate("MainWindow", "Save as...", None))
        self.actionfExport.setText(_translate("MainWindow", "Export...", None))
        self.actionFront.setText(_translate("MainWindow", "Front", None))
        self.actionBack.setText(_translate("MainWindow", "Back", None))
        self.actionLeft.setText(_translate("MainWindow", "Left", None))
        self.actionRight.setText(_translate("MainWindow", "Right", None))
        self.actionTop.setText(_translate("MainWindow", "Top", None))
        self.actionBottom.setText(_translate("MainWindow", "Bottom", None))
        self.actionSolid.setText(_translate("MainWindow", "Solid", None))
        self.actionWireframe.setText(_translate("MainWindow", "Wireframe", None))
        self.actionLighting.setText(_translate("MainWindow", "Lighting", None))
        self.actionBasecomp.setText(_translate("MainWindow", "&Base component", None))
        self.actionArrays.setText(_translate("MainWindow", "Arrays...", None))
        self.actionHelp.setText(_translate("MainWindow", "Help", None))
        self.actionERA.setText(_translate("MainWindow", "Explosive Reaction Armor ", None))
        self.action_Constrain.setText(_translate("MainWindow", "Co&nstrain...", None))
        self.actionManage.setText(_translate("MainWindow", "Manage...", None))
        self.actionfOpen.setText(_translate("MainWindow", "Open...", None))
        self.actionfClose.setText(_translate("MainWindow", "Close", None))
        self.actionEdit.setText(_translate("MainWindow", "Edit...", None))
        self.actionDeletecomp.setText(_translate("MainWindow", "Delete...", None))
        self.actionOpen_2.setText(_translate("MainWindow", "Open...", None))
        self.actionOpencomp.setText(_translate("MainWindow", "Load...", None))
        self.actionSavecomp.setText(_translate("MainWindow", "Save as...", None))
        self.actionSave_2.setText(_translate("MainWindow", "Save DB...", None))
        self.actionLoad.setText(_translate("MainWindow", "Open DB...", None))
        self.actionSavematdb.setText(_translate("MainWindow", "Save...", None))
        self.actionLoadmatdb.setText(_translate("MainWindow", "Load...", None))
        self.actionHomo.setText(_translate("MainWindow", "Homogeneous...", None))
        self.actionHetero.setText(_translate("MainWindow", "Heterogeneous...", None))

    def act_btn_add_basecomp(self):
        filedialog = QtGui.QFileDialog(self)
        filepath = filedialog.getOpenFileName(self, "Open STL geometry", "CNST\GEO\dz.stl", filter="stl (*.stl *.)")
        #filepath = "C:\\Users\\User\Documents\GitHub\ConstructorM4\CNST\GEO\\cube100.stl"
        if filepath:
            # self.act_btn_add(filepath)
            self.addwind = Ui_wid_addcomp()
            self.addwind.show()
            self.addwind.newwobj(filepath, self)

    def act_btn_add_era(self):
        self.addwinddz = Ui_wid_adddz()
        self.addwinddz.show()
        self.addwinddz.loadinit("skip", self)

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
        pass


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
        category = self.activecomp.categoryname
        if category == 'Main components':
            self.addwind = Ui_wid_addcomp()
            self.addwind.show()
            self.addwind.newwobj(self.activecomp, self)
        elif category == "ERA":
            self.addwinddz = Ui_wid_adddz()
            self.addwinddz.show()
            self.addwinddz.loadinit(self.activecomp, self)
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
        file = filedialog.getSaveFileName(self, "Save Model As", "SAVES\MODELS\MODEL.svm", filter="svm (*.svm *.)")
        if file:
            # file = 'RESULTS\SAVECOMP.sav'
            self.saveobj(self.components, file)

    def act_btn_open(self):
        filedialog = QtGui.QFileDialog(self)
        file = filedialog.getOpenFileName(self, "Load Model", "SAVES\MODELS\MODEL.svm", filter="svm (*.svm *.)")
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
                        self.materials.append(mat)
            self.glwidget.upmat()

    def act_btn_savecomp(self):
        comp = self.activecomp
        filedialog = QtGui.QFileDialog(self)
        file = filedialog.getSaveFileName(self, "Save Component As", "SAVES\COMPONENTS\\" + comp.getname() + ".svc",
                                          filter="svc (*.svc *.)")
        if file:
            # file = 'RESULTS\SAVECOMP.sav'
            self.saveobj(comp, file)

    def act_btn_opencomp(self):
        filedialog = QtGui.QFileDialog(self)
        file = filedialog.getOpenFileName(self, "Load Component", "SAVES\COMPONENTS\\", filter="svc (*.svc *.)")
        if file:
            tempcomp = self.loadobj(file)
            tempcomp.setid()
            comp = tempcomp.getcopy()
            catname = comp.categoryname
            self.pushcomponent(comp, catname)
            self.glwidget.upmat()

    def act_btn_savemat(self):
        mats = self.materials
        filedialog = QtGui.QFileDialog(self)
        file = filedialog.getSaveFileName(self, "Save Materials Database As", "SAVES\MATERIALS\\materials.svd",
                                          filter="svd (*.svd *.)")
        if file:
            # file = 'RESULTS\SAVECOMP.sav'
            self.saveobj(mats, file)

    def act_btn_loadmat(self):
        filedialog = QtGui.QFileDialog(self)
        file = filedialog.getOpenFileName(self, "Load Materials Database", "SAVES\MATERIALS\\", filter="svd (*.svd *.)")
        if file:
            tmats = self.loadobj(file)
            self.materials = tmats

    def act_btn_newmathetero(self):
        self.newmathetwind = Ui_newmathetero()
        self.newmathetwind.loadinit(self)
        self.newmathetwind.show()

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
                self.disablelay(True)
                self.clearlines()
                self.activecomp = None
                self.disablebtn(True)
            else:
                self.disablelay(False)
                self.activecomp = self.getcompbygeoid(activeid)
                self.disablebtn(False)

    def pushcomponent(self, comp, categoryname):
        comp.categoryname = categoryname
        self.components.append(comp)
        self.pushmaterials(comp)
        self.treenewentry(comp)
        self.glwidget.addobj(comp.getgeo())
        self.activecomp = comp

    def treenewentry(self, comp):
        name = comp.getname()
        category = self.setcategory(comp.categoryname)
        child = QtGui.QTreeWidgetItem(category,[name,str(comp.getid())])
        child.setCheckState(0, QtCore.Qt.Checked)
        child.setFlags(child.flags())
        self.tre_manager.clearSelection()
        self.activecomp = None
        self.disablebtn(True)

    def setcategory(self, cat):
        catitem = self.tre_manager.findItems(cat, QtCore.Qt.MatchFixedString)
        if not catitem:
            parent = QtGui.QTreeWidgetItem(self.tre_manager,[cat,'-1'])
            parent.setFlags(parent.flags() | QtCore.Qt.ItemIsTristate | QtCore.Qt.ItemIsUserCheckable)
            parent.setCheckState(0, QtCore.Qt.Checked)
            return parent
        else:
            return catitem[0]

    def pushmaterials(self,comp):
        matnames ={}
        for  mat in self.materials:
            matnames[mat.getname()] = mat

        for mat in comp.getmats():
            if mat not in self.materials:
                mname = mat.getname()
                if mname not in matnames.keys():
                    self.materials.add(mat)
                else:
                    realmat = matnames[mname]
                    for i in range(len(comp.matarr)):
                        if comp.matarr[i].getname() == mname:
                            comp.matarr[i] = realmat

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
        self.actionDeletecomp.setDisabled(bool)
        self.actionSavecomp.setDisabled(bool)

    def delcomp(self, comp):
        self.components.remove(comp)
        self.glwidget.objects.remove(comp.getgeo())
        parent = self.tre_manager.findItems(comp.categoryname, QtCore.Qt.MatchFixedString,0)[0]
        child = self.tre_manager.findItems(str(comp.getid()), QtCore.Qt.MatchFixedString | QtCore.Qt.MatchRecursive ,1)[0]
        parent.removeChild(child)
        if parent.childCount() == 0:
            (parent.parent() or self.tre_manager.invisibleRootItem()).removeChild(parent)

    def test(self):
        for mat in self.materials:
            print(mat,mat.getname())
        print(50*"#")

    def act_btn_edges(self):
        self.glwidget.edgemodeswitch()

    def getcompbygeoid(self, id):
        for comp in self.components:
            if comp.getid() == id:
                return comp
    #
    # def closeEvent(self, event):
    #     answer = QtGui.QMessageBox.question(
    #         self,
    #         'QUIT',
    #         'Are you sure?',
    #         QtGui.QMessageBox.Yes,
    #         QtGui.QMessageBox.No)
    #     if answer == QtGui.QMessageBox.Yes:
    #         event.accept()
    #     else:
    #         event.ignore()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec_())
