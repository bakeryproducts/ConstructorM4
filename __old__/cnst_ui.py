import math, random
import sys
from glwidget import *
import pickle
from PIL import Image
from PIL import ImageOps

from CNST.clGEOOBJ import GEOOBJ
from MATERIALS.db import DB
from addcomp_ui import Ui_wid_addcomp
# from crearray_ui import Ui_crearray
# from materials_ui import Ui_materials
# from creconstrained_ui import Ui_creconstrained
# from newmathetero_ui import Ui_newmathetero
# from adddz_ui import Ui_wid_adddz
# from color_ui import Ui_color
# from addslat_ui import Ui_wid_addslat
# from move_ui import Ui_move
# from addproj_ui import Ui_wid_addproj
# from stats_ui import Ui_wid_stats
# from statsfsv_ui import Ui_wid_statsfsv
# from axialff_ui import Ui_wid_axialff
# from statsshow_ui import Ui_wid_statsshow
# from fsu_ui import Ui_wid_fsu
# from addrevext_ui import Ui_wid_revext
# from standartshape_ui import Ui_wid_addshape
import re
#from PyQt4 import QtCore, QtGui
from qtpy import QtCore,QtGui,QtWidgets
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
        return QtWidgets.QApplication.translate(context, text, disambig)


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.wsizew, self.wsizeh = 1200, 600
        self.wox, self.woy = 100, 100
        self.setGeometry(100, 100, 100, 100)

        self.setupUi(self)
        self.components = []
        self.activecompid = 0

        # db = DB('MATERIALS\\GOST.xml')
        # mat = db.getdefmat()
        # self.materials = {db.exportmat(mat)}

        self.fexit = False
        #self.act_btn_open()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1000, 600)
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tre_manager = QtWidgets.QTreeWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tre_manager.sizePolicy().hasHeightForWidth())
        self.tre_manager.setSizePolicy(sizePolicy)
        self.tre_manager.setMaximumSize(QtCore.QSize(160, 16777215))
        self.tre_manager.setFrameShape(QtWidgets.QFrame.Box)
        self.tre_manager.setObjectName(_fromUtf8("tre_manager"))
        self.tre_manager.headerItem().setText(0, _fromUtf8("1"))
        self.horizontalLayout.addWidget(self.tre_manager)
        self.glbox = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.glbox.sizePolicy().hasHeightForWidth())
        self.glbox.setSizePolicy(sizePolicy)
        self.glbox.setMinimumSize(QtCore.QSize(200, 0))
        self.glbox.setObjectName(_fromUtf8("glbox"))
        self.horizontalLayout.addWidget(self.glbox)

        self.horizontalLayout.addWidget(self.glbox)
        self.glwidget = GLWidget()
        mainLayout = QtWidgets.QHBoxLayout()
        mainLayout.addWidget(self.glwidget)
        self.glbox.setLayout(mainLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 34))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuViews = QtWidgets.QMenu(self.menuView)
        self.menuViews.setObjectName(_fromUtf8("menuViews"))
        self.menuVisual_Style = QtWidgets.QMenu(self.menuView)
        self.menuVisual_Style.setObjectName(_fromUtf8("menuVisual_Style"))
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        self.menuComponents = QtWidgets.QMenu(self.menubar)
        self.menuComponents.setGeometry(QtCore.QRect(462, 234, 204, 168))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuComponents.sizePolicy().hasHeightForWidth())
        self.menuComponents.setSizePolicy(sizePolicy)
        self.menuComponents.setMinimumSize(QtCore.QSize(150, 0))
        self.menuComponents.setObjectName(_fromUtf8("menuComponents"))
        self.menuAddcomp = QtWidgets.QMenu(self.menuComponents)
        self.menuAddcomp.setGeometry(QtCore.QRect(661, 237, 304, 234))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuAddcomp.sizePolicy().hasHeightForWidth())
        self.menuAddcomp.setSizePolicy(sizePolicy)
        self.menuAddcomp.setMinimumSize(QtCore.QSize(0, 0))
        self.menuAddcomp.setObjectName(_fromUtf8("menuAddcomp"))
        self.menuStandart_shapes = QtWidgets.QMenu(self.menuAddcomp)
        self.menuStandart_shapes.setObjectName(_fromUtf8("menuStandart_shapes"))
        self.menuModify = QtWidgets.QMenu(self.menubar)
        self.menuModify.setObjectName(_fromUtf8("menuModify"))
        self.menuMove = QtWidgets.QMenu(self.menuModify)
        self.menuMove.setObjectName(_fromUtf8("menuMove"))
        self.menuMa_terials = QtWidgets.QMenu(self.menubar)
        self.menuMa_terials.setObjectName(_fromUtf8("menuMa_terials"))
        self.menuCurrent = QtWidgets.QMenu(self.menuMa_terials)
        self.menuCurrent.setObjectName(_fromUtf8("menuCurrent"))
        self.menuNewmaterial = QtWidgets.QMenu(self.menuMa_terials)
        self.menuNewmaterial.setObjectName(_fromUtf8("menuNewmaterial"))
        self.menuProjectile = QtWidgets.QMenu(self.menubar)
        self.menuProjectile.setObjectName(_fromUtf8("menuProjectile"))
        self.menuStatistics = QtWidgets.QMenu(self.menubar)
        self.menuStatistics.setObjectName(_fromUtf8("menuStatistics"))
        self.menuDirectional_shooting = QtWidgets.QMenu(self.menuStatistics)
        self.menuDirectional_shooting.setObjectName(_fromUtf8("menuDirectional_shooting"))
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        self.actionfSaveas = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/TBicons/folder_full_accept.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionfSaveas.setIcon(icon)
        self.actionfSaveas.setObjectName(_fromUtf8("actionfSaveas"))
        self.actionfExport = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/TBicons/application_next.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionfExport.setIcon(icon1)
        self.actionfExport.setObjectName(_fromUtf8("actionfExport"))
        self.actionFront = QtWidgets.QAction(MainWindow)
        self.actionFront.setObjectName(_fromUtf8("actionFront"))
        self.actionBack = QtWidgets.QAction(MainWindow)
        self.actionBack.setObjectName(_fromUtf8("actionBack"))
        self.actionLeft = QtWidgets.QAction(MainWindow)
        self.actionLeft.setObjectName(_fromUtf8("actionLeft"))
        self.actionRight = QtWidgets.QAction(MainWindow)
        self.actionRight.setObjectName(_fromUtf8("actionRight"))
        self.actionTop = QtWidgets.QAction(MainWindow)
        self.actionTop.setObjectName(_fromUtf8("actionTop"))
        self.actionBottom = QtWidgets.QAction(MainWindow)
        self.actionBottom.setObjectName(_fromUtf8("actionBottom"))
        self.actionSolid = QtWidgets.QAction(MainWindow)
        self.actionSolid.setObjectName(_fromUtf8("actionSolid"))
        self.actionWireframe = QtWidgets.QAction(MainWindow)
        self.actionWireframe.setObjectName(_fromUtf8("actionWireframe"))
        self.actionLighting = QtWidgets.QAction(MainWindow)
        self.actionLighting.setCheckable(True)
        self.actionLighting.setObjectName(_fromUtf8("actionLighting"))
        self.actionBasecomp = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/TBicons/page_add.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBasecomp.setIcon(icon2)
        self.actionBasecomp.setObjectName(_fromUtf8("actionBasecomp"))
        self.actionArrays = QtWidgets.QAction(MainWindow)
        self.actionArrays.setObjectName(_fromUtf8("actionArrays"))
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.actionERA = QtWidgets.QAction(MainWindow)
        self.actionERA.setObjectName(_fromUtf8("actionERA"))
        self.action_Constrain = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/TBicons/page_swap.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Constrain.setIcon(icon3)
        self.action_Constrain.setObjectName(_fromUtf8("action_Constrain"))
        self.actionManage = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/TBicons/database_process.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionManage.setIcon(icon4)
        self.actionManage.setObjectName(_fromUtf8("actionManage"))
        self.actionfOpen = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/TBicons/folder_full.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionfOpen.setIcon(icon5)
        self.actionfOpen.setObjectName(_fromUtf8("actionfOpen"))
        self.actionfClose = QtWidgets.QAction(MainWindow)
        self.actionfClose.setObjectName(_fromUtf8("actionfClose"))
        self.actionEdit = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/TBicons/note_edit.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEdit.setIcon(icon6)
        self.actionEdit.setObjectName(_fromUtf8("actionEdit"))
        self.actionDeletecomp = QtWidgets.QAction(MainWindow)
        self.actionDeletecomp.setObjectName(_fromUtf8("actionDeletecomp"))
        self.actionOpencomp = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/TBicons/page_up.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpencomp.setIcon(icon7)
        self.actionOpencomp.setObjectName(_fromUtf8("actionOpencomp"))
        self.actionSavecomp = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/TBicons/page_down.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSavecomp.setIcon(icon8)
        self.actionSavecomp.setObjectName(_fromUtf8("actionSavecomp"))
        self.actionSavematdb = QtWidgets.QAction(MainWindow)
        self.actionSavematdb.setObjectName(_fromUtf8("actionSavematdb"))
        self.actionLoadmatdb = QtWidgets.QAction(MainWindow)
        self.actionLoadmatdb.setObjectName(_fromUtf8("actionLoadmatdb"))
        self.actionHomo = QtWidgets.QAction(MainWindow)
        self.actionHomo.setObjectName(_fromUtf8("actionHomo"))
        self.actionHetero = QtWidgets.QAction(MainWindow)
        self.actionHetero.setObjectName(_fromUtf8("actionHetero"))
        self.actionColor = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/TBicons/process.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionColor.setIcon(icon9)
        self.actionColor.setObjectName(_fromUtf8("actionColor"))
        self.actionShooting = QtWidgets.QAction(MainWindow)
        self.actionShooting.setObjectName(_fromUtf8("actionShooting"))
        self.actionSlat_Armor = QtWidgets.QAction(MainWindow)
        self.actionSlat_Armor.setObjectName(_fromUtf8("actionSlat_Armor"))
        self.actionNew = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/TBicons/ico/blog_post.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon10)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionAssembly = QtWidgets.QAction(MainWindow)
        self.actionAssembly.setObjectName(_fromUtf8("actionAssembly"))
        self.actionShapes_generator = QtWidgets.QAction(MainWindow)
        self.actionShapes_generator.setObjectName(_fromUtf8("actionShapes_generator"))
        self.actionExtract_Revolve = QtWidgets.QAction(MainWindow)
        self.actionExtract_Revolve.setObjectName(_fromUtf8("actionExtract_Revolve"))
        self.actionMirror = QtWidgets.QAction(MainWindow)
        self.actionMirror.setObjectName(_fromUtf8("actionMirror"))
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setObjectName(_fromUtf8("actionPreferences"))
        self.actionOrbital_shooting = QtWidgets.QAction(MainWindow)
        self.actionOrbital_shooting.setObjectName(_fromUtf8("actionOrbital_shooting"))
        self.actionFunctional_scheme = QtWidgets.QAction(MainWindow)
        self.actionFunctional_scheme.setObjectName(_fromUtf8("actionFunctional_scheme"))
        self.actionArmor_th = QtWidgets.QAction(MainWindow)
        self.actionArmor_th.setCheckable(True)
        self.actionArmor_th.setObjectName(_fromUtf8("actionArmor_th"))
        self.actionSingle_shots = QtWidgets.QAction(MainWindow)
        self.actionSingle_shots.setObjectName(_fromUtf8("actionSingle_shots"))
        self.actionAxial_FF = QtWidgets.QAction(MainWindow)
        self.actionAxial_FF.setObjectName(_fromUtf8("actionAxial_FF"))
        self.actionTestop1 = QtWidgets.QAction(MainWindow)
        self.actionTestop1.setObjectName(_fromUtf8("actionTestop1"))
        self.actionTestop2 = QtWidgets.QAction(MainWindow)
        self.actionTestop2.setObjectName(_fromUtf8("actionTestop2"))
        self.actionFree_roaming = QtWidgets.QAction(MainWindow)
        self.actionFree_roaming.setObjectName(_fromUtf8("actionFree_roaming"))
        self.actionSet_on_coord = QtWidgets.QAction(MainWindow)
        self.actionSet_on_coord.setObjectName(_fromUtf8("actionSet_on_coord"))
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionfOpen)
        self.menuFile.addAction(self.actionfSaveas)
        self.menuFile.addAction(self.actionfExport)
        self.menuFile.addAction(self.actionPreferences)
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
        self.menuView.addAction(self.actionArmor_th)
        self.menuView.addAction(self.actionColor)
        self.menuAbout.addAction(self.actionHelp)
        self.menuAbout.addAction(self.actionTestop1)
        self.menuAbout.addAction(self.actionTestop2)
        self.menuStandart_shapes.addAction(self.actionShapes_generator)
        self.menuStandart_shapes.addAction(self.actionExtract_Revolve)
        self.menuAddcomp.addAction(self.actionOpencomp)
        self.menuAddcomp.addAction(self.actionBasecomp)
        self.menuAddcomp.addAction(self.menuStandart_shapes.menuAction())
        self.menuAddcomp.addAction(self.actionERA)
        self.menuAddcomp.addAction(self.actionSlat_Armor)
        self.menuComponents.addAction(self.menuAddcomp.menuAction())
        self.menuComponents.addAction(self.actionDeletecomp)
        self.menuComponents.addAction(self.actionSavecomp)
        self.menuMove.addAction(self.actionFree_roaming)
        self.menuMove.addAction(self.actionSet_on_coord)
        self.menuModify.addAction(self.actionEdit)
        self.menuModify.addAction(self.menuMove.menuAction())
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
        self.menuDirectional_shooting.addAction(self.actionSingle_shots)
        self.menuDirectional_shooting.addAction(self.actionAxial_FF)
        self.menuStatistics.addAction(self.menuDirectional_shooting.menuAction())
        self.menuStatistics.addAction(self.actionOrbital_shooting)
        self.menuStatistics.addAction(self.actionFunctional_scheme)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuComponents.menuAction())
        self.menubar.addAction(self.menuModify.menuAction())
        self.menubar.addAction(self.menuMa_terials.menuAction())
        self.menubar.addAction(self.menuProjectile.menuAction())
        self.menubar.addAction(self.menuStatistics.menuAction())
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


        # self.actionfExport.triggered.connect(self.act_btn_export)
        # self.actionfSaveas.triggered.connect(self.act_btn_saveas)
        # self.actionNew.triggered.connect(self.act_btn_new)
        # self.actionfOpen.triggered.connect(self.act_btn_open)
        # self.actionfClose.triggered.connect(self.close)
        #
        # self.actionBasecomp.triggered.connect(self.act_btn_add_basecomp)
        # self.actionERA.triggered.connect(self.act_btn_add_era)
        # self.actionSlat_Armor.triggered.connect(self.act_btn_add_slat)
        # self.actionExtract_Revolve.triggered.connect(self.act_btn_add_revext)
        # self.actionShapes_generator.triggered.connect(self.act_btn_shapegen)
        #
        # self.actionSavecomp.triggered.connect(self.act_btn_savecomp)
        # self.actionOpencomp.triggered.connect(self.act_btn_opencomp)
        # self.actionDeletecomp.triggered.connect(self.act_btn_delete)
        #
        # self.actionEdit.triggered.connect(self.act_btn_edit)
        # self.actionArrays.triggered.connect(self.act_btn_arrays)
        # self.action_Constrain.triggered.connect(self.act_btn_constrain)
        # self.actionFree_roaming.triggered.connect(self.act_btn_move)
        #
        # self.actionManage.triggered.connect(self.act_btn_materials)
        # self.actionSavematdb.triggered.connect(self.act_btn_savemat)
        # self.actionLoadmatdb.triggered.connect(self.act_btn_loadmat)
        #
        # self.actionHetero.triggered.connect(self.act_btn_newmathetero)
        # self.actionHelp.triggered.connect(self.act_btn_help)
        #
        # self.actionSingle_shots.triggered.connect(self.act_btn_stats)
        # self.actionTestop1.triggered.connect(self.act_btn_statsfsv)
        #
        # self.actionAxial_FF.triggered.connect(self.act_btn_axialff)
        # self.actionOrbital_shooting.triggered.connect(self.act_btn_statsshow)
        # self.actionFunctional_scheme.triggered.connect(self.act_btn_fsu)
        #
        # self.actionAssembly.triggered.connect(self.act_btn_add_projectile)
        #
        # self.actionLighting.triggered.connect(self.test)
        # self.actionArmor_th.triggered.connect(self.act_btn_armor)
        #
        # self.actionColor.triggered.connect(self.act_btn_color)
        # self.actionWireframe.triggered.connect(self.act_btn_edges)
        # self.actionSolid.triggered.connect(self.act_btn_solid)
        # self.actionFront.triggered.connect(self.act_btn_front)
        # self.actionBack.triggered.connect(self.act_btn_back)
        # self.actionTop.triggered.connect(self.act_btn_top)
        # self.actionBottom.triggered.connect(self.act_btn_bottom)
        # self.actionLeft.triggered.connect(self.act_btn_left)
        # self.actionRight.triggered.connect(self.act_btn_right)

        self.glwidget.mode = "pick0"
        #self.disablelay(True)
        self.disablebtn(True)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Constructor", None))
        self.menuFile.setTitle(_translate("MainWindow", "&File", None))
        self.menuView.setTitle(_translate("MainWindow", "&View", None))
        self.menuViews.setTitle(_translate("MainWindow", "Views", None))
        self.menuVisual_Style.setTitle(_translate("MainWindow", "Visual Style", None))
        self.menuAbout.setTitle(_translate("MainWindow", "Ab&out", None))
        self.menuComponents.setTitle(_translate("MainWindow", "&Components", None))
        self.menuAddcomp.setTitle(_translate("MainWindow", "&Add", None))
        self.menuStandart_shapes.setTitle(_translate("MainWindow", "Standart shapes", None))
        self.menuModify.setTitle(_translate("MainWindow", "&Modify", None))
        self.menuMove.setTitle(_translate("MainWindow", "Move...", None))
        self.menuMa_terials.setTitle(_translate("MainWindow", "Ma&terials", None))
        self.menuCurrent.setTitle(_translate("MainWindow", "Current", None))
        self.menuNewmaterial.setTitle(_translate("MainWindow", "New material", None))
        self.menuProjectile.setTitle(_translate("MainWindow", "Projectiles", None))
        self.menuStatistics.setTitle(_translate("MainWindow", "Statistics", None))
        self.menuDirectional_shooting.setTitle(_translate("MainWindow", "Directional shooting...", None))
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
        self.actionBasecomp.setText(_translate("MainWindow", "&Base component...", None))
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
        self.actionAssembly.setText(_translate("MainWindow", "Assembly", None))
        self.actionShapes_generator.setText(_translate("MainWindow", "Shapes generator", None))
        self.actionExtract_Revolve.setText(_translate("MainWindow", "Extract/Revolve", None))
        self.actionMirror.setText(_translate("MainWindow", "Mirror...", None))
        self.actionPreferences.setText(_translate("MainWindow", "Preferences...", None))
        self.actionOrbital_shooting.setText(_translate("MainWindow", "Orbital shooting...", None))
        self.actionFunctional_scheme.setText(_translate("MainWindow", "Functional scheme...", None))
        self.actionArmor_th.setText(_translate("MainWindow", "Armor th.", None))
        self.actionSingle_shots.setText(_translate("MainWindow", "Single shots", None))
        self.actionAxial_FF.setText(_translate("MainWindow", "Axial FF", None))
        self.actionTestop1.setText(_translate("MainWindow", "testop1", None))
        self.actionTestop2.setText(_translate("MainWindow", "testop2", None))
        self.actionFree_roaming.setText(_translate("MainWindow", "Free moving", None))
        self.actionSet_on_coord.setText(_translate("MainWindow", "Set on coord.", None))


    def act_btn_new(self):
        for comp in reversed(self.components):
            self.delcomp(comp)
        self.glwidget.objects.clear()
        db = DB('MATERIALS\\GOST.xml')
        mat = db.getdefmat()
        self.materials = {db.exportmat(mat)}
        self.glwidget.addtoconsole('New model.')

    # def act_btn_move(self):
    #     self.movewind = Ui_move(self.wox + self.frameGeometry().width() - 294, self.woy + 20)
    #     self.movewind.loadinit(self)
    #     self.movewind.show()
    #
    # def act_btn_add_basecomp(self):
    #     filedialog = QtWidgets.QFileDialog(self)
    #     filepath = filedialog.getOpenFileName(self, "Open STL geometry", "CNST\GEO\dz.stl", filter="stl (*.stl *.)")
    #     # filepath = "C:\\Users\\User\Documents\GitHub\ConstructorM4\CNST\GEO\\cube100.stl"
    #     if filepath:
    #         # self.act_btn_add(filepath)
    #         self.addwind = Ui_wid_addcomp()
    #         self.addwind.show()
    #         self.addwind.newwobj(filepath, self)
    #
    # def act_btn_add_era(self):
    #     self.addwinddz = Ui_wid_adddz()
    #     self.addwinddz.show()
    #     self.addwinddz.loadinit("skip", self)
    #
    # def act_btn_add_slat(self):
    #     self.addwindslat = Ui_wid_addslat()
    #     self.addwindslat.show()
    #     self.addwindslat.loadinit(self)
    #
    # def act_btn_add_revext(self):
    #     self.addwindrevext = Ui_wid_revext()
    #     self.addwindrevext.show()
    #     self.addwindrevext.loadinit(self)
    #
    # def act_btn_shapegen(self):
    #     self.addwindshapegen = Ui_wid_addshape()
    #     self.addwindshapegen.show()
    #     self.addwindshapegen.loadinit(self)
    #
    # def act_btn_add_projectile(self):
    #     self.addwindproj = Ui_wid_addproj()
    #     self.addwindproj.show()
    #     self.addwindproj.loadinit('skip', self)
    #
    # def act_btn_axialff(self):
    #     self.addwindaxial = Ui_wid_axialff()
    #     self.addwindaxial.show()
    #     self.addwindaxial.loadinit(self)


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


    def act_btn_armor(self):
        if self.actionArmor_th.isChecked():
            self.armor_color()
        else:
            self.activecomp.geoobj.ffc=False
            self.glwidget.upmat()

    # def armor_color(self):
    #     from colour import Color
    #     blue = Color("blue")
    #     comp = self.activecomp#self.components[0]
    #     ths = comp.thickarr[:]
    #     uniths = set(ths)
    #     n = len(uniths)
    #     colors = list(blue.range_to(Color("red"), n))
    #     cdict={}
    #     for th,col in zip(sorted(uniths),colors):
    #         cdict[th] = [255*c for c in col.rgb]
    #     newcols=[]
    #     for th in ths:
    #         newcols.append(cdict[th])
    #     newcols = np.array([newcols[j] for j, face in enumerate(comp.geoobj.faces) for i in range(len(face))], dtype=np.ubyte)
    #     comp.geoobj.cbinit(newcols)
    #     comp.geoobj.ffc = True
    #     self.glwidget.upmat()

    def act_btn_help(self):
        pass

    # def act_btn_stats(self):
    #     self.statswind = Ui_wid_stats()
    #     self.statswind.show()
    #     self.statswind.loadinit(self)
    #
    # def act_btn_statsfsv(self):
    #     self.statsfsvwind = Ui_wid_statsfsv()
    #     self.statsfsvwind.show()
    #     self.statsfsvwind.loadinit(self)
    #
    #
    # def act_btn_statsshow(self):
    #     self.statsshowwind = Ui_wid_statsshow()
    #     self.statsshowwind.show()
    #     self.statsshowwind.loadinit(self)
    #
    # def act_btn_fsu(self):
    #     self.fsuwind = Ui_wid_fsu()
    #     self.fsuwind.show()
    #     self.fsuwind.loadinit(self)
    #
    # def act_btn_arrays(self):
    #     self.arrayswind = Ui_crearray(self.wox + self.frameGeometry().width() - 294, self.woy + 20)
    #     self.arrayswind.loadinit(self)
    #     self.arrayswind.show()
    #
    # def act_btn_constrain(self):
    #     self.constrainwind = Ui_creconstrained(self.wox + self.frameGeometry().width() - 294, self.woy + 20)
    #     self.constrainwind.loadinit(self)
    #     self.constrainwind.show()
    #
    # def act_btn_materials(self):
    #     self.materialswind = Ui_materials()
    #     self.materialswind.loadinit(self)
    #     self.materialswind.show()
    #
    # def act_btn_color(self):
    #     self.colorwnd = Ui_color()
    #     self.colorwnd.loadinit(self, self.activecomp)
    #     self.colorwnd.show()

    def act_btn_solid(self):
        self.glwidget.dropsphs()
        self.glwidget.droplines()
        self.glwidget.sphinit()
        self.glwidget.lineinit()
        self.glwidget.upmat()

    # def act_btn_edit(self):
    #     category = self.activecomp.categoryname
    #     if category == 'Main components':
    #         self.addwind = Ui_wid_addcomp()
    #         self.addwind.show()
    #         self.addwind.newwobj(self.activecomp, self, edt=True)
    #     elif category == "ERA":
    #         self.addwinddz = Ui_wid_adddz()
    #         self.addwinddz.show()
    #         self.addwinddz.loadinit(self.activecomp, self, edt=True)
    #     elif category == 'SLAT':
    #         self.addwindslat = Ui_wid_addslat()
    #         self.addwindslat.show()
    #         self.addwindslat.loadinit(self, comp=self.activecomp)
    #     elif category == 'RV':
    #         self.addwindrevext = Ui_wid_revext()
    #         self.addwindrevext.show()
    #         self.addwindrevext.loadinit(self, comp=self.activecomp)
    #     else:
    #         pass

    def trywrite(self, text, file):
        try:
            file.write(text)
        except UnicodeEncodeError:
            file.write(text.encode('cp1251').decode('latin1'))

    def act_btn_export(self):
        filedialog = QtGui.QFileDialog(self)
        path = filedialog.getSaveFileName(self, "Save Model As", "RESULTS\EXPORT.trg", filter="trg (*.trg *.)")
        if path:
            # CANT DO ON UNIX
            pass


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
            self.glwidget.addtoconsole('Model saved as: ' + file)

    def act_btn_open(self):
        filedialog = QtGui.QFileDialog(self)
        file = filedialog.getOpenFileName(self, "Load Model", "SAVES\MODELS\MODEL.svm", filter="svm (*.svm *.)")
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

    # def act_btn_newmathetero(self):
    #     self.newmathetwind = Ui_newmathetero()
    #     self.newmathetwind.loadinit(self)
    #     self.newmathetwind.show()

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
                self.activecomp = None
                self.disablebtn(True)
            else:
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
        # cat = comp.categoryname
        cat = comp.comptype
        category = self.setcategory(cat)
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

    def test(self):
        pass

    def act_btn_edges(self):
        self.glwidget.edgemodeswitch()

    def getcompbygeoid(self, id):
        for comp in self.components:
            if comp.getid() == id:
                return comp

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

    def fsvinit(self, fsvstring):
        func = '''
def fsv(ARGS):
    t = FSV
    return t
    '''
        compstr = ''
        for i, comp in enumerate(self.components):
            compstr += comp.getname() + ','

        func = re.sub('ARGS', compstr[:-1], func)
        func = re.sub('FSV', fsvstring, func)
        print(func)
        exec(func, globals())

    # def fsvact(self, ids):
    #     li = len(self.components) * [0]
    #     for id in ids:
    #         li[id] = 1
    #     return fsv(*li)

    def closeEvent(self, event):
        self.glwidget.objects = []
        self.glwidget.upmat()
        for comp in self.components:
            del (comp.geoobj)
            # answer = QtGui.QMessageBox.question(
            #     self,
            #     'QUIT',
            #     'Are you sure?',
            #     QtGui.QMessageBox.Yes,
            #     QtGui.QMessageBox.No)
            # if answer == QtGui.QMessageBox.Yes:
            #     event.accept()
            # else:
            #     event.ignore()

            #
            # def keyPressEvent(self, event):
            #     if event.key() == QtCore.Qt.Key_E:
            #         picarr, w, h = self.glwidget.getpic()
            #         # picdata = picarr[0]
            #         # img = Image.frombytes("RGBA", (w, h), picdata)
            #         # img = ImageOps.flip(img)
            #         # img.save('RESULTS\pic.png', 'PNG')
            #         self.shoots(w, h, picarr)
            #
            #         def foo():
            #             self.shoots(w, h, picarr)
            #
            #             # import timeit
            #             # t = timeit.timeit(foo, number=10)
            #             # print(t)
            #             # self.startshoot(w, h, picdata)
            #
            #     # elif event.key() == QtCore.Qt.Key_Enter:
            #     #     self.proceed()
            #
            #     event.accept()



if __name__ == '__main__':
        app = QtWidgets.QApplication(sys.argv)
        window = Ui_MainWindow()
        window.show()
        sys.exit(app.exec_())
