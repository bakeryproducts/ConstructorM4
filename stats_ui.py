import numpy as np
from PIL import Image
from PIL import ImageOps
from CNST.techs import getangle
from shootsettings_ui import Ui_shootset
import mathutils as mth
from time import time
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

class Ui_wid_stats(QtGui.QWidget):
    def __init__(self):
        super(Ui_wid_stats, self).__init__()
        self.setupUi(self)
        #self.mainwindow = 0
        self.meanthick=[]
        self.probx,self.proby = 0,0


    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1200, 670)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget = QtGui.QWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout.addWidget(self.widget)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.tbl_res = QtGui.QTableWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbl_res.sizePolicy().hasHeightForWidth())
        self.tbl_res.setSizePolicy(sizePolicy)
        self.tbl_res.setObjectName(_fromUtf8("tbl_res"))
        self.tbl_res.setColumnCount(8)
        self.tbl_res.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tbl_res.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tbl_res.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tbl_res.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tbl_res.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tbl_res.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tbl_res.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tbl_res.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tbl_res.setHorizontalHeaderItem(7, item)
        self.verticalLayout.addWidget(self.tbl_res)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.line_3 = QtGui.QFrame(Form)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.horizontalLayout.addWidget(self.line_3)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_4.addWidget(self.label_7)
        self.cmb_shootset = QtGui.QComboBox(Form)
        self.cmb_shootset.setObjectName(_fromUtf8("cmb_shootset"))
        self.horizontalLayout_4.addWidget(self.cmb_shootset)
        self.btn_shootset = QtGui.QPushButton(Form)
        self.btn_shootset.setObjectName(_fromUtf8("btn_shootset"))
        self.horizontalLayout_4.addWidget(self.btn_shootset)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_17 = QtGui.QLabel(Form)
        self.label_17.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_4.addWidget(self.label_17, 2, 0, 1, 1)
        self.label_18 = QtGui.QLabel(Form)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_4.addWidget(self.label_18, 0, 0, 1, 1)
        self.line_2 = QtGui.QFrame(Form)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_4.addWidget(self.line_2, 1, 0, 1, 1)
        self.tab_prx = QtGui.QTabWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_prx.sizePolicy().hasHeightForWidth())
        self.tab_prx.setSizePolicy(sizePolicy)
        self.tab_prx.setMaximumSize(QtCore.QSize(400, 16777215))
        self.tab_prx.setDocumentMode(True)
        self.tab_prx.setObjectName(_fromUtf8("tab_prx"))
        self.tab_normalx = QtGui.QWidget()
        self.tab_normalx.setObjectName(_fromUtf8("tab_normalx"))
        self.gridLayout = QtGui.QGridLayout(self.tab_normalx)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.tab_normalx)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        self.ln_xnrsigma = QtGui.QLineEdit(self.tab_normalx)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_xnrsigma.sizePolicy().hasHeightForWidth())
        self.ln_xnrsigma.setSizePolicy(sizePolicy)
        self.ln_xnrsigma.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_xnrsigma.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_xnrsigma.setObjectName(_fromUtf8("ln_xnrsigma"))
        self.gridLayout.addWidget(self.ln_xnrsigma, 1, 2, 1, 1)
        self.ln_xnrmu = QtGui.QLineEdit(self.tab_normalx)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_xnrmu.sizePolicy().hasHeightForWidth())
        self.ln_xnrmu.setSizePolicy(sizePolicy)
        self.ln_xnrmu.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_xnrmu.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_xnrmu.setObjectName(_fromUtf8("ln_xnrmu"))
        self.gridLayout.addWidget(self.ln_xnrmu, 0, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.tab_normalx)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)
        self.tab_prx.addTab(self.tab_normalx, _fromUtf8(""))
        self.tab_unix = QtGui.QWidget()
        self.tab_unix.setObjectName(_fromUtf8("tab_unix"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab_unix)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.ln_unixlow = QtGui.QLineEdit(self.tab_unix)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_unixlow.sizePolicy().hasHeightForWidth())
        self.ln_unixlow.setSizePolicy(sizePolicy)
        self.ln_unixlow.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_unixlow.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_unixlow.setObjectName(_fromUtf8("ln_unixlow"))
        self.gridLayout_2.addWidget(self.ln_unixlow, 0, 2, 1, 1)
        self.ln_unixhigh = QtGui.QLineEdit(self.tab_unix)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_unixhigh.sizePolicy().hasHeightForWidth())
        self.ln_unixhigh.setSizePolicy(sizePolicy)
        self.ln_unixhigh.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_unixhigh.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_unixhigh.setObjectName(_fromUtf8("ln_unixhigh"))
        self.gridLayout_2.addWidget(self.ln_unixhigh, 1, 2, 1, 1)
        self.label_13 = QtGui.QLabel(self.tab_unix)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_2.addWidget(self.label_13, 1, 1, 1, 1)
        self.label_12 = QtGui.QLabel(self.tab_unix)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_2.addWidget(self.label_12, 0, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 0, 1, 1)
        self.tab_prx.addTab(self.tab_unix, _fromUtf8(""))
        self.tab_students = QtGui.QWidget()
        self.tab_students.setObjectName(_fromUtf8("tab_students"))
        self.gridLayout_5 = QtGui.QGridLayout(self.tab_students)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.ln_stk = QtGui.QLineEdit(self.tab_students)
        self.ln_stk.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_stk.setObjectName(_fromUtf8("ln_stk"))
        self.gridLayout_5.addWidget(self.ln_stk, 0, 2, 1, 1)
        self.label_6 = QtGui.QLabel(self.tab_students)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_5.addWidget(self.label_6, 0, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem2, 0, 0, 1, 1)
        self.tab_prx.addTab(self.tab_students, _fromUtf8(""))
        self.tab_exp = QtGui.QWidget()
        self.tab_exp.setObjectName(_fromUtf8("tab_exp"))
        self.gridLayout_6 = QtGui.QGridLayout(self.tab_exp)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.ln_explambda = QtGui.QLineEdit(self.tab_exp)
        self.ln_explambda.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_explambda.setObjectName(_fromUtf8("ln_explambda"))
        self.gridLayout_6.addWidget(self.ln_explambda, 0, 2, 1, 1)
        self.label_8 = QtGui.QLabel(self.tab_exp)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_6.addWidget(self.label_8, 0, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem3, 0, 0, 1, 1)
        self.tab_prx.addTab(self.tab_exp, _fromUtf8(""))
        self.tab_lognorm = QtGui.QWidget()
        self.tab_lognorm.setObjectName(_fromUtf8("tab_lognorm"))
        self.gridLayout_7 = QtGui.QGridLayout(self.tab_lognorm)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.ln_logsigma = QtGui.QLineEdit(self.tab_lognorm)
        self.ln_logsigma.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_logsigma.setObjectName(_fromUtf8("ln_logsigma"))
        self.gridLayout_7.addWidget(self.ln_logsigma, 1, 2, 1, 1)
        self.label_10 = QtGui.QLabel(self.tab_lognorm)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_7.addWidget(self.label_10, 1, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.tab_lognorm)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_7.addWidget(self.label_9, 0, 1, 1, 1)
        self.ln_logmu = QtGui.QLineEdit(self.tab_lognorm)
        self.ln_logmu.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_logmu.setObjectName(_fromUtf8("ln_logmu"))
        self.gridLayout_7.addWidget(self.ln_logmu, 0, 2, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem4, 1, 0, 1, 1)
        self.tab_prx.addTab(self.tab_lognorm, _fromUtf8(""))
        self.tab_x2 = QtGui.QWidget()
        self.tab_x2.setObjectName(_fromUtf8("tab_x2"))
        self.gridLayout_8 = QtGui.QGridLayout(self.tab_x2)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.label_19 = QtGui.QLabel(self.tab_x2)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout_8.addWidget(self.label_19, 0, 1, 1, 1)
        self.ln_xk = QtGui.QLineEdit(self.tab_x2)
        self.ln_xk.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_xk.setObjectName(_fromUtf8("ln_xk"))
        self.gridLayout_8.addWidget(self.ln_xk, 0, 2, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem5, 0, 0, 1, 1)
        self.tab_prx.addTab(self.tab_x2, _fromUtf8(""))
        self.tab_beta = QtGui.QWidget()
        self.tab_beta.setObjectName(_fromUtf8("tab_beta"))
        self.gridLayout_9 = QtGui.QGridLayout(self.tab_beta)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.label_20 = QtGui.QLabel(self.tab_beta)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout_9.addWidget(self.label_20, 0, 1, 1, 1)
        self.label_21 = QtGui.QLabel(self.tab_beta)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout_9.addWidget(self.label_21, 1, 1, 1, 1)
        self.ln_betabeta = QtGui.QLineEdit(self.tab_beta)
        self.ln_betabeta.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_betabeta.setObjectName(_fromUtf8("ln_betabeta"))
        self.gridLayout_9.addWidget(self.ln_betabeta, 1, 2, 1, 1)
        self.ln_betaalpha = QtGui.QLineEdit(self.tab_beta)
        self.ln_betaalpha.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_betaalpha.setObjectName(_fromUtf8("ln_betaalpha"))
        self.gridLayout_9.addWidget(self.ln_betaalpha, 0, 2, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem6, 0, 0, 1, 1)
        self.tab_prx.addTab(self.tab_beta, _fromUtf8(""))
        self.tab_gamma = QtGui.QWidget()
        self.tab_gamma.setObjectName(_fromUtf8("tab_gamma"))
        self.gridLayout_10 = QtGui.QGridLayout(self.tab_gamma)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.label_22 = QtGui.QLabel(self.tab_gamma)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout_10.addWidget(self.label_22, 0, 1, 1, 1)
        self.label_23 = QtGui.QLabel(self.tab_gamma)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.gridLayout_10.addWidget(self.label_23, 1, 1, 1, 1)
        self.ln_gammatheta = QtGui.QLineEdit(self.tab_gamma)
        self.ln_gammatheta.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_gammatheta.setObjectName(_fromUtf8("ln_gammatheta"))
        self.gridLayout_10.addWidget(self.ln_gammatheta, 0, 2, 1, 1)
        self.ln_gammak = QtGui.QLineEdit(self.tab_gamma)
        self.ln_gammak.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_gammak.setObjectName(_fromUtf8("ln_gammak"))
        self.gridLayout_10.addWidget(self.ln_gammak, 1, 2, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem7, 0, 0, 1, 1)
        self.tab_prx.addTab(self.tab_gamma, _fromUtf8(""))
        self.tab_weibull = QtGui.QWidget()
        self.tab_weibull.setObjectName(_fromUtf8("tab_weibull"))
        self.gridLayout_11 = QtGui.QGridLayout(self.tab_weibull)
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.ln_weilambda = QtGui.QLineEdit(self.tab_weibull)
        self.ln_weilambda.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_weilambda.setObjectName(_fromUtf8("ln_weilambda"))
        self.gridLayout_11.addWidget(self.ln_weilambda, 0, 2, 1, 1)
        self.ln_weik = QtGui.QLineEdit(self.tab_weibull)
        self.ln_weik.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_weik.setObjectName(_fromUtf8("ln_weik"))
        self.gridLayout_11.addWidget(self.ln_weik, 1, 2, 1, 1)
        self.label_25 = QtGui.QLabel(self.tab_weibull)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.gridLayout_11.addWidget(self.label_25, 1, 1, 1, 1)
        self.label_24 = QtGui.QLabel(self.tab_weibull)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.gridLayout_11.addWidget(self.label_24, 0, 1, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem8, 0, 0, 1, 1)
        self.tab_prx.addTab(self.tab_weibull, _fromUtf8(""))
        self.tab_custom = QtGui.QWidget()
        self.tab_custom.setObjectName(_fromUtf8("tab_custom"))
        self.gridLayout_12 = QtGui.QGridLayout(self.tab_custom)
        self.gridLayout_12.setObjectName(_fromUtf8("gridLayout_12"))
        self.label_26 = QtGui.QLabel(self.tab_custom)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.gridLayout_12.addWidget(self.label_26, 0, 1, 1, 1)
        self.btn_custom = QtGui.QToolButton(self.tab_custom)
        self.btn_custom.setObjectName(_fromUtf8("btn_custom"))
        self.gridLayout_12.addWidget(self.btn_custom, 0, 2, 1, 1)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem9, 0, 0, 1, 1)
        self.tab_prx.addTab(self.tab_custom, _fromUtf8(""))
        self.gridLayout_4.addWidget(self.tab_prx, 0, 1, 1, 1)
        self.line = QtGui.QFrame(Form)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_4.addWidget(self.line, 1, 1, 1, 1)
        self.tab_pry = QtGui.QTabWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_pry.sizePolicy().hasHeightForWidth())
        self.tab_pry.setSizePolicy(sizePolicy)
        self.tab_pry.setMaximumSize(QtCore.QSize(9000, 16777215))
        self.tab_pry.setDocumentMode(True)
        self.tab_pry.setObjectName(_fromUtf8("tab_pry"))
        self.tab_normaly = QtGui.QWidget()
        self.tab_normaly.setObjectName(_fromUtf8("tab_normaly"))
        self.gridLayout_30 = QtGui.QGridLayout(self.tab_normaly)
        self.gridLayout_30.setObjectName(_fromUtf8("gridLayout_30"))
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_30.addItem(spacerItem10, 0, 0, 1, 1)
        self.label_51 = QtGui.QLabel(self.tab_normaly)
        self.label_51.setObjectName(_fromUtf8("label_51"))
        self.gridLayout_30.addWidget(self.label_51, 0, 1, 1, 1)
        self.ln_nyrsigma = QtGui.QLineEdit(self.tab_normaly)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_nyrsigma.sizePolicy().hasHeightForWidth())
        self.ln_nyrsigma.setSizePolicy(sizePolicy)
        self.ln_nyrsigma.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_nyrsigma.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_nyrsigma.setObjectName(_fromUtf8("ln_nyrsigma"))
        self.gridLayout_30.addWidget(self.ln_nyrsigma, 1, 2, 1, 1)
        self.ln_ynrmu = QtGui.QLineEdit(self.tab_normaly)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_ynrmu.sizePolicy().hasHeightForWidth())
        self.ln_ynrmu.setSizePolicy(sizePolicy)
        self.ln_ynrmu.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_ynrmu.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_ynrmu.setObjectName(_fromUtf8("ln_ynrmu"))
        self.gridLayout_30.addWidget(self.ln_ynrmu, 0, 2, 1, 1)
        self.label_52 = QtGui.QLabel(self.tab_normaly)
        self.label_52.setObjectName(_fromUtf8("label_52"))
        self.gridLayout_30.addWidget(self.label_52, 1, 1, 1, 1)
        self.tab_pry.addTab(self.tab_normaly, _fromUtf8(""))
        self.tab_uniy = QtGui.QWidget()
        self.tab_uniy.setObjectName(_fromUtf8("tab_uniy"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_uniy)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_14 = QtGui.QLabel(self.tab_uniy)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_3.addWidget(self.label_14, 0, 1, 1, 1)
        self.ln_uniylow = QtGui.QLineEdit(self.tab_uniy)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_uniylow.sizePolicy().hasHeightForWidth())
        self.ln_uniylow.setSizePolicy(sizePolicy)
        self.ln_uniylow.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_uniylow.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_uniylow.setObjectName(_fromUtf8("ln_uniylow"))
        self.gridLayout_3.addWidget(self.ln_uniylow, 0, 2, 1, 1)
        self.label_15 = QtGui.QLabel(self.tab_uniy)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_3.addWidget(self.label_15, 1, 1, 1, 1)
        self.ln_uniyhigh = QtGui.QLineEdit(self.tab_uniy)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_uniyhigh.sizePolicy().hasHeightForWidth())
        self.ln_uniyhigh.setSizePolicy(sizePolicy)
        self.ln_uniyhigh.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_uniyhigh.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_uniyhigh.setObjectName(_fromUtf8("ln_uniyhigh"))
        self.gridLayout_3.addWidget(self.ln_uniyhigh, 1, 2, 1, 1)
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem11, 0, 0, 1, 1)
        self.tab_pry.addTab(self.tab_uniy, _fromUtf8(""))
        self.tab_students_4 = QtGui.QWidget()
        self.tab_students_4.setObjectName(_fromUtf8("tab_students_4"))
        self.gridLayout_31 = QtGui.QGridLayout(self.tab_students_4)
        self.gridLayout_31.setObjectName(_fromUtf8("gridLayout_31"))
        self.ln_stk_4 = QtGui.QLineEdit(self.tab_students_4)
        self.ln_stk_4.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_stk_4.setObjectName(_fromUtf8("ln_stk_4"))
        self.gridLayout_31.addWidget(self.ln_stk_4, 0, 2, 1, 1)
        self.label_53 = QtGui.QLabel(self.tab_students_4)
        self.label_53.setObjectName(_fromUtf8("label_53"))
        self.gridLayout_31.addWidget(self.label_53, 0, 1, 1, 1)
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_31.addItem(spacerItem12, 0, 0, 1, 1)
        self.tab_pry.addTab(self.tab_students_4, _fromUtf8(""))
        self.tab_exp_4 = QtGui.QWidget()
        self.tab_exp_4.setObjectName(_fromUtf8("tab_exp_4"))
        self.gridLayout_32 = QtGui.QGridLayout(self.tab_exp_4)
        self.gridLayout_32.setObjectName(_fromUtf8("gridLayout_32"))
        self.ln_explambda_4 = QtGui.QLineEdit(self.tab_exp_4)
        self.ln_explambda_4.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_explambda_4.setObjectName(_fromUtf8("ln_explambda_4"))
        self.gridLayout_32.addWidget(self.ln_explambda_4, 0, 2, 1, 1)
        self.label_54 = QtGui.QLabel(self.tab_exp_4)
        self.label_54.setObjectName(_fromUtf8("label_54"))
        self.gridLayout_32.addWidget(self.label_54, 0, 1, 1, 1)
        spacerItem13 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_32.addItem(spacerItem13, 0, 0, 1, 1)
        self.tab_pry.addTab(self.tab_exp_4, _fromUtf8(""))
        self.tab_lognorm_4 = QtGui.QWidget()
        self.tab_lognorm_4.setObjectName(_fromUtf8("tab_lognorm_4"))
        self.gridLayout_33 = QtGui.QGridLayout(self.tab_lognorm_4)
        self.gridLayout_33.setObjectName(_fromUtf8("gridLayout_33"))
        self.ln_logsigma_4 = QtGui.QLineEdit(self.tab_lognorm_4)
        self.ln_logsigma_4.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_logsigma_4.setObjectName(_fromUtf8("ln_logsigma_4"))
        self.gridLayout_33.addWidget(self.ln_logsigma_4, 1, 2, 1, 1)
        self.label_55 = QtGui.QLabel(self.tab_lognorm_4)
        self.label_55.setObjectName(_fromUtf8("label_55"))
        self.gridLayout_33.addWidget(self.label_55, 1, 1, 1, 1)
        self.label_56 = QtGui.QLabel(self.tab_lognorm_4)
        self.label_56.setObjectName(_fromUtf8("label_56"))
        self.gridLayout_33.addWidget(self.label_56, 0, 1, 1, 1)
        self.ln_logmu_4 = QtGui.QLineEdit(self.tab_lognorm_4)
        self.ln_logmu_4.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_logmu_4.setObjectName(_fromUtf8("ln_logmu_4"))
        self.gridLayout_33.addWidget(self.ln_logmu_4, 0, 2, 1, 1)
        spacerItem14 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_33.addItem(spacerItem14, 1, 0, 1, 1)
        self.tab_pry.addTab(self.tab_lognorm_4, _fromUtf8(""))
        self.tab_x2_4 = QtGui.QWidget()
        self.tab_x2_4.setObjectName(_fromUtf8("tab_x2_4"))
        self.gridLayout_34 = QtGui.QGridLayout(self.tab_x2_4)
        self.gridLayout_34.setObjectName(_fromUtf8("gridLayout_34"))
        self.label_57 = QtGui.QLabel(self.tab_x2_4)
        self.label_57.setObjectName(_fromUtf8("label_57"))
        self.gridLayout_34.addWidget(self.label_57, 0, 1, 1, 1)
        self.ln_xk_4 = QtGui.QLineEdit(self.tab_x2_4)
        self.ln_xk_4.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_xk_4.setObjectName(_fromUtf8("ln_xk_4"))
        self.gridLayout_34.addWidget(self.ln_xk_4, 0, 2, 1, 1)
        spacerItem15 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_34.addItem(spacerItem15, 0, 0, 1, 1)
        self.tab_pry.addTab(self.tab_x2_4, _fromUtf8(""))
        self.tab_beta_4 = QtGui.QWidget()
        self.tab_beta_4.setObjectName(_fromUtf8("tab_beta_4"))
        self.gridLayout_35 = QtGui.QGridLayout(self.tab_beta_4)
        self.gridLayout_35.setObjectName(_fromUtf8("gridLayout_35"))
        self.label_58 = QtGui.QLabel(self.tab_beta_4)
        self.label_58.setObjectName(_fromUtf8("label_58"))
        self.gridLayout_35.addWidget(self.label_58, 0, 1, 1, 1)
        self.label_59 = QtGui.QLabel(self.tab_beta_4)
        self.label_59.setObjectName(_fromUtf8("label_59"))
        self.gridLayout_35.addWidget(self.label_59, 1, 1, 1, 1)
        self.ln_betabeta_4 = QtGui.QLineEdit(self.tab_beta_4)
        self.ln_betabeta_4.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_betabeta_4.setObjectName(_fromUtf8("ln_betabeta_4"))
        self.gridLayout_35.addWidget(self.ln_betabeta_4, 1, 2, 1, 1)
        self.ln_betaalpha_4 = QtGui.QLineEdit(self.tab_beta_4)
        self.ln_betaalpha_4.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_betaalpha_4.setObjectName(_fromUtf8("ln_betaalpha_4"))
        self.gridLayout_35.addWidget(self.ln_betaalpha_4, 0, 2, 1, 1)
        spacerItem16 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_35.addItem(spacerItem16, 0, 0, 1, 1)
        self.tab_pry.addTab(self.tab_beta_4, _fromUtf8(""))
        self.tab_gamma_4 = QtGui.QWidget()
        self.tab_gamma_4.setObjectName(_fromUtf8("tab_gamma_4"))
        self.gridLayout_36 = QtGui.QGridLayout(self.tab_gamma_4)
        self.gridLayout_36.setObjectName(_fromUtf8("gridLayout_36"))
        self.label_60 = QtGui.QLabel(self.tab_gamma_4)
        self.label_60.setObjectName(_fromUtf8("label_60"))
        self.gridLayout_36.addWidget(self.label_60, 0, 1, 1, 1)
        self.label_61 = QtGui.QLabel(self.tab_gamma_4)
        self.label_61.setObjectName(_fromUtf8("label_61"))
        self.gridLayout_36.addWidget(self.label_61, 1, 1, 1, 1)
        self.ln_gammatheta_4 = QtGui.QLineEdit(self.tab_gamma_4)
        self.ln_gammatheta_4.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_gammatheta_4.setObjectName(_fromUtf8("ln_gammatheta_4"))
        self.gridLayout_36.addWidget(self.ln_gammatheta_4, 0, 2, 1, 1)
        self.ln_gammak_4 = QtGui.QLineEdit(self.tab_gamma_4)
        self.ln_gammak_4.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_gammak_4.setObjectName(_fromUtf8("ln_gammak_4"))
        self.gridLayout_36.addWidget(self.ln_gammak_4, 1, 2, 1, 1)
        spacerItem17 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_36.addItem(spacerItem17, 0, 0, 1, 1)
        self.tab_pry.addTab(self.tab_gamma_4, _fromUtf8(""))
        self.tab_weibull_4 = QtGui.QWidget()
        self.tab_weibull_4.setObjectName(_fromUtf8("tab_weibull_4"))
        self.gridLayout_37 = QtGui.QGridLayout(self.tab_weibull_4)
        self.gridLayout_37.setObjectName(_fromUtf8("gridLayout_37"))
        self.ln_weilambda_4 = QtGui.QLineEdit(self.tab_weibull_4)
        self.ln_weilambda_4.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_weilambda_4.setObjectName(_fromUtf8("ln_weilambda_4"))
        self.gridLayout_37.addWidget(self.ln_weilambda_4, 0, 2, 1, 1)
        self.ln_weik_4 = QtGui.QLineEdit(self.tab_weibull_4)
        self.ln_weik_4.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_weik_4.setObjectName(_fromUtf8("ln_weik_4"))
        self.gridLayout_37.addWidget(self.ln_weik_4, 1, 2, 1, 1)
        self.label_62 = QtGui.QLabel(self.tab_weibull_4)
        self.label_62.setObjectName(_fromUtf8("label_62"))
        self.gridLayout_37.addWidget(self.label_62, 1, 1, 1, 1)
        self.label_63 = QtGui.QLabel(self.tab_weibull_4)
        self.label_63.setObjectName(_fromUtf8("label_63"))
        self.gridLayout_37.addWidget(self.label_63, 0, 1, 1, 1)
        spacerItem18 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_37.addItem(spacerItem18, 0, 0, 1, 1)
        self.tab_pry.addTab(self.tab_weibull_4, _fromUtf8(""))
        self.tab_custom_4 = QtGui.QWidget()
        self.tab_custom_4.setObjectName(_fromUtf8("tab_custom_4"))
        self.gridLayout_38 = QtGui.QGridLayout(self.tab_custom_4)
        self.gridLayout_38.setObjectName(_fromUtf8("gridLayout_38"))
        self.label_64 = QtGui.QLabel(self.tab_custom_4)
        self.label_64.setObjectName(_fromUtf8("label_64"))
        self.gridLayout_38.addWidget(self.label_64, 0, 1, 1, 1)
        self.btn_custom_4 = QtGui.QToolButton(self.tab_custom_4)
        self.btn_custom_4.setObjectName(_fromUtf8("btn_custom_4"))
        self.gridLayout_38.addWidget(self.btn_custom_4, 0, 2, 1, 1)
        spacerItem19 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_38.addItem(spacerItem19, 0, 0, 1, 1)
        self.tab_pry.addTab(self.tab_custom_4, _fromUtf8(""))
        self.gridLayout_4.addWidget(self.tab_pry, 2, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_4)
        self.line_4 = QtGui.QFrame(Form)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.verticalLayout_2.addWidget(self.line_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_11 = QtGui.QLabel(Form)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_3.addWidget(self.label_11)
        self.ln_point = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_point.sizePolicy().hasHeightForWidth())
        self.ln_point.setSizePolicy(sizePolicy)
        self.ln_point.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_point.setObjectName(_fromUtf8("ln_point"))
        self.horizontalLayout_3.addWidget(self.ln_point)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(Form)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.ln_n = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_n.sizePolicy().hasHeightForWidth())
        self.ln_n.setSizePolicy(sizePolicy)
        self.ln_n.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_n.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_n.setObjectName(_fromUtf8("ln_n"))
        self.horizontalLayout_2.addWidget(self.ln_n)
        self.btn_start = QtGui.QPushButton(Form)
        self.btn_start.setAutoDefault(True)
        self.btn_start.setDefault(True)
        self.btn_start.setObjectName(_fromUtf8("btn_start"))
        self.horizontalLayout_2.addWidget(self.btn_start)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.tbl_tot = QtGui.QTableWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbl_tot.sizePolicy().hasHeightForWidth())
        self.tbl_tot.setSizePolicy(sizePolicy)
        self.tbl_tot.setMinimumSize(QtCore.QSize(350, 0))
        self.tbl_tot.setObjectName(_fromUtf8("tbl_tot"))
        self.tbl_tot.setColumnCount(2)
        self.tbl_tot.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tbl_tot.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tbl_tot.setHorizontalHeaderItem(1, item)
        self.verticalLayout_2.addWidget(self.tbl_tot)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.btn_start.clicked.connect(self.act_btn_start)

        self.btn_shootset.clicked.connect(self.act_btn_edit)

        self.tbl_res.itemSelectionChanged.connect(self.tblresselect)

        self.tbl_res.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.ResizeToContents)
        self.tbl_res.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.ResizeToContents)
        self.tbl_res.horizontalHeader().setResizeMode(2, QtGui.QHeaderView.ResizeToContents)
        self.tbl_res.horizontalHeader().setResizeMode(3, QtGui.QHeaderView.ResizeToContents)
        self.tbl_res.horizontalHeader().setResizeMode(4, QtGui.QHeaderView.ResizeToContents)
        self.tbl_res.horizontalHeader().setResizeMode(5, QtGui.QHeaderView.ResizeToContents)
        self.tbl_res.horizontalHeader().setResizeMode(6, QtGui.QHeaderView.ResizeToContents)
        self.tbl_res.horizontalHeader().setResizeMode(7, QtGui.QHeaderView.ResizeToContents)

        #header.setResizeMode(1, QtGui.QHeaderView.ResizeToContents)

        self.retranslateUi(Form)
        self.tab_prx.setCurrentIndex(0)
        self.tab_pry.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Shooting range", None))
        self.label_2.setText(_translate("Form", "Shooting results", None))
        item = self.tbl_res.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Shot #", None))
        item = self.tbl_res.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Component", None))
        item = self.tbl_res.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Face", None))
        item = self.tbl_res.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Material", None))
        item = self.tbl_res.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Thickness", None))
        item = self.tbl_res.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Angle", None))
        item = self.tbl_res.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Result", None))
        item = self.tbl_res.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Point", None))
        self.label_7.setText(_translate("Form", "Shooting settings", None))
        self.btn_shootset.setText(_translate("Form", "Edit", None))
        self.label_17.setText(_translate("Form", "Y axis:", None))
        self.label_18.setText(_translate("Form", "X axis:", None))
        self.label_4.setText(_translate("Form", "Mu", None))
        self.ln_xnrsigma.setText(_translate("Form", "100", None))
        self.ln_xnrmu.setText(_translate("Form", "0", None))
        self.label_5.setText(_translate("Form", "Sigma", None))
        self.tab_prx.setTabText(self.tab_prx.indexOf(self.tab_normalx), _translate("Form", "Normal", None))
        self.ln_unixlow.setText(_translate("Form", "0", None))
        self.ln_unixhigh.setText(_translate("Form", "100", None))
        self.label_13.setText(_translate("Form", "High", None))
        self.label_12.setText(_translate("Form", "Low", None))
        self.tab_prx.setTabText(self.tab_prx.indexOf(self.tab_unix), _translate("Form", "Uniform", None))
        self.label_6.setText(_translate("Form", "k", None))
        self.tab_prx.setTabText(self.tab_prx.indexOf(self.tab_students), _translate("Form", "Student\'s", None))
        self.label_8.setText(_translate("Form", "Lambda", None))
        self.tab_prx.setTabText(self.tab_prx.indexOf(self.tab_exp), _translate("Form", "Exponential", None))
        self.label_10.setText(_translate("Form", "Sigma", None))
        self.label_9.setText(_translate("Form", "Mu", None))
        self.tab_prx.setTabText(self.tab_prx.indexOf(self.tab_lognorm), _translate("Form", "Log Normal", None))
        self.label_19.setText(_translate("Form", "k", None))
        self.tab_prx.setTabText(self.tab_prx.indexOf(self.tab_x2), _translate("Form", "Chi-squared", None))
        self.label_20.setText(_translate("Form", "Alpha", None))
        self.label_21.setText(_translate("Form", "Beta", None))
        self.tab_prx.setTabText(self.tab_prx.indexOf(self.tab_beta), _translate("Form", "Beta", None))
        self.label_22.setText(_translate("Form", "Theta", None))
        self.label_23.setText(_translate("Form", "k", None))
        self.tab_prx.setTabText(self.tab_prx.indexOf(self.tab_gamma), _translate("Form", "Gamma", None))
        self.label_25.setText(_translate("Form", "k", None))
        self.label_24.setText(_translate("Form", "Lambda", None))
        self.tab_prx.setTabText(self.tab_prx.indexOf(self.tab_weibull), _translate("Form", "Weibull", None))
        self.label_26.setText(_translate("Form", "Load", None))
        self.btn_custom.setText(_translate("Form", "...", None))
        self.tab_prx.setTabText(self.tab_prx.indexOf(self.tab_custom), _translate("Form", "Custom", None))
        self.label_51.setText(_translate("Form", "Mu", None))
        self.ln_nyrsigma.setText(_translate("Form", "100", None))
        self.ln_ynrmu.setText(_translate("Form", "0", None))
        self.label_52.setText(_translate("Form", "Sigma", None))
        self.tab_pry.setTabText(self.tab_pry.indexOf(self.tab_normaly), _translate("Form", "Normal", None))
        self.label_14.setText(_translate("Form", "Low", None))
        self.ln_uniylow.setText(_translate("Form", "0", None))
        self.label_15.setText(_translate("Form", "High", None))
        self.ln_uniyhigh.setText(_translate("Form", "100", None))
        self.tab_pry.setTabText(self.tab_pry.indexOf(self.tab_uniy), _translate("Form", "Uniform", None))
        self.label_53.setText(_translate("Form", "k", None))
        self.tab_pry.setTabText(self.tab_pry.indexOf(self.tab_students_4), _translate("Form", "Student\'s", None))
        self.label_54.setText(_translate("Form", "Lambda", None))
        self.tab_pry.setTabText(self.tab_pry.indexOf(self.tab_exp_4), _translate("Form", "Exponential", None))
        self.label_55.setText(_translate("Form", "Sigma", None))
        self.label_56.setText(_translate("Form", "Mu", None))
        self.tab_pry.setTabText(self.tab_pry.indexOf(self.tab_lognorm_4), _translate("Form", "Log Normal", None))
        self.label_57.setText(_translate("Form", "k", None))
        self.tab_pry.setTabText(self.tab_pry.indexOf(self.tab_x2_4), _translate("Form", "Chi-squared", None))
        self.label_58.setText(_translate("Form", "Alpha", None))
        self.label_59.setText(_translate("Form", "Beta", None))
        self.tab_pry.setTabText(self.tab_pry.indexOf(self.tab_beta_4), _translate("Form", "Beta", None))
        self.label_60.setText(_translate("Form", "Theta", None))
        self.label_61.setText(_translate("Form", "k", None))
        self.tab_pry.setTabText(self.tab_pry.indexOf(self.tab_gamma_4), _translate("Form", "Gamma", None))
        self.label_62.setText(_translate("Form", "k", None))
        self.label_63.setText(_translate("Form", "Lambda", None))
        self.tab_pry.setTabText(self.tab_pry.indexOf(self.tab_weibull_4), _translate("Form", "Weibull", None))
        self.label_64.setText(_translate("Form", "Load", None))
        self.btn_custom_4.setText(_translate("Form", "...", None))
        self.tab_pry.setTabText(self.tab_pry.indexOf(self.tab_custom_4), _translate("Form", "Custom", None))
        self.label_11.setText(_translate("Form", "Central point:", None))
        self.ln_point.setText(_translate("Form", "0,0", None))
        self.label.setText(_translate("Form", "N:", None))
        self.ln_n.setText(_translate("Form", "1000", None))
        self.btn_start.setText(_translate("Form", "Start", None))
        self.label_3.setText(_translate("Form", "Shooting totals", None))
        item = self.tbl_tot.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Shot", None))
        item = self.tbl_tot.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Components", None))

    def loadinit(self, mainw):
        self.probdict = {0: np.random.normal, 1: np.random.standard_t,
                         2: np.random.exponential, 3: np.random.lognormal,
                         4: np.random.chisquare}

        self.mainwindow = mainw
        self.mainwindow.glwidget.crosscdinit()
        self.mainwindow.glwidget.crossinit()

    def probdet(self):
        # self.probx,self.proby
        i, j = self.tab_prx.currentIndex(), self.tab_pry.currentIndex()
        xparams, yparams = [], []
        wx, wy = self.tab_prx.widget(i), self.tab_pry.widget(j)
        chsx, chsy = wx.children(), wy.children()

        for chx, chy in zip(chsx, chsy):
            if isinstance(chx, QtGui.QLineEdit):
                xparams.append(float(chx.text()))
            if isinstance(chy, QtGui.QLineEdit):
                yparams.append(float(chy.text()))
        prx, pry = self.getdist(i), self.getdist(j)

        if i == 0:
            xparams = [self.mainwindow.glwidget.wi / 2 + float(self.ln_xnrmu.text()), float(self.ln_xnrsigma.text())]
        if j == 0:
            yparams = [self.mainwindow.glwidget.he / 2 - float(self.ln_ynrmu.text()), float(self.ln_nyrsigma.text())]

        return prx, pry, xparams, yparams

    def getdist(self, t):
        try:
            dist = self.probdict[t]
        except:
            print('NOT AVAILABLE')
            dist = self.probdict[0]
        return dist

    def act_btn_start(self,hedge=False):
        if not hedge:
            self.mainwindow.glwidget.dropsphs()
            self.mainwindow.glwidget.droplines()
        num = int(self.ln_n.text())
        prx, pry, xparams, yparams = self.probdet()
        #print(prx, pry, xparams, yparams)
        res = self.shoots(prx, pry, xparams, yparams, num,hedge)

        self.lookp1 = np.matmul(self.mainwindow.glwidget.mvMatrix, (0, 0, -5000, 1))[:3]
        self.lookp2 = np.matmul(self.mainwindow.glwidget.mvMatrix, (0, 0, 5000, 1))[:3]
        self.mainwindow.glwidget.addtoconsole('Taking ' + str(num) + ' shots : X-axis:,Y-axis')

        meanthick=False
        if res:
            self.results=res
            meanthick = self.resultsconvert()
        if hedge:
            if meanthick:
                self.meanthick.append(meanthick)
                return meanthick
            else:
                self.meanthick.append(None)
                return None

    def starthedge(self):

        # self.mainwindow.glwidget.dropsphs()
        # self.mainwindow.glwidget.droplines()
        num = int(self.ln_n.text())
        prx, pry, xparams, yparams = self.probdet()
        meanthick = self.shootshedge(prx, pry, xparams, yparams, num)
        self.mainwindow.glwidget.addtoconsole('Taking ' + str(num) + ' shots : X-axis:,Y-axis')
        if meanthick:
            self.meanthick.append(meanthick)
            return meanthick
        else:
            self.meanthick.append(None)
            return None

    def shootshedge(self, prx, pry, xparams, yparams, n):
        picarr, w, h = self.mainwindow.glwidget.getpic()
        sx = prx(*xparams, n)
        sy = pry(*yparams, n)
        sx = (sx[np.where(abs(sx - w / 2) < w / 2 - 1)])
        sy = (sy[np.where(abs(sy - h / 2) < h / 2 - 1)])
        sx = list(map(int, np.rint(sx).astype(int)))
        sy = list(map(int, np.rint(sy).astype(int)))
        eqthicks=[]
        checkedobjects = {}
        lookvec = np.matmul(self.mainwindow.glwidget.mvMatrix, (0, 0, 1, 1))[:3]
        for i, picdata in enumerate(picarr):
            imgc = Image.frombytes("RGBA", (w, h), picdata)
            imgc = ImageOps.flip(imgc)
            #imgc.save('RESULTS\\norm'+str(i)+'.png', 'PNG')
            datac = imgc.load()
            t1,t2,t3=0,0,0
            for i, x, y in zip(range(n), sx, sy):
                clr = datac[x, y]
                plid = clr[0] + clr[1] * 256
                oid = clr[2]
                if oid != 255:
                    #print('Num: ',i)
                    org,norm = None,None
                    comp = self.mainwindow.getcompbygeoid(oid)
                    if oid in checkedobjects.keys():
                        checkedplanes = checkedobjects[oid]
                        if plid in checkedplanes.keys():
                            org,norm = checkedplanes[plid]
                            t1+=1
                        else:
                            org, norm = self.getno(oid,plid)
                            checkedplanes[plid] = org,norm
                            t2+=1
                    else:
                        t3+=1
                        checkedplanes = {}
                        org, norm = self.getno(oid, plid)
                        checkedplanes[plid] = org, norm
                        checkedobjects[oid] = checkedplanes
                    #ci = self.getint(org, norm, (x, y))
                    cos = self.getcos(norm,lookvec)
                    thick = comp.thickarr[plid - 1]
                    #print(oid,plid,x,y,thick)
                    if cos > .20:
                        eqthicks.append(thick / cos)
        #print(t1,t2,t3)
        #meanthick = np.sqrt(np.mean(np.array(eqthicks) ** 2))
        meanthick = np.mean(eqthicks)
        #meanthick = np.median(eqthicks)
        return meanthick

    def getno(self,oid,plid):
        object = self.mainwindow.glwidget.objects[self.mainwindow.glwidget.getobjbyid(oid)]
        face = object.faces[plid - 1]
        org = object.points[face[0] - 1]
        norm = object.normals[3 * (plid - 1)]
        # m = np.transpose(self.mainwindow.glwidget.mvMatrix)
        # org = np.matmul(m, (*org, 1))[:3]
        # norm = np.matmul(m, (*norm, 0))[:3]

        return org,norm

    def getint(self,org,norm,pos):
        px, py = pos
        px = px - self.mainwindow.glwidget.wi / 2
        py = self.mainwindow.glwidget.he / 2 - py

        line_a = (px, py, -1200)
        line_b = (px, py, 1200)

        ci = mth.geometry.intersect_line_plane(line_a, line_b, org, norm)
        m = np.linalg.inv(m)
        ci = np.matmul(m, (*ci, 1))[:3]

    def getcos(self,norm,lookvec):
        #lookvec = np.matmul(self.mainwindow.glwidget.mvMatrix, (0, 0, 1, 1))[:3]
        #lookvec = np.array([0,0,1])
        angle = getangle(norm, lookvec)
        #print('Angle: ',angle)
        cosang = np.abs(np.cos(angle*np.pi/180))
        return cosang

    def shoots(self, prx, pry, xparams, yparams, n,hedge):
        picarr, w, h = self.mainwindow.glwidget.getpic()

        sx = prx(*xparams, n)
        sy = pry(*yparams, n)
        sx = (sx[np.where(abs(sx - w / 2) < w / 2 - 1)])
        sy = (sy[np.where(abs(sy - h / 2) < h / 2 - 1)])
        sx = list(map(int, np.rint(sx).astype(int)))
        sy = list(map(int, np.rint(sy).astype(int)))
        oids = {}
        results = []
        sphs=[]
        for i, picdata in enumerate(picarr):
            # print(20*'-',i)
            imgc = Image.frombytes("RGBA", (w, h), picdata)
            imgc = ImageOps.flip(imgc)
            #imgc.save('RESULTS\\norm'+str(i)+'.png', 'PNG')
            datac = imgc.load()
            for i, x, y in zip(range(n), sx, sy):
                clr = datac[x, y]
                plid = clr[0] + clr[1] * 256
                oid = clr[2]
                if oid != 255:
                    ci = self.mainwindow.glwidget.getint(oid, plid, (x, y))
                    results.append([i, oid, plid, ci])
                    sphs.append(list(ci))
                    oids.setdefault(oid, []).append(i)
        # for k,v in oids.items():
        #     print(k,'\t:\t',len(v))
        # self.mainwindow.glwidget.sphinit()
        # self.mainwindow.glwidget.upmat()
        if hedge:
            self.mainwindow.glwidget.sphcdlist = sphs[:10]
        else:
            self.mainwindow.glwidget.sphcdlist = sphs
            self.mainwindow.glwidget.sphinit()
            self.mainwindow.glwidget.upmat()

        return results

    def newrow(self, n, obj, face,mat, thick, angle,res,ci):
        rowPosition = self.tbl_res.rowCount()
        self.tbl_res.insertRow(rowPosition)
        item1 = QtGui.QTableWidgetItem(n)
        item1.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item1.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        item2 = QtGui.QTableWidgetItem(obj)
        item2.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item2.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        item3 = QtGui.QTableWidgetItem(face)
        item3.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item3.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        item4 = QtGui.QTableWidgetItem(mat)
        item4.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item4.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        item5 = QtGui.QTableWidgetItem(thick)
        item5.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item5.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        item6 = QtGui.QTableWidgetItem(angle)
        item6.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item6.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        item7 = QtGui.QTableWidgetItem(res)
        item7.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item7.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        item8 = QtGui.QTableWidgetItem(ci)
        item8.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item8.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        self.tbl_res.setItem(rowPosition, 0, item1)
        self.tbl_res.setItem(rowPosition, 1, item2)
        self.tbl_res.setItem(rowPosition, 2, item3)
        self.tbl_res.setItem(rowPosition, 3, item4)
        self.tbl_res.setItem(rowPosition, 4, item5)
        self.tbl_res.setItem(rowPosition, 5, item6)
        self.tbl_res.setItem(rowPosition, 6, item7)
        self.tbl_res.setItem(rowPosition, 7, item8)

    def newrowtot(self, n, arr):
        rowPosition = self.tbl_tot.rowCount()
        self.tbl_tot.insertRow(rowPosition)
        item1 = QtGui.QTableWidgetItem(n)
        item1.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item1.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        strarr = str(arr)
        item2 = QtGui.QTableWidgetItem(strarr)
        item2.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item2.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        self.tbl_tot.setItem(rowPosition, 0, item1)
        self.tbl_tot.setItem(rowPosition, 1, item2)

    def resultsconvert(self):

        shotdict = {}
        self.tbl_res.setRowCount(0)
        res = self.results
        eqthicks = []
        for r in res:
            n, objid, faceid, ci = r
            comp = self.mainwindow.getcompbygeoid(objid)
            cname = comp.getname()
            face = comp.getfacesnames()[faceid - 1]
            mat = comp.matarr[faceid-1]
            nthick = comp.thickarr[faceid - 1]
            thick = str(nthick)
            ci = str(ci)
            lookvec = np.matmul(self.mainwindow.glwidget.mvMatrix, (0, 0, 1, 1))[:3]
            nangle = getangle(comp.geoobj.getnormaltoface(faceid), lookvec)
            #nangle = getangle(comp.geoobj.normals[faceid-1], lookvec)
            angle = str(round(nangle,2))
            res = 'None'
            if np.abs(np.cos(nangle))>.34:
                eqthicks.append(np.abs(nthick/np.cos(nangle)))
            #eqthicks.append(nthick)
            #self.newrow(str(n), cname, face,mat.getname(), thick, angle,res,ci)
            if n in shotdict.keys():
                shotdict[n].append([cname, face,mat.getname(), thick, angle,res,ci])
            else:
                shotdict[n] = [[cname, face,mat.getname(), thick, angle,res,ci]]
        self.settbltot(shotdict)
        #meanthick = np.mean(eqthicks)
        #meanthick = np.median(eqthicks)
        meanthick =  np.sqrt(np.mean(np.array(eqthicks)**2))
        return meanthick

    def settbltot(self, shotdict):
        for k, vs in shotdict.items():
            for i,v in enumerate(vs):
                if i==0:
                    self.newrow(str(k),*v)
                else:
                    self.newrow('', *v)

                    #self.newrowtot(str(k), v)

    def tblresselect(self):
        if self.tbl_res.item(self.tbl_res.currentRow()+1, -1):
            cistr = self.tbl_res.item(self.tbl_res.currentRow()+1, -1).text()
            ci1, ci2 = self.lookp1 - self.lookp2 + eval(cistr), eval(cistr) + self.lookp2 - self.lookp1
            self.mainwindow.glwidget.droplines()
            self.mainwindow.glwidget.linecdlist.append([ci1, ci2])
            self.mainwindow.glwidget.lineinit()
            self.mainwindow.glwidget.upmat()

    def act_btn_edit(self):
        # self.addwind = Ui_shootset()
        # self.addwind.show()
        self.startshow()

    def closeEvent(self, event):
        self.mainwindow.glwidget.dropsphs()
        self.mainwindow.glwidget.droplines()
        self.mainwindow.glwidget.dropcross()
        self.mainwindow.glwidget.crossinit()
        self.mainwindow.glwidget.lineinit()
        self.mainwindow.glwidget.sphinit()

        event.accept()

    def startshow(self):
        self.mainwindow.glwidget.dropsphs()
        self.mainwindow.glwidget.droplines()
        timestart = time()
        hedge = {}
        k = .1
        a, b = 2, 2
        fxang,fyang = 180,90
        xoffset,yoffset = 0,0
        xang, yang = int(fxang / a), int(fyang/ b)
        xi, yi = a / k, b / k
        xcum, ycum = xoffset, 0
        for j in range(yang+1):

            xcum=xoffset
            for i in range(xang):
                self.mainwindow.glwidget.act_btn_front()
                xcum += xi
                self.mainwindow.glwidget.rot('xy', xcum, ycum)
                currthick = self.starthedge()
                #print('Mean thickness: ',currthick)
                hedge[str(xcum*k)+','+str(ycum*k)] = currthick
            ycum += yi
            #break
        self.mainwindow.glwidget.act_btn_front()
        self.mainwindow.glwidget.upmat()

        with open('results.csv','w') as f:
            for k,v in hedge.items():
                f.write(k+','+str(v)+'\n')
                #print(k,' -> ',v)

        print(time()-timestart)
        print(xang*yang)