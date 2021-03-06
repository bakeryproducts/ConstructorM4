import numpy as np
np.seterr(divide='ignore', invalid='ignore')
import math, random
import re
from PIL import Image
from PIL import ImageOps
from CNST.techs import getangle
from shootsettings_ui import Ui_shootset
import mathutils as mth
from time import time,sleep
from PyQt4 import QtCore, QtGui
from OpenGL.GL import *
import time

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D

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

class Ui_wid_axialff(QtGui.QWidget):
    def __init__(self):
        super(Ui_wid_axialff, self).__init__()
        self.setupUi(self)
        # self.mainwindow = 0
        self.meanthick = []
        self.probx, self.proby = 0, 0

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(523, 772)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget = QtGui.QWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
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
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbl_res.sizePolicy().hasHeightForWidth())
        self.tbl_res.setSizePolicy(sizePolicy)
        self.tbl_res.setMinimumSize(QtCore.QSize(200, 250))
        self.tbl_res.setObjectName(_fromUtf8("tbl_res"))
        self.tbl_res.setColumnCount(10)
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
        item = QtGui.QTableWidgetItem()
        self.tbl_res.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tbl_res.setHorizontalHeaderItem(9, item)
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
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_4.addWidget(self.label_17, 2, 0, 1, 1)
        self.label_18 = QtGui.QLabel(Form)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
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
        self.ln_ynrsigma = QtGui.QLineEdit(self.tab_normaly)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_ynrsigma.sizePolicy().hasHeightForWidth())
        self.ln_ynrsigma.setSizePolicy(sizePolicy)
        self.ln_ynrsigma.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_ynrsigma.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_ynrsigma.setObjectName(_fromUtf8("ln_ynrsigma"))
        self.gridLayout_30.addWidget(self.ln_ynrsigma, 1, 2, 1, 1)
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
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem20 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem20)
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
        self.ln_point.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_point.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_point.setObjectName(_fromUtf8("ln_point"))
        self.horizontalLayout_3.addWidget(self.ln_point)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.line_4 = QtGui.QFrame(Form)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.verticalLayout_2.addWidget(self.line_4)
        self.label_30 = QtGui.QLabel(Form)
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.verticalLayout_2.addWidget(self.label_30)
        self.gridLayout_14 = QtGui.QGridLayout()
        self.gridLayout_14.setObjectName(_fromUtf8("gridLayout_14"))
        self.ln_r2 = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_r2.sizePolicy().hasHeightForWidth())
        self.ln_r2.setSizePolicy(sizePolicy)
        self.ln_r2.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_r2.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_r2.setObjectName(_fromUtf8("ln_r2"))
        self.gridLayout_14.addWidget(self.ln_r2, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_14.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_28 = QtGui.QLabel(Form)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.gridLayout_14.addWidget(self.label_28, 1, 2, 1, 1)
        self.ln_gridr = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_gridr.sizePolicy().hasHeightForWidth())
        self.ln_gridr.setSizePolicy(sizePolicy)
        self.ln_gridr.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_gridr.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_gridr.setObjectName(_fromUtf8("ln_gridr"))
        self.gridLayout_14.addWidget(self.ln_gridr, 1, 3, 1, 1)
        self.label_16 = QtGui.QLabel(Form)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_14.addWidget(self.label_16, 1, 0, 1, 1)
        self.ln_r1 = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_r1.sizePolicy().hasHeightForWidth())
        self.ln_r1.setSizePolicy(sizePolicy)
        self.ln_r1.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_r1.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_r1.setObjectName(_fromUtf8("ln_r1"))
        self.gridLayout_14.addWidget(self.ln_r1, 0, 1, 1, 1)
        self.label_27 = QtGui.QLabel(Form)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.gridLayout_14.addWidget(self.label_27, 2, 0, 1, 1)
        self.ln_org = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_org.sizePolicy().hasHeightForWidth())
        self.ln_org.setSizePolicy(sizePolicy)
        self.ln_org.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_org.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_org.setObjectName(_fromUtf8("ln_org"))
        self.gridLayout_14.addWidget(self.ln_org, 2, 1, 1, 1)
        self.label_31 = QtGui.QLabel(Form)
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.gridLayout_14.addWidget(self.label_31, 0, 2, 1, 1)
        self.ln_grida = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_grida.sizePolicy().hasHeightForWidth())
        self.ln_grida.setSizePolicy(sizePolicy)
        self.ln_grida.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_grida.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_grida.setObjectName(_fromUtf8("ln_grida"))
        self.gridLayout_14.addWidget(self.ln_grida, 0, 3, 1, 1)
        self.btn_grid = QtGui.QPushButton(Form)
        self.btn_grid.setMaximumSize(QtCore.QSize(80, 16777215))
        self.btn_grid.setCheckable(True)
        self.btn_grid.setObjectName(_fromUtf8("btn_grid"))
        self.gridLayout_14.addWidget(self.btn_grid, 2, 3, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_14)
        self.line_6 = QtGui.QFrame(Form)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.verticalLayout_2.addWidget(self.line_6)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.chb_fsv = QtGui.QCheckBox(Form)
        self.chb_fsv.setObjectName(_fromUtf8("chb_fsv"))
        self.horizontalLayout_6.addWidget(self.chb_fsv)
        self.cmb_fsv = QtGui.QComboBox(Form)
        self.cmb_fsv.setObjectName(_fromUtf8("cmb_fsv"))
        self.horizontalLayout_6.addWidget(self.cmb_fsv)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.chb_rico = QtGui.QCheckBox(Form)
        self.chb_rico.setChecked(True)
        self.chb_rico.setObjectName(_fromUtf8("chb_rico"))
        self.horizontalLayout_9.addWidget(self.chb_rico)
        self.label_32 = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy)
        self.label_32.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.horizontalLayout_9.addWidget(self.label_32)
        self.ln_rico = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_rico.sizePolicy().hasHeightForWidth())
        self.ln_rico.setSizePolicy(sizePolicy)
        self.ln_rico.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ln_rico.setAlignment(QtCore.Qt.AlignCenter)
        self.ln_rico.setObjectName(_fromUtf8("ln_rico"))
        self.horizontalLayout_9.addWidget(self.ln_rico)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.line_7 = QtGui.QFrame(Form)
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.verticalLayout_2.addWidget(self.line_7)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_29 = QtGui.QLabel(Form)
        self.label_29.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.horizontalLayout_5.addWidget(self.label_29)
        self.ln_savefile = QtGui.QLineEdit(Form)
        self.ln_savefile.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_savefile.sizePolicy().hasHeightForWidth())
        self.ln_savefile.setSizePolicy(sizePolicy)
        self.ln_savefile.setObjectName(_fromUtf8("ln_savefile"))
        self.horizontalLayout_5.addWidget(self.ln_savefile)
        self.tbtn_filepath = QtGui.QToolButton(Form)
        self.tbtn_filepath.setObjectName(_fromUtf8("tbtn_filepath"))
        self.horizontalLayout_5.addWidget(self.tbtn_filepath)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.line_5 = QtGui.QFrame(Form)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.verticalLayout_2.addWidget(self.line_5)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(Form)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
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
        self.tableWidget = QtGui.QTableWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(130)
        self.verticalLayout_2.addWidget(self.tableWidget)
        spacerItem21 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem21)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.btn_grid.clicked.connect(self.act_btn_grid)
        self.btn_start.clicked.connect(self.act_btn_start)

        self.tbl_res.itemSelectionChanged.connect(self.tblresselect)

        self.tbtn_filepath.clicked.connect(self.act_savefile)

        self.tbl_res.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.ResizeToContents)
        self.tbl_res.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.ResizeToContents)
        self.tbl_res.horizontalHeader().setResizeMode(2, QtGui.QHeaderView.ResizeToContents)
        self.tbl_res.horizontalHeader().setResizeMode(3, QtGui.QHeaderView.ResizeToContents)
        self.tbl_res.horizontalHeader().setResizeMode(4, QtGui.QHeaderView.ResizeToContents)
        self.tbl_res.horizontalHeader().setResizeMode(5, QtGui.QHeaderView.ResizeToContents)
        self.tbl_res.horizontalHeader().setResizeMode(6, QtGui.QHeaderView.ResizeToContents)
        self.tbl_res.horizontalHeader().setResizeMode(7, QtGui.QHeaderView.ResizeToContents)
        self.tbl_res.horizontalHeader().setResizeMode(8, QtGui.QHeaderView.ResizeToContents)
        self.tbl_res.horizontalHeader().setResizeMode(9, QtGui.QHeaderView.ResizeToContents)

        self.tbl_res.hideColumn(9)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.widget.setLayout(layout)

        self.retranslateUi(Form)
        self.tab_prx.setCurrentIndex(0)
        self.tab_pry.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Directional shooting: AFF", None))
        self.label_2.setText(_translate("Form", "Shooting results", None))
        item = self.tbl_res.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Fragment #", None))
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
        item.setText(_translate("Form", "Eq. Thickness", None))
        item = self.tbl_res.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Result", None))
        item = self.tbl_res.horizontalHeaderItem(8)
        item.setText(_translate("Form", "Type: A", None))
        item = self.tbl_res.horizontalHeaderItem(9)
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
        self.ln_ynrsigma.setText(_translate("Form", "100", None))
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
        self.label_30.setText(_translate("Form", "FF cone parameters", None))
        self.ln_r2.setText(_translate("Form", "100", None))
        self.label_3.setText(_translate("Form", "Inner r", None))
        self.label_28.setText(_translate("Form", "Grid,rad.", None))
        self.ln_gridr.setText(_translate("Form", "6", None))
        self.label_16.setText(_translate("Form", "Outer R", None))
        self.ln_r1.setText(_translate("Form", "0", None))
        self.label_27.setText(_translate("Form", "Origin", None))
        self.ln_org.setText(_translate("Form", "0,0,500", None))
        self.label_31.setText(_translate("Form", "Grid,ang.", None))
        self.ln_grida.setText(_translate("Form", "12", None))
        self.btn_grid.setText(_translate("Form", "Show grid", None))
        self.chb_fsv.setText(_translate("Form", "Enable FSV analysis", None))
        self.chb_rico.setText(_translate("Form", "Enable ricochet", None))
        self.label_32.setText(_translate("Form", "Angle,deg:", None))
        self.ln_rico.setText(_translate("Form", "85", None))
        self.label_29.setText(_translate("Form", "Set results file ", None))
        self.tbtn_filepath.setText(_translate("Form", "...", None))
        self.label.setText(_translate("Form", "N:", None))
        self.ln_n.setText(_translate("Form", "500", None))
        self.btn_start.setText(_translate("Form", "Start", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Stat", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Res", None))

    def loadinit(self, mainw):
        self.probdict = {0: np.random.normal, 1: np.random.uniform,
                         2: np.random.standard_t,
                         3: np.random.exponential, 4: np.random.lognormal,
                         5: np.random.chisquare}

        self.ln_savefile.setText('RESULTS\\results.csv')

        # self.fsv = mainw.fsv
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

        w = self.mainwindow.glwidget.wi
        h = self.mainwindow.glwidget.he

        if i == 0:
            xparams = [w / 2 + float(self.ln_xnrmu.text()), float(self.ln_xnrsigma.text())]
        if j == 0:
            yparams = [h / 2 - float(self.ln_ynrmu.text()), float(self.ln_ynrsigma.text())]

        if i == 1:
            xparams = [w / 2 + float(self.ln_unixlow.text()), w / 2 + float(self.ln_unixhigh.text())]
        if j == 1:
            yparams = [h / 2 - float(self.ln_uniylow.text()), h / 2 - float(self.ln_uniyhigh.text())]

        return prx, pry, xparams, yparams

    def getdist(self, t):
        try:
            dist = self.probdict[t]
        except:
            print('NOT AVAILABLE')
            dist = self.probdict[0]
        return dist

    def act_btn_start(self):
        # self.lookp1 = np.matmul(self.mainwindow.glwidget.mvMatrix, (0, 0, -25000, 1))[:3]
        # self.lookp2 = np.matmul(self.mainwindow.glwidget.mvMatrix, (0, 0, 25000, 1))[:3]

        self.mainwindow.glwidget.dropsphs()
        # self.mainwindow.glwidget.droplines()
        self.mainwindow.glwidget.sphinit()
        # self.mainwindow.glwidget.lineinit()

        self.checkedplanes = self.genplanesdict()

        num = int(self.ln_n.text())
        prx, pry, xparams, yparams = self.probdet()
        packsdict,grid,org = self.gencone()
        gx,gy = grid
        rays = np.array([(x-org[0],y-org[1],-org[2]) for x,y in zip(gx,gy)])
        dir = -np.array(org)

        axss = np.cross(rays, dir)
        res1 = np.linalg.norm(axss, axis=1)
        nd = np.dot(rays, dir)
        angs = np.arctan2(res1, nd)
        mv = self.mainwindow.glwidget.mvMatrix
        morg = np.matmul((*org,1),np.linalg.inv(mv))[:-1]
        self.org = morg
        t=0
        res,sphcds = [],[]
        for pack,ang,axs in zip(packsdict.values(),angs,axss):
            print('Pack# ',t,' \tANG:',ang*180/np.pi)
            t+=1
            if not isinstance(pack,bool):
                self.mainwindow.glwidget.rotp(ang*180/np.pi,list(axs))
                packresults,packinters,flatinters = self.ffshoot(pack,org)
                res.append([packresults,packinters])
                sphcds.append(flatinters)
                self.mainwindow.glwidget.mvMatrix = mv


        self.results = res
        self.resultsconvert()

        sphcds = [j for i in sphcds for j in i]
        self.mainwindow.glwidget.sphcdlist = sphcds
        self.mainwindow.glwidget.sphinit(r=2)
        lcds = [(p,morg) for p in sphcds]
        self.mainwindow.glwidget.linecdlist = lcds
        self.mainwindow.glwidget.lineinit(thick=1)
        self.mainwindow.glwidget.upmat()

        # res = self.shoots(prx, pry, xparams, yparams, num)
        #
        # self.lookp1 = np.matmul(self.mainwindow.glwidget.mvMatrix, (0, 0, -25000, 1))[:3]
        # self.lookp2 = np.matmul(self.mainwindow.glwidget.mvMatrix, (0, 0, 25000, 1))[:3]
        # self.mainwindow.glwidget.addtoconsole('Taking ' + str(num) + ' shots : X-axis:' + str(prx) + ',Y-axis')
        #
        # # if res:
        # self.results = res
        # self.resultsconvert()

    def ffshoot(self, pack,morg):
        n = len(pack)
        start = time.time()
        picarr, deparr, w, h = self.mainwindow.glwidget.getpic()

        arrinter = np.zeros((len(picarr), n, 5))
        inters = np.zeros((len(picarr), n, 3))
        m = self.mainwindow.glwidget.mvMatrix
        invm = np.linalg.inv(m)
        lookvec = np.array([0, 0, 1])
        results = np.zeros((len(picarr), n, 4))

        for objind, picdata in enumerate(picarr):
            norms, orgs, raystart = np.zeros((n, 3)), np.zeros((n, 3)), np.zeros((n, 3))
            eqthicks, planeids, depths = np.zeros((n)), np.zeros((n)), np.zeros((n))

            imgc = Image.frombytes("RGBA", (w, h), picdata)
            imgc = ImageOps.flip(imgc)
            # imgc.save('RESULTS\\norm'+str(i)+'.png', 'PNG')
            datac = imgc.load()
            # objdepths = reversed(deparr[objind])
            objdepths = np.array(list(reversed(deparr[objind]))).reshape((-1, w))
            objdepths = np.flip(objdepths, 1)

            for row, p in zip(range(n), pack):
                x,y = int(p[0]+w/2),int(h/2-p[1])
                #print(row,x,y)
                if x>w or x<0 or y>h or y<0:
                    continue
                clr = datac[x, y]
                oid = clr[2]
                if oid != 255:
                    plid = clr[0] + clr[1] * 256
                    px, py = (x - w / 2), (h / 2 - y)
                    norm, org, thick = self.checkedplanes[oid][plid - 1]
                    planeids[row] = plid
                    norms[row] = norm
                    orgs[row] = org
                    depths[row] = objdepths[y, x]
                    eqthicks[row] = thick
                    raystart[row] = [px, py, 0]

            extnorms = np.pad(norms, (0, 1), 'constant')[:-1]
            multnorm = (np.matmul(extnorms, m))[:, :-1]

            #mlookvec = morg
            res1 = np.linalg.norm(np.cross(multnorm, lookvec), axis=1)
            nd = np.dot(multnorm, lookvec)
            ang = np.arctan2(res1, nd)
            if self.chb_rico.isChecked():
                val = float(self.ln_rico.text())
                cond = np.where(ang > val * np.pi / 180)
                ang[cond] = np.nan
            # print(ang*180/np.pi)
            eqthicks = np.round(eqthicks / np.cos(ang), 2)
            # meanthick = np.sqrt(np.mean(np.array(eqthicks) ** 2))
            # meanthick = np.mean(eqthicks)
            # meanthick = np.median(eqthicks)

            extorgs = np.pad(orgs, (0, 1), 'constant', constant_values=(1))[:-1]
            multorg = (np.matmul(extorgs, m))[:, :-1]

            nd = np.dot(multnorm, lookvec)
            ww = raystart - multorg
            si = -np.einsum('ij,ij->i', multnorm, ww) / nd
            psi = np.multiply(lookvec, si[:, np.newaxis]) + multorg + ww
            # psi[cond] = np.nan
            extpsi = np.pad(psi, (0, 1), 'constant', constant_values=(1))[:-1]
            multpsi = np.matmul(extpsi, invm)[:, :-1]
            inters[objind] = multpsi
            results[objind] = np.transpose((np.full((n), objind), planeids, ang, eqthicks))
            arrinter[objind] = np.transpose(
                (np.array(range(n)), np.full((n), objind), np.round(psi[:, -1], 2), eqthicks, depths))

        t1 = inters.flatten()
        t1 = t1[~np.isnan(t1)]
        t = list(t1.reshape((-1, 3)))
        # self.mainwindow.glwidget.sphcdlist = t
        # self.mainwindow.glwidget.sphinit()
        # self.mainwindow.glwidget.upmat()
        # print(n, ': ', time.time() - start)

        return [results,inters,t]#[results, inters, arrinter,t]

    def shoottest(self, prx, pry, xparams, yparams, n):

        start = time.time()
        picarr, deparr, w, h = self.mainwindow.glwidget.getpic()
        sx = prx(*xparams, n)
        sy = pry(*yparams, n)
        sx = (sx[np.where(abs(sx - w / 2) < w / 2 - 1)])
        sy = (sy[np.where(abs(sy - h / 2) < h / 2 - 1)])
        sx = list(map(int, np.rint(sx).astype(int)))
        sy = list(map(int, np.rint(sy).astype(int)))

        m = self.mainwindow.glwidget.mvMatrix
        lookvec = np.array([0, 0, 1])

        for objind, picdata in enumerate(picarr):
            norms, orgs, raystart = np.zeros((n, 3)), np.zeros((n, 3)), np.zeros((n, 3))
            eqthicks, planeids, depths = np.zeros((n)), np.zeros((n)), np.zeros((n))

            imgc = Image.frombytes("RGBA", (w, h), picdata)
            imgc = ImageOps.flip(imgc)
            # imgc.save('RESULTS\\norm'+str(i)+'.png', 'PNG')
            datac = imgc.load()
            # objdepths = reversed(deparr[objind])
            objdepths = np.array(list(reversed(deparr[objind]))).reshape((-1, w))
            objdepths = np.flip(objdepths, 1)
            for row, x, y in zip(range(n), sx, sy):
                clr = datac[x, y]
                oid = clr[2]
                if oid != 255:
                    plid = clr[0] + clr[1] * 256
                    px, py = (x - w / 2), (h / 2 - y)
                    norm, org, thick = self.checkedplanes[oid][plid - 1]
                    planeids[row] = plid
                    norms[row] = norm
                    orgs[row] = org
                    depths[row] = objdepths[y, x]
                    eqthicks[row] = thick
                    raystart[row] = [px, py, 0]

            extnorms = np.pad(norms, (0, 1), 'constant')[:-1]
            multnorm = (np.matmul(extnorms, m))[:, :-1]

            res1 = np.linalg.norm(np.cross(multnorm, lookvec), axis=1)
            nd = np.dot(multnorm, lookvec)
            ang = np.arctan2(res1, nd)
            if self.chb_rico.isChecked():
                val = float(self.ln_rico.text())
                cond = np.where(ang > val * np.pi / 180)
                ang[cond] = np.nan
            eqthicks = eqthicks / np.cos(ang)

            # meanthick = np.sqrt(np.mean(np.array(eqthicks) ** 2))
            meanthick = np.mean(eqthicks[np.where(eqthicks > 0)])
            # meanthick = np.median(eqthicks)

        print(n, ': ', time.time() - start)

        return meanthick

    def resultsconvert(self):

        res = self.results
        # if self.chb_fsv.isChecked():
        #     ftypes = True
        #     types = self.gettype(arrinter)
        # else:
        #     ftypes = False
        #     types = 'None'

        shotdict = {}
        self.tbl_res.setRowCount(0)

        for packres,packinters in res:
            for objres in packres:
                for ind, shot in enumerate(objres):
                    #print(shot)
                    objid, faceid, ang, eqthick = shot
                    objid, faceid = int(objid), int(faceid)

                    if faceid != 0:
                        comp = self.mainwindow.components[objid]
                        cname = comp.getname()
                        face = comp.getfacesnames()[faceid - 1]
                        mat = comp.matarr[faceid - 1]
                        nthick = comp.thickarr[faceid - 1]
                        thick = str(nthick)
                        eqthick = str(round(eqthick, 1))
                        ang = str(round(ang * 180 / np.pi, 1))
                        res = 'None'
                        # if ftypes:
                        #     typep = types[ind]
                        # else:
                        #     typep = types

                        ci = str(list(packinters[objid, ind]))
                        if ind in shotdict.keys():
                            shotdict[ind].append([cname, face, mat.getname(), thick, ang, eqthick, res, '--', ci])
                        else:
                            shotdict[ind] = [[cname, face, mat.getname(), thick, ang, eqthick, res, 'TYPE_', ci]]
        self.settbltot(shotdict)

    def newrow(self, n, obj, face, mat, thick, angle, eqthick, res, typep, ci):
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

        item7 = QtGui.QTableWidgetItem(eqthick)
        item7.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item7.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        item8 = QtGui.QTableWidgetItem(res)
        item8.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item8.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        item9 = QtGui.QTableWidgetItem(typep)
        item9.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item9.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        item10 = QtGui.QTableWidgetItem(ci)
        item10.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        item10.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        self.tbl_res.setItem(rowPosition, 0, item1)
        self.tbl_res.setItem(rowPosition, 1, item2)
        self.tbl_res.setItem(rowPosition, 2, item3)
        self.tbl_res.setItem(rowPosition, 3, item4)
        self.tbl_res.setItem(rowPosition, 4, item5)
        self.tbl_res.setItem(rowPosition, 5, item6)
        self.tbl_res.setItem(rowPosition, 6, item7)
        self.tbl_res.setItem(rowPosition, 7, item8)
        self.tbl_res.setItem(rowPosition, 8, item9)
        self.tbl_res.setItem(rowPosition, 9, item10)

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

    def settbltot(self, shotdict):
        for k, vs in shotdict.items():
            for i, v in enumerate(vs):
                if i == 0:
                    self.newrow(str(k), *v)
                else:
                    self.newrow('', *v)

                    # self.newrowtot(str(k), v)

    def tblresselect(self):
        if self.tbl_res.item(self.tbl_res.currentRow() + 1, -1):
            cistr = self.tbl_res.item(self.tbl_res.currentRow() + 1, -1).text()
            ci1 = eval(cistr)
            ci2 = self.org
            #ci1, ci2 = self.lookp1 - self.lookp2 + eval(cistr), eval(cistr) + self.lookp2 - self.lookp1
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

    def act_savefile(self):
        filedialog = QtGui.QFileDialog(self)
        file = filedialog.getSaveFileName(self, "Save resulting file as", "RESULTS\\results.csv",
                                          filter="csv (*.csv *.)")
        if file:
            self.lineEdit_5.setText(file)

    def genplanesdict(self):
        planesd = {}
        for comp in self.mainwindow.components:
            compdict = {}
            for plid in range(len(comp.geoobj.faces)):
                compdict[plid] = (comp.geoobj.normals[3 * (plid)],
                                  comp.geoobj.points[comp.geoobj.faces[plid][0] - 1],
                                  comp.thickarr[plid])
            planesd[comp.geoobj.getid()] = compdict

        return planesd

    def testconv(self):
        self.mainwindow.glwidget.dropsphs()
        self.mainwindow.glwidget.droplines()
        self.mainwindow.glwidget.sphinit()
        self.mainwindow.glwidget.lineinit()

        self.checkedplanes = self.genplanesdict()
        num0 = 100  # int(self.ln_n.text())
        num = num0
        limnum = int(self.ln_convcheck.text())
        prx, pry, xparams, yparams = self.probdet()
        hedge = {}
        totthick = 0
        mathick = []
        mawthick = []
        mawind = []
        wind = 3
        for i in range(40):
            currthick = self.shoottest(prx, pry, xparams, yparams, num)
            hedge[num] = currthick
            totthick += currthick
            mathick.append((totthick / (i + 1)))
            if len(mawind) > wind:
                mawind.pop(0)
            mawind.append(currthick)
            mawthick.append(np.mean(mawind))

            num += limnum / 40
            num = int(num)
            if num > limnum:
                break
                # print(num)

        self.mainwindow.glwidget.upmat()

        savefile = self.ln_savefile.text()

        with open('RESULTS\\test.csv', 'w') as f:
            for k, v in hedge.items():
                f.write(str(k) + ',' + str(v) + '\n')
                # print(k,' -> ',v)

                # create an axis

        print(hedge.values())
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.clear()
        ax.plot(hedge.keys(), hedge.values(), '*-')
        ax.plot(hedge.keys(), mathick, '^-')
        ax.plot(hedge.keys(), mawthick, 'o-')

        self.canvas.draw()

        # n = int(self.ln_n.text()) / 2
        self.mainwindow.glwidget.addtoconsole('Results saved to ' + savefile)
        self.mainwindow.glwidget.upmat()

    def gettype(self, arrinter):
        shotsuni = np.swapaxes(arrinter, 0, 1)
        shotsind = (-shotsuni)[:, :, 2].argsort()
        shotsrecomb = np.array([shotsuni[i, t] for i, t in enumerate(shotsind)])
        res = {}

        for i, shot in enumerate(shotsrecomb):
            cumvec = []
            cumth = 0
            shotres = 'NONE'
            print(shot)
            for n, o, z, t, d in shot:
                if t != 0 and t != np.nan:
                    cumvec.append(int(o))
                    cumth += t
                    # print(cumvec)
                    if self.mainwindow.fsvact(cumvec):  # self.getevalfsv(cumvec):
                        shotres = (str(cumth) + ' mm')
                        res[int(n)] = shotres
                        break

                res[n] = shotres

                # print('Shot #',i,': ',shotres)
        # print(res)
        return res

    def gencone(self):
        ga, gr = int(self.ln_grida.text()),int(self.ln_gridr.text())#12, 6
        r1, r2 = int(self.ln_r1.text()),int(self.ln_r2.text())
        n = int(self.ln_n.text())#15000, 500
        org = [int(el) for el in self.ln_org.text().split(',')]

        sx = np.random.normal(0, r2 / 3, n)
        sy = np.random.normal(0, r2 / 3, n)
        rs = np.sqrt(sx * sx + sy * sy)
        sx = sx[np.where(np.abs(rs - r1 - r2 / 2) < r2 / 2)]
        sy = sy[np.where(np.abs(rs - r1 - r2 / 2) < r2 / 2)]

        angs = np.arctan2(sx, sy)
        rs = np.sqrt(sx * sx + sy * sy)

        cangs = []
        for a in angs:
            if a < 0:
                a += 2 * np.pi
            cangs.append(a)
        angs = np.array(cangs)

        gridda = 2 * np.pi / ga
        griddr = (r2 - r1) / gr
        gridangs = [i * gridda for i in range(ga)]
        gridapoints = np.tile(gridangs, gr)
        gridrs = [r1 + griddr / 2 + i * griddr for i in range(gr + 1)]
        gridrpoints = [r1 + griddr / 2 + i * griddr for i in range(gr) for j in range(ga)]

        pdict = {}
        for r in gridrs:
            cond2 = np.abs(rs - r) < griddr / 2
            for a in gridangs:
                if a != 0:
                    cond1 = np.abs(angs - a) <= gridda / 2
                else:
                    cond1 = (angs >= 2 * np.pi - gridda / 2) + ((angs <= gridda / 2))

                rcond = cond1 * cond2
                if np.sum(rcond) > 0:
                    pdict[str(r)[:3] +'; '+ str(a)[:3]] = [rs[rcond], angs[rcond]]
                else:
                    pdict[str(r)[:3] +'; '+ str(a)[:3]] = False#[rs[rcond], angs[rcond]]

        gx = gridrpoints * np.cos(gridapoints)
        gy = gridrpoints * np.sin(gridapoints)
        tc=0
        resdict = {}
        for i, pair in enumerate(pdict.items()):
            k, v = pair
            if not isinstance(v,bool):
                rs, angs = v
                resdict[i] = [(r * np.cos(a), r * np.sin(a), 0) for r, a in zip(rs, angs)]
                tc+=1
            else:
                resdict[i] = False
            #print(k,resdict[i])
        print(tc,len(gx))
        return resdict, (gx, gy),org

    def act_btn_grid(self):
        rdict,grid,org = self.gencone()
        gx,gy = grid
        k = self.mainwindow.glwidget.scalefree
        m = self.mainwindow.glwidget.mvMatrix

        gp = [(x, y, 0) for x, y in zip(gx,gy)]
        extgp = np.pad(gp, (0, 1), 'constant', constant_values=(1))[:-1]
        multgp = (np.matmul(extgp, np.linalg.inv(m)))[:, :-1]
        multorg = np.matmul((*org,1),np.linalg.inv(m))[:-1]

        lcds = [(multorg, p) for p in multgp]

        pcds = [j for i in rdict.values() if not isinstance(i,bool) for j in i ]
        extpcds = np.pad(pcds, (0, 1), 'constant', constant_values=(1))[:-1]
        multpcds = (np.matmul(extpcds, np.linalg.inv(m)))[:, :-1]

        self.mainwindow.glwidget.sphcdlist = list(multpcds)
        self.mainwindow.glwidget.sphinit(r=2)
        self.mainwindow.glwidget.linecdlist = lcds
        # self.mainwindow.glwidget.lineinit(thick=2)
        self.mainwindow.glwidget.upmat()

