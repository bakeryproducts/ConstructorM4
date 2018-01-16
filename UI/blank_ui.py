# TODO cleanup input for characters
# TODO carefully separate inputs
# TODO should category from qt tree be in components?
# TODO components should totaly use geos id


import sys
from glwidget import *
from addcomp_ui import Ui_wid_addcomp
from crearray_ui import Ui_crearray

class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.parents = []
        self.components = []
        self.treeids = {}
        self.activecompid = 0
        self.idcounter = 1
        self.draftflip=1

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
        self.tre_manager.setMaximumSize(QtCore.QSize(180, 16777215))
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
        self.btn_posreset = QtGui.QPushButton(self.centralwidget)
        self.btn_posreset.setObjectName(_fromUtf8("btn_posreset"))
        self.lay_pos.addWidget(self.btn_posreset)
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
        self.btn_rotreset = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_rotreset.sizePolicy().hasHeightForWidth())
        self.btn_rotreset.setSizePolicy(sizePolicy)
        self.btn_rotreset.setObjectName(_fromUtf8("btn_rotreset"))
        self.lay_rot.addWidget(self.btn_rotreset)
        self.lay_right.addLayout(self.lay_rot)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.lay_right.addWidget(self.line)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.lay_right.addWidget(self.label)
        self.lay_draftbase = QtGui.QHBoxLayout()
        self.lay_draftbase.setObjectName(_fromUtf8("lay_draftbase"))
        self.lbl_draftbase = QtGui.QLabel(self.centralwidget)
        self.lbl_draftbase.setObjectName(_fromUtf8("lbl_draftbase"))
        self.lay_draftbase.addWidget(self.lbl_draftbase)
        self.btn_draftbase = QtGui.QPushButton(self.centralwidget)
        self.btn_draftbase.setObjectName(_fromUtf8("btn_draftbase"))
        self.lay_draftbase.addWidget(self.btn_draftbase)
        self.ln_draftbase = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_draftbase.sizePolicy().hasHeightForWidth())
        self.ln_draftbase.setSizePolicy(sizePolicy)
        self.ln_draftbase.setMaximumSize(QtCore.QSize(100, 16777215))
        self.ln_draftbase.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_draftbase.setObjectName(_fromUtf8("ln_draftbase"))
        self.lay_draftbase.addWidget(self.ln_draftbase)
        self.btn_draftlock1 = QtGui.QPushButton(self.centralwidget)
        self.btn_draftlock1.setObjectName(_fromUtf8("btn_draftlock1"))
        self.lay_draftbase.addWidget(self.btn_draftlock1)
        self.lay_right.addLayout(self.lay_draftbase)
        self.lay_draftmove = QtGui.QHBoxLayout()
        self.lay_draftmove.setObjectName(_fromUtf8("lay_draftmove"))
        self.lbl_draftmove = QtGui.QLabel(self.centralwidget)
        self.lbl_draftmove.setObjectName(_fromUtf8("lbl_draftmove"))
        self.lay_draftmove.addWidget(self.lbl_draftmove)
        self.btn_draftmove = QtGui.QPushButton(self.centralwidget)
        self.btn_draftmove.setObjectName(_fromUtf8("btn_draftmove"))
        self.lay_draftmove.addWidget(self.btn_draftmove)
        self.ln_draftmove = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_draftmove.sizePolicy().hasHeightForWidth())
        self.ln_draftmove.setSizePolicy(sizePolicy)
        self.ln_draftmove.setMaximumSize(QtCore.QSize(100, 16777215))
        self.ln_draftmove.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_draftmove.setObjectName(_fromUtf8("ln_draftmove"))
        self.lay_draftmove.addWidget(self.ln_draftmove)
        self.btn_draftlock2 = QtGui.QPushButton(self.centralwidget)
        self.btn_draftlock2.setObjectName(_fromUtf8("btn_draftlock2"))
        self.lay_draftmove.addWidget(self.btn_draftlock2)
        self.lay_right.addLayout(self.lay_draftmove)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.ln_draftoffset = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_draftoffset.sizePolicy().hasHeightForWidth())
        self.ln_draftoffset.setSizePolicy(sizePolicy)
        self.ln_draftoffset.setMaximumSize(QtCore.QSize(100, 16777215))
        self.ln_draftoffset.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_draftoffset.setObjectName(_fromUtf8("ln_draftoffset"))
        self.horizontalLayout_2.addWidget(self.ln_draftoffset)
        self.btn_draftoffset = QtGui.QPushButton(self.centralwidget)
        self.btn_draftoffset.setObjectName(_fromUtf8("btn_draftoffset"))
        self.horizontalLayout_2.addWidget(self.btn_draftoffset)
        self.btn_draftflip = QtGui.QPushButton(self.centralwidget)
        self.btn_draftflip.setObjectName(_fromUtf8("btn_draftflip"))
        self.horizontalLayout_2.addWidget(self.btn_draftflip)
        self.lay_right.addLayout(self.horizontalLayout_2)
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 34))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuShow = QtGui.QMenu(self.menuView)
        self.menuShow.setObjectName(_fromUtf8("menuShow"))
        self.menuVisual_Style = QtGui.QMenu(self.menuView)
        self.menuVisual_Style.setObjectName(_fromUtf8("menuVisual_Style"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        self.menuComponents = QtGui.QMenu(self.menubar)
        self.menuComponents.setGeometry(QtCore.QRect(265, 177, 192, 102))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuComponents.sizePolicy().hasHeightForWidth())
        self.menuComponents.setSizePolicy(sizePolicy)
        self.menuComponents.setMinimumSize(QtCore.QSize(150, 0))
        self.menuComponents.setObjectName(_fromUtf8("menuComponents"))
        self.menuAdd = QtGui.QMenu(self.menuComponents)
        self.menuAdd.setGeometry(QtCore.QRect(452, 180, 208, 134))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuAdd.sizePolicy().hasHeightForWidth())
        self.menuAdd.setSizePolicy(sizePolicy)
        self.menuAdd.setMinimumSize(QtCore.QSize(0, 0))
        self.menuAdd.setObjectName(_fromUtf8("menuAdd"))
        self.menuModify = QtGui.QMenu(self.menubar)
        self.menuModify.setObjectName(_fromUtf8("menuModify"))
        MainWindow.setMenuBar(self.menubar)
        self.actionImport = QtGui.QAction(MainWindow)
        self.actionImport.setObjectName(_fromUtf8("actionImport"))
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionPoints = QtGui.QAction(MainWindow)
        self.actionPoints.setObjectName(_fromUtf8("actionPoints"))
        self.actionFaces = QtGui.QAction(MainWindow)
        self.actionFaces.setObjectName(_fromUtf8("actionFaces"))
        self.actionLeft = QtGui.QAction(MainWindow)
        self.actionLeft.setObjectName(_fromUtf8("actionLeft"))
        self.actionRight = QtGui.QAction(MainWindow)
        self.actionRight.setObjectName(_fromUtf8("actionRight"))
        self.actionTop = QtGui.QAction(MainWindow)
        self.actionTop.setObjectName(_fromUtf8("actionTop"))
        self.actionBack = QtGui.QAction(MainWindow)
        self.actionBack.setObjectName(_fromUtf8("actionBack"))
        self.actionSolid = QtGui.QAction(MainWindow)
        self.actionSolid.setObjectName(_fromUtf8("actionSolid"))
        self.actionWireframe = QtGui.QAction(MainWindow)
        self.actionWireframe.setObjectName(_fromUtf8("actionWireframe"))
        self.actionLighting = QtGui.QAction(MainWindow)
        self.actionLighting.setCheckable(True)
        self.actionLighting.setObjectName(_fromUtf8("actionLighting"))
        self.actionActive_Armor = QtGui.QAction(MainWindow)
        self.actionActive_Armor.setObjectName(_fromUtf8("actionActive_Armor"))
        self.actionArrays = QtGui.QAction(MainWindow)
        self.actionArrays.setObjectName(_fromUtf8("actionArrays"))
        self.actionHelp = QtGui.QAction(MainWindow)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.actionDynamic_Armor = QtGui.QAction(MainWindow)
        self.actionDynamic_Armor.setObjectName(_fromUtf8("actionDynamic_Armor"))
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.actionClose)
        self.menuShow.addAction(self.actionPoints)
        self.menuShow.addAction(self.actionFaces)
        self.menuShow.addAction(self.actionLeft)
        self.menuShow.addAction(self.actionRight)
        self.menuShow.addAction(self.actionTop)
        self.menuShow.addAction(self.actionBack)
        self.menuVisual_Style.addAction(self.actionSolid)
        self.menuVisual_Style.addAction(self.actionWireframe)
        self.menuView.addAction(self.menuShow.menuAction())
        self.menuView.addAction(self.menuVisual_Style.menuAction())
        self.menuView.addAction(self.actionLighting)
        self.menuAbout.addAction(self.actionHelp)
        self.menuAdd.addAction(self.actionActive_Armor)
        self.menuAdd.addAction(self.actionDynamic_Armor)
        self.menuComponents.addAction(self.menuAdd.menuAction())
        self.menuModify.addAction(self.actionArrays)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuComponents.menuAction())
        self.menubar.addAction(self.menuModify.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

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
        self.tre_manager.itemSelectionChanged.connect(self.act_tre_test)

        self.glwidget.mode = "pick0"

        self.btn_draftbase.setCheckable(True)
        self.btn_draftmove.setCheckable(True)
        self.btn_draftlock1.setEnabled(False)
        self.ln_draftbase.setEnabled(False)
        self.btn_draftlock2.setEnabled(False)
        self.ln_draftmove.setEnabled(False)

        # self.btn_draftoffset.setEnabled(False)
        # self.ln_draftoffset.setEnabled(False)

        self.btn_draftbase.clicked.connect(self.act_btn_draftbase)
        self.btn_draftlock1.clicked.connect(self.act_btn_draftlock1)
        self.btn_draftmove.clicked.connect(self.act_btn_draftmove)
        self.btn_draftlock2.clicked.connect(self.act_btn_draftlock2)
        self.btn_draftoffset.clicked.connect(self.act_btn_draftoffset)
        self.btn_draftangle.clicked.connect(self.act_btn_draftangle)

        self.glwidget.ObjSelected.connect(self.setselectedplane)
        # self.glwidget.signal.connect(self.glwidget.signal,self.DOSIG)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Constructor", None))
        self.lbl_pos.setText(_translate("MainWindow", "Component position (X,Y,Z)", None))
        self.ln_pos.setText(_translate("MainWindow", "0,0,0", None))
        self.btn_setpos.setText(_translate("MainWindow", "Set position", None))
        self.btn_posreset.setText(_translate("MainWindow", "Reset", None))
        self.lbl_rot.setText(_translate("MainWindow", "Component Rotation angles (from OX,OY,OZ)", None))
        self.ln_rot.setText(_translate("MainWindow", "0,0,0", None))
        self.btn_setrot.setText(_translate("MainWindow", "Set rotation", None))
        self.btn_rotreset.setText(_translate("MainWindow", "Reset", None))
        self.label.setText(_translate("MainWindow", "Constrain 2 components", None))
        self.lbl_draftbase.setText(_translate("MainWindow", "1. Base", None))
        self.btn_draftbase.setText(_translate("MainWindow", "Select plane 1", None))
        self.ln_draftbase.setText(_translate("MainWindow", "Plane #1", None))
        self.btn_draftlock1.setText(_translate("MainWindow", "Lock", None))
        self.lbl_draftmove.setText(_translate("MainWindow", "2. Attachement", None))
        self.btn_draftmove.setText(_translate("MainWindow", "Select plane 2", None))
        self.ln_draftmove.setText(_translate("MainWindow", "Plane #2", None))
        self.btn_draftlock2.setText(_translate("MainWindow", "Lock", None))
        self.ln_draftoffset.setText(_translate("MainWindow", "0,0,0", None))
        self.btn_draftoffset.setText(_translate("MainWindow", "Set offset C1 from C2", None))
        self.btn_draftflip.setText(_translate("MainWindow", "Flip", None))
        self.menuFile.setTitle(_translate("MainWindow", "&File", None))
        self.menuView.setTitle(_translate("MainWindow", "&View", None))
        self.menuShow.setTitle(_translate("MainWindow", "Views", None))
        self.menuVisual_Style.setTitle(_translate("MainWindow", "Visual Style", None))
        self.menuAbout.setTitle(_translate("MainWindow", "Ab&out", None))
        self.menuComponents.setTitle(_translate("MainWindow", "&Components", None))
        self.menuAdd.setTitle(_translate("MainWindow", "&Add", None))
        self.menuModify.setTitle(_translate("MainWindow", "&Modify", None))
        self.actionImport.setText(_translate("MainWindow", "import", None))
        self.actionClose.setText(_translate("MainWindow", "close", None))
        self.actionPoints.setText(_translate("MainWindow", "Front", None))
        self.actionFaces.setText(_translate("MainWindow", "Back", None))
        self.actionLeft.setText(_translate("MainWindow", "Left", None))
        self.actionRight.setText(_translate("MainWindow", "Right", None))
        self.actionTop.setText(_translate("MainWindow", "Top", None))
        self.actionBack.setText(_translate("MainWindow", "Back", None))
        self.actionSolid.setText(_translate("MainWindow", "Solid", None))
        self.actionWireframe.setText(_translate("MainWindow", "Wireframe", None))
        self.actionLighting.setText(_translate("MainWindow", "Lighting", None))
        self.actionActive_Armor.setText(_translate("MainWindow", "&Base component", None))
        self.actionArrays.setText(_translate("MainWindow", "Arrays", None))
        self.actionHelp.setText(_translate("MainWindow", "Help", None))
        self.actionDynamic_Armor.setText(_translate("MainWindow", "&Dynamic Armor", None))

        def act_btn_add_aa(self):
            # self.filedialog = QtGui.QFileDialog(self)
            # filepath = self.filedialog.getOpenFileName()
            filepath = "C:\\Users\\User\PycharmProjects\CNSTgui\CNST\GEO\\dz.stl"
            self.act_btn_add(filepath)

        def act_btn_add(self, path):
            self.addwind = Ui_wid_addcomp()
            self.addwind.show()
            self.addwind.newwobj(path, self)

        def act_btn_rotation(self):
            text = self.ln_rot.text()
            x, y, z = [int(el) for el in text.split(',')]
            ang = (x, y, z)
            self.glwidget.objects[self.activecompid].setrotate(ang)
            self.glwidget.upmat()
            print(x, y, z)

        def act_btn_position(self):
            text = self.ln_pos.text()
            x, y, z = [int(el) for el in text.split(',')]
            pos = (x, y, z)
            self.glwidget.objects[self.activecompid].setcoord(pos)
            self.glwidget.upmat()
            print(x, y, z)

        def act_btn_help(self):
            self.act_btn_add_aa()
            self.act_btn_add_aa()

        def act_btn_arrays(self):
            self.arrayswind = Ui_crearray()
            self.arrayswind.loadinit(self)
            self.arrayswind.show()

        # checkboxes in tree
        def act_tre_check(self, item, column):
            index = self.findid(item.text(0))
            self.tre_manager.blockSignals(True)
            if item.checkState(0) == QtCore.Qt.Checked:
                self.glwidget.delinvisible(index)
            elif item.checkState(0) == QtCore.Qt.Unchecked:
                self.glwidget.addinvisible(index)
            self.tre_manager.blockSignals(False)

        # one click selection in tree
        def act_tre_test(self):
            getselected = self.tre_manager.selectedItems()
            activecomp = getselected[0].text(0)

            if activecomp in self.parents:
                self.disablelay(True)
                self.clearlines()
            else:
                self.disablelay(False)
                acid = self.findid(getselected[0].text(0)) - 1
                if self.activecompid != acid:
                    self.clearlines()
                self.activecompid = acid

        def act_btn_draftbase(self):
            self.glwidget.dropselection()
            self.glwidget.mode = "pickone"
            self.btn_draftlock1.setEnabled(True)
            self.btn_draftlock2.setEnabled(False)

        def act_btn_draftlock1(self):
            if len(self.glwidget.selection) > 0:
                self.btn_draftlock1.setEnabled(False)
                self.btn_draftbase.setChecked(False)
                self.ln_draftbase.setText(str(self.glwidget.selection[0][1]))
                self.basec = self.glwidget.selection[0]

                baseid = self.glwidget.getobjbyid(self.basec[0])
                baseobj = self.glwidget.objects[baseid]
                baseobj.setcol((.3, .2, 1, 1))
                self.basepoint = self.glwidget.draftpoint

                self.glwidget.upmat()
                self.glwidget.mode = "pick0"
                self.glwidget.dropselection()

            else:
                print("CHOOSE PLANE BOI")  # TODO POPPING UP

        def act_btn_draftmove(self):
            self.glwidget.dropselection()
            self.glwidget.mode = "pickone"
            self.btn_draftlock2.setEnabled(True)
            self.btn_draftlock1.setEnabled(False)

        def act_btn_draftlock2(self):
            if len(self.glwidget.selection) > 0:
                self.btn_draftmove.setChecked(False)
                self.btn_draftlock2.setEnabled(False)
                self.ln_draftmove.setText(str(self.glwidget.selection[0][1]))

                self.movec = self.glwidget.selection[0]
                moveid = self.glwidget.getobjbyid(self.movec[0])
                moveobj = self.glwidget.objects[moveid]
                # self.tmp = clELEM.ELEM(moveobj.getcp())# TODO work in progress
                # self.glwidget.addobj(self.tmp.geoobj)
                self.movepoint = self.glwidget.draftpoint

                self.glwidget.dropselection()
                self.glwidget.mode = "pick0"

            else:
                print("CHOOSE PLANE BOI")  # TODO POPPING UP

        def setselectedplane(self, arg):
            if self.btn_draftlock1.isEnabled():
                self.ln_draftbase.setText(str(arg[0][1]))
            elif self.btn_draftlock2.isEnabled():
                self.ln_draftmove.setText(str(arg[0][1]))

        def act_btn_draftoffset(self):
            offset = self.ln_draftoffset.text().split(",")
            offset = [int(offset[i]) for i in (0, 1, 2)]
            angle = int(self.ln_draftangle.text())
            self.constrain(offset, angle)

        def act_btn_draftangle(self):
            pass
            # self.constrain(angle=angle)

        # point to point cosntrain two objects
        # TODO color- shadowing
        # def constrain(self, offset=(0, 0, 0), angle=0):
        #     baseid = self.glwidget.getobjbyid(self.basec[0])
        #     baseplane = self.basec[1]
        #     baseobj = self.glwidget.objects[baseid]
        #
        #     moveid = self.glwidget.getobjbyid(self.movec[0])
        #     moveplane = self.movec[1]
        #     moveobj = self.glwidget.objects[moveid]
        #
        #     normalbase = baseobj.getnormaltoface(baseplane) * (-1)
        #     pointend = self.basepoint
        #     pointstart = self.movepoint
        #     #self.basepoint, self.movepoint = None, None
        #
        #     pointend = [pointend[i] + int(offset[i]) for i in (0, 1, 2)]
        #
        #     moveobj.setup(normalbase, moveplane, pointstart, pointend, angle)
        #     #moveobj.setcol((.3, .3, .3, 1))
        #     self.movepoint = self.basepoint
        #     # self.tmp.geoobj.setup(normalbase, normalmove, pointstart, pointend)
        #     # self.tmp.geoobj.setcol((.3, .3, .3, 1))
        #     self.glwidget.upmat()

        def constrain(self, offset=(0, 0, 0), angle=0, grid=None, angbasis=0):
            ''' at the time there are two components represented by
                geo objects from picking: base comp, move(able) comp
                on each comp there are point of constraining:
                base- move- points.
                    if there is no grid when constrain() called
                lets just  get those components together with
                offset in local basis and rotate angle from local normal
                    But active grid= array sends us to
                component 2d flat rect array creator
                damn
            '''

            baseid = self.glwidget.getobjbyid(self.basec[0])
            baseplane = self.basec[1]
            baseobj = self.glwidget.objects[baseid]

            moveid = self.glwidget.getobjbyid(self.movec[0])
            moveplane = self.movec[1]
            moveobj = self.glwidget.objects[moveid]

            normalbase = baseobj.getnormaltoface(baseplane) * (-1)
            pointend = self.basepoint
            pointstart = self.movepoint

            if grid == None:
                moveobj.setup(normalbase, moveplane, pointstart, pointend, offset, angle)
                self.movepoint = self.basepoint
                # self.tmp.geoobj.setup(normalbase, normalmove, pointstart, pointend)
                # self.tmp.geoobj.setcol((.3, .3, .3, 1))
            else:
                comp = self.getcompbygeoid(moveobj.getid())
                nx, ny, dx, dy = grid
                for j in range(ny):
                    for i in range(nx):
                        tmpcomp = comp.getcopy()
                        toffset = offset[0] + i * dx, offset[1], offset[2]
                        toffset = toffset[0], toffset[1] + j * dy, toffset[2]

                        tmpcomp.geoobj.setup(normalbase, moveplane, pointstart, pointend, toffset, angle, angbasis)
                        self.pushcomponent(tmpcomp, tmpcomp.category)
            self.glwidget.upmat()

        def treenewentry(self, name, parent):
            name = str(self.idcounter) + ".  " + name
            self.parents.append(parent.text(0))
            child = QtGui.QTreeWidgetItem(parent)
            child.setText(0, name)
            child.setCheckState(0, QtCore.Qt.Checked)
            child.setFlags(child.flags())
            self.treeids[name] = self.idcounter
            self.idcounter += 1

        # go from widget item in tree to real representing object id
        def findid(self, treewiditem):
            # key = treewiditem.text(0)
            key = treewiditem
            try:
                componentid = self.treeids[key]
            except:
                componentid = -1

            return componentid

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
        def pushcomponent(self, comp, parent):
            self.components.append(comp)
            self.treenewentry(comp.getname(), parent)
            self.glwidget.addobj(comp.getgeo())

        def getcompbygeoid(self, id):
            for comp in self.components:
                if comp.getid() == id:
                    return comp

    def act_btn_add_aa(self):
        # self.filedialog = QtGui.QFileDialog(self)
        # filepath = self.filedialog.getOpenFileName()
        filepath = "C:\\Users\\User\PycharmProjects\CNSTgui\CNST\GEO\\dz.stl"
        self.act_btn_add(filepath)

    def act_btn_add(self, path):
        self.addwind = Ui_wid_addcomp()
        self.addwind.show()
        self.addwind.newwobj(path, self)

    def act_btn_rotation(self):
        text = self.ln_rot.text()
        x, y, z = [int(el) for el in text.split(',')]
        ang = (x, y, z)
        self.glwidget.objects[self.activecompid].setrotate(ang)
        self.glwidget.upmat()
        print(x, y, z)

    def act_btn_position(self):
        text = self.ln_pos.text()
        x, y, z = [int(el) for el in text.split(',')]
        pos = (x, y, z)
        self.glwidget.objects[self.activecompid].setcoord(pos)
        self.glwidget.upmat()
        print(x, y, z)

    def act_btn_help(self):
        self.act_btn_add_aa()
        self.act_btn_add_aa()

    def act_btn_arrays(self):
        self.arrayswind = Ui_crearray()
        self.arrayswind.loadinit(self)
        self.arrayswind.show()

        # checkboxes in tree

    def act_tre_check(self, item, column):
        index = self.findid(item.text(0))
        self.tre_manager.blockSignals(True)
        if item.checkState(0) == QtCore.Qt.Checked:
            self.glwidget.delinvisible(index)
        elif item.checkState(0) == QtCore.Qt.Unchecked:
            self.glwidget.addinvisible(index)
        self.tre_manager.blockSignals(False)

        # one click selection in tree

    def act_tre_test(self):
        getselected = self.tre_manager.selectedItems()
        activecomp = getselected[0].text(0)

        if activecomp in self.parents:
            self.disablelay(True)
            self.clearlines()
        else:
            self.disablelay(False)
            acid = self.findid(getselected[0].text(0)) - 1
            if self.activecompid != acid:
                self.clearlines()
            self.activecompid = acid

    def act_btn_draftbase(self):
        self.glwidget.dropselection()
        self.glwidget.mode = "pickone"
        self.btn_draftlock1.setEnabled(True)
        self.btn_draftlock2.setEnabled(False)

    def act_btn_draftlock1(self):
        if len(self.glwidget.selection) > 0:
            self.btn_draftlock1.setEnabled(False)
            self.btn_draftbase.setChecked(False)
            self.ln_draftbase.setText(str(self.glwidget.selection[0][1]))
            self.basec = self.glwidget.selection[0]

            baseid = self.glwidget.getobjbyid(self.basec[0])
            baseobj = self.glwidget.objects[baseid]
            baseobj.setcol((.3, .2, 1, 1))
            self.basepoint = self.glwidget.draftpoint

            self.glwidget.upmat()
            self.glwidget.mode = "pick0"
            self.glwidget.dropselection()

        else:
            print("CHOOSE PLANE BOI")  # TODO POPPING UP

    def act_btn_draftmove(self):
        self.glwidget.dropselection()
        self.glwidget.mode = "pickone"
        self.btn_draftlock2.setEnabled(True)
        self.btn_draftlock1.setEnabled(False)

    def act_btn_draftlock2(self):
        if len(self.glwidget.selection) > 0:
            self.btn_draftmove.setChecked(False)
            self.btn_draftlock2.setEnabled(False)
            self.ln_draftmove.setText(str(self.glwidget.selection[0][1]))

            self.movec = self.glwidget.selection[0]
            moveid = self.glwidget.getobjbyid(self.movec[0])
            moveobj = self.glwidget.objects[moveid]
            # self.tmp = clELEM.ELEM(moveobj.getcp())# TODO work in progress
            # self.glwidget.addobj(self.tmp.geoobj)
            self.movepoint = self.glwidget.draftpoint

            self.glwidget.dropselection()
            self.glwidget.mode = "pick0"

        else:
            print("CHOOSE PLANE BOI")  # TODO POPPING UP

    def setselectedplane(self, arg):
        if self.btn_draftlock1.isEnabled():
            self.ln_draftbase.setText(str(arg[0][1]))
        elif self.btn_draftlock2.isEnabled():
            self.ln_draftmove.setText(str(arg[0][1]))

    def act_btn_draftoffset(self):
        offset = self.ln_draftoffset.text().split(",")
        offset = [int(offset[i]) for i in (0, 1, 2)]
        angle = int(self.ln_draftangle.text())
        self.constrain(offset, angle)

    def act_btn_draftangle(self):
        pass
        # self.constrain(angle=angle)

        # point to point cosntrain two objects
        # TODO color- shadowing
        # def constrain(self, offset=(0, 0, 0), angle=0):
        #     baseid = self.glwidget.getobjbyid(self.basec[0])
        #     baseplane = self.basec[1]
        #     baseobj = self.glwidget.objects[baseid]
        #
        #     moveid = self.glwidget.getobjbyid(self.movec[0])
        #     moveplane = self.movec[1]
        #     moveobj = self.glwidget.objects[moveid]
        #
        #     normalbase = baseobj.getnormaltoface(baseplane) * (-1)
        #     pointend = self.basepoint
        #     pointstart = self.movepoint
        #     #self.basepoint, self.movepoint = None, None
        #
        #     pointend = [pointend[i] + int(offset[i]) for i in (0, 1, 2)]
        #
        #     moveobj.setup(normalbase, moveplane, pointstart, pointend, angle)
        #     #moveobj.setcol((.3, .3, .3, 1))
        #     self.movepoint = self.basepoint
        #     # self.tmp.geoobj.setup(normalbase, normalmove, pointstart, pointend)
        #     # self.tmp.geoobj.setcol((.3, .3, .3, 1))
        #     self.glwidget.upmat()

    def constrain(self, offset=(0, 0, 0), angle=0, grid=None, angbasis=0):
        ''' at the time there are two components represented by
            geo objects from picking: base comp, move(able) comp
            on each comp there are point of constraining:
            base- move- points.
                if there is no grid when constrain() called
            lets just  get those components together with
            offset in local basis and rotate angle from local normal
                But active grid= array sends us to
            component 2d flat rect array creator
            damn
        '''

        baseid = self.glwidget.getobjbyid(self.basec[0])
        baseplane = self.basec[1]
        baseobj = self.glwidget.objects[baseid]

        moveid = self.glwidget.getobjbyid(self.movec[0])
        moveplane = self.movec[1]
        moveobj = self.glwidget.objects[moveid]

        normalbase = baseobj.getnormaltoface(baseplane) * (-1)
        pointend = self.basepoint
        pointstart = self.movepoint

        if grid == None:
            moveobj.setup(normalbase, moveplane, pointstart, pointend, offset, angle)
            self.movepoint = self.basepoint
            # self.tmp.geoobj.setup(normalbase, normalmove, pointstart, pointend)
            # self.tmp.geoobj.setcol((.3, .3, .3, 1))
        else:
            comp = self.getcompbygeoid(moveobj.getid())
            nx, ny, dx, dy = grid
            for j in range(ny):
                for i in range(nx):
                    tmpcomp = comp.getcopy()
                    toffset = offset[0] + i * dx, offset[1], offset[2]
                    toffset = toffset[0], toffset[1] + j * dy, toffset[2]

                    tmpcomp.geoobj.setup(normalbase, moveplane, pointstart, pointend, toffset, angle, angbasis)
                    self.pushcomponent(tmpcomp, tmpcomp.category)
        self.glwidget.upmat()

    def treenewentry(self, name, parent):
        name = str(self.idcounter) + ".  " + name
        self.parents.append(parent.text(0))
        child = QtGui.QTreeWidgetItem(parent)
        child.setText(0, name)
        child.setCheckState(0, QtCore.Qt.Checked)
        child.setFlags(child.flags())
        self.treeids[name] = self.idcounter
        self.idcounter += 1

        # go from widget item in tree to real representing object id

    def findid(self, treewiditem):
        # key = treewiditem.text(0)
        key = treewiditem
        try:
            componentid = self.treeids[key]
        except:
            componentid = -1

        return componentid

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

    def pushcomponent(self, comp, parent):
        self.components.append(comp)
        self.treenewentry(comp.getname(), parent)
        self.glwidget.addobj(comp.getgeo())

    def getcompbygeoid(self, id):
        for comp in self.components:
            if comp.getid() == id:
                return comp

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
        self.setupUi(self)
        self.category = "New component"
        self.steq = 13

    self.glwidget = GLWidget()
    mainLayout = QtGui.QHBoxLayout()
    mainLayout.addWidget(self.glwidget)
    self.glbox.setLayout(mainLayout)
    self.glwidget.mode = "pick0"

    self.btn_setname.clicked.connect(self.act_btn_setname)
    self.btn_ok.clicked.connect(self.act_btn_ok)
    self.btn_cancel.clicked.connect(self.close)
    self.btn_startselect.clicked.connect(self.act_btn_startselect)
    self.btn_doneselect.clicked.connect(self.act_btn_doneselect)
    self.btn_startselect.setCheckable(True)

    def newwobj(self, path, mainw):
        geos = techs.georedo(path, 100)
        name = path.split("/")[-1]
        geoobj = clGEOOBJ.GEOOBJ(geos, name)
        # self.comp = CNST.clELEM.ELEM(geoobj)
        self.comp = CNST.clTARGETMAIN.TARGETMAIN(geoobj)
        self.glwidget.addobj(self.comp.getgeo())
        self.ln_name.setText(name)
        self.mainwindow = mainw

    # is there such type of components in tree?
    def checkcategory(self):
        tree = self.mainwindow.tre_manager
        res = tree.findItems(self.category, QtCore.Qt.MatchFixedString)
        return res

    # set new type in tree
    def setcategory(self):
        catitem = self.checkcategory()
        if not catitem:
            parent = QtGui.QTreeWidgetItem(self.mainwindow.tre_manager)
            parent.setText(0, self.category)
            parent.setFlags(parent.flags() | QtCore.Qt.ItemIsTristate | QtCore.Qt.ItemIsUserCheckable)
            parent.setCheckState(0, QtCore.Qt.Checked)
            return parent
        else:
            return catitem[0]

    def act_btn_startselect(self):
        self.glwidget.mode = "pickmany"

    def act_btn_doneselect(self):
        self.steq = int(self.ln_steq.text())
        self.ln_steq.setText("0")
        for objid, planeid in self.glwidget.selection:
            self.comp.changesteq(planeid, self.steq)
        self.glwidget.mode = "pick0"
        self.glwidget.dropselection()
        self.btn_startselect.toggle()

    def act_btn_ok(self):
        self.glwidget.doneCurrent()
        self.mainwindow.glwidget.makeCurrent()
        self.mainwindow.pushcomponent(self.comp.getcopy(), self.setcategory())
        self.checkcategory()
        self.glwidget.objects.clear()
        self.comp.export()
        self.close()

    def act_btn_setname(self):
        name = self.ln_name.text()
        self.comp.setname(name)
        self.lbl_gl.setText("Component preview: "+name)

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