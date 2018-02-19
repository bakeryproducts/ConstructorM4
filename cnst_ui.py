import sys
from glwidget import *
import pickle
from PIL import Image
from PIL import ImageOps

from CNST.clGEOOBJ import GEOOBJ
from MATERIALS.db import DB
from addcomp_ui import Ui_wid_addcomp
from crearray_ui import Ui_crearray
from materials_ui import Ui_materials
from creconstrained_ui import Ui_creconstrained
from newmathetero_ui import Ui_newmathetero
from adddz_ui import Ui_wid_adddz
from color_ui import Ui_color
from addslat_ui import Ui_wid_addslat
from move_ui import Ui_move
from addproj_ui import Ui_wid_addproj
from stats_ui import Ui_wid_stats
from addrevext_ui import Ui_wid_revext
from standartshape_ui import Ui_wid_addshape

from PyQt4 import QtCore, QtGui
import UI.Resourses.resIcons


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
        self.materials = {db.exportmat(mat)}

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
        self.tre_manager.headerItem().setText(0, _fromUtf8("1"))
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
        self.btn_okc.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.btn_okc.setObjectName(_fromUtf8("btn_okc"))
        self.lay_okc.addWidget(self.btn_okc, QtCore.Qt.AlignRight)
        self.lay_right.addLayout(self.lay_okc)
        self.horizontalLayout.addLayout(self.lay_right)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 949, 34))
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
        self.menuComponents.setGeometry(QtCore.QRect(450, 217, 204, 168))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuComponents.sizePolicy().hasHeightForWidth())
        self.menuComponents.setSizePolicy(sizePolicy)
        self.menuComponents.setMinimumSize(QtCore.QSize(150, 0))
        self.menuComponents.setObjectName(_fromUtf8("menuComponents"))
        self.menuAddcomp = QtGui.QMenu(self.menuComponents)
        self.menuAddcomp.setGeometry(QtCore.QRect(649, 220, 304, 234))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuAddcomp.sizePolicy().hasHeightForWidth())
        self.menuAddcomp.setSizePolicy(sizePolicy)
        self.menuAddcomp.setMinimumSize(QtCore.QSize(0, 0))
        self.menuAddcomp.setObjectName(_fromUtf8("menuAddcomp"))
        self.menuStandart_shapes = QtGui.QMenu(self.menuAddcomp)
        self.menuStandart_shapes.setObjectName(_fromUtf8("menuStandart_shapes"))
        self.menuModify = QtGui.QMenu(self.menubar)
        self.menuModify.setObjectName(_fromUtf8("menuModify"))
        self.menuMa_terials = QtGui.QMenu(self.menubar)
        self.menuMa_terials.setObjectName(_fromUtf8("menuMa_terials"))
        self.menuCurrent = QtGui.QMenu(self.menuMa_terials)
        self.menuCurrent.setObjectName(_fromUtf8("menuCurrent"))
        self.menuNewmaterial = QtGui.QMenu(self.menuMa_terials)
        self.menuNewmaterial.setObjectName(_fromUtf8("menuNewmaterial"))
        self.menuProjectile = QtGui.QMenu(self.menubar)
        self.menuProjectile.setObjectName(_fromUtf8("menuProjectile"))
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        self.actionfSaveas = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/TBicons/folder_full_accept.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionfSaveas.setIcon(icon)
        self.actionfSaveas.setObjectName(_fromUtf8("actionfSaveas"))
        self.actionfExport = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/TBicons/application_next.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionfExport.setIcon(icon1)
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/TBicons/page_add.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBasecomp.setIcon(icon2)
        self.actionBasecomp.setObjectName(_fromUtf8("actionBasecomp"))
        self.actionArrays = QtGui.QAction(MainWindow)
        self.actionArrays.setObjectName(_fromUtf8("actionArrays"))
        self.actionHelp = QtGui.QAction(MainWindow)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.actionERA = QtGui.QAction(MainWindow)
        self.actionERA.setObjectName(_fromUtf8("actionERA"))
        self.action_Constrain = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/TBicons/page_swap.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Constrain.setIcon(icon3)
        self.action_Constrain.setObjectName(_fromUtf8("action_Constrain"))
        self.actionManage = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/TBicons/database_process.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionManage.setIcon(icon4)
        self.actionManage.setObjectName(_fromUtf8("actionManage"))
        self.actionfOpen = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/TBicons/folder_full.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionfOpen.setIcon(icon5)
        self.actionfOpen.setObjectName(_fromUtf8("actionfOpen"))
        self.actionfClose = QtGui.QAction(MainWindow)
        self.actionfClose.setObjectName(_fromUtf8("actionfClose"))
        self.actionEdit = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/TBicons/note_edit.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEdit.setIcon(icon6)
        self.actionEdit.setObjectName(_fromUtf8("actionEdit"))
        self.actionDeletecomp = QtGui.QAction(MainWindow)
        self.actionDeletecomp.setObjectName(_fromUtf8("actionDeletecomp"))
        self.actionOpencomp = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/TBicons/page_up.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpencomp.setIcon(icon7)
        self.actionOpencomp.setObjectName(_fromUtf8("actionOpencomp"))
        self.actionSavecomp = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/TBicons/page_down.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSavecomp.setIcon(icon8)
        self.actionSavecomp.setObjectName(_fromUtf8("actionSavecomp"))
        self.actionSavematdb = QtGui.QAction(MainWindow)
        self.actionSavematdb.setObjectName(_fromUtf8("actionSavematdb"))
        self.actionLoadmatdb = QtGui.QAction(MainWindow)
        self.actionLoadmatdb.setObjectName(_fromUtf8("actionLoadmatdb"))
        self.actionHomo = QtGui.QAction(MainWindow)
        self.actionHomo.setObjectName(_fromUtf8("actionHomo"))
        self.actionHetero = QtGui.QAction(MainWindow)
        self.actionHetero.setObjectName(_fromUtf8("actionHetero"))
        self.actionColor = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/TBicons/process.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionColor.setIcon(icon9)
        self.actionColor.setObjectName(_fromUtf8("actionColor"))
        self.actionShooting = QtGui.QAction(MainWindow)
        self.actionShooting.setObjectName(_fromUtf8("actionShooting"))
        self.actionSlat_Armor = QtGui.QAction(MainWindow)
        self.actionSlat_Armor.setObjectName(_fromUtf8("actionSlat_Armor"))
        self.actionNew = QtGui.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/TBicons/ico/blog_post.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon10)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionMove = QtGui.QAction(MainWindow)
        self.actionMove.setObjectName(_fromUtf8("actionMove"))
        self.actionAssembly = QtGui.QAction(MainWindow)
        self.actionAssembly.setObjectName(_fromUtf8("actionAssembly"))
        self.actionShapes_generator = QtGui.QAction(MainWindow)
        self.actionShapes_generator.setObjectName(_fromUtf8("actionShapes_generator"))
        self.actionExtract_Revolve = QtGui.QAction(MainWindow)
        self.actionExtract_Revolve.setObjectName(_fromUtf8("actionExtract_Revolve"))
        self.actionMirror = QtGui.QAction(MainWindow)
        self.actionMirror.setObjectName(_fromUtf8("actionMirror"))
        self.menuFile.addAction(self.actionNew)
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
        self.menuView.addAction(self.actionColor)
        self.menuAbout.addAction(self.actionHelp)
        self.menuStandart_shapes.addAction(self.actionShapes_generator)
        self.menuStandart_shapes.addAction(self.actionExtract_Revolve)
        self.menuAddcomp.addAction(self.actionOpencomp)
        self.menuAddcomp.addAction(self.actionBasecomp)
        self.menuAddcomp.addAction(self.actionERA)
        self.menuAddcomp.addAction(self.actionSlat_Armor)
        self.menuAddcomp.addAction(self.menuStandart_shapes.menuAction())
        self.menuComponents.addAction(self.menuAddcomp.menuAction())
        self.menuComponents.addAction(self.actionDeletecomp)
        self.menuComponents.addAction(self.actionSavecomp)
        self.menuModify.addAction(self.actionEdit)
        self.menuModify.addAction(self.actionMove)
        self.menuModify.addAction(self.action_Constrain)
        self.menuModify.addAction(self.actionArrays)
        self.menuModify.addAction(self.actionMirror)
        self.menuCurrent.addAction(self.actionSavematdb)
        self.menuCurrent.addAction(self.actionLoadmatdb)
        self.menuNewmaterial.addAction(self.actionHomo)
        self.menuNewmaterial.addAction(self.actionHetero)
        self.menuMa_terials.addAction(self.actionManage)
        self.menuMa_terials.addAction(self.menuNewmaterial.menuAction())
        self.menuMa_terials.addAction(self.menuCurrent.menuAction())
        self.menuProjectile.addAction(self.actionAssembly)
        self.menuProjectile.addAction(self.actionShooting)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuComponents.menuAction())
        self.menubar.addAction(self.menuModify.menuAction())
        self.menubar.addAction(self.menuMa_terials.menuAction())
        self.menubar.addAction(self.menuProjectile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.toolBar.addAction(self.actionfOpen)
        self.toolBar.addAction(self.actionfSaveas)
        self.toolBar.addAction(self.actionfExport)
        self.toolBar.addAction(self.actionOpencomp)
        self.toolBar.addAction(self.actionBasecomp)
        self.toolBar.addAction(self.actionSavecomp)
        self.toolBar.addAction(self.actionEdit)
        self.toolBar.addAction(self.action_Constrain)
        self.toolBar.addAction(self.actionManage)
        self.toolBar.addAction(self.actionColor)

        self.tre_manager.itemChanged.connect(self.act_tre_check)
        self.tre_manager.setHeaderLabels(["Target", "col1"])
        self.tre_manager.itemSelectionChanged.connect(self.act_tre_test)
        self.tre_manager.itemClicked.connect(self.act_tre_test)
        self.tre_manager.hideColumn(1)

        self.btn_setrot.clicked.connect(self.act_btn_rotation)
        self.btn_setpos.clicked.connect(self.act_btn_position)

        self.actionfExport.triggered.connect(self.act_btn_export)
        self.actionfSaveas.triggered.connect(self.act_btn_saveas)
        self.actionNew.triggered.connect(self.act_btn_new)
        self.actionfOpen.triggered.connect(self.act_btn_open)
        self.actionfClose.triggered.connect(self.close)

        self.actionBasecomp.triggered.connect(self.act_btn_add_basecomp)
        self.actionERA.triggered.connect(self.act_btn_add_era)
        self.actionSlat_Armor.triggered.connect(self.act_btn_add_slat)
        self.actionExtract_Revolve.triggered.connect(self.act_btn_add_revext)
        self.actionShapes_generator.triggered.connect(self.act_btn_shapegen)

        self.actionSavecomp.triggered.connect(self.act_btn_savecomp)
        self.actionOpencomp.triggered.connect(self.act_btn_opencomp)
        self.actionDeletecomp.triggered.connect(self.act_btn_delete)

        self.actionEdit.triggered.connect(self.act_btn_edit)
        self.actionArrays.triggered.connect(self.act_btn_arrays)
        self.action_Constrain.triggered.connect(self.act_btn_constrain)
        self.actionMove.triggered.connect(self.act_btn_move)

        self.actionManage.triggered.connect(self.act_btn_materials)
        self.actionSavematdb.triggered.connect(self.act_btn_savemat)
        self.actionLoadmatdb.triggered.connect(self.act_btn_loadmat)

        self.actionHetero.triggered.connect(self.act_btn_newmathetero)
        self.actionHelp.triggered.connect(self.act_btn_help)

        self.actionShooting.triggered.connect(self.act_btn_stats)
        self.actionAssembly.triggered.connect(self.act_btn_add_projectile)

        self.actionLighting.triggered.connect(self.test)
        self.actionColor.triggered.connect(self.act_btn_color)
        self.actionWireframe.triggered.connect(self.act_btn_edges)
        self.actionSolid.triggered.connect(self.act_btn_solid)

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
        self.menuStandart_shapes.setTitle(_translate("MainWindow", "Standart shapes", None))
        self.menuModify.setTitle(_translate("MainWindow", "&Modify", None))
        self.menuMa_terials.setTitle(_translate("MainWindow", "Ma&terials", None))
        self.menuCurrent.setTitle(_translate("MainWindow", "Current", None))
        self.menuNewmaterial.setTitle(_translate("MainWindow", "New material", None))
        self.menuProjectile.setTitle(_translate("MainWindow", "Projectiles", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
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
        self.actionOpencomp.setText(_translate("MainWindow", "Load...", None))
        self.actionSavecomp.setText(_translate("MainWindow", "Save as...", None))
        self.actionSavematdb.setText(_translate("MainWindow", "Save...", None))
        self.actionLoadmatdb.setText(_translate("MainWindow", "Load...", None))
        self.actionHomo.setText(_translate("MainWindow", "Homogeneous...", None))
        self.actionHetero.setText(_translate("MainWindow", "Heterogeneous...", None))
        self.actionColor.setText(_translate("MainWindow", "Color...", None))
        self.actionShooting.setText(_translate("MainWindow", "Shooting", None))
        self.actionSlat_Armor.setText(_translate("MainWindow", "Slat Armor", None))
        self.actionNew.setText(_translate("MainWindow", "New...", None))
        self.actionMove.setText(_translate("MainWindow", "Move...", None))
        self.actionAssembly.setText(_translate("MainWindow", "Assembly", None))
        self.actionShapes_generator.setText(_translate("MainWindow", "Shapes generator", None))
        self.actionExtract_Revolve.setText(_translate("MainWindow", "Extract/Revolve", None))
        self.actionMirror.setText(_translate("MainWindow", "Mirror...", None))

    def act_btn_new(self):
        for comp in reversed(self.components):
            self.delcomp(comp)
        self.glwidget.objects.clear()
        db = DB('MATERIALS\\GOST.xml')
        mat = db.getdefmat()
        self.materials = {db.exportmat(mat)}
        self.glwidget.addtoconsole('New model.')

    def act_btn_move(self):
        self.movewind = Ui_move(self.wox + self.frameGeometry().width() - 294, self.woy + 20)
        self.movewind.loadinit(self)
        self.movewind.show()

    def act_btn_add_basecomp(self):
        filedialog = QtGui.QFileDialog(self)
        filepath = filedialog.getOpenFileName(self, "Open STL geometry", "CNST\GEO\dz.stl", filter="stl (*.stl *.)")
        # filepath = "C:\\Users\\User\Documents\GitHub\ConstructorM4\CNST\GEO\\cube100.stl"
        if filepath:
            # self.act_btn_add(filepath)
            self.addwind = Ui_wid_addcomp()
            self.addwind.show()
            self.addwind.newwobj(filepath, self)

    def act_btn_add_era(self):
        self.addwinddz = Ui_wid_adddz()
        self.addwinddz.show()
        self.addwinddz.loadinit("skip", self)

    def act_btn_add_slat(self):
        self.addwindslat = Ui_wid_addslat()
        self.addwindslat.show()
        self.addwindslat.loadinit('skip', self)

    def act_btn_add_revext(self):
        self.addwindrevext = Ui_wid_revext()
        self.addwindrevext.show()
        self.addwindrevext.loadinit(self)

    def act_btn_shapegen(self):
        self.addwindshapegen = Ui_wid_addshape()
        self.addwindshapegen.show()
        self.addwindshapegen.loadinit(self)

    def act_btn_add_projectile(self):
        self.addwindproj = Ui_wid_addproj()
        self.addwindproj.show()
        self.addwindproj.loadinit('skip', self)

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
            self.glwidget.addtoconsole('Component removed.')

    def act_btn_help(self):
        ps = self.activecomp.geoobj.psMatrix
        self.components[1].geoobj.setonmv(ps)
        self.glwidget.upmat()

    def act_btn_stats(self):
        self.statswind = Ui_wid_stats()
        self.statswind.show()
        self.statswind.loadinit(self)

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

    def act_btn_color(self):
        self.colorwnd = Ui_color()
        self.colorwnd.loadinit(self, self.activecomp)
        self.colorwnd.show()

    def act_btn_solid(self):
        self.glwidget.dropsphs()
        self.glwidget.droplines()
        self.glwidget.sphinit()
        self.glwidget.lineinit()
        self.glwidget.upmat()

    def act_btn_edit(self):
        category = self.activecomp.categoryname
        if category == 'Main components':
            self.addwind = Ui_wid_addcomp()
            self.addwind.show()
            self.addwind.newwobj(self.activecomp, self, edt=True)
        elif category == "ERA":
            self.addwinddz = Ui_wid_adddz()
            self.addwinddz.show()
            self.addwinddz.loadinit(self.activecomp, self, edt=True)
        elif category == 'SLAT':
            self.addwindslat = Ui_wid_addslat()
            self.addwindslat.show()
            self.addwindslat.loadinit(self.activecomp, self, edt=True)
        elif category == 'RV':
            self.addwindrevext = Ui_wid_revext()
            self.addwindrevext.show()
            self.addwindrevext.loadinit(self,comp = self.activecomp)
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
            self.glwidget.addtoconsole('Model saved as: '+file)

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
                        self.materials.add(mat)
            self.glwidget.upmat()

    def act_btn_savecomp(self):
        comp = self.activecomp
        filedialog = QtGui.QFileDialog(self)
        file = filedialog.getSaveFileName(self, "Save Component As", "SAVES\COMPONENTS\\" + comp.getname() + ".svc",
                                          filter="svc (*.svc *.)")
        if file:
            # file = 'RESULTS\SAVECOMP.sav'
            self.saveobj(comp, file)
            self.glwidget.addtoconsole('Component saved as: ' + file)

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
        file = filedialog.getOpenFileName(self, "Load Materials Database", "SAVES\MATERIALS\\",
                                          filter="svd (*.svd *.)")
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
        child = QtGui.QTreeWidgetItem(category, [name, str(comp.getid())])
        child.setCheckState(0, QtCore.Qt.Checked)
        child.setFlags(child.flags())
        self.tre_manager.clearSelection()
        self.activecomp = None
        self.disablebtn(True)

    def setcategory(self, cat):
        catitem = self.tre_manager.findItems(cat, QtCore.Qt.MatchFixedString)
        if not catitem:
            parent = QtGui.QTreeWidgetItem(self.tre_manager, [cat, '-1'])
            parent.setFlags(parent.flags() | QtCore.Qt.ItemIsTristate | QtCore.Qt.ItemIsUserCheckable)
            parent.setCheckState(0, QtCore.Qt.Checked)
            return parent
        else:
            return catitem[0]

    def pushmaterials(self, comp):
        matnames = {}
        for mat in self.materials:
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
        self.actionColor.setDisabled(bool)

    def delcomp(self, comp):
        parent = self.tre_manager.findItems(comp.categoryname, QtCore.Qt.MatchFixedString, 0)[0]
        child = \
            self.tre_manager.findItems(str(comp.getid()), QtCore.Qt.MatchFixedString | QtCore.Qt.MatchRecursive, 1)[
                0]
        child.setCheckState(0, QtCore.Qt.Checked)
        parent.removeChild(child)
        if parent.childCount() == 0:
            (parent.parent() or self.tre_manager.invisibleRootItem()).removeChild(parent)

        self.components.remove(comp)
        self.glwidget.objects.remove(comp.getgeo())

    def test(self):
        print(self.glwidget.objects[0].col)

    def act_btn_edges(self):
        self.glwidget.edgemodeswitch()

    def getcompbygeoid(self, id):
        for comp in self.components:
            if comp.getid() == id:
                return comp

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

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_E:
            picarr, w, h = self.glwidget.getpic()
            # picdata = picarr[0]
            # img = Image.frombytes("RGBA", (w, h), picdata)
            # img = ImageOps.flip(img)
            # img.save('RESULTS\pic.png', 'PNG')
            self.shoots(w, h, picarr)

            def foo():
                self.shoots(w, h, picarr)

                # import timeit
                # t = timeit.timeit(foo, number=10)
                # print(t)
                # self.startshoot(w, h, picdata)
        # elif event.key() == QtCore.Qt.Key_Enter:
        #     self.proceed()

        event.accept()

    def shoots(self, w, h, picarr):
        self.glwidget.dropsphs()
        mux, muy = w / 2, h / 2
        n, mu, sigmax, sigmay = 1000, 0, w / 6, h / 6
        sx = np.random.normal(mux, sigmax, n)
        sy = np.random.normal(muy, sigmay, n)
        sx = (sx[np.where(abs(sx - w / 2) < w / 2 - 1)])
        sy = (sy[np.where(abs(sy - h / 2) < h / 2 - 1)])
        sx = list(map(int, np.rint(sx).astype(int)))
        sy = list(map(int, np.rint(sy).astype(int)))
        oids = {}
        cds = []
        for i, picdata in enumerate(picarr):
            # print(20*'-',i)
            imgc = Image.frombytes("RGBA", (w, h), picdata)
            imgc = ImageOps.flip(imgc)
            # imgc.save('RESULTS\\norm'+str(i)+'.png', 'PNG')
            datac = imgc.load()
            for i, x, y in zip(range(n), sx, sy):
                clr = datac[x, y]
                plid = clr[0] + clr[1] * 256
                oid = clr[2]
                if oid != 255:
                    ci = self.glwidget.getint(oid, plid, (x, y))
                    self.glwidget.sphcdlist.append(list(ci))
                    # cds.append(ci)
                    oids.setdefault(oid, []).append(i)
        # for k,v in oids.items():
        #     print(k,'\t:\t',len(v))
        self.glwidget.sphinit()
        self.glwidget.upmat()

    def startshoot(self, w, h, picdata):
        mux, muy = w / 2, h / 2
        n, mu, sigmax, sigmay = 100, 0, w / 6, h / 6
        sx = np.random.normal(mux, sigmax, n)
        sy = np.random.normal(muy, sigmay, n)
        orgpic = glReadPixels(0, 0, w, h, GL_RGBA, GL_UNSIGNED_BYTE)
        img = Image.frombytes("RGBA", (w, h), orgpic)
        data = img.load()
        imgc = Image.frombytes("RGBA", (w, h), picdata)
        imgc = ImageOps.flip(imgc)
        datac = imgc.load()
        oids = {}
        cds = []
        self.glwidget.dropsphs()
        for x, y in zip(sx, sy):
            if x <= w and x >= 0 and y >= 0 and y <= h:
                clr = datac[int(x), int(y)]
                # print(clr)
                plid = clr[0] + clr[1] * 256
                oid = clr[2]
                if oid != 255:
                    ci = self.glwidget.getint(oid, plid, (x, y))
                    if ci:
                        self.glwidget.sphcdlist.append(list(ci))
                        cds.append(ci)

                        # self.glwidget.sphinit()
                if plid not in oids.keys():
                    oids[plid] = 1
                else:
                    oids[plid] += 1
                data[int(x), int(y)] = (255, 0, 0, 255)

        self.glwidget.upmat()
        for k, v in oids.items():
            print(k, v)
        with open('RESULTS\ints.txt', 'w') as f:
            for cd in cds:
                f.write(str(cd) + '\n')
        # print(list(cds[0]))
        img = ImageOps.flip(img)
        img.show()
        img.save('RESULTS\\norm2.png', 'PNG')

if __name__ == '__main__':
        app = QtGui.QApplication(sys.argv)
        window = Ui_MainWindow()
        window.show()
        sys.exit(app.exec_())

