import sys
from glwidget import *
import CNST.clELEM
import CNST.clDZ
import CNST.clSLAT
import CNST.FC.boxmaker
from CNST.remesh import remeshing
import UI.Resourses.resIcons

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


class Ui_wid_addslat(QtGui.QWidget):
    def __init__(self):
        super(Ui_wid_addslat, self).__init__()
        #self.mainwindow=0
        self.fedit=False
        self.setupUi(self)
        self.fmouseclick = False
        self.category = "SLAT"
        self.thickness = 13
        self.contour = []

    def setupUi(self, wid_addslat):
        wid_addslat.setObjectName(_fromUtf8("wid_addslat"))
        wid_addslat.resize(1000, 600)
        wid_addslat.setMinimumSize(QtCore.QSize(800, 0))
        self.horizontalLayout = QtGui.QHBoxLayout(wid_addslat)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tbl_points = QtGui.QTableWidget(wid_addslat)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbl_points.sizePolicy().hasHeightForWidth())
        self.tbl_points.setSizePolicy(sizePolicy)
        self.tbl_points.setMinimumSize(QtCore.QSize(255, 0))
        self.tbl_points.setMaximumSize(QtCore.QSize(255, 16777215))
        self.tbl_points.setObjectName(_fromUtf8("tbl_points"))
        self.tbl_points.setColumnCount(2)
        self.tbl_points.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tbl_points.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tbl_points.setHorizontalHeaderItem(1, item)
        self.tbl_points.horizontalHeader().setDefaultSectionSize(110)
        self.verticalLayout.addWidget(self.tbl_points)
        self.label_7 = QtGui.QLabel(wid_addslat)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout.addWidget(self.label_7)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.ln_addpoint = QtGui.QLineEdit(wid_addslat)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_addpoint.sizePolicy().hasHeightForWidth())
        self.ln_addpoint.setSizePolicy(sizePolicy)
        self.ln_addpoint.setMaximumSize(QtCore.QSize(123, 16777215))
        self.ln_addpoint.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_addpoint.setObjectName(_fromUtf8("ln_addpoint"))
        self.horizontalLayout_5.addWidget(self.ln_addpoint)
        self.btn_addpoint = QtGui.QPushButton(wid_addslat)
        self.btn_addpoint.setObjectName(_fromUtf8("btn_addpoint"))
        self.horizontalLayout_5.addWidget(self.btn_addpoint)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.ln_delpoint = QtGui.QLineEdit(wid_addslat)
        self.ln_delpoint.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_delpoint.sizePolicy().hasHeightForWidth())
        self.ln_delpoint.setSizePolicy(sizePolicy)
        self.ln_delpoint.setMaximumSize(QtCore.QSize(123, 16777215))
        self.ln_delpoint.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_delpoint.setObjectName(_fromUtf8("ln_delpoint"))
        self.horizontalLayout_7.addWidget(self.ln_delpoint)
        self.btn_delpoint = QtGui.QPushButton(wid_addslat)
        self.btn_delpoint.setObjectName(_fromUtf8("btn_delpoint"))
        self.horizontalLayout_7.addWidget(self.btn_delpoint)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.btn_rectangle = QtGui.QPushButton(wid_addslat)
        self.btn_rectangle.setObjectName(_fromUtf8("btn_rectangle"))
        self.horizontalLayout_9.addWidget(self.btn_rectangle)
        self.btn_dropcont = QtGui.QPushButton(wid_addslat)
        self.btn_dropcont.setObjectName(_fromUtf8("btn_dropcont"))
        self.horizontalLayout_9.addWidget(self.btn_dropcont)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.lay_gl = QtGui.QVBoxLayout()
        self.lay_gl.setObjectName(_fromUtf8("lay_gl"))
        self.lbl_gl = QtGui.QLabel(wid_addslat)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_gl.sizePolicy().hasHeightForWidth())
        self.lbl_gl.setSizePolicy(sizePolicy)
        self.lbl_gl.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_gl.setObjectName(_fromUtf8("lbl_gl"))
        self.lay_gl.addWidget(self.lbl_gl)
        self.glbox = QtGui.QWidget(wid_addslat)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.glbox.sizePolicy().hasHeightForWidth())
        self.glbox.setSizePolicy(sizePolicy)
        self.glbox.setMinimumSize(QtCore.QSize(300, 300))
        self.glbox.setObjectName(_fromUtf8("glbox"))
        self.lay_gl.addWidget(self.glbox)
        self.horizontalLayout.addLayout(self.lay_gl)
        self.line_4 = QtGui.QFrame(wid_addslat)
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.horizontalLayout.addWidget(self.line_4)
        self.rightBox = QtGui.QVBoxLayout()
        self.rightBox.setObjectName(_fromUtf8("rightBox"))
        self.lay_name = QtGui.QHBoxLayout()
        self.lay_name.setObjectName(_fromUtf8("lay_name"))
        self.lbl_name = QtGui.QLabel(wid_addslat)
        self.lbl_name.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_name.setObjectName(_fromUtf8("lbl_name"))
        self.lay_name.addWidget(self.lbl_name)
        self.ln_name = QtGui.QLineEdit(wid_addslat)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_name.sizePolicy().hasHeightForWidth())
        self.ln_name.setSizePolicy(sizePolicy)
        self.ln_name.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_name.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ln_name.setObjectName(_fromUtf8("ln_name"))
        self.lay_name.addWidget(self.ln_name)
        self.rightBox.addLayout(self.lay_name)
        self.line = QtGui.QFrame(wid_addslat)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.rightBox.addWidget(self.line)
        self.label_2 = QtGui.QLabel(wid_addslat)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.rightBox.addWidget(self.label_2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(wid_addslat)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.ln_thick = QtGui.QLineEdit(wid_addslat)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_thick.sizePolicy().hasHeightForWidth())
        self.ln_thick.setSizePolicy(sizePolicy)
        self.ln_thick.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_thick.setObjectName(_fromUtf8("ln_thick"))
        self.horizontalLayout_2.addWidget(self.ln_thick)
        self.label_5 = QtGui.QLabel(wid_addslat)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_2.addWidget(self.label_5)
        self.ln_depth = QtGui.QLineEdit(wid_addslat)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_depth.sizePolicy().hasHeightForWidth())
        self.ln_depth.setSizePolicy(sizePolicy)
        self.ln_depth.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_depth.setObjectName(_fromUtf8("ln_depth"))
        self.horizontalLayout_2.addWidget(self.ln_depth)
        self.rightBox.addLayout(self.horizontalLayout_2)
        self.label_8 = QtGui.QLabel(wid_addslat)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.rightBox.addWidget(self.label_8)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_6 = QtGui.QLabel(wid_addslat)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_6.addWidget(self.label_6)
        self.ln_nx = QtGui.QLineEdit(wid_addslat)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_nx.sizePolicy().hasHeightForWidth())
        self.ln_nx.setSizePolicy(sizePolicy)
        self.ln_nx.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_nx.setObjectName(_fromUtf8("ln_nx"))
        self.horizontalLayout_6.addWidget(self.ln_nx)
        self.label_3 = QtGui.QLabel(wid_addslat)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_6.addWidget(self.label_3)
        self.ln_ny = QtGui.QLineEdit(wid_addslat)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_ny.sizePolicy().hasHeightForWidth())
        self.ln_ny.setSizePolicy(sizePolicy)
        self.ln_ny.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_ny.setObjectName(_fromUtf8("ln_ny"))
        self.horizontalLayout_6.addWidget(self.ln_ny)
        self.rightBox.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_9 = QtGui.QLabel(wid_addslat)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_4.addWidget(self.label_9)
        self.ln_ix = QtGui.QLineEdit(wid_addslat)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_ix.sizePolicy().hasHeightForWidth())
        self.ln_ix.setSizePolicy(sizePolicy)
        self.ln_ix.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_ix.setObjectName(_fromUtf8("ln_ix"))
        self.horizontalLayout_4.addWidget(self.ln_ix)
        self.label_4 = QtGui.QLabel(wid_addslat)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.ln_iy = QtGui.QLineEdit(wid_addslat)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_iy.sizePolicy().hasHeightForWidth())
        self.ln_iy.setSizePolicy(sizePolicy)
        self.ln_iy.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_iy.setObjectName(_fromUtf8("ln_iy"))
        self.horizontalLayout_4.addWidget(self.ln_iy)
        self.rightBox.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_10 = QtGui.QLabel(wid_addslat)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_3.addWidget(self.label_10)
        self.ln_dx = QtGui.QLineEdit(wid_addslat)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_dx.sizePolicy().hasHeightForWidth())
        self.ln_dx.setSizePolicy(sizePolicy)
        self.ln_dx.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_dx.setObjectName(_fromUtf8("ln_dx"))
        self.horizontalLayout_3.addWidget(self.ln_dx)
        self.label_11 = QtGui.QLabel(wid_addslat)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_3.addWidget(self.label_11)
        self.ln_dy = QtGui.QLineEdit(wid_addslat)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_dy.sizePolicy().hasHeightForWidth())
        self.ln_dy.setSizePolicy(sizePolicy)
        self.ln_dy.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_dy.setObjectName(_fromUtf8("ln_dy"))
        self.horizontalLayout_3.addWidget(self.ln_dy)
        self.rightBox.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.btn_update = QtGui.QPushButton(wid_addslat)
        self.btn_update.setObjectName(_fromUtf8("btn_update"))
        self.horizontalLayout_8.addWidget(self.btn_update)
        self.btn_default = QtGui.QPushButton(wid_addslat)
        self.btn_default.setObjectName(_fromUtf8("btn_default"))
        self.horizontalLayout_8.addWidget(self.btn_default)
        self.rightBox.addLayout(self.horizontalLayout_8)
        self.line_5 = QtGui.QFrame(wid_addslat)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.rightBox.addWidget(self.line_5)
        self.lbl_set = QtGui.QLabel(wid_addslat)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_set.sizePolicy().hasHeightForWidth())
        self.lbl_set.setSizePolicy(sizePolicy)
        self.lbl_set.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_set.setObjectName(_fromUtf8("lbl_set"))
        self.rightBox.addWidget(self.lbl_set)
        self.lay_material = QtGui.QHBoxLayout()
        self.lay_material.setObjectName(_fromUtf8("lay_material"))
        self.lbl_material = QtGui.QLabel(wid_addslat)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_material.sizePolicy().hasHeightForWidth())
        self.lbl_material.setSizePolicy(sizePolicy)
        self.lbl_material.setObjectName(_fromUtf8("lbl_material"))
        self.lay_material.addWidget(self.lbl_material)
        self.cmb_material = QtGui.QComboBox(wid_addslat)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmb_material.sizePolicy().hasHeightForWidth())
        self.cmb_material.setSizePolicy(sizePolicy)
        self.cmb_material.setMinimumSize(QtCore.QSize(200, 0))
        self.cmb_material.setMaximumSize(QtCore.QSize(200, 16777215))
        self.cmb_material.setObjectName(_fromUtf8("cmb_material"))
        self.lay_material.addWidget(self.cmb_material)
        self.rightBox.addLayout(self.lay_material)
        self.label_12 = QtGui.QLabel(wid_addslat)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.rightBox.addWidget(self.label_12)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_13 = QtGui.QLabel(wid_addslat)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_10.addWidget(self.label_13)
        self.ln_remesh = QtGui.QLineEdit(wid_addslat)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_remesh.sizePolicy().hasHeightForWidth())
        self.ln_remesh.setSizePolicy(sizePolicy)
        self.ln_remesh.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_remesh.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_remesh.setObjectName(_fromUtf8("ln_remesh"))
        self.horizontalLayout_10.addWidget(self.ln_remesh)
        self.rightBox.addLayout(self.horizontalLayout_10)
        self.btn_remesh = QtGui.QPushButton(wid_addslat)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_remesh.sizePolicy().hasHeightForWidth())
        self.btn_remesh.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/TBicons/ico/clock.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_remesh.setIcon(icon)
        self.btn_remesh.setObjectName(_fromUtf8("btn_remesh"))
        self.rightBox.addWidget(self.btn_remesh)
        self.line_2 = QtGui.QFrame(wid_addslat)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.rightBox.addWidget(self.line_2)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.rightBox.addItem(spacerItem1)
        self.line_3 = QtGui.QFrame(wid_addslat)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.rightBox.addWidget(self.line_3)
        self.lay_btns = QtGui.QHBoxLayout()
        self.lay_btns.setObjectName(_fromUtf8("lay_btns"))
        self.btn_ok = QtGui.QPushButton(wid_addslat)
        self.btn_ok.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btn_ok.setDefault(True)
        self.btn_ok.setObjectName(_fromUtf8("btn_ok"))
        self.lay_btns.addWidget(self.btn_ok)
        self.btn_cancel = QtGui.QPushButton(wid_addslat)
        self.btn_cancel.setObjectName(_fromUtf8("btn_cancel"))
        self.lay_btns.addWidget(self.btn_cancel)
        self.rightBox.addLayout(self.lay_btns)
        self.horizontalLayout.addLayout(self.rightBox)

        self.glwidget = GLWidget()
        mainLayout = QtGui.QHBoxLayout()
        mainLayout.addWidget(self.glwidget)
        self.glbox.setLayout(mainLayout)
        self.glwidget.mode = "pick0"

        self.btn_ok.clicked.connect(self.act_btn_ok)
        self.btn_cancel.clicked.connect(self.close)
        # self.btn_startselect.clicked.connect(self.act_btn_startselect)
        # self.btn_startselect.setCheckable(True)
        # self.btn_selectall.setCheckable(True)
        # self.btn_selectall.clicked.connect(self.act_btn_selectall)
        self.tbl_points.setSelectionBehavior(QtGui.QTableView.SelectRows)
        # self.tbl_points.itemSelectionChanged.connect(self.act_tblselchanged)
        self.tbl_points.itemChanged.connect(self.act_tblchanged)

        self.btn_update.clicked.connect(self.act_btn_update)
        self.btn_default.clicked.connect(self.act_btn_default)
        self.btn_addpoint.clicked.connect(self.act_btn_addpoint)
        self.btn_delpoint.clicked.connect(self.act_btn_delpoint)
        self.btn_rectangle.clicked.connect(self.act_btn_rectangle)
        self.btn_dropcont.clicked.connect(self.act_btn_dropcont)

        self.btn_remesh.clicked.connect(self.act_btn_remesh)
        # self.tbl_points.clicked.connect(self.act_tblclicked)

        # self.tbl_points.hideColumn(3)
        # self.glwidget.ObjSelected.connect(self.select)

        self.retranslateUi(wid_addslat)
        QtCore.QMetaObject.connectSlotsByName(wid_addslat)

    def retranslateUi(self, wid_addslat):
        wid_addslat.setWindowTitle(_translate("wid_addslat", "New Slat armor element", None))
        item = self.tbl_points.horizontalHeaderItem(0)
        item.setText(_translate("wid_addslat", "X, mm", None))
        item = self.tbl_points.horizontalHeaderItem(1)
        item.setText(_translate("wid_addslat", "Y, mm", None))
        self.label_7.setText(_translate("wid_addslat", "Contour", None))
        self.ln_addpoint.setText(_translate("wid_addslat", "0,0", None))
        self.btn_addpoint.setText(_translate("wid_addslat", "Add point", None))
        self.btn_delpoint.setText(_translate("wid_addslat", "Delete point", None))
        self.btn_rectangle.setText(_translate("wid_addslat", "Rectangle", None))
        self.btn_dropcont.setText(_translate("wid_addslat", "Drop contour", None))
        self.lbl_gl.setText(_translate("wid_addslat", "Component preview", None))
        self.lbl_name.setText(_translate("wid_addslat", "Component name:", None))
        self.ln_name.setText(_translate("wid_addslat", "TESTNAME", None))
        self.label_2.setText(_translate("wid_addslat", "Component parameters", None))
        self.label.setText(_translate("wid_addslat", "Outer thick. :", None))
        self.ln_thick.setText(_translate("wid_addslat", "10", None))
        self.label_5.setText(_translate("wid_addslat", "Depth: ", None))
        self.ln_depth.setText(_translate("wid_addslat", "30", None))
        self.label_8.setText(_translate("wid_addslat", "Grid parameters", None))
        self.label_6.setText(_translate("wid_addslat", "N, X:", None))
        self.ln_nx.setText(_translate("wid_addslat", "2", None))
        self.label_3.setText(_translate("wid_addslat", "Y:", None))
        self.ln_ny.setText(_translate("wid_addslat", "2", None))
        self.label_9.setText(_translate("wid_addslat", "Thick. , X:", None))
        self.ln_ix.setText(_translate("wid_addslat", "5", None))
        self.label_4.setText(_translate("wid_addslat", "Y:", None))
        self.ln_iy.setText(_translate("wid_addslat", "5", None))
        self.label_10.setText(_translate("wid_addslat", "Step, X:", None))
        self.ln_dx.setText(_translate("wid_addslat", "200", None))
        self.label_11.setText(_translate("wid_addslat", "Y:", None))
        self.ln_dy.setText(_translate("wid_addslat", "40", None))
        self.btn_update.setText(_translate("wid_addslat", "Update", None))
        self.btn_default.setText(_translate("wid_addslat", "Default", None))
        self.lbl_set.setText(_translate("wid_addslat", "Material", None))
        self.lbl_material.setText(_translate("wid_addslat", "Material:", None))
        self.label_12.setText(_translate("wid_addslat", "Remeshing", None))
        self.label_13.setText(_translate("wid_addslat", "Offset distance parameter:", None))
        self.ln_remesh.setText(_translate("wid_addslat", "1e-2", None))
        self.btn_remesh.setText(_translate("wid_addslat", "Apply Remeshing", None))
        self.btn_ok.setText(_translate("wid_addslat", "OK", None))
        self.btn_cancel.setText(_translate("wid_addslat", "Cancel", None))

    # def select(self, arg):
    #     plane = arg[1]
    #     self.fmouseclick = True
    #     self.tbl_points.selectRow(plane - 1)
    #     self.fmouseclick = False

    # def act_btn_startselect(self):
    #     self.glwidget.dropselection()
    #     self.btn_selectall.setChecked(False)
    #     self.glwidget.mode = "pickmany"
    #     self.btn_set.setEnabled(True)

    # def act_btn_selectall(self):
    #     self.glwidget.dropselection()
    #     self.btn_startselect.setChecked(False)
    #     self.glwidget.mode = "pickwhole"
    #     self.btn_set.setEnabled(True)

    def act_btn_set(self):

        thickness = int(self.ln_thickness.text())
        materialname = self.cmb_material.currentText()
        for mat in self.materials:
            if materialname == mat.getname():
                material = mat

        self.ln_thickness.setText("0")

        for indface in range(len(self.comp.geoobj.faces)):
            self.comp.setthick(indface, thickness)
            self.comp.setmat(indface, material)
            # self.editrow(planeid - 1, str(thickness), str(materialname),material.getcategory())

        # self.glwidget.mode = "pick0"
        # self.glwidget.dropselection()
        self.btn_startselect.setChecked(False)
        self.btn_selectall.setChecked(False)
        self.btn_set.setEnabled(False)

    def act_btn_ok(self):
        self.glwidget.doneCurrent()
        self.mainwindow.glwidget.makeCurrent()

        if self.fedit:
            self.mainwindow.delcomp(self.orgcomp)

        self.comp.setname(self.ln_name.text())
        self.mainwindow.pushcomponent(self.comp.getcopy(), self.category)
        self.glwidget.objects.clear()
        del (self.comp)
        self.close()

    # def act_tblclicked(self, row):
    #     self.glwidget.dropselection()
    #     self.glwidget.setselection((self.glwidget.objects[0].getid(), 1 + row.row()))

    # def act_tblselchanged(self):
    #     if self.tbl_points.selectedItems() and not self.fmouseclick:
    #         itemid = 1 + self.tbl_points.selectedItems()[0].row()
    #         self.glwidget.dropselection()
    #         self.glwidget.setselection((self.glwidget.objects[0].getid(), itemid))

    def act_tblchanged(self, item):
        row = item.row()
        value = item.text()
        column = item.column()
        if column == 0:
            # self.comp.setx(value, row)
            pass
        elif column == 1:
            pass
            # self.comp.sety(value, row)

    def act_btn_addpoint(self):
        point = self.ln_addpoint.text()
        point = point.split(',')
        self.newrow(*point[:2])

    def act_btn_delpoint(self):
        row = self.tbl_points.currentRow()
        self.tbl_points.removeRow(row)

    def newrow(self, rowname, rowvalue):
        rowPosition = self.tbl_points.rowCount()
        self.tbl_points.insertRow(rowPosition)
        item1 = QtGui.QTableWidgetItem(rowname)
        item1.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)

        item2 = QtGui.QTableWidgetItem(rowvalue)
        item2.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)

        self.tbl_points.setItem(rowPosition, 0, item1)
        self.tbl_points.setItem(rowPosition, 1, item2)

    def editrow(self, rowPosition, rowValue):
        item1 = QtGui.QTableWidgetItem(rowPosition)
        item1.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)

        item2 = QtGui.QTableWidgetItem(rowValue)
        item2.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)

        self.tbl_points.setItem(rowPosition, 1, item1)
        self.tbl_points.setItem(rowPosition, 2, item2)

    def loadinit(self, path, mainw,edt=False):
        self.mainwindow = mainw
        name = 'SlatArmor'
        if not edt:
            self.tabloaddef()
            self.recreate()
        else:
            self.fedit = True
            self.orgcomp = path
            self.comp = path.getcopy()
            name = self.comp.getname()
            self.tabinit()

        name = name.split('/')[-1]
        self.ln_name.setText(name)
        self.lbl_gl.setText("Component preview: " + name)
        self.glinit()
        self.cmbinit()

        # TODO IMHERE
        # self.act_btn_ok()

    def act_btn_update(self):
        # self.tbl_points.setRowCount(0)
        # self.tabinit()
        self.recreate()
    def getparams(self):
        points = self.pointsload()
        slatthick = int(self.ln_thick.text())
        slatdepth = int(self.ln_depth.text())
        nx = int(self.ln_nx.text())
        ny = int(self.ln_ny.text())
        dx = int(self.ln_dx.text())
        dy = int(self.ln_dy.text())
        ix = int(self.ln_ix.text())
        iy = int(self.ln_iy.text())
        params = (points, slatthick, slatdepth, nx, ny, dx, dy, ix, iy)
        return params

    def recreate(self):
        # points = self.pointsload()
        # slatthick = int(self.ln_thick.text())
        # slatdepth = int(self.ln_depth.text())
        # nx = int(self.ln_nx.text())
        # ny = int(self.ln_ny.text())
        # dx = int(self.ln_dx.text())
        # dy = int(self.ln_dy.text())
        # ix = int(self.ln_ix.text())
        # iy = int(self.ln_iy.text())

        name = 'SlatArmor'
        geoparams = self.getparams()#(points, slatthick, slatdepth, nx, ny, dx, dy, ix, iy)
        print(geoparams)
        pie = CNST.FC.boxmaker.Slatarmor(*geoparams)
        geos = pie.getgeo()
        geoobj = clGEOOBJ.GEOOBJ(geos, name)
        compparams = (geoobj,*geoparams)#(geoobj,points, slatthick, slatdepth, nx, ny, dx, dy, ix, iy)
        self.comp = CNST.clSLAT.SLAT(compparams)
        self.comp.defmatinit(list(self.mainwindow.materials)[0])
        self.glinit()

    def glinit(self):
        self.glwidget.dropselection()
        self.glwidget.cleartmpobjs()
        self.glwidget.objects.clear()
        self.glwidget.addobj(self.comp.getgeo())
        self.glwidget.upmat()

    def tabinit(self):
        # self.btn_set.setEnabled(False)
        for p in self.comp.points:
            self.newrow(str(p[0]), str(p[1]))

        self.ln_thick.setText(str(self.comp.slatthick))
        self.ln_depth.setText(str(self.comp.slatdepth))
        self.ln_nx.setText(str(self.comp.nx))
        self.ln_ny.setText(str(self.comp.ny))
        self.ln_dx.setText(str(self.comp.dx))
        self.ln_dy.setText(str(self.comp.dy))
        self.ln_ix.setText(str(self.comp.ix))
        self.ln_iy.setText(str(self.comp.iy))

    def tabloaddef(self):
        self.tbl_points.setRowCount(0)
        points = [(0, 0, 0), (200, 0, 0), (250, 100, 0), (0, 100, 0)]
        for p in points:
            self.newrow(str(p[0]), str(p[1]))

    def pointsload(self):
        points = []
        for i in range(self.tbl_points.rowCount()):
            x = self.tbl_points.item(i, 0).text()
            y = self.tbl_points.item(i, 1).text()
            points.append((int(x), int(y), 0))
        return points

    def act_btn_rectangle(self):
        self.tabloaddef()

    def act_btn_dropcont(self):
        self.tbl_points.setRowCount(0)

    def act_btn_default(self):
        self.ln_thick.setText(str(10))
        self.ln_depth.setText(str(30))
        self.ln_nx.setText(str(2))
        self.ln_ny.setText(str(2))
        self.ln_dx.setText(str(200))
        self.ln_dy.setText(str(40))
        self.ln_ix.setText(str(5))
        self.ln_iy.setText(str(5))

    def cmbinit(self):
        self.materials = []
        args = []
        for mat in self.mainwindow.materials:
            self.materials.append(mat)
            args.append(mat.getname())

        self.cmb_material.addItems(args)

        # def closeEvent(self, QCloseEvent):
        #     self.act_btn_cancel()

    def act_btn_remesh(self):
        #self.recreate(rms=True)
        g = self.comp.geoobj
        geos = remeshing(list(g.points), list(g.faces))
        geoobj = clGEOOBJ.GEOOBJ(geos, self.comp.geoobj.getname())
        compparams = (geoobj, *self.getparams())
        self.comp = CNST.clSLAT.SLAT(compparams)
        self.tbl_points.setRowCount(0)
        self.glinit()
        self.tabinit()