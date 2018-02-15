import sys
from glwidget import *
#import CNST.clELEM
from CNST.remesh import remeshing
from CNST.PROJECTILE import clDETAIL
from CNST.FC.boxmaker import Revolver,Uni
from CNST.geoimport import importges
from CNST.clGEOOBJ import GEOOBJ
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

class Ui_wid_addproj(QtGui.QWidget):
    def __init__(self):
        super(Ui_wid_addproj, self).__init__()
        #self.mainwindow=0
        self.fedit=False
        self.setupUi(self)
        self.fmouseclick = False
        self.category = "PROJECTILE"
        self.components = []
        self.stls={}
        self.activecomp=None
        self.contour = []

    def setupUi(self, wid_addproj):
        wid_addproj.setObjectName(_fromUtf8("wid_addproj"))
        wid_addproj.resize(1200, 700)
        wid_addproj.setMinimumSize(QtCore.QSize(950, 0))
        self.horizontalLayout = QtGui.QHBoxLayout(wid_addproj)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tre_details = QtGui.QTreeWidget(wid_addproj)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tre_details.sizePolicy().hasHeightForWidth())
        self.tre_details.setSizePolicy(sizePolicy)
        self.tre_details.setMinimumSize(QtCore.QSize(255, 0))
        self.tre_details.setMaximumSize(QtCore.QSize(255, 16777215))
        self.tre_details.setObjectName(_fromUtf8("tre_details"))
        self.tre_details.headerItem().setText(0, _fromUtf8("1"))
        self.verticalLayout.addWidget(self.tre_details)
        self.tbl_points = QtGui.QTableWidget(wid_addproj)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbl_points.sizePolicy().hasHeightForWidth())
        self.tbl_points.setSizePolicy(sizePolicy)
        self.tbl_points.setMinimumSize(QtCore.QSize(255, 0))
        self.tbl_points.setMaximumSize(QtCore.QSize(255, 16777215))
        self.tbl_points.setObjectName(_fromUtf8("tbl_points"))
        self.tbl_points.setColumnCount(3)
        self.tbl_points.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tbl_points.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tbl_points.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tbl_points.setHorizontalHeaderItem(2, item)
        self.tbl_points.horizontalHeader().setDefaultSectionSize(110)
        self.verticalLayout.addWidget(self.tbl_points)
        self.label_7 = QtGui.QLabel(wid_addproj)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout.addWidget(self.label_7)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.btn_adddetail = QtGui.QPushButton(wid_addproj)
        self.btn_adddetail.setObjectName(_fromUtf8("btn_adddetail"))
        self.horizontalLayout_5.addWidget(self.btn_adddetail)
        self.btn_deldetail = QtGui.QPushButton(wid_addproj)
        self.btn_deldetail.setObjectName(_fromUtf8("btn_deldetail"))
        self.horizontalLayout_5.addWidget(self.btn_deldetail)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.btn_rectangle = QtGui.QPushButton(wid_addproj)
        self.btn_rectangle.setObjectName(_fromUtf8("btn_rectangle"))
        self.horizontalLayout_9.addWidget(self.btn_rectangle)
        self.btn_dropcont = QtGui.QPushButton(wid_addproj)
        self.btn_dropcont.setObjectName(_fromUtf8("btn_dropcont"))
        self.horizontalLayout_9.addWidget(self.btn_dropcont)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.lay_gl = QtGui.QVBoxLayout()
        self.lay_gl.setObjectName(_fromUtf8("lay_gl"))
        self.lbl_gl = QtGui.QLabel(wid_addproj)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_gl.sizePolicy().hasHeightForWidth())
        self.lbl_gl.setSizePolicy(sizePolicy)
        self.lbl_gl.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_gl.setObjectName(_fromUtf8("lbl_gl"))
        self.lay_gl.addWidget(self.lbl_gl)
        self.glbox = QtGui.QWidget(wid_addproj)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.glbox.sizePolicy().hasHeightForWidth())
        self.glbox.setSizePolicy(sizePolicy)
        self.glbox.setMinimumSize(QtCore.QSize(300, 300))
        self.glbox.setObjectName(_fromUtf8("glbox"))
        self.lay_gl.addWidget(self.glbox)
        self.horizontalLayout.addLayout(self.lay_gl)
        self.line_4 = QtGui.QFrame(wid_addproj)
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.horizontalLayout.addWidget(self.line_4)
        self.rightBox = QtGui.QVBoxLayout()
        self.rightBox.setObjectName(_fromUtf8("rightBox"))
        self.lay_name = QtGui.QHBoxLayout()
        self.lay_name.setObjectName(_fromUtf8("lay_name"))
        self.lbl_name = QtGui.QLabel(wid_addproj)
        self.lbl_name.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_name.setObjectName(_fromUtf8("lbl_name"))
        self.lay_name.addWidget(self.lbl_name)
        self.ln_name = QtGui.QLineEdit(wid_addproj)
        self.ln_name.setEnabled(False)
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
        self.line = QtGui.QFrame(wid_addproj)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.rightBox.addWidget(self.line)
        self.label_2 = QtGui.QLabel(wid_addproj)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.rightBox.addWidget(self.label_2)
        self.tbl_params = QtGui.QTableWidget(wid_addproj)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbl_params.sizePolicy().hasHeightForWidth())
        self.tbl_params.setSizePolicy(sizePolicy)
        self.tbl_params.setObjectName(_fromUtf8("tbl_params"))
        self.tbl_params.setColumnCount(2)
        self.tbl_params.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tbl_params.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tbl_params.setHorizontalHeaderItem(1, item)
        self.tbl_params.horizontalHeader().setDefaultSectionSize(120)
        self.rightBox.addWidget(self.tbl_params)
        self.label_8 = QtGui.QLabel(wid_addproj)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.rightBox.addWidget(self.label_8)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_10 = QtGui.QLabel(wid_addproj)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_3.addWidget(self.label_10)
        self.ln_angle = QtGui.QLineEdit(wid_addproj)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_angle.sizePolicy().hasHeightForWidth())
        self.ln_angle.setSizePolicy(sizePolicy)
        self.ln_angle.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_angle.setObjectName(_fromUtf8("ln_angle"))
        self.horizontalLayout_3.addWidget(self.ln_angle)
        self.label_11 = QtGui.QLabel(wid_addproj)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_3.addWidget(self.label_11)
        self.ln_dy = QtGui.QLineEdit(wid_addproj)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_dy.sizePolicy().hasHeightForWidth())
        self.ln_dy.setSizePolicy(sizePolicy)
        self.ln_dy.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_dy.setObjectName(_fromUtf8("ln_dy"))
        self.horizontalLayout_3.addWidget(self.ln_dy)
        self.rightBox.addLayout(self.horizontalLayout_3)
        self.line_5 = QtGui.QFrame(wid_addproj)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.rightBox.addWidget(self.line_5)
        self.lbl_set = QtGui.QLabel(wid_addproj)
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
        self.lbl_material = QtGui.QLabel(wid_addproj)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_material.sizePolicy().hasHeightForWidth())
        self.lbl_material.setSizePolicy(sizePolicy)
        self.lbl_material.setObjectName(_fromUtf8("lbl_material"))
        self.lay_material.addWidget(self.lbl_material)
        self.cmb_material = QtGui.QComboBox(wid_addproj)
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
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.btn_update = QtGui.QPushButton(wid_addproj)
        self.btn_update.setObjectName(_fromUtf8("btn_update"))
        self.horizontalLayout_8.addWidget(self.btn_update)
        self.btn_default = QtGui.QPushButton(wid_addproj)
        self.btn_default.setObjectName(_fromUtf8("btn_default"))
        self.horizontalLayout_8.addWidget(self.btn_default)
        self.rightBox.addLayout(self.horizontalLayout_8)
        self.label_12 = QtGui.QLabel(wid_addproj)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.rightBox.addWidget(self.label_12)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_13 = QtGui.QLabel(wid_addproj)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_10.addWidget(self.label_13)
        self.ln_remesh = QtGui.QLineEdit(wid_addproj)
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
        self.btn_remesh = QtGui.QPushButton(wid_addproj)
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
        self.line_2 = QtGui.QFrame(wid_addproj)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.rightBox.addWidget(self.line_2)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.rightBox.addItem(spacerItem1)
        self.line_3 = QtGui.QFrame(wid_addproj)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.rightBox.addWidget(self.line_3)
        self.lay_btns = QtGui.QHBoxLayout()
        self.lay_btns.setObjectName(_fromUtf8("lay_btns"))
        self.btn_ok = QtGui.QPushButton(wid_addproj)
        self.btn_ok.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btn_ok.setDefault(True)
        self.btn_ok.setObjectName(_fromUtf8("btn_ok"))
        self.lay_btns.addWidget(self.btn_ok)
        self.btn_cancel = QtGui.QPushButton(wid_addproj)
        self.btn_cancel.setObjectName(_fromUtf8("btn_cancel"))
        self.lay_btns.addWidget(self.btn_cancel)
        self.rightBox.addLayout(self.lay_btns)
        self.horizontalLayout.addLayout(self.rightBox)

        self.glwidget = GLWidget()
        mainLayout = QtGui.QHBoxLayout()
        mainLayout.addWidget(self.glwidget)
        self.glbox.setLayout(mainLayout)
        self.glwidget.mode = "pick0"

        self.tre_details.itemChanged.connect(self.act_tre_check)
        # self.tre_details.itemSelectionChanged.connect(self.act_tre_test)
        self.tre_details.itemClicked.connect(self.act_tre_test)
        self.tre_details.setHeaderLabels(["Projectile", "col1"])
        self.tre_details.hideColumn(1)

        self.tbl_points.verticalHeader().setVisible(False)
        self.tbl_points.itemSelectionChanged.connect(self.act_tblselchange)
        self.tbl_points.hideColumn(2)

        #self.tbl_params.itemChanged.connect(self.act_tblchanged)


        self.btn_update.clicked.connect(self.act_btn_set)
        self.btn_adddetail.clicked.connect(self.act_btn_adddetail)
        self.btn_rectangle.clicked.connect(self.act_btn_adddets)
        self.btn_deldetail.clicked.connect(self.act_btn_delete)
        self.btn_default.clicked.connect(self.act_btn_default)

        self.btn_ok.clicked.connect(self.act_btn_ok)
        self.btn_cancel.clicked.connect(self.close)

        self.retranslateUi(wid_addproj)
        QtCore.QMetaObject.connectSlotsByName(wid_addproj)

    def retranslateUi(self, wid_addproj):
        wid_addproj.setWindowTitle(_translate("wid_addproj", "Projectile Assembly", None))
        item = self.tbl_points.horizontalHeaderItem(0)
        item.setText(_translate("wid_addproj", "#Point", None))
        item = self.tbl_points.horizontalHeaderItem(1)
        item.setText(_translate("wid_addproj", "Connection", None))
        item = self.tbl_points.horizontalHeaderItem(2)
        item.setText(_translate("wid_addproj", "PID", None))
        self.label_7.setText(_translate("wid_addproj", "Contour", None))
        self.btn_adddetail.setText(_translate("wid_addproj", "Add detail", None))
        self.btn_deldetail.setText(_translate("wid_addproj", "Delete detail", None))
        self.btn_rectangle.setText(_translate("wid_addproj", "Rectangle", None))
        self.btn_dropcont.setText(_translate("wid_addproj", "Drop contour", None))
        self.lbl_gl.setText(_translate("wid_addproj", "Component preview", None))
        self.lbl_name.setText(_translate("wid_addproj", "Detail name:", None))
        self.ln_name.setText(_translate("wid_addproj", "TESTNAME", None))
        self.label_2.setText(_translate("wid_addproj", "Detail parameters", None))
        item = self.tbl_params.horizontalHeaderItem(0)
        item.setText(_translate("wid_addproj", "Parameter", None))
        item = self.tbl_params.horizontalHeaderItem(1)
        item.setText(_translate("wid_addproj", "Value", None))
        self.label_8.setText(_translate("wid_addproj", "View parameters", None))
        self.label_10.setText(_translate("wid_addproj", "Angle", None))
        self.ln_angle.setText(_translate("wid_addproj", "180", None))
        self.label_11.setText(_translate("wid_addproj", "Y:", None))
        self.ln_dy.setText(_translate("wid_addproj", "40", None))
        self.lbl_set.setText(_translate("wid_addproj", "Material", None))
        self.lbl_material.setText(_translate("wid_addproj", "Material:", None))
        self.btn_update.setText(_translate("wid_addproj", "Update", None))
        self.btn_default.setText(_translate("wid_addproj", "Default", None))
        self.label_12.setText(_translate("wid_addproj", "Remeshing", None))
        self.label_13.setText(_translate("wid_addproj", "Offset distance parameter:", None))
        self.ln_remesh.setText(_translate("wid_addproj", "1e-2", None))
        self.btn_remesh.setText(_translate("wid_addproj", "Apply Remeshing", None))
        self.btn_ok.setText(_translate("wid_addproj", "OK", None))
        self.btn_cancel.setText(_translate("wid_addproj", "Cancel", None))

    def loadinit(self, path, mainw, edt=False):
        self.mainwindow = mainw
        self.setcategory()
        name = 'Proj1'
        if edt:
            self.fedit = True
            self.orgcomp = path
            self.comp = path.getcopy()
            name = self.comp.getname()
            self.tabinit()

        name = name.split('/')[-1]
        self.ln_name.setText(name)
        self.lbl_gl.setText("Detail preview: " + name)
        self.glinit()
        self.cmbinit()
        #self.act_btn_adddets()
        # TODO IMHERE
        # self.act_btn_ok()

    # def recreate(self):
    #     pass
    #     # name = 'Projectile'
    #     # geoparams = self.getparams()
    #     # pie = CNST.FC.boxmaker.Slatarmor(*geoparams)
    #     # geos = pie.getgeo()
    #     # geoobj = clGEOOBJ.GEOOBJ(geos, name)
    #     # compparams = (geoobj, *geoparams)
    #     # self.comp = CNST.clSLAT.SLAT(compparams)
    #     # self.comp.defmatinit(list(self.mainwindow.materials)[0])
    #     # self.glinit()

    def act_btn_set(self):
        if self.getdetchanges():
            self.act_btn_adddetail(edt=True)
        base = False
        conndict = {}
        for row in range(self.tbl_points.rowCount()):
            kitem = self.tbl_points.item(row,2)
            item = self.tbl_points.cellWidget(row, 1)
            cmbtext = item.currentText()
            if cmbtext == '<0,0>':
                base = True
                basepointind = row
            elif cmbtext == '<Join>':
                joinpointind = row
            elif cmbtext != 'None':
                conndict[kitem.text()] = cmbtext

        # if base:
        #     pos = -np.array(list(self.activecomp.contpoints.values())[basepointind])
        #     self.activecomp.geoobj.move(pos)
        #     for k, v in self.activecomp.contpoints.items():
        #         self.activecomp.contpoints[k] = list(np.array(v) + pos)
        #
        #     self.activecomp.connpoints = conndict
        #
        #     self.glwidget.upmat()
        #     self.inittabpoints()

        self.activecomp.connpoints = conndict
        # basecomp = self.checkforbase()
        for indp,connp in self.activecomp.connpoints.items():
            print(indp,connp)
            basep = np.array(self.activecomp.contpoints[indp])
            comp = self.getcompbyname(connp)
            if comp:
                for k,v in comp.connpoints.items():
                    print(k,v)
                    if v == connp:
                        oldk = k
                movep = np.array(comp.contpoints[oldk])
                print(movep,basep)
                pos = basep-movep
                comp.geoobj.move(pos)
                for k, v in comp.contpoints.items():
                    comp.contpoints[k] = list(np.array(v) + pos)
                if np.linalg.norm(pos):
                    name, pps, flags, arcs, galts, freverse, pars = importges(comp.path, False)
                    ax = [(0, 0, 0), (200, 0, 0)]
                    for k,v in pps.items():
                        pps[k] = list(np.array(v)+pos)
                    georevolver = Revolver(pps, ax, arcs, galts, freverse, 360)
                    pstl = 'CNST\GEO\M4\GEO2STL\\' + name + '.stl'
                    georevolver.getobj(pstl)

        self.glwidget.upmat()

    def checkforbase(self):
        base = self.components[0]
        for comp in self.components:
            name = comp.getname()
            if name not in list(comp.connpoints.values()):
                base = comp
                break
        return base

    def getcompbyname(self,name):
        for comp in self.components:
            if comp.getname() == name:
                return comp
        return None

    def act_btn_ok(self):
        self.glwidget.doneCurrent()
        self.mainwindow.glwidget.makeCurrent()

        if self.fedit:
            self.mainwindow.delcomp(self.orgcomp)

        for comp in reversed(self.components):
            self.mainwindow.pushcomponent(comp.getcopy(), self.category)
            del (comp)

        self.glwidget.objects.clear()
        self.close()

    def getdetchanges(self):
        identic=True
        pardict = {}
        olddict = self.activecomp.params
        for row in range(self.tbl_params.rowCount()):
            par = self.tbl_params.item(row,0).text()
            val = self.tbl_params.item(row,1).text()
            pardict[par] = val
            if olddict[par]!=val:
                identic=False
        angle = int(self.ln_angle.text())
        if angle != self.activecomp.angle or not identic:
            self.activecomp.angle = angle
            self.activecomp.params = pardict
            return True
        return False


    def act_tbl_selection(self):
        item = self.tbl_points.selectedItems()
        if item:
            tbltext = '(' + item[0].text() + ', ' + item[1].text() + ')'
            self.ln_delpoint.setText(tbltext)
        else:
            self.ln_delpoint.setText('Select from table')

    def act_btn_adddetail(self,edt=False,path=None):
        angle = int(self.ln_angle.text())
        pardict=False

        if edt:
            path = self.activecomp.path
            angle = self.activecomp.angle
            pardict = self.activecomp.params
            self.delcomp(self.activecomp)
            self.activecomp=None
        elif path:
            pass
        else:
            filedialog = QtGui.QFileDialog(self)
            path = filedialog.getOpenFileName(self, "Open geometry", "CNST\GEO\M4\korpus.geo", filter="geo (*.geo *.)")

        name, pps, flags, arcs, galts,freverse,pars = importges(path,pardict)

        # TODO get rid of
        angle = 360

        ax = [(0, 0, 0), (200, 0, 0)]
        georevolver = Revolver(pps, ax, arcs, galts,freverse, angle)
        geos = georevolver.getgeo()
        pstl = 'CNST\GEO\M4\GEO2STL\\' + name + '.stl'
        georevolver.getobj(pstl)
        geoobj = GEOOBJ(geos, name)
        comp = clDETAIL.DETAIL(geoobj, pps, arcs, galts, flags,pars,path,angle)
        self.pushcomponent(comp)
        self.stls[comp] = pstl

        return comp


    def poinewrow(self, pointd, rowvalue):
        # print(pointd,'\t')
        rowname = str(pointd[1])
        rowPosition = self.tbl_points.rowCount()
        self.tbl_points.insertRow(rowPosition)
        item1 = QtGui.QTableWidgetItem(rowname)
        item1.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item1.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        item2 = QtGui.QComboBox()
        item2.addItem('None')
        item2.addItem('<0,0>')
        item2.addItem('<Join>')
        ind = 0
        for i, cp in enumerate(self.activecomp.connpoints.items()):
            # print(cp)
            item2.addItem(cp[1])
            if pointd[0] == cp[0]:
                ind = i + 3

        item2.setCurrentIndex(ind)

        item3 = QtGui.QTableWidgetItem(pointd[0])
        item3.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)

        self.tbl_points.setItem(rowPosition, 0, item1)
        self.tbl_points.setCellWidget(rowPosition, 1, item2)
        self.tbl_points.setItem(rowPosition, 2, item3)

    def poieditrow(self, tab, rowPosition, rowValue):
        item1 = QtGui.QTableWidgetItem(rowPosition)
        item1.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)

        item2 = QtGui.QTableWidgetItem(rowValue)
        item2.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)

        tab.setItem(rowPosition, 1, item1)
        tab.setItem(rowPosition, 2, item2)

    def parnewrow(self, rowname, rowvalue):

        rowPosition = self.tbl_params.rowCount()
        self.tbl_params.insertRow(rowPosition)
        item1 = QtGui.QTableWidgetItem(rowname)
        item1.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item1.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        item2 = QtGui.QTableWidgetItem(rowvalue)
        item2.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)

        self.tbl_params.setItem(rowPosition, 0, item1)
        self.tbl_params.setItem(rowPosition, 1, item2)

    # def pareditrow(self, rowPosition, rowValue):
    #     # item1 = QtGui.QTableWidgetItem(rowPosition)
    #     # item1.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
    #
    #     item2 = QtGui.QTableWidgetItem(rowValue)
    #     item2.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
    #
    #     #self.tbl_params.setItem(rowPosition, 0, item1)
    #     self.tbl_params.setItem(rowPosition, 1, item2)

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

    def glinit(self):
        self.glwidget.dropselection()
        self.glwidget.cleartmpobjs()
        self.glwidget.objects.clear()
        # self.glwidget.addobj(self.comp.getgeo())
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
        points = [(0, 0, 0), (200, 0, 0), (200, 100, 0), (0, 100, 0)]
        for p in points:
            self.newrow(str(p[0]), str(p[1]))

    def pointsload(self):
        points = []
        for i in range(self.tbl_points.rowCount()):
            x = self.tbl_points.item(i, 0).text()
            y = self.tbl_points.item(i, 1).text()
            points.append((int(x), int(y), 0))
        return points

    def act_btn_adddets(self):
        paths = ['CNST\\GEO\\M4\\korpus.geo', 'CNST\\GEO\\M4\\BB.geo', 'CNST\\GEO\\M4\\BP1.geo',
                 'CNST\\GEO\\M4\\BP2.geo',
                 'CNST\\GEO\\M4\\BU.geo', 'CNST\\GEO\\M4\\nak.geo', 'CNST\\GEO\\M4\\Colpak.geo']
        angle = int(self.ln_angle.text())
        for path in paths:
            self.act_btn_adddetail(path=path)


    def act_btn_dropcont(self):
        self.tbl_points.setRowCount(0)

    def act_btn_default(self):
        self.genuni()

    def cmbinit(self):
        self.materials = []
        args = []
        for mat in self.mainwindow.materials:
            self.materials.append(mat)
            args.append(mat.getname())

        self.cmb_material.addItems(args)

        # def closeEvent(self, QCloseEvent):
        #     self.act_btn_cancel()

    # def act_btn_remesh(self):
    #     # self.recreate(rms=True)
    #     g = self.comp.geoobj
    #     geos = remeshing(list(g.points), list(g.faces))
    #     geoobj = clGEOOBJ.GEOOBJ(geos, self.comp.geoobj.getname())
    #     compparams = (geoobj, *self.getparams())
    #     self.comp = CNST.clSLAT.SLAT(compparams)
    #     self.tbl_points.setRowCount(0)
    #     self.glinit()
    #     self.tabinit()

    def act_tre_test(self):
        # one click selection in tree
        getselected = self.tre_details.selectedItems()
        if getselected:
            activetree = getselected[0]
            activeid = int(activetree.text(1))

            if activeid == -1:
                # self.disablelay(True)
                # self.clearlines()
                self.activecomp = None
                # self.disablebtn(True)
            else:
                # self.disablelay(False)
                self.activecomp = self.getcompbygeoid(activeid)
                self.ln_name.setText(self.activecomp.getname())
                self.ln_angle.setText(str(self.activecomp.angle))
                self.inittblpoints()
                self.inittblpars()
                # self.disablebtn(False)

    def pushcomponent(self, comp):
        comp.categoryname = self.category
        self.components.append(comp)
        # self.pushmaterials(comp)
        self.treenewentry(comp)
        comp.geoobj.edgeswitch()
        self.glwidget.addobj(comp.getgeo())
        self.activecomp = comp

    def treenewentry(self, comp):
        name = comp.getname()
        child = QtGui.QTreeWidgetItem(self.parent, [name, str(comp.getid())])
        child.setCheckState(0, QtCore.Qt.Checked)
        child.setFlags(child.flags())
        self.tre_details.clearSelection()
        self.activecomp = None
        # self.disablebtn(True)

    def setcategory(self):
        parent = QtGui.QTreeWidgetItem(self.tre_details, [self.category, '-1'])
        parent.setFlags(parent.flags() | QtCore.Qt.ItemIsTristate | QtCore.Qt.ItemIsUserCheckable)
        parent.setCheckState(0, QtCore.Qt.Checked)
        self.parent = parent

    def getcompbygeoid(self, id):
        for comp in self.components:
            if comp.getid() == id:
                return comp

    def act_tre_check(self, item, column):
        # checkboxes in tree
        tid = item.text(1)
        if tid:
            changecomp = [self.getcompbygeoid(int(tid))]
            self.tre_details.blockSignals(True)
            if item.checkState(0) == QtCore.Qt.Checked:
                self.glwidget.delinvisible(changecomp)
            elif item.checkState(0) == QtCore.Qt.Unchecked:
                self.glwidget.addinvisible(changecomp)
            self.tre_details.blockSignals(False)

    def inittblpoints(self):
        self.tbl_points.setRowCount(0)
        for ind, p in enumerate(self.activecomp.contpoints.items()):
            self.poinewrow(p, 0)

    def inittblpars(self):
        comp = self.activecomp
        self.tbl_params.setRowCount(0)
        for k,v in comp.params.items():
            self.parnewrow(k,v)

    def act_tblselchange(self):
        sel = self.tbl_points.selectedItems()
        if sel:
            row = 1 + sel[0].row()
            if row:
                pos = eval(self.tbl_points.item(row - 1, 0).text())
                self.glwidget.sphcdlist = [pos]
                self.glwidget.sphinit(1)
                self.glwidget.upmat()

    def delcomp(self, comp):
        parent = self.tre_details.findItems(comp.categoryname, QtCore.Qt.MatchFixedString, 0)[0]
        child = \
            self.tre_details.findItems(str(comp.getid()), QtCore.Qt.MatchFixedString | QtCore.Qt.MatchRecursive, 1)[
                0]
        child.setCheckState(0, QtCore.Qt.Checked)
        parent.removeChild(child)
        # if parent.childCount() == 0:
        #     (parent.parent() or self.tre_details.invisibleRootItem()).removeChild(parent)
        del(self.stls[comp])
        self.components.remove(comp)
        self.glwidget.objects.remove(comp.getgeo())

    def act_btn_delete(self):
        self.delcomp(self.activecomp)
        self.tbl_params.setRowCount(0)
        self.tbl_points.setRowCount(0)
        self.activecomp=None

    def genuni(self):
        unif = Uni(list(self.stls.values()))
        unif.generate()
