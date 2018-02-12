from glwidget import *
import CNST.FC.boxmaker
import CNST.clEXT,CNST.clREV
from CNST.remesh import remeshing
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

class Ui_wid_revext(QtGui.QWidget):
    def __init__(self):
        super(Ui_wid_revext, self).__init__()
        self.setupUi(self)
        self.fedit=False
        self.category = 'RV'

    def setupUi(self, wid_revext):
        wid_revext.setObjectName(_fromUtf8("wid_revext"))
        wid_revext.resize(950, 600)
        wid_revext.setMinimumSize(QtCore.QSize(950, 0))
        self.horizontalLayout = QtGui.QHBoxLayout(wid_revext)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tbl_points = QtGui.QTableWidget(wid_revext)
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
        self.label_7 = QtGui.QLabel(wid_revext)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout.addWidget(self.label_7)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.ln_addpoint = QtGui.QLineEdit(wid_revext)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_addpoint.sizePolicy().hasHeightForWidth())
        self.ln_addpoint.setSizePolicy(sizePolicy)
        self.ln_addpoint.setMaximumSize(QtCore.QSize(123, 16777215))
        self.ln_addpoint.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_addpoint.setObjectName(_fromUtf8("ln_addpoint"))
        self.horizontalLayout_5.addWidget(self.ln_addpoint)
        self.btn_addpoint = QtGui.QPushButton(wid_revext)
        self.btn_addpoint.setObjectName(_fromUtf8("btn_addpoint"))
        self.horizontalLayout_5.addWidget(self.btn_addpoint)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.ln_delpoint = QtGui.QLineEdit(wid_revext)
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
        self.btn_delpoint = QtGui.QPushButton(wid_revext)
        self.btn_delpoint.setObjectName(_fromUtf8("btn_delpoint"))
        self.horizontalLayout_7.addWidget(self.btn_delpoint)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.btn_rectangle = QtGui.QPushButton(wid_revext)
        self.btn_rectangle.setObjectName(_fromUtf8("btn_rectangle"))
        self.horizontalLayout_9.addWidget(self.btn_rectangle)
        self.btn_dropcont = QtGui.QPushButton(wid_revext)
        self.btn_dropcont.setObjectName(_fromUtf8("btn_dropcont"))
        self.horizontalLayout_9.addWidget(self.btn_dropcont)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.pushButton_2 = QtGui.QPushButton(wid_revext)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.pushButton = QtGui.QPushButton(wid_revext)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.lay_gl = QtGui.QVBoxLayout()
        self.lay_gl.setObjectName(_fromUtf8("lay_gl"))
        self.lbl_gl = QtGui.QLabel(wid_revext)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_gl.sizePolicy().hasHeightForWidth())
        self.lbl_gl.setSizePolicy(sizePolicy)
        self.lbl_gl.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_gl.setObjectName(_fromUtf8("lbl_gl"))
        self.lay_gl.addWidget(self.lbl_gl)
        self.glbox = QtGui.QWidget(wid_revext)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.glbox.sizePolicy().hasHeightForWidth())
        self.glbox.setSizePolicy(sizePolicy)
        self.glbox.setMinimumSize(QtCore.QSize(300, 300))
        self.glbox.setObjectName(_fromUtf8("glbox"))
        self.lay_gl.addWidget(self.glbox)
        self.horizontalLayout.addLayout(self.lay_gl)
        self.line_4 = QtGui.QFrame(wid_revext)
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.horizontalLayout.addWidget(self.line_4)
        self.rightBox = QtGui.QVBoxLayout()
        self.rightBox.setObjectName(_fromUtf8("rightBox"))
        self.lay_name = QtGui.QHBoxLayout()
        self.lay_name.setObjectName(_fromUtf8("lay_name"))
        self.lbl_name = QtGui.QLabel(wid_revext)
        self.lbl_name.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_name.setObjectName(_fromUtf8("lbl_name"))
        self.lay_name.addWidget(self.lbl_name)
        self.ln_name = QtGui.QLineEdit(wid_revext)
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
        self.line = QtGui.QFrame(wid_revext)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.rightBox.addWidget(self.line)
        self.label_2 = QtGui.QLabel(wid_revext)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.rightBox.addWidget(self.label_2)
        self.tab_inter = QtGui.QTabWidget(wid_revext)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_inter.sizePolicy().hasHeightForWidth())
        self.tab_inter.setSizePolicy(sizePolicy)
        self.tab_inter.setTabPosition(QtGui.QTabWidget.North)
        self.tab_inter.setDocumentMode(True)
        self.tab_inter.setObjectName(_fromUtf8("tab_inter"))
        self.tab_revolve = QtGui.QWidget()
        self.tab_revolve.setObjectName(_fromUtf8("tab_revolve"))
        self.gridLayout = QtGui.QGridLayout(self.tab_revolve)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_8 = QtGui.QLabel(self.tab_revolve)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 0, 2, 1, 1)
        self.ln_revang = QtGui.QLineEdit(self.tab_revolve)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_revang.sizePolicy().hasHeightForWidth())
        self.ln_revang.setSizePolicy(sizePolicy)
        self.ln_revang.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_revang.setObjectName(_fromUtf8("ln_revang"))
        self.gridLayout.addWidget(self.ln_revang, 1, 1, 1, 1)
        self.label = QtGui.QLabel(self.tab_revolve)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.ln_revax1 = QtGui.QLineEdit(self.tab_revolve)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_revax1.sizePolicy().hasHeightForWidth())
        self.ln_revax1.setSizePolicy(sizePolicy)
        self.ln_revax1.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_revax1.setObjectName(_fromUtf8("ln_revax1"))
        self.gridLayout.addWidget(self.ln_revax1, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.tab_revolve)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.ln_revax2 = QtGui.QLineEdit(self.tab_revolve)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_revax2.sizePolicy().hasHeightForWidth())
        self.ln_revax2.setSizePolicy(sizePolicy)
        self.ln_revax2.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_revax2.setObjectName(_fromUtf8("ln_revax2"))
        self.gridLayout.addWidget(self.ln_revax2, 0, 3, 1, 1)
        self.tab_inter.addTab(self.tab_revolve, _fromUtf8(""))
        self.tab_extract = QtGui.QWidget()
        self.tab_extract.setObjectName(_fromUtf8("tab_extract"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab_extract)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.ln_extax = QtGui.QLineEdit(self.tab_extract)
        self.ln_extax.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_extax.setObjectName(_fromUtf8("ln_extax"))
        self.gridLayout_2.addWidget(self.ln_extax, 0, 2, 1, 1)
        self.ln_exthei = QtGui.QLineEdit(self.tab_extract)
        self.ln_exthei.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_exthei.setObjectName(_fromUtf8("ln_exthei"))
        self.gridLayout_2.addWidget(self.ln_exthei, 1, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.tab_extract)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 0, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.tab_extract)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 1, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 0, 1, 1)
        self.tab_inter.addTab(self.tab_extract, _fromUtf8(""))
        self.rightBox.addWidget(self.tab_inter)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.btn_update = QtGui.QPushButton(wid_revext)
        self.btn_update.setObjectName(_fromUtf8("btn_update"))
        self.horizontalLayout_8.addWidget(self.btn_update)
        self.rightBox.addLayout(self.horizontalLayout_8)
        self.line_5 = QtGui.QFrame(wid_revext)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.rightBox.addWidget(self.line_5)
        self.lbl_set = QtGui.QLabel(wid_revext)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_set.sizePolicy().hasHeightForWidth())
        self.lbl_set.setSizePolicy(sizePolicy)
        self.lbl_set.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_set.setObjectName(_fromUtf8("lbl_set"))
        self.rightBox.addWidget(self.lbl_set)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.btn_startselect = QtGui.QPushButton(wid_revext)
        self.btn_startselect.setObjectName(_fromUtf8("btn_startselect"))
        self.horizontalLayout_2.addWidget(self.btn_startselect)
        self.btn_selectall = QtGui.QPushButton(wid_revext)
        self.btn_selectall.setObjectName(_fromUtf8("btn_selectall"))
        self.horizontalLayout_2.addWidget(self.btn_selectall)
        self.rightBox.addLayout(self.horizontalLayout_2)
        self.lay_material = QtGui.QHBoxLayout()
        self.lay_material.setObjectName(_fromUtf8("lay_material"))
        self.lbl_material = QtGui.QLabel(wid_revext)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_material.sizePolicy().hasHeightForWidth())
        self.lbl_material.setSizePolicy(sizePolicy)
        self.lbl_material.setObjectName(_fromUtf8("lbl_material"))
        self.lay_material.addWidget(self.lbl_material)
        self.cmb_material = QtGui.QComboBox(wid_revext)
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
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_6 = QtGui.QLabel(wid_revext)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_3.addWidget(self.label_6)
        self.ln_thickness = QtGui.QLineEdit(wid_revext)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_thickness.sizePolicy().hasHeightForWidth())
        self.ln_thickness.setSizePolicy(sizePolicy)
        self.ln_thickness.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_thickness.setObjectName(_fromUtf8("ln_thickness"))
        self.horizontalLayout_3.addWidget(self.ln_thickness)
        self.rightBox.addLayout(self.horizontalLayout_3)
        self.btn_set = QtGui.QPushButton(wid_revext)
        self.btn_set.setObjectName(_fromUtf8("btn_set"))
        self.rightBox.addWidget(self.btn_set)
        self.line_6 = QtGui.QFrame(wid_revext)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.rightBox.addWidget(self.line_6)
        self.label_12 = QtGui.QLabel(wid_revext)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.rightBox.addWidget(self.label_12)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_13 = QtGui.QLabel(wid_revext)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_10.addWidget(self.label_13)
        self.ln_remesh = QtGui.QLineEdit(wid_revext)
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
        self.btn_remesh = QtGui.QPushButton(wid_revext)
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
        self.line_2 = QtGui.QFrame(wid_revext)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.rightBox.addWidget(self.line_2)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.rightBox.addItem(spacerItem2)
        self.line_3 = QtGui.QFrame(wid_revext)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.rightBox.addWidget(self.line_3)
        self.lay_btns = QtGui.QHBoxLayout()
        self.lay_btns.setObjectName(_fromUtf8("lay_btns"))
        self.btn_ok = QtGui.QPushButton(wid_revext)
        self.btn_ok.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btn_ok.setAutoDefault(True)
        self.btn_ok.setDefault(True)
        self.btn_ok.setObjectName(_fromUtf8("btn_ok"))
        self.lay_btns.addWidget(self.btn_ok)
        self.btn_cancel = QtGui.QPushButton(wid_revext)
        self.btn_cancel.setObjectName(_fromUtf8("btn_cancel"))
        self.lay_btns.addWidget(self.btn_cancel)
        self.rightBox.addLayout(self.lay_btns)
        self.horizontalLayout.addLayout(self.rightBox)

        self.glwidget = GLWidget()
        mainLayout = QtGui.QHBoxLayout()
        mainLayout.addWidget(self.glwidget)
        self.glbox.setLayout(mainLayout)

        self.btn_addpoint.clicked.connect(self.act_btn_addpoint)
        self.btn_delpoint.clicked.connect(self.act_btn_delpoint)
        self.btn_rectangle.clicked.connect(self.act_btn_rectangle)
        self.btn_dropcont.clicked.connect(self.act_btn_dropcont)

        self.btn_update.clicked.connect(self.act_btn_update)
        self.btn_remesh.clicked.connect(self.act_btn_remesh)
        self.btn_ok.clicked.connect(self.act_btn_ok)
        self.btn_cancel.clicked.connect(self.close)

        self.tbl_points.setSelectionBehavior(QtGui.QTableView.SelectRows)
        self.tbl_points.itemSelectionChanged.connect(self.act_tbl_selection)

        self.retranslateUi(wid_revext)
        self.tab_inter.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(wid_revext)

    def retranslateUi(self, wid_revext):
        wid_revext.setWindowTitle(_translate("wid_revext", "Revolve / Extract", None))
        item = self.tbl_points.horizontalHeaderItem(0)
        item.setText(_translate("wid_revext", "X, mm", None))
        item = self.tbl_points.horizontalHeaderItem(1)
        item.setText(_translate("wid_revext", "Y, mm", None))
        self.label_7.setText(_translate("wid_revext", "Contour", None))
        self.ln_addpoint.setText(_translate("wid_revext", "0,0", None))
        self.btn_addpoint.setText(_translate("wid_revext", "Add point", None))
        self.btn_delpoint.setText(_translate("wid_revext", "Delete point", None))
        self.btn_rectangle.setText(_translate("wid_revext", "Rectangle", None))
        self.btn_dropcont.setText(_translate("wid_revext", "Drop points", None))
        self.pushButton_2.setText(_translate("wid_revext", "Load points", None))
        self.pushButton.setText(_translate("wid_revext", "Save points", None))
        self.lbl_gl.setText(_translate("wid_revext", "Component preview", None))
        self.lbl_name.setText(_translate("wid_revext", "Component name:", None))
        self.ln_name.setText(_translate("wid_revext", "TESTNAME", None))
        self.label_2.setText(_translate("wid_revext", "Component parameters", None))
        self.label_8.setText(_translate("wid_revext", "Axis p2", None))
        self.ln_revang.setText(_translate("wid_revext", "360", None))
        self.label.setText(_translate("wid_revext", "Axis p1", None))
        self.ln_revax1.setText(_translate("wid_revext", "0,0,0", None))
        self.label_3.setText(_translate("wid_revext", "Angle", None))
        self.ln_revax2.setText(_translate("wid_revext", "1,0,0", None))
        self.tab_inter.setTabText(self.tab_inter.indexOf(self.tab_revolve), _translate("wid_revext", "Revolve", None))
        self.ln_extax.setText(_translate("wid_revext", "0,0,1", None))
        self.ln_exthei.setText(_translate("wid_revext", "100", None))
        self.label_4.setText(_translate("wid_revext", "Axis", None))
        self.label_5.setText(_translate("wid_revext", "Height", None))
        self.tab_inter.setTabText(self.tab_inter.indexOf(self.tab_extract), _translate("wid_revext", "Extract", None))
        self.btn_update.setText(_translate("wid_revext", "Update", None))
        self.lbl_set.setText(_translate("wid_revext", "Material", None))
        self.btn_startselect.setText(_translate("wid_revext", "Select planes", None))
        self.btn_selectall.setText(_translate("wid_revext", "Select All", None))
        self.lbl_material.setText(_translate("wid_revext", "Material:", None))
        self.label_6.setText(_translate("wid_revext", "Thickness, mm", None))
        self.ln_thickness.setText(_translate("wid_revext", "0", None))
        self.btn_set.setText(_translate("wid_revext", "Apply", None))
        self.label_12.setText(_translate("wid_revext", "Remeshing", None))
        self.label_13.setText(_translate("wid_revext", "Offset distance parameter:", None))
        self.ln_remesh.setText(_translate("wid_revext", "0.01", None))
        self.btn_remesh.setText(_translate("wid_revext", "Apply Remeshing", None))
        self.btn_ok.setText(_translate("wid_revext", "OK", None))
        self.btn_cancel.setText(_translate("wid_revext", "Cancel", None))

    def loadinit(self,mainw,comp=None):
        self.mainwindow = mainw
        if not comp:
            self.tabloaddef()
        else:
            self.fedit=True
            self.orgcomp = comp
            #self.fieldinit(comp)
            self.tabinit(comp)
            self.recreate()
            self.glinit()

        self.cmbinit()

    def act_tbl_selection(self):
        item = self.tbl_points.selectedItems()
        if item:
            tbltext = '(' + item[0].text() + ', ' + item[1].text() + ')'
            self.ln_delpoint.setText(tbltext)
        else:
            self.ln_delpoint.setText('Select from table')

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

    def glinit(self):
        self.glwidget.dropselection()
        self.glwidget.cleartmpobjs()
        self.glwidget.objects.clear()
        self.glwidget.addobj(self.comp.getgeo())
        self.glwidget.upmat()

    def tabinit(self,comp):
        for p in comp.points:
            self.newrow(str(p[0]), str(p[1]))
        self.fieldinit(comp)

    def fieldinit(self,comp):
        if isinstance(comp,CNST.clEXT.EXT):
            self.tab_inter.setCurrentIndex(1)
            self.ln_extax.setText(str(comp.axis)[1:-1])
            self.ln_exthei.setText(str(comp.height))

        elif isinstance(comp,CNST.clREV.REV):
            self.tab_inter.setCurrentIndex(0)
            self.ln_revang.setText(str(comp.angle))
            self.ln_revax1.setText(str(comp.axis[0])[1:-1])
            self.ln_revax2.setText(str(comp.axis[1])[1:-1])



    def tabloaddef(self):
        self.tbl_points.setRowCount(0)
        points = [(0, 0, 0), (200, 0, 0), (200, 100, 0), (0, 100, 0)]
        for p in points:
            self.newrow(str(p[0]), str(p[1]))

    def act_btn_rectangle(self):
        self.tabloaddef()

    def pointsload(self):
        points = []
        for i in range(self.tbl_points.rowCount()):
            x = self.tbl_points.item(i, 0).text()
            y = self.tbl_points.item(i, 1).text()
            points.append((int(x), int(y), 0))
        return points

    def act_btn_dropcont(self):
        self.tbl_points.setRowCount(0)

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
        # self.recreate(rms=True)
        g = self.comp.geoobj
        geos = remeshing(list(g.points), list(g.faces))
        geoobj = clGEOOBJ.GEOOBJ(geos, self.comp.geoobj.getname())
        params = self.comp.getparams()
        #compparams = (geoobj, *params)
        if isinstance(self.comp,CNST.clEXT.EXT):
            self.comp = CNST.clEXT.EXT(geoobj,*params)
        elif isinstance(self.comp,CNST.clREV.REV):
            self.comp = CNST.clREV.REV(geoobj, *params)

        #self.comp = CNST.clSLAT.SLAT(compparams)
        self.tbl_points.setRowCount(0)
        self.glinit()
        self.tabinit(self.comp)

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
        materialname = self.cmb_material.currentText()
        for mat in self.materials:
            if materialname == mat.getname():
                material = mat

        self.ln_thickness.setText("0")

        for objid, planeid in self.glwidget.selection:
            self.comp.setthick(planeid - 1, thickness)
            self.comp.setmat(planeid - 1, material)
            self.editrow(planeid - 1, str(thickness), str(materialname))

        self.glwidget.mode = "pick0"
        self.glwidget.dropselection()
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

    def act_btn_update(self):
        self.glwidget.objects.clear()
        # del(self.comp)
        self.recreate()
        self.glinit()

    def recreate(self):
        if self.tab_inter.currentIndex() == 0:
            self.recreaterev()
        elif self.tab_inter.currentIndex() == 1:
            self.recreateext()

    def recreaterev(self):
        name = 'RevShape'
        axisstrp1 = self.ln_revax1.text().split(',')
        axisp1 = [float(cd) for cd in axisstrp1]
        axisstrp2 = self.ln_revax2.text().split(',')
        axisp2 = [float(cd) for cd in axisstrp2]
        angle = int(self.ln_revang.text())
        points = self.pointsload()
        pie = CNST.FC.boxmaker.Rev(points, (axisp1, axisp2), angle)
        geos = pie.getgeo()
        geoobj = clGEOOBJ.GEOOBJ(geos, name)
        self.comp = CNST.clREV.REV(geoobj,points, (axisp1, axisp2), angle)
        self.comp.defmatinit(list(self.mainwindow.materials)[0])
        self.glinit()

    def recreateext(self):
        name = 'ExtShape'
        axisstr = self.ln_extax.text().split(',')
        axis = [float(cd) for cd in axisstr]
        height = int(self.ln_exthei.text())
        points = self.pointsload()
        pie = CNST.FC.boxmaker.Ext(points, axis, height)
        geos = pie.getgeo()
        geoobj = clGEOOBJ.GEOOBJ(geos, name)
        self.comp = CNST.clEXT.EXT(geoobj,points, axis, height)
        self.comp.defmatinit(list(self.mainwindow.materials)[0])
        self.glinit()
